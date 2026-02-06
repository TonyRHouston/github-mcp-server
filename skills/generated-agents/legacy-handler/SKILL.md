---
name: legacy-handler
description: Skill for legacy-handler (auto-generated).
keywords: []
source: partially-processed/agents/legacy-handler.py
---

name: legacy-handler
description: Legacy Handler — handles legacy 'review_task' calls and simple legacy flows.
keywords: [legacy-handler, review]
source: partially-processed/agents/legacy_handler.py

# Legacy Handler

When to use
- Internal compatibility: invoked for legacy 'review_task' type messages or similar legacy triggers.

Workflow
1. Inspect `self.data['type']` and route to legacy handling (e.g., complete review task).
2. Otherwise raise an error for unknown legacy reasons.

Dependencies
- `core.agents.base.BaseAgent` and AgentResponse utilities.

Output
- Typically completes a step (calls `next_state.complete_step('review_task')`) and returns `AgentResponse.done`.

## When to use

Use this skill when you need legacy-handler automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

