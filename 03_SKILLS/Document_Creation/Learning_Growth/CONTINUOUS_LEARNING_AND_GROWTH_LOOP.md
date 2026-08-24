# UNPS Continuous Learning & Agent Growth Loop

Status: Candidate  
Version: 0.1.0  
Owner: Unparalleled Source

## Purpose
Allow UNPS agents to become more useful over time by learning from corrections, failed attempts, repeated friction, proven preferences, and successful patterns while keeping learning explicit, human-readable, scoped, reversible, and evidence-based.

## Core Rule
A mistake should produce more than a patch. When practical, identify the cause, correct the current task, capture the durable lesson at the narrowest appropriate scope, and add a regression guard so the same failure is less likely to recur.

Do not treat every user comment or one-off event as a global rule.

## Learning Triggers
Consider a learning pass when any of these occurs:
- the user corrects the agent;
- a test, build, calculation, deliverable, or workflow fails;
- the same clarification is requested repeatedly;
- a routing/file-placement mistake occurs;
- a tool/harness repeatedly performs poorly or exceptionally well;
- a workflow produces a materially better result than the current standard;
- a previously hidden dependency, constraint, preference, or source-of-truth rule is discovered;
- independent review exposes a systematic weakness.

## Learning Loop
1. **Observe** — capture the concrete outcome, not a vague impression.
2. **Diagnose** — identify root cause: missing context, poor routing, wrong tool, stale source, weak prompt, inadequate verification, ambiguous requirement, dependency issue, or execution error.
3. **Correct** — fix the current work first.
4. **Scope** — decide where the lesson belongs.
5. **Record** — write a concise human-readable lesson when it is durable.
6. **Guard** — add a checklist item, test, routing rule, eval, prompt change, or workflow gate when appropriate.
7. **Re-test** — verify the correction against the original failure mode.
8. **Promote** — broaden the rule only after evidence supports broader use.
9. **Retire** — remove or deprecate learnings that become stale, contradicted, or harmful.

## Learning Scope Ladder
Promote learning upward gradually:

```text
Task-local observation
        ↓
Project-specific lesson
        ↓
Client/account preference
        ↓
Reusable UNPS workflow/skill
        ↓
Global BRAIN rule
```

Use the **lowest scope that fully solves the problem**.

A single mistake normally does not justify a BRAIN-level rule. Global promotion should require repeated evidence across materially different tasks or explicit user direction.

## Human-Readable Memory
Durable learning should live in readable artifacts such as:
- `LEARNINGS.md` — concise validated lessons;
- `DECISIONS.md` / ADRs — decisions and rationale;
- `RETRO.md` — what worked, failed, and should change after a meaningful project phase;
- `CHANGELOG.md` — changes to reusable agents/skills/workflows;
- tests/evals — machine-verifiable guards;
- project `STATUS.md` / `PROGRESS.md` — current execution state.

Hidden/vector/semantic memory may index these artifacts but must not become the sole canonical source of important operational knowledge.

## Learning Entry Template
```markdown
## YYYY-MM-DD — <short lesson>
- Context:
- Expected:
- Observed:
- Root cause:
- Correction:
- Scope: task | project | client | UNPS
- Regression guard:
- Evidence / links:
- Status: candidate | validated | superseded
```

Keep entries short. Link to evidence rather than pasting large histories.

## Preference Learning
When the user expresses a stable working preference that materially improves future execution, incorporate it at the appropriate scope. Do not infer sensitive personal facts, credentials, secrets, or regulated information into reusable learning artifacts.

## Success Learning
Learn from wins as well as failures. If an approach repeatedly saves time/tokens, improves quality, reduces clarification, or produces stronger outcomes, capture the method and consider promoting it to a reusable skill or workflow.

## Anti-Overfitting Rules
- Do not convert a one-off exception into a universal rule.
- Do not preserve obsolete constraints after the underlying project changes.
- Do not duplicate the same lesson across many files; reference the canonical rule.
- Do not allow a learned convenience to weaken security, compliance, source fidelity, accessibility, validation, or user control.
- Do not silently rewrite global behavior when a scoped project correction is sufficient.

## Growth Metric
Agent growth is demonstrated by measurable reduction in repeated mistakes, unnecessary clarification, token/context waste, duplicate work, misfiled artifacts, stale assumptions, and verification failures — not by accumulating more instructions.
