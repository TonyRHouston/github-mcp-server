---
name: human-input
description: Skill for human-input (auto-generated).
keywords: []
source: partially-processed/agents/human-input.py
---

name: human-input
description: Human Input — prompts the user for manual intervention or file edits when required by a step.
keywords: [human-input, user-interaction]
source: partially-processed/agents/human_input.py

# Human Input

When to use
- When a task step requires human intervention or file edits that cannot be automated.

Workflow
1. Present `human_intervention_description` to the user and wait for confirmation.
2. If files/lines are specified, open editor at locations and return after user action.
3. Mark step as complete in `next_state`.

Dependencies
- UI `open_editor` and `ask_question` helpers.

Output
- Completes human-intervention steps and returns `AgentResponse.done`.

## When to use

Use this skill when you need human-input automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

