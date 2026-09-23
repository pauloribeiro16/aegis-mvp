# End-to-End Case Studies — Data Minimization & Privacy Balance

Realistic before-and-after case studies demonstrating schema minimization, purpose-bound collection, and privacy-preserving balance.

---

## Case Study 1: Task Management SaaS Onboarding & Collaboration API

### Context
TinyTask onboarding flow asks new users for information, and the task detail view displays collaborator information.

### Initial (Flawed) Implementation

#### Inbound Registration Payload
```json
{
  "email": "user@example.com",
  "password": "SecretPassword123!",
  "fullName": "Jane Doe",
  "phone": "+351912345678",
  "birthDate": "1990-05-15",
  "taxIdentifier": "PT123456789",
  "companyAddress": "Rua Central 123, Braga"
}
```

#### Outbound Collaborator Schema
```json
{
  "userId": "usr_9981",
  "fullName": "Jane Doe",
  "email": "user@example.com",
  "phone": "+351912345678",
  "lastLoginIp": "194.65.10.42",
  "stripeCustomerId": "cus_99182"
}
```

### Analysis & Privacy Violations

1. **Unjustified Inbound Collection (`PRIN-PRV-01`):**  
   TinyTask is a project management tool. Collecting `birthDate`, `phone`, and `taxIdentifier` during initial sign-up violates data minimization. Billing details should only be collected when upgrading to a paid plan.
2. **Excessive Egress Exposure (`PRIN-PRV-01`):**  
   Any collaborator assigned to a shared task can view `lastLoginIp`, `phone`, and `stripeCustomerId`. This enables tracking, phishing, and enumeration.

---

### Remediated Implementation

#### 1. Purpose-Bound Inbound Registration Schema
```typescript
interface SignUpRequestDTO {
  email: string;       // Required: Account identifier and auth recovery
  password: string;    // Required: Authentication credential
  displayName: string; // Required: Public handle visible to collaborators
  // Removed: phone, birthDate, taxIdentifier, companyAddress
}
```

#### 2. Minimized Public Collaborator DTO
```typescript
interface CollaboratorDTO {
  id: string;          // Opaque UUID
  displayName: string; // "Jane Doe"
  avatarUrl?: string;  // Profile picture URL
  // Excluded: email, phone, lastLoginIp, stripeCustomerId
}
```

### Minimization Ledger

| Field | Location | Initial Status | Finding | Remediated Status | Principle |
|---|---|---|---|---|---|
| `phone` | Ingress / Sign-up | Collected | No functional necessity for SaaS app | **Removed** from sign-up schema | `PRIN-PRV-01` |
| `birthDate` | Ingress / Sign-up | Collected | Unnecessary PII | **Removed** from database schema | `PRIN-PRV-01` |
| `taxIdentifier` | Ingress / Sign-up | Collected | Premature collection before checkout | **Deferred** to billing upgrade flow | `PRIN-PRV-01` |
| `lastLoginIp` | Egress / Collaborator | Exposed | Network tracking risk | **Restricted** to internal audit logs | `PRIN-PRV-03` |
| `stripeCustomerId`| Egress / Collaborator | Exposed | Financial metadata leak | **Restricted** to billing service | `PRIN-PRV-01` |
