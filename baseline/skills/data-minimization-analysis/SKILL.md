---
name: data-minimization-analysis
description: Audits API schemas, database fields, and telemetry payloads to eliminate extraneous personal data collection, prevent over-exposure, and enforce purpose binding.
---

# Data Minimization & Privacy Balance Analysis

Inspects API schemas, request/response Data Transfer Objects (DTOs), database table columns, and telemetry payloads to eliminate extraneous data collection and prevent sensitive field leakage while preserving application functionality.

> **Target Principle:**  
> - `PRIN-ENG-06` (Proactive Data Minimization & Scoped Projection — Cavoukian / GDPR Art. 5)

---

## 1. Operational Mandate & Scope

The agent acts as a Principal Privacy Engineer and API Architect reviewing:
- **API Interfaces & DTOs:** OpenAPI schemas, Pydantic models, TypeScript interfaces, GraphQL query/mutation types.
- **Data Ingestion Schemas:** Registration forms, profile update payloads, third-party webhook integrations.
- **Telemetry & Logging Payloads:** Application log formats, error tracking payloads (Sentry), analytics event dictionaries.

The objective is to ensure that no superfluous personal or sensitive data is collected at ingress, that internal database entities are never passed raw to egress, and that necessary functionality is achieved using the least privacy-invasive representations.

---

## 2. Evaluation Procedure

1. **Schema Field Inventory:** Extract all fields collected at ingress (request bodies) and emitted at egress (response bodies).
2. **Strict Purpose Binding Verification (`PRIN-PRV-01`):** For each collected field, identify the exact functional requirement that justifies its collection. If a field is collected "for potential future analytics", flag it for immediate removal.
3. **Egress Entity Exposure Audit:** Inspect response DTOs. Verify that database ORM models are not serialized directly to API responses (preventing accidental exposure of password hashes, internal IDs, or sensitive PII).
4. **Coarsening & Privacy-Preserving Transformation (`PRIN-PRV-03`):** Where data is required for application features (e.g. fraud detection, localized content), determine if coarse-grained representations suffice (e.g. ISO country code instead of precise GPS coordinates; year of birth instead of exact timestamp).
5. **Telemetry & Log Scrubbing:** Confirm that error loggers and analytics pipelines automatically strip or hash IP addresses, email addresses, and auth tokens.
6. **Ledger Output:** Produce a Data Minimization Audit Ledger.

---

## 3. Concrete Walkthrough Example

### 3.1 Input Artifact: Vulnerable User Profile API & Schema

```python
# Pydantic ORM Model passed directly to API response
from pydantic import BaseModel
from datetime import datetime

class UserEntityResponse(BaseModel):
    id: str
    email: str
    password_hash: str            # CRITICAL LEAK: Password hash exposed
    full_name: str
    date_of_birth: str            # SMELL: Exact birthdate exposed to all collaborators
    home_address: str             # SMELL: Physical address collected for online SaaS
    failed_login_attempts: int    # SMELL: Internal security telemetry leaked
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# FastApi endpoint
@app.get("/api/v1/users/{user_id}", response_model=UserEntityResponse)
def get_user_profile(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    return user # Directly serializes database entity to JSON
```

### 3.2 Analytical Evaluation

1. **Violation of `PRIN-PRV-01` (Proactive Data Minimization):**
   - Serializing the database `User` entity directly leaks `password_hash` and `failed_login_attempts` to the client.
   - The SaaS application collects `home_address` and `date_of_birth` during onboarding, neither of which is required for task tracking or collaboration.
2. **Violation of `PRIN-PRV-03` (Full Functionality & Privacy Balance):**
   - Collaborators viewing a task assignee only need a display identifier and an avatar. Exposing personal emails and full birthdates violates privacy without offering additional functional utility.

### 3.3 Remediated Data Transfer Objects (DTOs)

```python
from pydantic import BaseModel, Field

# 1. Public Profile DTO (Used for team collaborators and task assignees)
class PublicCollaboratorDTO(BaseModel):
    id: str = Field(..., description="Opaque UUIDv4 identifier")
    display_name: str = Field(..., description="Chosen public display nickname")
    avatar_url: str | None = Field(None, description="Public avatar URL")

# 2. Private Account DTO (Returned strictly to the authenticated user themselves)
class AuthenticatedAccountProfileDTO(BaseModel):
    id: str
    display_name: str
    email: str = Field(..., description="Account recovery email")
    # Minimization: No physical address, no DOB, no password hashes or internal counts

# Hardened API Route: Strict DTO Projection
@app.get("/api/v1/users/{user_id}", response_model=PublicCollaboratorDTO)
def get_collaborator_profile(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # Explicit mapping: Only minimum fields populated
    return PublicCollaboratorDTO(
        id=user.id,
        display_name=user.display_name or "Anonymous",
        avatar_url=user.avatar_url
    )
```

### 3.4 Data Minimization Audit Ledger

| Field | Original Handling | Risk / Violation | Remediated Handling | Principle |
|---|---|---|---|---|
| `password_hash` | Serialized in API response | Offline brute-force credential compromise | **Excluded** from all DTO schemas | `PRIN-PRV-01` |
| `home_address` | Collected at onboarding | Unnecessary collection of sensitive PII | **Removed** from database schema and signup form | `PRIN-PRV-01` |
| `date_of_birth` | Exposed to team members | Privacy invasion / identity theft vector | **Removed**; age-gating replaced by self-attestation checkbox | `PRIN-PRV-03` |
| `failed_logins` | Leaked in JSON | Account takeover reconnaissance | **Restricted** to internal logging stream | `PRIN-PRV-01` |

---

## 4. Reference Catalogs

- **Detailed Heuristics:** Consult [`references/heuristics.md`](references/heuristics.md) for ingress validation rules, DTO projection guidelines, and log scrubbing algorithms.
- **Concrete Anti-Patterns:** Consult [`references/antipatterns.md`](references/antipatterns.md) for mass assignment vulnerabilities, over-collection forms, and raw entity serializations.
- **End-to-End Case Studies:** Consult [`references/examples.md`](references/examples.md) for full REST and GraphQL API schema minimization case studies.
- **Audit Checklist:** Consult [`references/checklist.md`](references/checklist.md) for the structured data minimization audit checklist.
