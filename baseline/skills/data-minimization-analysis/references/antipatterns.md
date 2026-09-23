# Anti-Patterns & Smells — Data Minimization & Privacy Balance

Concrete architectural smells and code anti-patterns that lead to data over-collection, mass assignment, and sensitive field leakage.

---

## 1. Mass Assignment via Unfiltered Ingress

### Bad Pattern: Spreading Request Body into Database Model

```javascript
// Express.js handler
app.post('/api/v1/users/profile', async (req, res) => {
    const user = await User.findByPk(req.user.id);
    // SMELL: Mass assignment vulnerability. Client can pass { role: "admin", is_verified: true }
    await user.update(req.body);
    res.json(user);
});
```

**Consequence:** Attackers send malicious JSON properties (`role: "admin"`, `credit_balance: 999999`) to escalate privileges or bypass payment gates.

**Hardened Pattern:**

```typescript
// Explicit schema parsing with Zod
const UpdateProfileSchema = z.object({
    displayName: z.string().min(1).max(50).optional(),
    avatarUrl: z.string().url().optional()
}).strict(); // Rejects any extra fields

app.post('/api/v1/users/profile', async (req, res) => {
    const validatedData = UpdateProfileSchema.parse(req.body);
    const user = await User.findByPk(req.user.id);
    await user.update(validatedData);
    res.json({
        id: user.id,
        displayName: user.displayName,
        avatarUrl: user.avatarUrl
    });
});
```

---

## 2. Raw Database Model Serialization (Egress Leakage)

### Bad Pattern: Returning SQLAlchemy Model in API Response

```python
@app.get("/api/v1/projects/{project_id}")
def get_project(project_id: str, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    # SMELL: Serializes all relationships, including tenant encryption keys and creator metadata
    return project.__dict__
```

**Consequence:** Internal database columns, soft-deleted flags, audit trails, and encrypted secrets are dumped into JSON responses.

**Hardened Pattern:**

```python
class ProjectSummaryResponse(BaseModel):
    id: str
    title: str
    status: str
    task_count: int

@app.get("/api/v1/projects/{project_id}", response_model=ProjectSummaryResponse)
def get_project(project_id: str, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return ProjectSummaryResponse(
        id=project.id,
        title=project.title,
        status=project.status,
        task_count=len(project.tasks)
    )
```

---

## 3. PII in Application Logging & Error Trackers

### Bad Pattern: Logging User Objects and Query Parameters

```python
# Application logger
logger.info(f"Failed login attempt for user: {user.__dict__} with headers: {request.headers}")
```

**Consequence:** Passwords, Authorization tokens, and sensitive PII are persisted to plain-text log files, SIEM systems, and third-party monitoring platforms.

**Hardened Pattern:**

```python
# Structured logging with explicit masking
logger.warning(
    "Failed login attempt",
    extra={
        "event": "auth_failure",
        "actor_ip_hash": hash_ip(request.remote_addr),
        "username_attempted": mask_email(request.json.get("username")),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
)
```
