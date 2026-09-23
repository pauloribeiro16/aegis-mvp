# Anti-Patterns & Smells — Data Lifecycle & Irreversible Erasure

Functional use case smells and anti-patterns that prevent effective data erasure or violate user autonomy.

---

## 1. Soft-Delete without Anonymization

### Bad Use Case Design Smell
```markdown
### Use Case: Delete User Account
1. User clicks "Delete Account".
2. System sets user status to "deleted" in database.
3. System prevents user from logging in.
```

**Why It Fails `PRIN-ENG-07`:**
- Retains plain-text email addresses, passwords, names, and activity logs in storage indefinitely. Violates GDPR Art. 17 right to erasure.

**Hardened Use Case Pattern:**
- System permanently purges private records, irreversibly anonymizes shared activity feeds with synthetic pseudonyms, and records an erasure tombstone.

---

## 2. Orphaned Cloud Assets on Deletion

### Bad Use Case Design Smell
```markdown
### Use Case: Delete Project
1. Project Owner clicks "Delete Project".
2. System removes project record from dashboard.
```

**Why It Fails `PRIN-ENG-07`:**
- Fails to specify cascading deletion for attached files, documents, and exported archives, leaving orphaned data indefinitely in storage tiers.
