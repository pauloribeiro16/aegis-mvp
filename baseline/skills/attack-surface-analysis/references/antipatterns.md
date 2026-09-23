# Anti-Patterns & Smells — Attack Surface & Peripheral Resilience

Concrete bad patterns and code/configuration smells that expose unnecessary attack surface or compromise peripheral resilience.

---

## 1. Public Diagnostic & Framework Consoles

### Bad Pattern: Spring Boot Actuator or FastAPI Docs Exposed Globally

```yaml
# Ingress / Gateway routing configuration
routes:
  - path: /actuator/**
    upstream: internal-billing-service:8080
    # SMELL: Public exposure of heap dumps, env vars, thread dumps
```

```python
# FastAPI application entrypoint
app = FastAPI(
    docs_url="/docs",      # SMELL: Interactive Swagger UI accessible in production
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)
```

**Consequence:** Attackers harvest internal system environment variables, database connection strings, and application route schemas directly from internet scanners.

**Hardened Pattern:**

```python
import os
from fastapi import FastAPI

is_prod = os.getenv("ENVIRONMENT") == "production"

app = FastAPI(
    docs_url=None if is_prod else "/docs",
    redoc_url=None if is_prod else "/redoc",
    openapi_url=None if is_prod else "/openapi.json"
)
```

---

## 2. Inadvertent Database & Cache Port Exposure

### Bad Pattern: Docker Compose Exposing Data Stores to `0.0.0.0`

```yaml
version: '3.8'
services:
  db:
    image: postgres:16-alpine
    ports:
      - "5432:5432"  # SMELL: Binds to 0.0.0.0:5432 on the host, exposing DB publicly
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"  # SMELL: Unauthenticated cache exposed to internet port scanners
```

**Consequence:** Automated bots exploit weak passwords, default credentials, or remote code execution flaws in exposed database and Redis ports.

**Hardened Pattern:**

```yaml
version: '3.8'
services:
  db:
    image: postgres:16-alpine
    # Hardened: No host port mapping. Only reachable via internal container bridge
    networks:
      - backend-tier
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
  redis:
    image: redis:7-alpine
    networks:
      - backend-tier

networks:
  backend-tier:
    internal: true # Cannot route to or from the public internet
```

---

## 3. Unauthenticated & Unbounded Webhook Ingress

### Bad Pattern: Blind Webhook Consumer

```python
# Flask / Django webhook receiver
@app.route('/webhooks/payment', methods=['POST'])
def handle_payment_webhook():
    payload = request.get_json() # SMELL: No signature check, no timestamp check
    event_type = payload.get('type')
    
    if event_type == 'invoice.paid':
        mark_account_active(payload['data']['account_id'])
    return {"status": "ok"}, 200
```

**Consequence:** Any remote actor can spoof `invoice.paid` payloads and activate paid accounts for free or flood the database with fake events.

**Hardened Pattern:**

```python
import hmac
import hashlib
import time
from flask import request, abort

WEBHOOK_SECRET = os.environ['PAYMENT_WEBHOOK_SECRET'].encode('utf-8')
TOLERANCE_SECONDS = 300

@app.route('/webhooks/payment', methods=['POST'])
def handle_payment_webhook():
    sig_header = request.headers.get('X-Signature-SHA256')
    timestamp = request.headers.get('X-Signature-Timestamp')
    
    if not sig_header or not timestamp:
        abort(400, "Missing signature headers")
        
    # Replay protection
    if abs(time.time() - float(timestamp)) > TOLERANCE_SECONDS:
        abort(400, "Timestamp outside tolerance window")
        
    # Verify cryptographic signature using constant-time comparison
    signed_payload = f"{timestamp}.".encode('utf-8') + request.get_data()
    expected_sig = hmac.new(WEBHOOK_SECRET, signed_payload, hashlib.sha256).hexdigest()
    
    if not hmac.compare_digest(sig_header, expected_sig):
        abort(403, "Invalid cryptographic signature")
        
    payload = request.get_json()
    process_verified_event(payload)
    return {"status": "accepted"}, 202
```

---

## 4. Wildcard CORS with Credentials

### Bad Pattern: Permissive CORS Configuration

```nginx
# Nginx gateway config
add_header 'Access-Control-Allow-Origin' '*';
add_header 'Access-Control-Allow-Credentials' 'true'; # SMELL: Extreme browser vulnerability
```

**Consequence:** Malicious third-party websites visited by an authenticated user can perform authenticated requests and read cross-origin response data.

**Hardened Pattern:**

```nginx
# Explicit origin validation
map $http_origin $cors_origin {
    default "";
    "https://app.tinytask.eu" "$http_origin";
    "https://admin.tinytask.eu" "$http_origin";
}

add_header 'Access-Control-Allow-Origin' $cors_origin always;
add_header 'Access-Control-Allow-Credentials' 'true' always;
add_header 'Vary' 'Origin' always;
```
