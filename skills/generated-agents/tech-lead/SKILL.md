---
name: tech-lead
description: Skill for tech-lead (auto-generated).
keywords: []
source: partially-processed/agents/tech-lead.py
---

name: tech-lead
description: Tech Lead — creates development plans, epics and breaks down features into tasks.
keywords: [tech-lead, planning, epics]
source: partially-processed/agents/tech_lead.py

# Tech Lead

When to use
- When initial project planning or feature breakdown is required; to produce epics and task-level plans.

Workflow
1. Create initial project epic when bootstrapping.
2. Apply project templates if available and produce relevant file modifications.
3. Produce development plans and epics using LLM-driven templates and update `next_state.epics`.

Dependencies
- `core.templates.registry.PROJECT_TEMPLATES`, telemetry, `core.db.models.Complexity`.

Output
- Updates `next_state.epics`, may set `next_state.relevant_files` and `next_state.modified_files`.

## When to use

Use this skill when you need tech-lead automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

