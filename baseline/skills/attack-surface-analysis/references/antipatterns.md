# Anti-Patterns & Smells — Attack Surface & Peripheral Resilience

Functional use case design smells and anti-patterns that expose unnecessary attack surface or compromise peripheral resilience.

---

## 1. Unauthenticated Temporary Workspaces / Previews

### Bad Use Case Design Smell
```markdown
### Use Case: Collaborative Brainstorming
1. User navigates to the public homepage.
2. System immediately creates an anonymous workspace with full edit rights and generates a public link.
3. User shares link with collaborators; anyone with the link can upload files and execute scripts.
```

**Why It Fails `PRIN-ENG-02`:**
- Creates an unauthenticated, publicly accessible storage and compute sink that can be exploited by automated bots for hosting malware, spam, or resource exhaustion.

**Hardened Use Case Pattern:**
```markdown
### Use Case: Collaborative Brainstorming (Hardened)
1. User initiates workspace creation within an authenticated session.
2. System establishes the workspace bound to the user's verified identity.
3. User invites collaborators via email; invitees must authenticate before gaining workspace edit access.
```

---

## 2. Blind Peripheral Webhook Triggers

### Bad Use Case Design Smell
```markdown
### Use Case: Payment Webhook Confirmation
1. External Billing Provider posts transaction outcome to the public notification receiver.
2. System reads the account ID and marks the account tier as Enterprise.
```

**Why It Fails `PRIN-ENG-02`:**
- The peripheral interaction treats external notifications with implicit trust, allowing malicious actors to spoof payment success events.

**Hardened Use Case Pattern:**
```markdown
### Use Case: Payment Webhook Confirmation (Hardened)
1. External Billing Provider sends signed transaction outcome to the notification gateway.
2. Gateway cryptographically verifies the sender's signature, timestamp tolerance, and idempotency key.
3. System verifies transaction validity before updating account tier.
```

---

## 3. Administrative Side-Channels Embedded in User Use Cases

### Bad Use Case Design Smell
```markdown
### Use Case: User Profile Update
1. User submits profile changes.
2. If user appends an `override_role` parameter, the system elevates their role to Administrator for debugging purposes.
```

**Why It Fails `PRIN-ENG-02`:**
- Embeds privileged administrative capabilities directly into consumer-facing interaction paths, opening privilege escalation vectors.
