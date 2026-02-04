---
name: troubleshooter
description: Skill for troubleshooter (auto-generated).
keywords: []
source: partially-processed/agents/troubleshooter.py
---

name: troubleshooter
description: Troubleshooter — creates debugging/troubleshooting iterations and proposes solutions.
keywords: [troubleshooter, debug, iteration]
source: partially-processed/agents/troubleshooter.py

# Troubleshooter

When to use
- When a task or iteration fails testing, or when user reports issues requiring investigation.

Workflow
1. Gather run command and user test instructions; if missing, request them.
2. Generate bug reports or alternative solutions using LLM prompts and helper mixins.
3. Create new iterations, update statuses (e.g., HUNTING_FOR_BUG, IMPLEMENT_SOLUTION), and coordinate testing.

Dependencies
- `core.agents.mixins` (ChatWithBreakdownMixin, IterationPromptMixin, RelevantFilesMixin), `core.llm.parser`.

Output
- Appends new iterations to `next_state.iterations`, updates `next_state.current_iteration` and `next_state.action`.

## When to use

Use this skill when you need troubleshooter automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

