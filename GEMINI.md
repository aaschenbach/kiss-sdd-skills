# Project Overview: Codex Skills (KISS Edition)

This repository contains a collection of AI "skills" designed for the **Codex** ecosystem. These skills facilitate the entire product lifecycle—from initial discovery and strategy to technical architecture, backlog management, and execution—following the **KISS (Keep It Simple, Stupid)** principle.

## Core Technologies & Structure
- **Languages:** Markdown (Instructions/Templates), Python (Validation), YAML (Agent Config).
- **Organization:** All skills reside in the `skills/` directory.
- **Key Files:**
  - `README.md` / `README.en.md`: Primary project documentation.
  - `AGENTS.md`: Operational guide for maintaining the repository.
  - `quick_validate.py`: Validation script for naming and structure consistency.
  - `skills/kiss-*/SKILL.md`: Core instruction set for each specific AI agent.

## Building and Running

### Validation
To ensure all skills follow the naming and structure conventions, run the validation script:
```bash
python quick_validate.py
```

### Installation
Skills can be installed in either Codex or Gemini CLI:
- **Codex (Windows):** `%USERPROFILE%\.codex\skills`
- **Codex (Linux/macOS):** `~/.codex/skills`
- **Gemini CLI (Windows):** `%USERPROFILE%\.gemini\skills`
- **Gemini CLI (Linux/macOS):** `~/.gemini/skills`

### Usage
Skills are invoked within the terminal/prompt using the `$` prefix followed by the skill name (e.g., `$kiss-estrategista-de-produto`).

## Development Conventions

### Naming & Structure
- **Prefix:** Every skill **MUST** use the `kiss-` prefix in both the directory name and the `name` field within its `SKILL.md`.
- **Consistency:** The directory name must exactly match the `name` field in `SKILL.md`.
- **Versioning:** The project follows Semantic Versioning (MAJOR.MINOR.PATCH), tracked in `CHANGELOG.md`.

### Workflow & Output
The "KISS" workflow follows a specific sequence:
1.  `kiss-estrategista-de-produto`: Discovery -> PRD.
2.  `kiss-posicionamento-de-marca`: (Optional) Brand Identity.
3.  `kiss-arquiteto-de-sistemas`: Architecture -> Stack/APIs.
4.  `kiss-backlog-de-produto`: Backlog -> Kanban.
5.  `kiss-detalhador-de-tarefas`: Task Breakdown (FXXTYY format).
6.  `kiss-executor-de-entrega`: Implementation & Execution Reports.
7.  `kiss-orquestrador-de-produto`: End-to-end coordination.

### Standardized Paths & Formats
- **Documentation:** `dev-docs/` (e.g., `01-produto/`, `02-arquitetura/`, `03-backlog/`).
- **Backlog Items:** `FXXTYY-slug-do-item.md` (F = Phase, T = Task/Item).
- **Kanban Board:** `dev-docs/03-backlog/kanban.md` using states: `todo | ready | in_progress | blocked | review | done`.
- **Language:** The primary language (e.g., `pt-BR`, `en-US`) should be defined early and propagated through all artifacts and commit messages.

## Operational Mandates for AI Agents
- Always suggest **commit messages** in the project's primary language upon completing a task.
- Ensure **multiple options** are provided for brand/marketing tasks (never a single choice).
- Update `AGENTS.md` and `README.md` if changes impact the overall workflow or conventions.
- Encourage a **Git flow** (pull `main`, work on branch, open PR) for significant changes.
