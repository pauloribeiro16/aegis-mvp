# End-to-End Case Studies — Fail-Safe Defaults & Closed Failure States

Realistic before-and-after scenarios evaluating gateway routing, circuit breakers, and database transactions under unexpected failure conditions.

---

## Case Study 1: Payment Webhook Transaction & Circuit Breaker

### Context
TinyTask receives payment confirmation webhooks from an external billing processor (Stripe) to provision tenant subscription seats.

### Initial (Flawed) Implementation
```python
@app.post("/webhooks/stripe")
async def handle_stripe_event(request: Request, db: Session = Depends(get_db)):
    event = await request.json()
    
    # Step 1: Update subscription status
    db.execute(
        "UPDATE subscriptions SET status = 'active' WHERE customer_id = :cid",
        {"cid": event["customer_id"]}
    )
    
    # Step 2: Allocate user seats in license service
    # SMELL: If license service fails, DB update was already executed without transaction!
    await license_service.allocate_seats(event["customer_id"], seats=10)
    
    return {"status": "ok"}
```

### Analysis & Vulnerability
- **Partial Failure & Inconsistent State (`PRIN-ENG-04`):** If `allocate_seats` raises a network exception, the subscription remains marked as `'active'` in the database while the user received zero seats. There is no rollback mechanism.
- **Fail-Open Risk:** The webhook handler returns an unhandled HTTP 500 without recording a state rollback, leaving the system in an indeterminate state.

---

### Remediated Implementation

```python
@app.post("/webhooks/stripe")
async def handle_stripe_event(request: Request, db: Session = Depends(get_db)):
    correlation_id = str(uuid.uuid4())
    payload = await request.body()
    sig_header = request.headers.get("Stripe-Signature")
    
    # 1. Verify Signature (Default Deny)
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, WEBHOOK_SECRET)
    except Exception as e:
        logger.warning(f"[{correlation_id}] Webhook signature verification failed: {e}")
        return JSONResponse(status_code=400, content={"error": "invalid_signature"})
        
    # 2. Transactional Execution with Atomic Rollback
    try:
        with db.begin(): # Atomic transaction block
            # Idempotency check
            if db.query(ProcessedWebhook).filter_by(event_id=event.id).first():
                return JSONResponse(status_code=200, content={"status": "already_processed"})
                
            db.execute(
                "UPDATE subscriptions SET status = 'active' WHERE customer_id = :cid",
                {"cid": event.data.object.customer}
            )
            
            # Allocate seats synchronously within transaction guard
            await license_service.allocate_seats(event.data.object.customer, seats=10)
            
            db.add(ProcessedWebhook(event_id=event.id, processed_at=datetime.now(timezone.utc)))
            # Transaction commits automatically here if no exceptions
    except Exception as e:
        # Hardened: Transaction rolls back automatically, system fails closed
        logger.exception(f"[{correlation_id}] Webhook provisioning failed. Transaction rolled back.")
        return JSONResponse(
            status_code=500,
            content={"error": "provisioning_failed", "correlation_id": correlation_id}
        )
        
    return JSONResponse(status_code=200, content={"status": "success"})
```

### Remediation Ledger

| Scenario | Initial State | Hazard | Remediated State | Principle |
|---|---|---|---|---|
| Partial Seat Allocation | No transaction | Partial billing state without seats | **Atomic Transaction**: Auto-rollback on any exception | `PRIN-ENG-04` |
| Invalid Webhook Header | Unhandled crash | Stack trace returned | **Default-Deny**: Early HTTP 400 rejection | `PRIN-ENG-04` |
| Upstream License Outage | Inconsistent state | Phantom subscriptions | **Fails Closed**: Returns HTTP 500, Stripe retries cleanly | `PRIN-ENG-04` |
