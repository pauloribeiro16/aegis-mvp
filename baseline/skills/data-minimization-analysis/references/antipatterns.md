# Anti-Patterns & Smells — Data Minimization & Privacy Balance

Functional use case smells and anti-patterns that lead to data over-collection and exposure.

---

## 1. Premature Collection of Financial / Identity Data

### Bad Use Case Design Smell
```markdown
### Use Case: Sign Up for Free Tier
1. User enters name, email, password, and credit card number.
2. System validates card and creates free account.
```

**Why It Fails `PRIN-ENG-06`:**
- Collecting payment card details during free tier onboarding creates unnecessary liability, storage overhead, and privacy invasion for users who may never upgrade.

**Hardened Use Case Pattern:**
- Free onboarding collects only authentication credentials; billing details are deferred to a dedicated Upgrade Use Case.

---

## 2. Global Entity Dumping in Collaboration Views

### Bad Use Case Design Smell
```markdown
### Use Case: View Task Details
1. Collaborator opens task assigned to Jane Doe.
2. System displays task details and full account profile for Jane Doe (including private email, phone, and home address).
```

**Why It Fails `PRIN-ENG-06`:**
- Exposes private contact attributes to all team members without functional justification.
