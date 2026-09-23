# Anti-Patterns & Smells — Least Privilege & Shared Mechanism

Concrete configuration smells and architectural anti-patterns violating least privilege and least common mechanism.

---

## 1. Container Root Execution & Docker Socket Mounting

### Bad Pattern: Root Container with Host Docker Socket

```yaml
# docker-compose.yml
services:
  monitoring-agent:
    image: custom-agent:latest
    user: root # SMELL: Runs with UID 0
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock # SMELL: Full host control
    privileged: true # SMELL: Disables all kernel security controls
```

**Consequence:** A compromise of `custom-agent` gives the attacker instant root access to the entire host operating system and all other co-located containers.

**Hardened Pattern:**

```yaml
# docker-compose.yml
services:
  monitoring-agent:
    image: custom-agent:latest
    user: "10001:10001"
    read_only: true
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
    # Hardened: No docker.sock mount; uses read-only cgroup metrics interface
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:ro
```

---

## 2. Shared Database Superuser Connection

### Bad Pattern: Application Using Postgres Superuser

```env
# .env application configuration
DATABASE_URL=postgresql://postgres:master_password@db-host:5432/tinytask_prod
```

**Consequence:** A single SQL injection flaw in any endpoint allows an attacker to execute administrative functions, write to the host filesystem via `pg_read_file` / `COPY`, or drop entire databases.

**Hardened Pattern:**

```sql
-- Database role hardening script
CREATE ROLE tinytask_app WITH LOGIN PASSWORD 'app_secure_password';

-- Grant only required table-level DML
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO tinytask_app;
REVOKE CREATE ON SCHEMA public FROM tinytask_app;
REVOKE ALL PRIVILEGES ON DATABASE tinytask_prod FROM tinytask_app;
```

```env
# Hardened connection string
DATABASE_URL=postgresql://tinytask_app:app_secure_password@db-host:5432/tinytask_prod
```

---

## 3. Shared Cryptographic Master Key Across Tenants

### Bad Pattern: Single Global Encryption Key Without Context

```python
# Encrypting tenant files using a static key without tenant separation
def encrypt_tenant_file(file_bytes):
    # SMELL: Shared mechanism. A key leak compromises all tenants simultaneously
    cipher = Fernet(GLOBAL_SECRET_KEY)
    return cipher.encrypt(file_bytes)
```

**Consequence:** If one tenant's ciphertext is tampered with or if access is obtained by an insider, all tenant data is compromised simultaneously without cryptographic provenance.

**Hardened Pattern:**

```python
# Envelope encryption with mandatory tenant encryption context in KMS
def encrypt_tenant_file(file_bytes, tenant_id):
    kms_client = boto3.client('kms')
    response = kms_client.generate_data_key(
        KeyId='alias/tinytask-data-kek',
        KeySpec='AES_256',
        EncryptionContext={'TenantId': tenant_id} # Hardened cryptographic binding
    )
    dek = response['Plaintext']
    encrypted_dek = response['CiphertextBlob']
    
    # Encrypt file locally with DEK
    nonce = os.urandom(12)
    cipher = AESGCM(dek)
    ciphertext = cipher.encrypt(nonce, file_bytes, tenant_id.encode('utf-8'))
    
    return {
        'encrypted_dek': base64.b64encode(encrypted_dek).decode(),
        'nonce': base64.b64encode(nonce).decode(),
        'ciphertext': base64.b64encode(ciphertext).decode()
    }
```
