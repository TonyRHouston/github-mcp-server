---
name: external-docs
description: Skill for external-docs (auto-generated).
keywords: []
source: partially-processed/agents/external-docs.py
---

name: external-docs
description: External Documentation — discovers and stores external documentation snippets per task.
keywords: [external-docs, docs, rag]
source: partially-processed/agents/external_docs.py

# External Documentation

When to use
- When a task requires external documentation or when project complexity suggests fetching reference docs.

Workflow
1. Fetch available docsets from `EXTERNAL_DOCUMENTATION_API`.
2. Use LLM to select relevant docsets and craft search queries.
3. Fetch snippets via docs API and store into `next_state.docs` for the current task.

Dependencies
- `core.config.EXTERNAL_DOCUMENTATION_API`, `httpx`, telemetry, `core.llm.parser.JSONParser`.

Output
- Populates `next_state.docs` with selected doc snippets and metadata.

## When to use

Use this skill when you need external-docs automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

