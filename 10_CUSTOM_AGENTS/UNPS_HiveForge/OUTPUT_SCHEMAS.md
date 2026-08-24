# UNPS HiveForge — Output Schemas

Version: 0.3.0  
Status: Candidate

## Default maintenance response

Every completed library-maintenance action should report:

1. Outcome
2. Files created, updated, moved, archived, or intentionally left unchanged
3. Canonical location
4. Verification performed
5. Maturity/status impact
6. Remaining blocker or next highest-value test

## Asset record

```markdown
# <Asset name>
id: <stable-id>
version: <semantic-version>
status: experimental | candidate | production | deprecated
owner: Unparalleled Source
updated: YYYY-MM-DD

## Purpose
## Trigger / use case
## Required inputs
## Dependencies and tools
## Procedure or instruction
## Output contract
## Failure and uncertainty behavior
## Verification
## Provenance
```

## Package validation record

```markdown
# <Agent> Validation
- Package version:
- Date:
- Environment:
- Required files present:
- Shared references resolved:
- Scenario tests passed:
- Scenario tests failed:
- Security/credential scan:
- Context-loading review:
- Decision: candidate | production | blocked
- Evidence:
```

## Existing deliverable schemas

Use the canonical schemas under `08_OUTPUT_SCHEMAS` for executive briefs, decision briefs, research reports, proposals, and capture plans. Load only the schema required by the active deliverable.
