# Anti-Patterns & Smells — Fail-Safe Defaults & Closed Failure States

Concrete configuration smells and architectural anti-patterns that result in fail-open vulnerabilities or information leakage.

---

## 1. Fail-Open Authorization on Cache / Service Outages

### Bad Pattern: Bypassing Auth Check when Redis or IDP is Unreachable

```python
# Authorization filter
def is_user_authorized(user_id, resource_id):
    try:
        cached_permission = redis_client.get(f"perm:{user_id}:{resource_id}")
        if cached_permission:
            return cached_permission == "ALLOW"
        return query_authorization_service(user_id, resource_id)
    except ConnectionError:
        # SMELL: Fails open during Redis outage
        logger.error("Redis down! Allowing access to prevent customer interruption.")
        return True
```

**Consequence:** When Redis experiences high load or crashes, all access controls disappear, allowing unauthorized users to access any resource.

**Hardened Pattern:**

```python
def is_user_authorized(user_id, resource_id):
    try:
        cached_permission = redis_client.get(f"perm:{user_id}:{resource_id}")
        if cached_permission:
            return cached_permission == "ALLOW"
        return query_authorization_service(user_id, resource_id)
    except Exception as e:
        # Hardened: Fail closed upon authorization error
        logger.error(f"Authorization evaluation failed: {e}. Defaulting to DENY.")
        return False
```

---

## 2. Ingress Router Default Fallthrough

### Bad Pattern: Nginx Reverse Proxy Missing Catch-All Deny

```nginx
# Nginx configuration
server {
    listen 80;
    server_name api.tinytask.eu;

    location /api/v1/tasks {
        proxy_pass http://tasks-backend:8080;
    }
    
    # SMELL: No default location / block. Unmatched requests serve local filesystem or Nginx defaults
}
```

**Consequence:** Requests targeting undeclared paths may expose default server directories or leak server version information.

**Hardened Pattern:**

```nginx
server {
    listen 443 ssl http2;
    server_name api.tinytask.eu;

    location /api/v1/tasks {
        proxy_pass http://tasks-backend:8080;
    }

    # Hardened: Default catch-all denies unmatched routes
    location / {
        return 404 '{"error": "route_not_found"}';
        add_header Content-Type application/json;
    }
}
```

---

## 3. Raw Database Error Leaks in API Responses

### Bad Pattern: Returning SQL Syntax Errors to Clients

```javascript
// Express.js route handler
app.get('/api/v1/users', async (req, res) => {
    try {
        const users = await db.rawQuery(req.query.filter);
        res.json(users);
    } catch (err) {
        // SMELL: Leaks table names, column names, and SQL dialect
        res.status(500).json({ error: err.message, sql: err.sql });
    }
});
```

**Consequence:** Attackers harvest exact database schemas and SQL dialect syntax to refine SQL injection payloads.

**Hardened Pattern:**

```typescript
app.get('/api/v1/users', async (req, res) => {
    const correlationId = crypto.randomUUID();
    try {
        const filter = sanitizeFilter(req.query.filter);
        const users = await db.safeQuery(filter);
        res.json(users);
    } catch (err) {
        logger.error({ correlationId, error: err }, "Database query execution failed");
        res.status(500).json({
            error: "internal_server_error",
            correlationId
        });
    }
});
```
