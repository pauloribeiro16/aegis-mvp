# Anti-Patterns & Smells — Least Privilege & Mechanism Isolation

Functional use case smells and anti-patterns violating least privilege and mechanism isolation.

---

## 1. Monolithic Role Authority

### Bad Use Case Design Smell
```markdown
### Use Case: Manage Workspace
1. User logs in.
2. User can invite members, delete workspace, edit tasks, view billing invoices, and export system audit logs.
```

**Why It Fails `PRIN-ENG-03`:**
- Merges routine operational tasks (editing tasks) with high-risk administrative (deleting workspace) and financial (viewing invoices) capabilities into a single unsegregated role.

**Hardened Use Case Pattern:**
- Split into discrete, role-gated use cases: `UC-02: Task Collaboration` (Member), `UC-ADM-01: Workspace Governance` (Admin), and `UC-BIL-01: Invoice Management` (Owner).

---

## 2. Omnipotent Background Workers

### Bad Use Case Design Smell
```markdown
### Use Case: Generate Monthly Activity PDF
1. System triggers monthly reporting worker.
2. Worker queries all customer databases, payment ledgers, and authentication credential tables to compile PDF.
```

**Why It Fails `PRIN-ENG-03`:**
- Grants the reporting worker broad read access to sensitive authentication and billing data that is completely irrelevant to compiling task activity statistics.
