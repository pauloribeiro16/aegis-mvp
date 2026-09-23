# End-to-End Case Studies — Least Privilege & Shared Mechanism

Realistic before-and-after scenarios evaluating cloud IAM, container workloads, and cryptographic key custody.

---

## Case Study 1: Multi-Tenant Cloud Architecture & Kubernetes Workload

### Context
A microservice running on AWS EKS processes sensitive customer financial reports.

### Initial Configuration (Over-Privileged)

#### 1. Kubernetes Pod Specification
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: report-generator
spec:
  containers:
    - name: generator
      image: company/report-gen:v1.2
      # SMELL: Runs as root, write access to root filesystem, full host network
      hostNetwork: true
      securityContext:
        privileged: true
```

#### 2. IAM Role for Service Accounts (IRSA)
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:*",
        "kms:*"
      ],
      "Resource": "*"
    }
  ]
}
```

### Analysis & Vulnerabilities
1. **Privileged Pod Execution (`PRIN-SEC-01`):** `privileged: true` disables AppArmor and seccomp profiles, mounts all host devices, and allows container escape directly to the underlying EC2 node.
2. **Global IAM Actions (`PRIN-SEC-01`):** `s3:*` allows destroying production buckets.
3. **Shared Mechanism Compromise (`PRIN-SEC-07`):** Unconstrained `kms:*` allows decrypting records belonging to other services in the AWS organization.

---

### Remediated Hardened Configuration

#### 1. Kubernetes Pod Specification
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: report-generator
spec:
  automountServiceAccountToken: false
  securityContext:
    runAsNonRoot: true
    runAsUser: 10001
    runAsGroup: 10001
    fsGroup: 10001
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: generator
      image: company/report-gen:v1.2
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop:
            - ALL
      volumeMounts:
        - name: ephemeral-tmp
          mountPath: /tmp
  volumes:
    - name: ephemeral-tmp
      emptyDir:
        medium: Memory
        sizeLimit: 128Mi
```

#### 2. Scoped AWS IAM Policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowReportS3BucketActions",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::tinytask-reports-prod/reports/${aws:PrincipalTag/TenantId}/*"
    },
    {
      "Sid": "AllowKMSDecryptWithContext",
      "Effect": "Allow",
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "arn:aws:kms:eu-central-1:123456789012:key/report-encryption-key-id",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:Service": "ReportGenerator",
          "kms:EncryptionContext:TenantId": "${aws:PrincipalTag/TenantId}"
        }
      }
    }
  ]
}
```

### Remediation Ledger

| Component | Initial State | Hazard | Remediated State | Principle |
|---|---|---|---|---|
| Container User | Root (UID 0) | Host breakout | Non-root `UID 10001`, `drop: ALL` capabilities | `PRIN-SEC-01` |
| Filesystem | Read-Write rootfs | Persistent malware injection | `readOnlyRootFilesystem: true`, tmpfs memory mount | `PRIN-SEC-01` |
| S3 Storage | `s3:*` on `*` | Data destruction & leakage | `s3:GetObject, s3:PutObject` strictly scoped to tenant folder | `PRIN-SEC-01` |
| KMS Decryption | `kms:*` on `*` | Global key abuse | Restricted to report key + tenant encryption context | `PRIN-SEC-07` |
