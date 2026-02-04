---
name: code-monkey
description: Skill for code-monkey (auto-generated).
keywords: []
source: partially-processed/agents/code-monkey.py
---

name: code-monkey
description: Code Monkey — implements code changes, processes <pythagoracode> blocks, and reviews hunks.
keywords: [code-monkey, implement, code]
source: partially-processed/agents/code_monkey.py

# Code Monkey

When to use
- When a task step requires creating or changing files (save_file steps) with auto-generated code blocks.

Workflow
1. Extract `<pythagoracode>` blocks from instructions if present.
2. Attempt Relace-based edits or use standard LLM prompts to implement changes.
3. Produce diffs/hunks and handle review cycles; apply or rework hunks as needed.

Dependencies
- `core.llm.parser.OptionalCodeBlockParser`, `core.agents.mixins.FileDiffMixin`, file/DB models.

Output
- Writes or updates files in the workspace, returns AgentResponse to indicate success or request review.

## When to use

Use this skill when you need code-monkey automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

