---
name: tech-writer
description: Skill for tech-writer (auto-generated).
keywords: []
source: partially-processed/agents/tech-writer.py
---

name: tech-writer
description: Technical Writer — creates documentation (README, docs) after task completion.
keywords: [tech-writer, docs, README]
source: partially-processed/agents/tech_writer.py

# Technical Writer

When to use
- After tasks or epics finish to generate user-facing documentation, README, and project notes.

Workflow
1. Trigger on task completion thresholds or explicit requests.
2. Generate README or other docs via LLM prompts and save files via `state_manager.save_file`.
3. Mark tasks as documented in `next_state`.

Dependencies
- UI helpers, telemetry, `core.ui.base.success_source`.

Output
- Creates/updates documentation files (e.g., `README.md`), sets task status to DOCUMENTED.

## When to use

Use this skill when you need tech-writer automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

