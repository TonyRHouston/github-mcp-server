---
name: task-completer
description: Skill for task-completer (auto-generated).
keywords: []
source: partially-processed/agents/task-completer.py
---

name: pyathagora-task-completer
description: Task Completer (Pythagora) — finalizes tasks, commits via Git when enabled, and signals completion.
keywords: [task-completer, commit, finish]
source: partially-processed/agents/task_completer.py

# Task Completer

When to use
- When a task is finished and the system should mark it as completed and optionally commit changes.

Workflow
1. If Git is available and used, run `git_commit()`.
2. Update `next_state` to mark task done, log completion, and send progress to UI.
3. If last task, emit app/feature finished events.

Dependencies
- `core.agents.git.GitMixin`, telemetry, UI.

Output
- Commits to Git (if configured), updates task status, and emits progress events.

## When to use

Use this skill when you need task-completer automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

