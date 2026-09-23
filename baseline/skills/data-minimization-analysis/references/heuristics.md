# Analytical Heuristics — Data Minimization & Privacy Balance

Technology-agnostic heuristics for inspecting functional Use Cases (`UC-*`) against `PRIN-ENG-06`.

---

## 1. Ingress Minimization in Use Cases (PRIN-ENG-06)

### Rule 1.1: The Indispensability Test
- For every data attribute specified in a use case step:
  $$\text{IsEssential}(\mathtt{Attribute}, \mathtt{UseCaseGoal}) \implies \mathtt{RETAIN}$$
  $$\neg\text{IsEssential}(\mathtt{Attribute}, \mathtt{UseCaseGoal}) \implies \mathtt{FLAG\_FOR\_REMOVAL}$$
- Collecting data for speculative future analytics or marketing without explicit functional necessity violates `PRIN-ENG-06`.

### Rule 1.2: Proportionality in Onboarding
- Unauthenticated visitors or new users must not be required to provide high-impact identifiers (national ID, physical address, biometric markers) when establishing basic software accounts.

---

## 2. Egress Scoping & Persona-Based Projection (PRIN-ENG-06)

### Rule 2.1: Scoped Presentation to Secondary Actors
- When a use case displays data to secondary actors (e.g. collaborators on a shared board):
  1. The displayed representation must project only public attributes (e.g. display name, avatar).
  2. Direct contact channels (personal email, phone) and internal security telemetry must be excluded from collaborator views.

### Rule 2.2: Data Coarsening
- Where contextual information (location, device time) is used to adapt system presentation, the use case must specify coarse attributes (e.g. country code) rather than precise geographic coordinates.
