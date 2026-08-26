# UNPS HiveForge — Package Manifest

id: UNPS-AGENT-PROMPTDB-001  
name: UNPS HiveForge  
role: Prompt Database Agent  
version: 0.7.0
status: production  
owner: Unparalleled Source  
updated: 2026-08-24

## Purpose

This manifest is the compact routing map for the deployable Prompt Database Agent. It identifies what must load at startup, what remains shared in `PROMPTS.UNPS`, and what should load only when the active task requires it.

## Minimum startup set

Load in this order:

1. `BRAIN.md`
2. `AGENT.md`
3. `SYSTEM_INSTRUCTIONS.md`
4. `PACKAGE_MANIFEST.md`

Then load a validated user working profile when relevant, resolve project/client scope, and hydrate only the workflow-specific assets needed for the task.

## Package files

| File | Function | Load policy |
|---|---|---|
| `README.md` | Human landing page | Human/onboarding |
| `BRAIN.md` | Portable orchestration contract | Always |
| `AGENT.md` | Identity, mission, scope | Always |
| `SYSTEM_INSTRUCTIONS.md` | Persistent operating policy | Always |
| `PACKAGE_MANIFEST.md` | Package routing and integrity | Always |
| `SKILLS.md` | Skill resolver | On demand |
| `WORKFLOWS.md` | Workflow resolver | On demand |
| `MCP_PREFERENCES.md` | Connector/tool routing | On demand |
| `DEPENDENCIES.md` | Runtime and optional capability requirements | On demand |
| `OUTPUT_SCHEMAS.md` | Output selection and minimum contracts | On demand |
| `TOOL_POLICY.md` | Permission, evidence, and mutation rules | Before tool use |
| `INSTALL.md` | Deployment and validation | Installation |
| `CHANGELOG.md` | Material package history | Maintenance |

## Canonical shared references

- Library governance: `00_README/README.md` and `00_README/LIBRARY_INDEX.md`
- Bootstrap: `00_README/UNPS_AGENT_BOOTSTRAP.md`
- User onboarding: `docs/GETTING_STARTED.md` and `docs/USER_INTAKE.md`
- Workflow selection: `docs/WORKFLOW_GUIDE.md`
- Command reference: `docs/COMMAND_REFERENCE.md`
- Tool/capability guide: `docs/TOOLING_GUIDE.md`
- ToolJet setup: `docs/TOOLJET_SETUP.md`
- File routing: `03_SKILLS/Document_Creation/Information_Architecture/FILE_ROUTING_AND_WORKSPACE_STANDARD.md`
- Continuous learning: `03_SKILLS/Document_Creation/Learning_Growth/CONTINUOUS_LEARNING_AND_GROWTH_LOOP.md`
- Model routing: `04_MCP_CONNECTORS/Models_Harnesses/MODEL_HARNESS_ROUTER.md`
- Connector registry: `04_MCP_CONNECTORS/MCP_REGISTRY.md`
- Workspace hygiene: `05_WORKFLOWS/Workspace_Maintenance/WORKSPACE_HYGIENE_WORKFLOW.md`
- Prompt Database control plane: `05_WORKFLOWS/Agent_Control_Plane/PROMPT_DATABASE_AGENT_CONTROL_PLANE.md`
- ToolJet registry contract: `05_WORKFLOWS/Agent_Control_Plane/TOOLJET_AGENT_CAPABILITY_REGISTRY.md`
- Dependency maturity: `06_DEPENDENCIES/DEPENDENCY_STATUS_MANIFEST.md`
- Graphify capability: `06_DEPENDENCIES/Python/CLI_Tools/Graphify/GRAPHIFY_CAPABILITY.md`
- Media ingestion policy: `06_DEPENDENCIES/Python/CLI_Tools/Media_Ingestion/MEDIA_INGESTION_TOOLING.md`
- Composio staging: `06_DEPENDENCIES/External_Services/Agent_Orchestration/COMPOSIO_STAGING.md`
- LangGraph staging: `06_DEPENDENCIES/External_Services/Agent_Orchestration/LANGGRAPH_STAGING.md`
- Acceptance evaluation: `09_TESTS_EVALS/Prompt_Tests/PROMPT_DATABASE_AGENT_ACCEPTANCE_EVAL.md`
- v0.7.0 production evidence: `09_TESTS_EVALS/Prompt_Tests/PRODUCTION_ACCEPTANCE_MATRIX_v0.7.0.md`

## Integrity rules

- The shared library remains canonical; this package composes it by reference.
- Package-local files may summarize routing but must not fork shared policies silently.
- Material behavioral changes require a version bump and changelog entry.
- HiveForge v0.7.0 Production status is tied to its recorded release evidence and green Production Gate.
- Credentials, access tokens, private keys, regulated data, client/opportunity records, and private connector exports never belong in the public package.
- Optional dependencies remain optional unless their own promotion gate explicitly moves them to CORE.
