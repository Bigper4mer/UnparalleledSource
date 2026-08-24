\# Skill: Ponytail Token-Efficient Engineering

id: UNPS-SKILL-CODING-EFFICIENCY-001  
version: 0.1.0  
status: Candidate  
owner: Unparalleled Source  
updated: 2026-08-23

\#\# Purpose  
Reduce context usage, implementation sprawl, and dependency growth while preserving correctness, security, accessibility, and maintainability.

\#\# Trigger Conditions  
Use by default for coding, technical implementation, debugging, refactoring, agent scaffolding, and architecture tasks unless the task explicitly requires a larger redesign.

\#\# Core Rules  
1\. Inspect the existing codebase before proposing a solution.  
2\. Prefer the shortest correct implementation.  
3\. Apply YAGNI: do not build capabilities that are not required now.  
4\. Reuse existing components, utilities, patterns, and dependencies.  
5\. Prefer the standard library or already-installed packages before adding new dependencies.  
6\. Make minimal diffs when a targeted change solves the problem.  
7\. Fix root causes rather than stacking patches or workarounds.  
8\. Preserve security, validation, accessibility, error handling, and data-loss protections.  
9\. Avoid duplicated logic and duplicated instructions.  
10\. Do not rewrite stable code merely for stylistic preference.

\#\# Context Rules  
\- Read only the files needed to understand the active problem.  
\- Summarize large files instead of repeatedly injecting them.  
\- Reference shared skills and project conventions rather than copying them into every prompt.  
\- Prefer repository search and targeted reads over loading an entire codebase into context.

\#\# Dependency Gate  
Before adding a package, answer:  
\- Is the capability already present?  
\- Can the standard library solve it cleanly?  
\- Is the dependency maintained and appropriate?  
\- Does its value justify install size, security surface, and long-term maintenance?  
If not, do not add it.

\#\# Change Strategy  
Prefer this order:  
1\. configuration fix  
2\. reuse existing helper/component  
3\. small targeted code change  
4\. small new helper/component  
5\. dependency addition  
6\. architecture change  
7\. rewrite

Move down the list only when the simpler option cannot satisfy the requirement.

\#\# Output Standard  
For implementation work, state:  
\- root cause or requirement  
\- minimal solution  
\- files changed  
\- dependencies added, if any  
\- validation/tests performed  
\- remaining risks or follow-up only when material

\#\# Promotion Criteria  
Promote to Production after repeated coding tasks show lower context/dependency cost without increasing regressions or technical debt.  
