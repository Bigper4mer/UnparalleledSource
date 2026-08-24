# Prompt Database Agent Control Plane

Version: 0.1.0  
Status: Candidate  
Owner: Unparalleled Source  
Updated: 2026-08-24

## Purpose

Provide the repeatable operating workflow for maintaining `PROMPTS.UNPS` and its portable Custom Agent builds without duplicating assets or loading the full library.

## Trigger

Use for prompt intake, library organization, Custom Agent packaging, system-instruction changes, workflow/skill extraction, connector or dependency changes, evaluation design, promotion, deprecation, archive decisions, and workspace hardening.

## Workflow

1. **Resolve scope** — identify Internal/client/project/opportunity and authorized write boundary.
2. **Inspect** — read the library index, target folder, current package manifest, and relevant revision history.
3. **Search** — find existing or overlapping prompts, skills, workflows, policies, and packages.
4. **Classify** — determine asset type, canonical source, provenance, sensitivity, maturity, and owner.
5. **Design** — prefer one canonical asset plus thin references; define trigger, inputs, dependencies, output, uncertainty, and verification.
6. **Implement** — make the smallest coherent change; preserve IDs/history when updating established files.
7. **Verify** — check links, names, package completeness, duplicate risk, tool boundaries, credentials, context cost, and scenario behavior.
8. **Route** — place the asset using the file-routing standard and refresh affected navigation.
9. **Learn** — record only durable validated lessons at the narrowest useful scope.
10. **Report** — state outcome, changed files, canonical locations, verification, maturity effect, and remaining gate.

## Context packet

Always load: `BRAIN.md`, active agent identity, system instructions, package manifest.  
Then load: one workflow, only required skills, exact source sections, connector/dependency policy, and output schema.

## Promotion gates

- no canonical duplicate;
- clear trigger and required inputs;
- explicit tools and dependencies;
- defined output and failure behavior;
- safe write/permission boundaries;
- human-readable placement and navigation;
- representative evaluation;
- evidence of reuse before Production.

## Failure behavior

- Missing target or low routing confidence: stage; do not guess.
- Missing connector: use a capability-equivalent fallback or stop if the system of record cannot be accessed safely.
- Conflicting canonical files: do not overwrite; report and resolve authority.
- Failed evaluation: keep Candidate/Experimental and record the failure mode.
- Sensitive content: keep project-scoped and exclude it from reusable packages.

