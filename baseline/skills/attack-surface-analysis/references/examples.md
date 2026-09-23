# End-to-End Case Studies — Attack Surface & Peripheral Resilience

Comprehensive before-and-after evaluations of functional Use Cases (`UC-*`) against `PRIN-ENG-02`.

---

## Case Study 1: External Billing & Subscription Notification (`UC-05`)

### Initial (Flawed) Functional Use Case

```markdown
### Use Case: UC-05 — External Billing Notification Ingestion
- **Primary Actor:** Third-Party Payment Gateway (External)
- **Pre-conditions:** A tenant has initiated a subscription upgrade on the platform.
- **Trigger:** Payment gateway completes invoice processing and dispatches an HTTP notification.
- **Data Exchanged:** Customer ID, invoice status, amount paid, subscription tier.

#### Main Success Scenario:
1. Payment gateway sends event payload to the notification ingestion path.
2. System receives the payload and checks if `invoice_status == "paid"`.
3. System locates the customer account and increments licensed user seats to the new tier.
4. System dispatches a success email to the customer contact.

#### Failure Scenarios:
- 2a. Customer ID not found: System logs error and ignores event.
```

---

### Step-by-Step Analytical Evaluation

1. **Step 1 & 2 Finding — Unauthenticated Public Ingress Point (`PRIN-ENG-02`):**  
   *Risk:* The use case allows any external sender to trigger step 3 (license tier elevation) without proving authenticity. Because the path is exposed publicly to receive callbacks, anyone can forge a `"paid"` payload.
2. **Missing Replay Defense (`PRIN-ENG-02`):**  
   *Risk:* There is no requirement in the functional flow to evaluate timestamp freshness or deduplicate events, allowing replay attacks.
3. **Step 4 Finding — Auxiliary Flooding Vector:**  
   *Risk:* Forged payloads can trigger email flooding to arbitrary customer addresses.

---

### Derived Atomic Security Requirements (EARS Syntax)

- `REQ-SEC-SURF-010` (Cryptographic Origin Verification):  
  *When* an external billing event notification is received, *the* Ingestion Gateway *SHALL* cryptographically verify the signature of the payload against the established pre-shared key before invoking subscription processing logic.
- `REQ-SEC-SURF-011` (Event Freshness & Idempotency):  
  *When* evaluating an inbound billing event, *the* Ingestion Gateway *SHALL* verify that the event timestamp is within a 300-second window and that the event identifier has not been previously processed, rejecting duplicates.

---

### Remediated Functional Use Case (`UC-05`)

```markdown
### Use Case: UC-05 — External Billing Notification Ingestion (Hardened)
- **Primary Actor:** Verified Third-Party Payment Gateway
- **Pre-conditions:** Tenant exists; cryptographic shared secret is established between platform and payment gateway.
- **Trigger:** Gateway dispatches signed event payload to the secured webhook receiver.
- **Data Exchanged:** Signed event payload, cryptographic signature header, event timestamp, unique event ID.

#### Main Success Scenario:
1. External Gateway dispatches signed notification to the webhook receiver.
2. The System validates the cryptographic signature using the shared verification key.
3. The System verifies that the timestamp is fresh and the event ID is not a replay.
4. The System executes the subscription tier upgrade in an atomic transaction.
5. The System returns an acknowledgment receipt to the Payment Gateway.

#### Failure Scenarios:
- 2a. Cryptographic signature is invalid or missing: System terminates interaction immediately with access denied.
- 3a. Event is older than tolerance window or already processed: System records audit entry and rejects processing.
```
