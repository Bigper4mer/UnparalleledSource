# UNPS Prompt & Agent Engineering Library Index

Status: Candidate  
Version: 0.2.0  
Updated: 2026-08-24  
Owner: Unparalleled Source

## Purpose

This index is the canonical routing map for reusable prompts, skills, workflows, connector profiles, dependencies, output schemas, evaluations, and deployable Custom Agent builds.

## Routing order

1. Resolve the client, project, opportunity, or Internal scope.
2. Classify the task and required evidence depth.
3. Select the narrowest applicable Custom Agent or system instruction.
4. Load one applicable workflow.
5. Load only the skills required by that workflow.
6. Resolve preferred connectors, models/harnesses, and dependencies.
7. Apply the target output schema.
8. Verify and route the result.
9. Run relevant evaluations before promoting reusable changes.

## Library map

- `00_README` — governance, index, bootstrap, naming, changelog
- `01_SYSTEM_INSTRUCTIONS` — reusable system-level instruction sets
- `02_PROMPTS` — task prompts and source references
- `03_SKILLS` — modular capability instructions
- `04_MCP_CONNECTORS` — preferred tools, connectors, model/harness routing, MCP profiles
- `05_WORKFLOWS` — repeatable multi-step operating procedures
- `06_DEPENDENCIES` — packages, APIs, plugins, repositories, external services
- `07_TEMPLATES` — reusable authoring templates and manifests
- `08_OUTPUT_SCHEMAS` — document, report, and deliverable structures
- `09_TESTS_EVALS` — regression tests, examples, golden outputs, evaluation rubrics
- `10_CUSTOM_AGENTS` — portable agent builds
- `99_ARCHIVE` — superseded and deprecated assets

## Core control plane

- Bootstrap: `00_README/UNPS_AGENT_BOOTSTRAP.md`
- File routing: `03_SKILLS/Document_Creation/Information_Architecture/FILE_ROUTING_AND_WORKSPACE_STANDARD.md`
- Continuous learning: `03_SKILLS/Document_Creation/Learning_Growth/CONTINUOUS_LEARNING_AND_GROWTH_LOOP.md`
- Model/harness router: `04_MCP_CONNECTORS/Models_Harnesses/MODEL_HARNESS_ROUTER.md`
- Connector registry: `04_MCP_CONNECTORS/MCP_REGISTRY.md`
- Prompt Database workflow: `05_WORKFLOWS/Agent_Control_Plane/PROMPT_DATABASE_AGENT_CONTROL_PLANE.md`
- Workspace hygiene: `05_WORKFLOWS/Workspace_Maintenance/WORKSPACE_HYGIENE_WORKFLOW.md`
- Prompt Database evaluation: `09_TESTS_EVALS/Prompt_Tests/PROMPT_DATABASE_AGENT_ACCEPTANCE_EVAL.md`

## Current seed assets

### Prompts

- `Research_SWOT`
- `SEO`
- `Video_Cinematography`

### Skill groups

- Research
- Coding
- Government Contracting
- Procurement
- Document Creation
- Token Efficiency
- Cinematography

### Workflow groups

- Agent Control Plane
- Workspace Maintenance
- Opportunity Capture
- Proposal Production
- Market Research
- Document Production
- Software Development

### Connector groups

- Google Workspace
- GitHub
- Firecrawl
- Research Sources
- Models and Harnesses
- MCP Profiles

### Custom Agent builds

- `UNPS_HiveForge` — deployment-ready Candidate, v0.3.0; technical role: Prompt Database Agent
- `Government_Capture_Agent` — Candidate shell
- `Research_Intelligence_Agent` — Candidate shell
- `Coding_Agent` — Candidate shell
- `Document_Production_Agent` — Candidate shell

## UNPS HiveForge package

Minimum startup set:

`BRAIN.md → AGENT.md → SYSTEM_INSTRUCTIONS.md → PACKAGE_MANIFEST.md`

All skills, workflows, connector preferences, dependencies, schemas, and evaluations load on demand. The package contains 13 required files and references shared library policies rather than copying them.

## Promotion rule

Do not promote an asset to Production merely because it sounds useful. A production candidate must demonstrate reuse, predictable quality, explicit dependencies, defined failure behavior, safe tool routing, human-readable placement, and passing representative evaluations.

## Context-efficiency rule

Reference shared skills and workflows instead of copying them into every agent. Load only what the current task requires. Prefer minimal dependencies and avoid overlapping connectors when one trusted capability covers the job.

## Canonical format

Markdown is the canonical agent-readable format. Google Docs may be maintained as human-facing companions. PDFs are reference or published artifacts, not the only canonical source.
