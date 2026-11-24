---
description: Multi-pillar review with 4 parallel reviewer subagents
agent: pkm-orchestrator
---
Do NOT read files yourself. If you have not made a task tool call, you have not started.
Run a multi-pillar review on: $ARGUMENTS
Use the task tool with subagent_type: pkm-review-structure and prompt: "Review <scope>. Return your exact output format."
Use the task tool with subagent_type: pkm-review-content and prompt: "Review <scope>. Return your exact output format."
Use the task tool with subagent_type: pkm-review-security and prompt: "Review <scope>. Return your exact output format."
Use the task tool with subagent_type: pkm-review-format and prompt: "Review <scope>. Return your exact output format."
Merge the results:
- Summary table | Pillar | Verdict | High | Medium | Low | Escalate |
- All findings in one table, sorted by severity, duplicates (same file + quote) removed.
- If two pillars contradict each other on the same line -> ESCALATE 7.
- OVERALL: APPROVE only if all 4 PASS and there are no escalations, otherwise REVISE.
If there is any escalation, ask me (the Architect) first. Do not fix anything.
Save to test/multi-review/report-<today YYYY-MM-DD>.md.
