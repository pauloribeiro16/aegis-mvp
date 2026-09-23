# Anti-Patterns & Smells — Trust Boundary & Complete Mediation

Functional use case smells and anti-patterns violating trust boundaries and complete mediation.

---

## 1. Perimeter-Only Verification (The Flat Internal Trust Fallacy)

### Bad Use Case Design Smell
```markdown
### Use Case: View Project Tasks
1. User requests task list for Project ID `proj_123`.
2. API Gateway validates that the user is logged in.
3. System fetches all tasks matching `proj_123` from database and returns them to the user.
```

**Why It Fails `PRIN-ENG-01`:**
- Step 3 relies entirely on the gateway's authentication check and assumes that because the user is logged in, they are entitled to view `proj_123`. Any user can view other tenants' projects by guessing or enumerating IDs.

**Hardened Use Case Pattern:**
```markdown
### Use Case: View Project Tasks (Hardened)
1. User requests task list for Project ID `proj_123`.
2. Ingress Gateway authenticates user and extracts verified tenant identity.
3. Core Project Service mediates request: verifies that `proj_123` belongs to user's authorized tenant.
4. Core Project Service queries tasks scoped strictly to both `proj_123` AND user's tenant identifier.
```

---

## 2. Ingress Bypass to Persistent Storage

### Bad Use Case Design Smell
```markdown
### Use Case: Upload User Avatar
1. User selects image file in browser.
2. Web application uploads file directly to public object storage bucket using a shared public key.
3. Web application saves the public image URL into user profile.
```

**Why It Fails `PRIN-ENG-01`:**
- Completely bypasses the system's boundary mediation. Clients with shared credentials can overwrite, enumerate, or delete objects belonging to other users.

**Hardened Use Case Pattern:**
```markdown
### Use Case: Upload User Avatar (Hardened)
1. User initiates avatar upload.
2. Core User Service validates user identity, evaluates file size/type constraints, and generates an ephemeral, strictly scoped upload authorization restricted to the user's isolated storage prefix.
3. User transmits file using the scoped authorization.
4. System validates completion and commits avatar reference to user profile.
```
