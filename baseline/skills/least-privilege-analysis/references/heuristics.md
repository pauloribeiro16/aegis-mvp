# Analytical Heuristics — Least Privilege & Shared Mechanism

Detailed technical heuristics for inspecting cloud IAM policies, database privileges, and container configurations against `PRIN-SEC-01` and `PRIN-SEC-07`.

---

## 1. Cloud IAM & RBAC Pruning Heuristic (PRIN-SEC-01)

### Rule 1.1: Action-Level Granularity
- Never use wildcard action qualifiers (`*`, `s3:*`, `iam:*`, `dynamodb:*`):
  1. Distinguish between Data Plane (`GetObject`, `PutItem`) and Control Plane (`CreateBucket`, `DeleteTable`). Runtime applications must NEVER have Control Plane permissions.
  2. Forbid destructive actions (`Delete*`, `Drop*`, `Purge*`) unless assigned to dedicated, human-supervised or approval-gated roles.

### Rule 1.2: Resource ARN Constraints & ABAC
- Permissions must never target universal resources (`Resource: "*"`), except for actions that strictly do not support resource-level constraints (e.g. `ec2:DescribeInstances`):
  1. S3 buckets must be constrained to exact bucket names and prefix patterns: `arn:aws:s3:::bucket-name/${aws:PrincipalTag/TenantId}/*`.
  2. Cryptographic operations must specify exact Key IDs and bind encryption context conditions.

---

## 2. Database Privilege Scoping Heuristic (PRIN-SEC-01)

### Rule 2.1: Operational DML vs DDL Segregation
- Database user accounts must be strictly segmented into:
  1. **Migration / Schema User (Admin):** Allowed `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`. Used exclusively in CI/CD release pipelines.
  2. **Application Runtime User (DML Only):** Granted `SELECT`, `INSERT`, `UPDATE`, `DELETE` only on specific application tables. Prohibited from modifying schemas or database users.
  3. **Read-Only Analytics / Audit User:** Granted `SELECT` only, with connections routed to read replicas.

---

## 3. Container Runtime Least Privilege (PRIN-SEC-01)

### Rule 3.1: Non-Root Execution & Capability Dropping
- Container execution specifications must enforce:
  1. Explicit non-root user identifier (e.g. `USER 10001:10001` in Dockerfile, `runAsNonRoot: true`, `runAsUser: 10001` in Kubernetes).
  2. Linux capabilities dropped completely: `drop: ["ALL"]`, adding back only if strictly required (e.g. `NET_BIND_SERVICE`).
  3. Read-only root filesystem: `readOnlyRootFilesystem: true`, mounting ephemeral storage only at `/tmp` (`tmpfs`).

---

## 4. Least Common Mechanism Isolation (PRIN-SEC-07)

### Rule 4.1: Cryptographic Separation of Multi-Tenant Data
- Multi-tenant data stores must not rely on a single shared key without cryptographic domain separation:
  1. Enforce envelope encryption using tenant-specific Key Encryption Keys (KEKs) or AWS KMS with mandatory `EncryptionContext: { "TenantId": "..." }`.
  2. Prevent shared ambient state: message queues and caching layers must isolate tenant payloads using tenant-prefixed keys or partitioned channels.
