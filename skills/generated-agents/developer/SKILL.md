---
name: developer
description: Skill for developer (auto-generated).
keywords: []
source: partially-processed/agents/developer.py
---

name: developer
description: Developer — breaks down tasks/iterations into executable steps and coordinates execution.
keywords: [developer, breakdown, implement]
source: partially-processed/agents/developer.py

# Developer

When to use
- When a task needs stepwise implementation, iteration breakdowns, or when running utility functions.

Workflow
1. Determine if utility function step or normal task; check for unfinished tasks/iterations.
2. Ask user to execute or run task as needed, get relevant files, and call parsing LLM prompts to produce `TaskSteps`.
3. Set next steps in state and trigger execution flows (Executor/CodeMonkey) as appropriate.

Dependencies
- `core.agents.mixins` (ChatWithBreakdownMixin, RelevantFilesMixin), LLM parsers, telemetry.

Output
- Writes `next_state.steps`, sets `next_state.action` to execution/review states, and flags modified tasks.

## When to use

Use this skill when you need developer automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

