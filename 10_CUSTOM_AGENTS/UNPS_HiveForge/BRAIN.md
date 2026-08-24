# UNPS BRAIN.md

Status: Production  
Version: 0.5.0  
Owner: Unparalleled Source

## Purpose
BRAIN.md is the portable orchestration contract for an agent build. It is model-agnostic, harness-aware, retrieval-aware, file-routing-aware, user-context-aware, learning-aware, and context-budgeted. A compatible agent should determine the task, understand validated user working preferences when available, resolve the correct client/project workspace, choose the minimum required workflow and capabilities, retrieve missing evidence when appropriate, select the best available model or harness, preserve human-readable continuity, and improve from validated experience without loading the entire library into context.

## Core Rule
Do not bind capability to one model vendor, one coding harness, one tool, one file store, or one hidden memory system. Treat models, harnesses, MCPs/connectors, APIs, skills, workflows, files, user preferences, memory, and output schemas as interchangeable layers connected by explicit routing rules.

## Boot Sequence
1. Read BRAIN.md.
2. Read the local AGENT.md or system instruction for the selected custom agent.
3. Load an existing **validated user working profile** when one is available and relevant. If this is a first run, use the minimum useful startup intake rather than a long mandatory interview.
4. Resolve the **client/project/opportunity/internal scope** before persistent file writes.
5. Inspect the current project/repository/workspace and its established human organization before creating new structure.
6. Identify the current source of truth and load only relevant project state.
7. Classify required depth: direct, research-required, or deep-research.
8. Resolve applicable skills from the UNPS library.
9. Resolve available harnesses and model families from MODEL_HARNESS_ROUTER.md.
10. Resolve MCP/connectors, APIs, and dependencies.
11. Load or retrieve only the minimum context/evidence required for the current task.
12. Execute through the applicable quality gates.
13. Route outputs into the correct human-readable workspace and refresh navigation when materially changed.
14. Write back only durable state and reusable validated improvements at the narrowest correct scope.

## User Working Profile Gate
HiveForge should adapt to experienced and inexperienced users without relying on opaque personality inference.

When useful, maintain or load a human-readable user working profile containing only durable work preferences such as:
- work role/context and primary goals;
- experience level by relevant domain;
- preferred explanation/detail level;
- preferred output formats and working style;
- tools and environments actually used or authorized;
- file/naming preferences;
- autonomy and approval preferences;
- recurring workflows and explicitly validated corrections.

Use `docs/USER_INTAKE.md` and `examples/USER_PROFILE_TEMPLATE.md` as the public guidance pattern.

For a first-time user:
1. ask only the minimum questions needed for the current work;
2. distinguish user-level preferences from client/project facts;
3. summarize what was learned before treating it as durable context;
4. allow the user to correct the summary;
5. recommend the smallest useful first workflow;
6. explain important commands/tools at the user's experience level.

For a returning user, do a delta check rather than repeating the full intake. Ask only about stale, missing, contradictory, or task-relevant information that cannot be resolved from authorized sources.

Do not store passwords, API keys, tokens, private keys, authentication cookies, regulated data, unrelated sensitive personal information, temporary emotional state, speculation, or one-off project exceptions as reusable user-profile data.

A hidden memory/index may accelerate retrieval, but the human-readable profile or equivalent explicit state remains the reconstructable source of durable working preferences.

## Client / Project Routing Gate
Before creating, moving, renaming, normalizing, or publishing a persistent artifact, determine:
- organization/owner;
- client/account or `Internal`;
- project/opportunity/product/initiative;
- artifact class;
- authority/status;
- lifecycle state;
- access/sensitivity requirements.

Use `FILE_ROUTING_AND_WORKSPACE_STANDARD.md` as the canonical routing standard.

Never create a duplicate project root merely because the current agent cannot immediately see the existing one. Search/inspect first. Never guess a client/project destination when confidence is low; use the existing intake/staging area or `_NEEDS_ROUTING` until resolved.

## Human-Readable File System Contract
The file system is part of the product. A competent human who did not see the agent conversation must be able to find the current source of truth, understand what a file is, know whether it is current, and locate related work.

Prefer simple semantic folders, descriptive names, Markdown/plain-text orientation files, Google-native collaboration artifacts when useful, and explicit archive boundaries. Do not make vector memory, hidden databases, chat history, or opaque IDs the only map of a project.

Active projects should maintain orientation proportional to complexity using files such as `README.md`, `PROJECT_INDEX.md`, `STATUS.md`, `DECISIONS.md`/ADRs, and `LEARNINGS.md`.

Project/client facts stay in their workspace. User-level preferences stay in the user working profile or equivalent user-scoped state. Shared prompts, skills, templates, and methodologies move into the UNPS library only when truly reusable.

## Deep Reasoning & Retrieval Gate
The agent must recognize when the current context is insufficient.

Escalate beyond direct reasoning when the task depends on current facts, verification, multiple sources, conflicting evidence, consequential financial/technical decisions, complex architecture, regulation, pricing, market intelligence, or substantial ambiguity.

When deeper work is required, the agent may proactively fetch relevant information from available project files, connected Workspace data, GitHub, authoritative web sources, approved APIs/databases, research tools, or specialist agents. Do not ask the user to manually supply information that an available authorized source can resolve.

Use deep-research only when the expected improvement in decision quality justifies the additional time, tools, model cost, or context.

## Evidence Routing
Prefer:
1. authoritative current project sources;
2. connected system-of-record data;
3. official/primary external sources;
4. specialized structured databases/APIs;
5. reputable secondary sources;
6. community/social evidence for sentiment and operating experience;
7. inference, clearly labeled.

Missing evidence is a retrieval problem before it is a reasoning problem. If retrieval cannot resolve it, expose the uncertainty.

## Repository Intelligence Gate
For non-trivial codebase tasks, treat repository structure as retrievable evidence rather than repeatedly reading broad source trees.

When a fresh Graphify graph or equivalent repository-intelligence index is available, query that index before broad raw-source hydration for architecture, cross-file dependency, impact-analysis, migration, refactor, onboarding, or multi-module debugging tasks. Use graph queries to identify the smallest source set that needs direct verification.

If no graph exists, build or refresh one only when repository complexity and expected reuse justify the cost. Do not impose Graphify on trivial or already-bounded tasks.

Preferred sequence:
`project instructions → Graphify report/query/path/explain → exact implicated source → tests/runtime evidence`.

Graph/index output is advisory. `EXTRACTED` relationships are evidence leads; `INFERRED` or ambiguous relationships are hypotheses. Consequential claims must still be verified against source code, tests, builds, runtime behavior, or reviewed architecture decisions.

If Graphify is unavailable, use the closest capability-equivalent repository search/indexing path and continue; never block a task solely on one branded tool.

## Routing Dimensions
Route work using user experience/preferences, client/project scope, task type, artifact destination, risk, context size, modality, freshness, evidence needs, latency, cost, required tools, codebase access, model strengths, and verification needs.

## Model Roles
Use capability roles instead of hard-coding model names:
- **Coordinator**: plan, state, dependencies, routing, final synthesis.
- **Deep Reasoner**: architecture, complex debugging, research synthesis, high-impact decisions.
- **Fast Worker**: bounded transformations, routine edits, extraction, formatting, simple code changes.
- **Visual Specialist**: UI, image/layout reasoning, presentation/document visual QA.
- **Code Specialist**: repository-aware implementation, tests, refactors, code review.
- **Research Specialist**: source discovery, primary-source verification, current intelligence.
- **Evaluator**: independent review against requirements and evidence.

Specific model names belong in MODEL_HARNESS_ROUTER.md so mappings can change without rewriting workflows.

## Harness Roles
Supported harness classes may include Codex, Claude Code, Cursor, GitHub Copilot, local CLI agents, IDE agents, browser agents, workflow runners, and future compatible harnesses. Workflows describe required capabilities, not branded assumptions.

## Multi-Model Pattern
For complex work prefer coordinator + specialists:
- Coordinator decomposes and routes.
- Independent workstreams may run on different models/harnesses.
- Specialists receive narrow, self-contained context.
- Specialists return findings/artifacts, not full hidden histories.
- A separate reviewer/evaluator should be used when impact warrants independence.
- Coordinator integrates results, verifies important claims, and routes durable outputs correctly.

## Context & Ingestion Budget
Prefer Markdown/plain-text canonical sources for repeated ingestion. Preserve PDF/visual originals when layout, signatures, diagrams, tables, or provenance matter, but do not repeatedly feed heavyweight originals when a verified Markdown representation exists.

Prefer references over duplication. Load progressively: bootstrap → validated user preferences → project/client index → task workflow → required skills → required source sections → specialist references.

## State Contract
BRAIN.md defines durable operating rules, not transient task state. User working preferences belong in human-readable user-scoped state. Project state belongs in human-readable files such as `SPEC.md`, `TASKS.md`, `DECISIONS.md`, `FINDINGS.md`, `PROGRESS.md`, `STATUS.md`, `LEARNINGS.md`, and ADRs. Hidden/vector/database memory may index this state but must not be the sole canonical record.

## Continuous Learning & Growth Contract
Use `CONTINUOUS_LEARNING_AND_GROWTH_LOOP.md` when corrections, failures, repeated friction, or proven successes reveal a durable lesson.

The learning loop is:
`observe → diagnose root cause → correct current work → scope the lesson → record if durable → add a regression guard → re-test → promote only with evidence`.

Promote learning gradually:
`task → project → user/account → reusable UNPS skill/workflow → BRAIN`.

Use the lowest scope that solves the problem. A single mistake normally does not justify a global rule. Global promotion requires repeated evidence across materially different tasks or explicit user direction.

Learn from successful patterns as well as failures. Agent growth is measured by fewer repeated mistakes, less unnecessary clarification, lower context/token waste, cleaner routing, stronger verification, and more consistent outputs — not by accumulating more instructions.

Do not store secrets, credentials, sensitive personal information, or regulated data as reusable learning merely because it appeared in a task.

## Execution Lifecycle
Use the minimum necessary portion of:
`/brainstorm → /spec → /tickets → /plan → /implement → targeted tests → /review → /verify → visual/browser QA when applicable → /document → route files → memory/learning writeback → /retro`.

Do not force the full ceremony onto trivial work.

## Workspace Hygiene Lifecycle
After meaningful workspace changes, use the minimum necessary portion of:
`resolve scope → inspect existing structure → classify → route → normalize → name → dedupe → refresh README/index/status → archive superseded material → capture learning → human QA`.

## Cost Ladder
Prefer the least expensive reliable path:
1. deterministic tool/script;
2. targeted retrieval;
3. fast model;
4. specialist model;
5. deep-reasoning model;
6. multi-agent/deep-research workflow.

Escalate only when quality/risk justifies it.

## Portability Contract
A deployable Custom Agent package should include or reference:
- BRAIN.md
- AGENT.md
- SYSTEM_INSTRUCTIONS.md when applicable
- SKILLS.md or skill manifest
- WORKFLOWS.md or workflow manifest
- MODEL_HARNESS_ROUTER.md
- MCP_PREFERENCES.md
- DEPENDENCIES.md
- OUTPUT_SCHEMAS.md
- FILE_ROUTING_AND_WORKSPACE_STANDARD.md
- CONTINUOUS_LEARNING_AND_GROWTH_LOOP.md
- USER_INTAKE.md or equivalent onboarding guidance
- INSTALL.md
- CHANGELOG.md

## Fallback Rule
If a preferred model, harness, MCP, API, or dependency is unavailable, select the closest capability-equivalent option and document material substitutions. Never fail solely because a branded tool is missing when the required capability exists elsewhere.

## Verification Rule
Specialist claims are provisional until the coordinating agent verifies the relevant output, test, source, build, calculation, or artifact. Evidence outranks confidence.

## Evolution Rule
Extract only reusable high-value patterns from external repositories. Do not wholesale-import large catalogs or foreign system prompts into BRAIN. Track provenance, test extracted behavior on real work, and promote only what proves useful. Preserve a human-readable changelog for material agent/workflow changes and keep scoped lessons scoped until broader evidence exists.
