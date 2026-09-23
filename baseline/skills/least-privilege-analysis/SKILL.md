---
name: least-privilege-analysis
description: Evaluates IAM policies, container execution privileges, database roles, and encryption key custody to enforce minimal operational access and eliminate shared ambient authority.
---

# Least Privilege & Shared Mechanism Analysis

Inspects cloud IAM permissions, container runtime privileges, database access grants, and cryptographic key custody to ensure every identity operates strictly with the minimum privileges necessary and eliminates shared mechanisms across trust boundaries.

> **Target Principle:**  
> - `PRIN-ENG-03` (Least Privilege & Mechanism Isolation — Saltzer & Schroeder)

---

## 1. Operational Mandate & Scope

The agent acts as an Infrastructure & Cloud Security Architect evaluating:
- **Cloud IAM & RBAC Policies:** AWS IAM JSON, GCP IAM YAML, Azure RBAC definitions, Kubernetes ClusterRole/RoleBindings.
- **Container Runtime Security:** Dockerfiles, Docker Compose security contexts, Kubernetes `securityContext` specs.
- **Database Grants & Roles:** PostgreSQL/MySQL role definitions, schema grants, connection pool configurations.
- **Cryptographic Key Custody:** Cloud KMS key policies, key usage constraints, encryption context enforcement.

The objective is to eliminate wildcard permissions, restrict container execution to non-root users, scope database access to necessary tables, and isolate cryptographic keys per tenant or data classification tier.

---

## 2. Evaluation Procedure

1. **Permission Inventory & Action Extraction:** Parse policy documents and identify all granted verbs/actions, resource targets, and operational conditions.
2. **Wildcard & Superuser Flagging:** Identify any use of administrative privileges (`*`, `AdministratorAccess`, `ALL PRIVILEGES`, root container execution).
3. **Action-Level Pruning (`PRIN-SEC-01`):** Replace broad action categories (e.g. `s3:*`) with the exact operational verbs required for runtime operation (e.g. `s3:GetObject`, `s3:PutObject`).
4. **Resource & Condition Scoping:** Restrict resource ARNs from universal (`*`) to specific bucket prefixes, database schemas, or resource tags. Enforce multi-tenant boundaries via ABAC condition keys.
5. **Shared Mechanism Isolation (`PRIN-SEC-07`):** Ensure that distinct tenants, workloads, or data sensitivity levels do not share common encryption keys, unpartitioned queues, or shared database superuser accounts.
6. **Ledger Output:** Produce a Least Privilege Reduction Ledger detailing original vs hardened permissions.

---

## 3. Concrete Walkthrough Example

### 3.1 Input Artifact: Over-Privileged AWS IAM Policy for SaaS Task Worker

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "OverPrivilegedS3Access",
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": "*"
    },
    {
      "Sid": "OverPrivilegedKMSAccess",
      "Effect": "Allow",
      "Action": "kms:*",
      "Resource": "*"
    }
  ]
}
```

### 3.2 Analytical Evaluation

1. **Violation of `PRIN-SEC-01` (Least Privilege):**
   - The policy grants `s3:*` on all resources (`*`), enabling the worker to delete entire buckets (`s3:DeleteBucket`), modify bucket policies, or read files belonging to other workloads.
   - The worker only needs to read and write task attachments within a specific bucket.
2. **Violation of `PRIN-SEC-07` (Least Common Mechanism):**
   - Granting global `kms:*` allows the worker to create, disable, schedule deletion of, or decrypt data across any KMS key in the account, breaking cryptographic separation between tenants and operational services.
   - The worker only requires decryption and data key generation for the dedicated task attachments key, constrained by tenant encryption context.

### 3.3 Remediated Least-Privilege IAM Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ScopedS3AttachmentReadWrite",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:AbortMultipartUpload"
      ],
      "Resource": "arn:aws:s3:::tinytask-attachments-prod/${aws:PrincipalTag/TenantId}/*"
    },
    {
      "Sid": "ScopedKMSAttachmentDecryption",
      "Effect": "Allow",
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "arn:aws:kms:eu-central-1:123456789012:key/task-attachments-prod-key",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:TenantId": "${aws:PrincipalTag/TenantId}"
        }
      }
    }
  ]
}
```

### 3.4 Least Privilege Reduction Ledger

| Policy Block | Original Scope | Evaluated Blast Radius | Remediated Scope | Principle |
|---|---|---|---|---|
| S3 Storage | `s3:*` on `*` | Full account bucket destruction / cross-tenant read | `s3:GetObject`, `s3:PutObject` strictly scoped to tenant prefix | `PRIN-SEC-01` |
| KMS Custody | `kms:*` on `*` | Key deletion, cross-service decryption | `kms:Decrypt`, `kms:GenerateDataKey` bound to specific key & tenant context | `PRIN-SEC-07` |

---

## 4. Reference Catalogs

- **Detailed Heuristics:** Consult [`references/heuristics.md`](references/heuristics.md) for IAM, database grant, and container security heuristics.
- **Concrete Anti-Patterns:** Consult [`references/antipatterns.md`](references/antipatterns.md) for Docker root execution, shared database superusers, and wildcard policies.
- **End-to-End Case Studies:** Consult [`references/examples.md`](references/examples.md) for complete multi-tier cloud IAM and Kubernetes container context hardening.
- **Audit Checklist:** Consult [`references/checklist.md`](references/checklist.md) for the structured least privilege evaluation checklist.
