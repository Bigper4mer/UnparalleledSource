# HiveForge Architecture

## System boundary

HiveForge separates user/project context, orchestration, reusable intelligence, external capabilities, execution state and verification so each layer can change without rewriting the entire agent.

```mermaid
flowchart TD
    U[User working preferences] --> C[Coordinator / BRAIN]
    P[Project / client context] --> C
    C --> R[Scope + depth + risk router]
    R --> A[Agent package]
    A --> W[Workflow]
    W --> S[Skills]
    W --> M[Models + harnesses]
    W --> T[Connectors + dependencies]
    S --> E[Execution]
    M --> E
    T --> E
    E --> Q[Quality gates]
    Q --> O[Artifact / decision / project state]
    Q --> L[Scoped learning]
    L --> U
    L --> P
    L --> S
```

## Human-readable context model

HiveForge does not treat chat history or opaque model memory as the only map of a user or project.

```mermaid
flowchart LR
    A[User working profile] --> B[BRAIN routing]
    C[Project README / PROJECT / STATUS] --> B
    D[DECISIONS / ADRs] --> B
    E[LEARNINGS] --> B
    B --> F[Current task]
    F --> G[Validated updates]
    G --> A
    G --> C
    G --> D
    G --> E
```

User-level preferences and project/client facts remain separate. Existing project conventions should be reused instead of forcing `.hiveforge/` or another taxonomy into a healthy workspace.

## Layer model

| Layer | Owns | Must not own |
|---|---|---|
| User profile | Durable working preferences | Secrets, unrelated sensitive personal data, client facts |
| Project state | Scope, status, decisions, findings, project learning | Universal behavior rules |
| Brain | Durable orchestration and routing rules | Project-specific task state |
| Agent package | Identity, scope, package composition | Shared asset duplication |
| Workflow | Ordered execution and checkpoints | Hard-coded vendor assumptions |
| Skill | Reusable capability instructions | Transient client facts |
| Connector profile | Tool selection, permissions, fallbacks | Credentials |
| Dependency manifest | Runtime and optional requirements | Hidden installation side effects |
| Output schema | Deliverable structure and required evidence | Unsupported claims |
| Evaluation | Acceptance tests and regression guards | Self-certified confidence |
| Command Center | Sanitized run telemetry and operator approvals | Prompt content, credentials, authoritative business records |
| ToolJet cockpit | Shared visual registry/control surface | Canonical BRAIN or unrestricted direct mutations |

## Runtime observability

The built-in Command Center uses a dependency-free local runtime for immediate deployment. Instrumented commands and external agent hosts emit lifecycle events to a bounded JSON state store. The localhost dashboard reads that store and exposes session-token-protected approval decisions.

```mermaid
flowchart LR
    A[Agent or command] --> R[HiveForge runtime]
    R --> S[Bounded state store]
    S --> D[Local Command Center]
    D --> R
```

Lifecycle vocabulary includes:

```text
started
progress
heartbeat
approval requested
approval decided
completed
failed
```

## Shared operations with ToolJet

ToolJet can add a team-facing control surface without becoming the source of truth.

```mermaid
flowchart TD
    H[Human team] --> T[ToolJet]
    T --> RV[Registry read views]
    T --> SM[Staged mutations]
    SM --> PG[Policy / approval gate]
    RV --> C[Canonical registry + runtime facts]
    PG --> C
    C --> B[BRAIN / Markdown / backend records]
```

See [`TOOLJET_SETUP.md`](TOOLJET_SETUP.md).

## Progressive disclosure

HiveForge loads context in stages:

```text
BRAIN
→ agent identity/system policy/package manifest
→ validated user working preferences
→ project/client index and source of truth
→ applicable workflow
→ required skills
→ exact source sections
→ required connectors/dependencies
→ output schema
```

The agent should not hydrate the next layer until the task demonstrates a need for it.

## Evidence ladder

1. Authoritative project sources
2. Connected systems of record
3. Official or primary external sources
4. Specialized structured databases
5. Reputable secondary sources
6. Community evidence for sentiment and operating experience
7. Clearly labeled inference

## Cost ladder

1. Deterministic operation
2. Targeted retrieval
3. Fast worker
4. Specialist model
5. Deep reasoner
6. Coordinated multi-specialist workflow

Escalation is based on risk and expected quality improvement—not habit.

## Recommended workflow lifecycle

```mermaid
flowchart LR
    A[Discover] --> B[Brainstorm]
    B --> C[Spec]
    C --> D[Tickets]
    D --> E[Plan]
    E --> F[Implement]
    F --> G[Test]
    G --> H[Review]
    H --> I[Verify]
    I --> J[Document]
    J --> K[Retro / learning]
```

Use only the necessary portion for the task.

## Learning loop

```mermaid
flowchart TD
    A[Observe] --> B[Diagnose]
    B --> C[Correct current work]
    C --> D{Durable lesson?}
    D -->|No| E[Keep local]
    D -->|Yes| F[Scope it]
    F --> G[Record human-readably]
    G --> H[Add regression guard when warranted]
    H --> I[Re-test]
    I --> J[Promote only with evidence]
```

Learning moves upward gradually:

```text
task
→ project
→ user/account
→ reusable skill/workflow
→ BRAIN only when truly universal
```

## User journey

```mermaid
flowchart LR
    A[Install] --> B[Doctor]
    B --> C[Bootstrap]
    C --> D[Startup intake]
    D --> E[Project inspection]
    E --> F[Workflow recommendation]
    F --> G[First task]
    G --> H[Verification]
    H --> I[Validated learning]
```

See [`GETTING_STARTED.md`](GETTING_STARTED.md) for the full guided path.