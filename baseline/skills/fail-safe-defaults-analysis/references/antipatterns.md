# Anti-Patterns & Smells — Fail-Safe Defaults & Closed Failure States

Functional use case smells and anti-patterns that create fail-open vulnerabilities or partial state corruption.

---

## 1. Fail-Open Authorization on Service Outage

### Bad Use Case Design Smell
```markdown
### Use Case: Access Secured Workspace Resource
1. User requests access to confidential project report.
2. System attempts to verify user permissions with Authorization Service.
3. If Authorization Service times out, system allows access to avoid customer disruption.
```

**Why It Fails `PRIN-ENG-04`:**
- Degrades security to maintain availability under failure conditions, allowing unauthorized actors to access confidential assets during network or service glitches.

**Hardened Pattern:**
- System fails closed: if Authorization Service is unavailable, access is denied immediately and user is advised to retry.

---

## 2. Partial Mutations without Rollback

### Bad Use Case Design Smell
```markdown
### Use Case: Delete Workspace and Transfer Data
1. System deletes all user accounts from workspace.
2. System transfers workspace files to external archive.
3. If transfer fails, system displays error (accounts remain permanently deleted and files are lost).
```

**Why It Fails `PRIN-ENG-04`:**
- Multi-step destructive action lacks rollback semantics, leaving the system in a corrupted, irreversible state upon partial failure.
