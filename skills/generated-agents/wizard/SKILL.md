---
name: wizard
description: Skill for wizard (auto-generated).
keywords: []
source: partially-processed/agents/wizard.py
---

name: wizard
description: Wizard — sets up initial project templates (frontend), handles OpenAPI uploads and project bootstrap.
keywords: [wizard, bootstrap, template]
source: partially-processed/agents/wizard.py

# Wizard

When to use
- During initial project setup to initialize templates, frontend epics, and project knowledge base.

Workflow
1. If project type is `swagger`, request OpenAPI/Swagger docs and upload them; otherwise set default options.
2. Initialize knowledge base and create initial frontend epic.
3. Return `AgentResponse.create_specification` to trigger Spec Writer flow.

Dependencies
- `core.db.models.KnowledgeBase`, `core.ui.base`, HTTP upload to RAG service (`PYTHAGORA_API`).

Output
- Initializes `next_state.epics`, `next_state.knowledge_base`, and may set template options.

## When to use

Use this skill when you need wizard automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

