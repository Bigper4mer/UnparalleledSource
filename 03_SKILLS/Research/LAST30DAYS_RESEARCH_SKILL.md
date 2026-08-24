\# Skill: Last 30 Days Research

id: UNPS-SKILL-RESEARCH-RECENCY-001  
version: 0.1.0  
status: Candidate  
owner: Unparalleled Source  
updated: 2026-08-23

\#\# Purpose  
Provide a disciplined recency-first research pattern for questions such as latest developments, recent sentiment, what people are saying, recent product/repository activity, competitor movement, or other fast-changing topics.

\#\# Trigger Conditions  
Use when the task explicitly or implicitly depends on current information, especially phrases such as: latest, recent, last 30 days, current, what are people saying, trending, new, changed, updated, recent reviews, or recent GitHub activity.

\#\# Preferred Method  
1\. Search the most recent 30-day window first.  
2\. Broaden only when the recent window lacks enough evidence.  
3\. Separate discovery sources from authoritative verification sources.  
4\. Verify consequential claims against primary sources, official documentation, company pages, filings, repositories, or other authoritative evidence.  
5\. When community sentiment matters, include representative community sources while clearly labeling them as anecdotal or opinion-based.  
6\. Distinguish what changed recently from stable background context.  
7\. Report publication/update dates where recency materially affects interpretation.

\#\# Output Standard  
Return:  
\- recent findings  
\- source/date context  
\- what changed  
\- confidence or evidence quality  
\- implications  
\- practical next actions

\#\# Anti-Patterns  
\- Do not rely on stale evergreen pages for a current-state claim.  
\- Do not equate social chatter with verified fact.  
\- Do not expand to years of history before exhausting the requested recent window.  
\- Do not repeat identical search results from syndicated sources as independent corroboration.

\#\# Tool Routing  
Use web/current-research tools for discovery. Use GitHub when repository activity is relevant. Use specialized connectors when they provide unique first-party data. Use Firecrawl when structured extraction materially improves the research.

\#\# Promotion Criteria  
Promote to Production after repeated use demonstrates that the workflow consistently improves recency, source quality, and actionability without unnecessary search overhead.  
