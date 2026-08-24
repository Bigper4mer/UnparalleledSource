# ToolJet Agent & Capability Registry

Status: IMPLEMENTATION-READY / STAGED  
Version: 0.1.0  
Owner: Unparalleled Source  
Updated: 2026-08-24

## Purpose

Provide a human-facing control surface over the UNPS agent ecosystem without making ToolJet the source of truth. The registry exposes agents, skills, workflows, dependencies, connectors, commands, maturity states, test evidence, promotion queues, and capability gaps in one maintainable interface.

## Architecture boundary

**ToolJet = presentation + controlled workflow layer.**

Canonical authority remains in BRAIN.md, Markdown manifests, reviewed project files, and approved backend records. ToolJet page JavaScript must not contain provider secrets, database owner credentials, unrestricted API keys, or canonical policy logic.

## Data flow

```text
PROMPTS.UNPS Markdown + approved runtime facts
              ↓
        Registry compiler/sync
              ↓
      Normalized backend views
              ↓
   ToolJet Agent & Capability Registry
              ↓
 draft/staged admin requests only
              ↓
 policy-enforced backend functions
              ↓
 reviewed Markdown/backend update
```

## Minimum data model

### agents

`agent_id`, `name`, `purpose`, `status`, `version`, `owner`, `brain_version`, `default_harness_role`, `workspace_path`, `last_validated_at`

### capabilities

`capability_id`, `name`, `category`, `status`, `description`, `canonical_path`, `preferred_for`, `fallback_capability_id`, `last_validated_at`

### agent_capabilities

`agent_id`, `capability_id`, `requirement`, `trigger_condition`, `notes`

### dependency_tests

`test_id`, `capability_id`, `test_type`, `result`, `tested_version`, `tested_at`, `evidence_path`, `environment`, `failure_reason`

### promotion_queue

`request_id`, `capability_id`, `from_status`, `requested_status`, `reason`, `required_checks`, `approval_status`, `requested_by`, `reviewed_by`, `created_at`

## Registry compiler contract

The compiler reads canonical Markdown metadata and produces normalized rows. It must:

1. preserve canonical file paths/URLs;
2. never infer CORE status when status is absent;
3. surface malformed/duplicate IDs as errors;
4. retain provenance for every row;
5. support dry-run validation before writes;
6. never delete a canonical asset because a sync row disappeared without explicit archive/deprecation.

## ToolJet page layout

Main tabs:

1. **Agents** — agent builds and attached capability matrix.
2. **Capabilities** — skills/tools/APIs/connectors/CLIs/services with status and fallback.
3. **Dependencies** — install/setup, current state, last test, promotion gate.
4. **Tests & Evidence** — latest regression/integration result and evidence links.
5. **Promotion Queue** — staged/candidate changes awaiting review.
6. **Routing Simulator** — show which capabilities BRAIN would select; simulation only, no automatic execution.

## Query contract

Reads use `get_`, validated mutations use `do_`, draft/staged operations use `stage_`, and approvals use `approve_`.

Required reads:

- `get_registry_health`
- `get_agents`
- `get_capabilities`
- `get_agent_capability_matrix`
- `get_dependency_tests`
- `get_promotion_queue`
- `get_capability_detail`
- `get_routing_simulation`

Controlled writes:

- `stage_capability_status_change`
- `stage_dependency_test_result`
- `stage_agent_capability_change`
- `approve_capability_promotion`
- `do_refresh_registry`

No ToolJet query may directly mutate arbitrary Markdown files or bypass the reviewed backend/service boundary.

## Permissions

Suggested roles:

- **Viewer** — read registry and evidence.
- **Operator** — refresh and create staged test/status requests.
- **Reviewer** — approve candidate/staged promotion after gates pass.
- **Admin** — manage registry mappings and integrations.

Server-side authorization remains mandatory even when UI components are hidden.

## Acceptance test

PASS requires:

- every seeded agent is visible;
- every seeded capability has a maturity state and canonical source;
- agent→capability relationships render correctly;
- stale and failed test states are visibly distinct;
- unauthorized promotion fails server-side;
- an authorized reviewer can approve a staged status request through a validated function;
- registry refresh does not overwrite canonical policy directly;
- missing backend returns last-good/stale state rather than false success;
- routing simulation returns a capability path without executing tools;
- no credential appears in browser storage, page JS, exports, or logs.

## Promotion rule

ToolJet may move from STAGED to CORE for the registry cockpit only after the page is backed by canonical registry data, role enforcement is tested, and at least one real dependency promotion request completes through the controlled workflow.
