# HiveForge Workflow Guide

Use this guide to choose the right operating mode and provide HiveForge with useful inputs without dumping unnecessary context into the conversation.

## Workflow selector

| Goal | Recommended mode | Best first input |
|---|---|---|
| Explore options before acting | `/brainstorm` | Goal + constraints + current state |
| Turn discussion into a buildable definition | `/spec` | Approved direction + requirements + definition of done |
| Break work into bounded implementation units | `/tickets` | Settled spec |
| Decide execution order | `/plan` | Spec/tickets + dependencies/constraints |
| Execute approved work | `/implement` | Approved plan/tickets + target repo/workspace |
| Independently critique work | `/review` | Diff/artifact + requirements |
| Prove completion | `/verify` | Requirements + tests/artifacts/evidence |
| Research a current or uncertain topic | `/research` | Question + decision context + recency requirement |
| Understand unfamiliar code | repository intelligence / Graphify when justified | Repo + architectural question/problem |
| Clean a workspace | workspace hygiene | Canonical folder/repo + desired outcome |
| Produce a client-facing artifact | document production | Source set + audience + decision/output format |
| Improve a README | `/readme` | Repo + target audience + install/use path |
| Produce a diagram | `/diagram` | System/process + intended audience + question the diagram should answer |
| Capture reusable learning | `/retro` | Outcome + failures + corrections + evidence |

## Recommended lifecycle

For meaningful engineering or operational work:

```mermaid
flowchart LR
    A[Discover] --> B[Brainstorm]
    B --> C[Spec]
    C --> D[Tickets]
    D --> E[Plan]
    E --> F[Implement]
    F --> G[Targeted tests]
    G --> H[Review]
    H --> I[Verify]
    I --> J[Document]
    J --> K[Learn / Retro]
```

Do not force every box onto a trivial task.

## 1. Discovery / project startup

Use when HiveForge has entered a new repository, Drive workspace, client folder, or project.

### Recommended inputs

Required:

- project/repository/folder;
- goal;
- what success looks like.

Helpful:

- deadline;
- known source-of-truth files;
- constraints;
- people who review the result;
- actions HiveForge may or may not take.

### Starter prompt

```text
Inspect this workspace before changing anything. Identify its scope, source of truth, current organization, active work, stale or duplicate material, and the smallest workflow/tool set needed for my goal. Tell me what you found and what you recommend next.
```

## 2. `/brainstorm`

Use when the direction is not settled.

### Recommended inputs

- problem or opportunity;
- constraints;
- known alternatives;
- existing architecture/process;
- risk tolerance.

### Expected output

- options;
- trade-offs;
- assumptions;
- recommendation;
- unknowns that require retrieval or testing.

### Example

```text
/brainstorm We need a human-facing dashboard for this agent system. Compare the smallest viable options, reuse what we already have, and do not change files yet.
```

## 3. `/spec`

Use after the desired direction is stable enough to define precisely.

### Recommended inputs

- approved direction;
- users/audience;
- functional requirements;
- non-functional requirements;
- interfaces/data sources;
- definition of done;
- acceptance criteria.

### Expected output

A durable specification that another fresh agent could execute without relying on hidden chat context.

## 4. `/tickets`

Use when the spec is settled and work should be split into manageable slices.

### Recommended inputs

- spec;
- dependencies;
- known migration constraints;
- deployment order if relevant.

### Good ticket rule

Each ticket should fit a fresh context window and produce a testable vertical improvement.

## 5. `/plan`

Use immediately before execution when sequencing matters.

### Recommended inputs

- approved spec/tickets;
- current repository/workspace state;
- risk and rollback requirements;
- environments;
- test strategy.

### Expected output

- ordered steps;
- affected components;
- checkpoints;
- tests;
- rollback/fallback;
- approval gates.

## 6. `/implement`

Use only after intent is sufficiently stable.

### Recommended inputs

- approved ticket/plan;
- target repo/folder;
- test commands;
- coding/project instructions;
- constraints.

### Expected behavior

```text
inspect exact source
→ implement smallest coherent change
→ targeted tests
→ typecheck/build/lint when applicable
→ review diff
→ full verification appropriate to risk
```

Graphify or equivalent repository intelligence should be used only when repository complexity justifies it.

## 7. `/review`

Use an independent reviewer mindset.

### Recommended inputs

- requirements/spec;
- diff or artifact;
- test evidence;
- known risk areas.

Review for correctness, regressions, security, maintainability, scope creep, missing tests and unsupported claims.

## 8. `/verify`

Verification answers: **What evidence proves the requested outcome actually exists?**

### Recommended inputs

- definition of done;
- acceptance criteria;
- test commands/results;
- artifact paths;
- runtime/browser evidence where applicable.

### Strong evidence examples

- passing targeted tests;
- successful build/typecheck;
- browser/UI behavior;
- exact source citations;
- generated files at expected paths;
- external system state after an authorized action.

## 9. `/research`

Use when the answer depends on current information, external evidence, conflicting sources, markets, vendors, regulation, pricing, technical choices or other uncertainty.

### Recommended inputs

Required:

- research question;
- why the answer matters.

Strongly helpful:

- date/recency requirement;
- geography;
- acceptable sources;
- decision threshold;
- known documents or links;
- desired output format.

### Example

```text
/research Which current tools are the strongest fit for authenticated agent actions across SaaS apps? Prefer primary documentation, distinguish stable production tools from experimental candidates, and recommend what HiveForge should stage rather than install globally.
```

## 10. Document production

Use for briefs, proposals, reports, playbooks, client documents and other deliverables.

### Recommended inputs

- audience;
- decision/purpose;
- authoritative source files;
- required sections;
- tone;
- brand/template requirements;
- output format;
- page/length constraint.

### Important rule

Published PDF/DOCX/slide outputs are deliverables. Preserve an editable canonical source whenever the document is expected to evolve.

## 11. Workspace hygiene

Use when files are scattered, duplicated or difficult for a human to navigate.

### Recommended inputs

- target folder/workspace;
- known client/project scope;
- what must remain untouched;
- source-of-truth rules.

### Workflow

```text
resolve scope
→ inspect existing structure
→ classify
→ route
→ normalize
→ deduplicate
→ refresh README/index/status
→ archive superseded material
→ record material decisions
```

Do not redesign an already-good human structure just to enforce a HiveForge taxonomy.

## 12. `/readme`

Use to make a repository understandable and installable.

### Recommended inputs

- target users;
- one-sentence value proposition;
- installation path;
- first successful action;
- screenshots/diagrams/assets if available;
- architecture and dependencies;
- support/licensing/security information.

A strong README should answer:

1. What is this?
2. Why should I care?
3. How do I install it?
4. What do I do first?
5. How does it work?
6. What commands/tools are available?
7. Where do I go when something fails?

## 13. `/diagram`

Choose the diagram based on the question, not visual novelty.

| Question | Useful diagram |
|---|---|
| What talks to what? | Architecture / component diagram |
| What happens in order? | Flowchart / sequence diagram |
| Who owns what? | Swimlane / org/ownership diagram |
| How does data move? | Data-flow diagram |
| What depends on what? | Dependency graph |
| How does state change? | State diagram |
| What happens over time? | Timeline / Gantt |

## 14. `/retro`

Use after consequential work, failures, repeated friction, or a successful pattern worth reusing.

### Recommended inputs

- what was attempted;
- what happened;
- evidence;
- corrections;
- what should be different next time.

### Expected output

```text
Observation
→ Root cause
→ Local correction
→ Regression guard
→ Scope of lesson
→ Candidate reusable improvement
```

## Input quality rule

You do **not** need to write perfect prompts. The most useful input usually contains:

```text
GOAL
CURRENT CONTEXT / SOURCE
CONSTRAINTS
DESIRED OUTPUT
DEFINITION OF DONE
```

Example:

```text
Goal: prepare this repository for a public release.
Context: use the current repo as source of truth.
Constraints: do not expose client data; optional dependencies must remain optional.
Output: tested release branch and concise release report.
Done: CI green on Linux/macOS/WSL, dashboard and fallback tests pass, immutable release artifact has checksum.
```

HiveForge should ask only for missing information it cannot retrieve safely from authorized sources.