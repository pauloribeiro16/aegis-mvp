# Evaluation Checklist — Least Privilege & Shared Mechanism

Comprehensive verification checklist for evaluating IAM policies, database privileges, and container environments against `PRIN-SEC-01` and `PRIN-SEC-07`.

---

## 1. Cloud IAM & Cloud Security Groups (`PRIN-SEC-01`)

- [ ] **No Wildcard Actions:** Policy statements contain zero wildcard actions (`*`, `s3:*`, `iam:*`, `dynamodb:*`).
- [ ] **Resource-Constrained Statements:** Resource ARNs point to explicit entities or scoped prefix templates (no universal `Resource: "*"` on data-plane operations).
- [ ] **Data Plane vs Control Plane:** Application runtime identities have zero control-plane actions (e.g. cannot create or delete databases, buckets, or IAM roles).
- [ ] **ABAC & Multi-Tenancy:** Multi-tenant resource operations enforce attribute-based conditions (e.g. `kms:EncryptionContext`, S3 prefix tagging).

---

## 2. Container Runtime Privileges (`PRIN-SEC-01`)

- [ ] **Non-Root User:** Dockerfile and Kubernetes manifests specify non-root execution (`USER 10001:10001` or `runAsNonRoot: true`).
- [ ] **No Privileged Containers:** `privileged: true` is absent from all container specifications.
- [ ] **Capabilities Dropped:** All Linux capabilities are dropped (`capabilities: drop: ["ALL"]`).
- [ ] **Read-Only Root Filesystem:** Root filesystems are mounted read-only (`readOnlyRootFilesystem: true`), with writable space limited to temporary in-memory `tmpfs` mounts.
- [ ] **No Host Socket Mounting:** Docker socket (`/var/run/docker.sock`) is not mounted into application containers.

---

## 3. Database Privilege Scoping (`PRIN-SEC-01`)

- [ ] **No Superuser Application Connections:** Web applications do not connect using `postgres`, `root`, or `sa` accounts.
- [ ] **Schema vs Runtime Isolation:** Migration tasks running DDL (`CREATE`, `ALTER`) run under dedicated CI/CD credentials separate from runtime DML service accounts.
- [ ] **Table-Level Grants:** Runtime database users are granted permissions (`SELECT`, `INSERT`, `UPDATE`) only on tables strictly required for their operational domain.

---

## 4. Cryptographic & Mechanism Isolation (`PRIN-SEC-07`)

- [ ] **Domain-Specific KMS Keys:** Separate cryptographic keys are used for application data, backup storage, and system secrets.
- [ ] **Cryptographic Context Binding:** Multi-tenant decryption operations require tenant ID verification via encryption context.
- [ ] **Partitioned Queue & Cache Isolation:** Multi-tenant cache and queue keys include tenant-specific namespaces to prevent cross-tenant key pollution.
