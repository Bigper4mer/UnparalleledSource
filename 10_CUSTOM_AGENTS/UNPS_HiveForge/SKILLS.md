# UNPS HiveForge — Skill Manifest

Version: 0.3.0  
Status: Candidate

## Load policy

Resolve the task first, then load only the smallest skill set that covers it. A folder reference is not permission to hydrate every file inside that folder.

## Core routing skills

| Trigger | Canonical skill | Requirement |
|---|---|---|
| Creating, moving, renaming, or organizing persistent files | `Document_Creation/Information_Architecture/FILE_ROUTING_AND_WORKSPACE_STANDARD.md` | Required |
| Capturing validated corrections, failures, or successful patterns | `Document_Creation/Learning_Growth/CONTINUOUS_LEARNING_AND_GROWTH_LOOP.md` | Required when triggered |
| Repeated ingestion of PDFs, rich documents, or large sources | `Token_Efficiency/SOURCE_INGESTION_NORMALIZATION.md` | Required when triggered |
| Coding or technical implementation | `Token_Efficiency/PONYTAIL_TOKEN_EFFICIENT_ENGINEERING.md` | Required when triggered |
| README creation or repair | `Document_Creation/README_Design/BEAUTIFUL_README_SKILL.md` | Required when triggered |
| Recent/current research | `Research/LAST30DAYS_RESEARCH_SKILL.md` plus primary-source verification | Preferred when applicable |
| Non-trivial repository intelligence | `Coding/Architecture/GRAPHIFY_CODEBASE_INTELLIGENCE.md` | Optional candidate |

## Domain skill groups

Load only for work in that domain:

- `03_SKILLS/Research`
- `03_SKILLS/Coding`
- `03_SKILLS/Government_Contracting`
- `03_SKILLS/Procurement`
- `03_SKILLS/Document_Creation`
- `03_SKILLS/Token_Efficiency`
- `03_SKILLS/Cinematography`

## Selection test

Before loading a skill, answer:

1. Does the current task trigger it?
2. Does an already-loaded instruction cover the same behavior?
3. Will loading it materially improve accuracy, safety, portability, or output quality?
4. Can the task proceed with a short reference instead of full hydration?

If the benefit is unclear, keep the skill referenced but unloaded.
