# End-to-End Case Studies — Trust Boundary & Complete Mediation

Realistic before-and-after architecture scenarios demonstrating trust boundary demarcation and complete mediation.

---

## Case Study 1: Asynchronous Worker & Queue Boundary Remediation

### Context
A document conversion platform processes user uploaded files asynchronously via a background task queue (RabbitMQ / SQS).

### Initial (Flawed) Architecture

```mermaid
flowchart TD
    User["Browser Client"]
    Web["Web API Service"]
    Queue["Task Message Queue"]
    Worker["Background PDF Converter"]
    S3[("S3 Storage Bucket")]
    DB[("Customer DB")]

    User -->|"1. POST /convert (File Upload)"| Web
    Web -->|"2. Write file directly"| S3
    Web -->|"3. Push message: { s3_key, user_id }"| Queue
    Queue -->|"4. Consume message"| Worker
    Worker -->|"5. Fetch S3 Object"| S3
    Worker -->|"6. Direct SQL write (App DB Superuser)"| DB
```

### Analysis & Vulnerability Findings

1. **Missing Boundary Isolation on Storage (`PRIN-MOD-01`):**  
   Both `Web` and `Worker` use shared AWS IAM credentials with full read/write access to the entire `S3` bucket. If the worker's PDF parser is compromised (e.g. via an ImageMagick or Ghostscript vulnerability), the attacker has full read/write access to all tenants' uploaded files.
2. **Missing Complete Mediation on Asynchronous Jobs (`PRIN-SEC-02`):**  
   The message queue payload contains unverified `s3_key` and `user_id`. An attacker able to publish to the queue can direct the worker to process arbitrary files or overwrite arbitrary records.
3. **Privilege Over-Assignment on Data Store (`PRIN-SEC-04`):**  
   The worker uses the database superuser connection, allowing it to modify user account tables, billing data, or schemas, none of which are required for document conversion.

---

### Remediated Architecture

```mermaid
flowchart TD
    subgraph IngressTier ["Zone 1: Web Ingress"]
        User["Browser Client"]
        Web["Web API Service<br>(IAM: PutObject Only)"]
    end

    subgraph QueueTier ["Zone 2: Decoupled Queue"]
        Queue["Signed Message Queue<br>(HMAC Signature Verified)"]
    end

    subgraph SandboxTier ["Zone 3: Isolated Worker Sandbox"]
        Worker["PDF Converter Container<br>(Non-root, No DB Write, Read-Only FS)"]
    end

    subgraph StorageTier ["Zone 4: Scoped Storage & Results DB"]
        S3In[("S3 Inbound Bucket<br>(Tenant Scoped Prefixes)")]
        S3Out[("S3 Outbound Results Bucket")]
        DB[("Conversion Status DB<br>(Role: worker_status_writer)")]
    end

    User -->|"1. HTTPS / JWT"| Web
    Web -->|"2. Scoped PutObject"| S3In
    Web -->|"3. Sign & Publish Job"| Queue
    Queue -->|"4. Verify Signature & Consume"| Worker
    Worker -->|"5. Scoped GetObject"| S3In
    Worker -->|"6. Write Output PDF"| S3Out
    Worker -->|"7. INSERT INTO task_status"| DB
```

### Remediation Ledger

| Component / Boundary | Initial State | Finding | Remediated State | Principle |
|---|---|---|---|---|
| Ingress $\rightarrow$ S3 | Global bucket write | Excessive blast radius | Scoped IAM role: `PutObject` strictly to `inbound/${tenant_id}/*` | `PRIN-SEC-01` |
| Queue Message | Unsigned JSON | Spoofed queue jobs | Message payload cryptographically signed with HMAC secret | `PRIN-MOD-01` |
| Worker Container | Root user, shared DB admin | Sandbox escape risk | Isolated container with read-only rootfs; scoped DB user `worker_status_writer` | `PRIN-SEC-04` |
| Worker $\rightarrow$ DB | Full read/write | Unauthorized data access | Restricted DB role: `INSERT, UPDATE (status)` on `task_status` table only | `PRIN-SEC-02` |
