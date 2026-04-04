# Project Overview: Codex Skills (KISS Edition)

This repository contains a collection of AI "skills" designed for the **Codex**, **Gemini CLI**, and **Claude Code** ecosystems. These skills facilitate the entire product lifecycle—from initial discovery and strategy to technical architecture, backlog management, and execution—following the **KISS (Keep It Simple, Stupid)** principle.

## Core Technologies & Structure
- **Languages:** Markdown (Instructions/Templates), Python (Validation), YAML (Agent Config).
- **Organization:** All skills reside in the `skills/` directory.
- **Key Files:**
  - `README.md` / `README.en.md`: Primary project documentation.
  - `AGENTS.md`: Operational guide for maintaining the repository.
  - `CHANGELOG.md`: Tracks version history (Semantic Versioning).
  - `CLAUDE.md`: Guidance for Claude Code users.
  - `quick_validate.py`: Validation script for naming and structure consistency.
  - `skills/kiss-*/SKILL.md`: Core instruction set for each specific AI agent.

## Building and Running

### Validation
To ensure all skills follow the naming and structure conventions, run the validation script:
```bash
python quick_validate.py
```
This script checks:
- Directory naming (must start with `kiss-`).
- Presence and consistency of `SKILL.md` (name field must match folder name).
- Presence of `agents/openai.yaml` and `agents/gemini.yaml`.

### Installation
Skills can be installed via npm (easiest), Git (recommended for development), or manually:
- **npm:** `npx kiss-sdd-skills install [codex|gemini|claude|all]`
- **Directories:**
  - **Codex:** `%USERPROFILE%\.codex\skills` (Windows) or `~/.codex/skills` (Unix)
  - **Gemini CLI:** `%USERPROFILE%\.gemini\skills` (Windows) or `~/.gemini/skills` (Unix)
  - **Claude Code:** `~/.claude/commands/` (via npm installer)

### Usage
Skills are invoked using the tool-specific prefix:
- **Codex / Gemini CLI:** `$kiss-<skill-name>`
- **Claude Code:** `/kiss-<skill-name>`

## Development Conventions

### Naming & Structure
- **Prefix:** Every skill **MUST** use the `kiss-` prefix in both the directory name and the `name` field within its `SKILL.md`.
- **Consistency:** The directory name must exactly match the `name` field in `SKILL.md`.
- **Multi-Plataform:** Maintain parity between `agents/openai.yaml` and `agents/gemini.yaml` in each skill.

### Workflow & Output
The "KISS" workflow implements a staged product lifecycle pipeline:

| Stage | Skill | Output location |
|-------|-------|-----------------|
| Discovery / PRD | `kiss-estrategista-de-produto` | `dev-docs/01-produto/` |
| Brand (optional) | `kiss-posicionamento-de-marca` | `dev-docs/01-produto/brand-direction.md` |
| Architecture | `kiss-arquiteto-de-sistemas` | `dev-docs/02-arquitetura/` |
| Backlog | `kiss-backlog-de-produto` | `dev-docs/03-backlog/` |
| Task breakdown | `kiss-detalhador-de-tarefas` | `dev-docs/04-tarefas/FXXTYY-slug.md` |
| Execution | `kiss-executor-de-entrega` | `dev-docs/05-execucao/FXXTYY-slug.execution.md` |
| Full orchestration | `kiss-orquestrador-de-produto` | All of the above |

### Standardized Paths & Formats
- **Documentation:** `dev-docs/` (e.g., `01-produto/`, `02-arquitetura/`, `03-backlog/`).
- **Backlog Items:** `FXXTYY-slug-do-item.md` (F = Phase, T = Task/Item).
- **Kanban Board:** `dev-docs/03-backlog/kanban.md` using states: `todo | ready | in_progress | blocked | review | done`.
- **Language:** The primary language (e.g., `pt-BR`, `en-US`) should be defined early and propagated through all artifacts and commit messages.

## Operational Mandates for AI Agents
- **Git Flow:** Sync with `main` (`git pull`), work on branches, and use Pull Requests.
- **Commits:** Always suggest commit messages in the project's primary language upon completing a task.
- **Options:** Ensure **multiple options** are provided for brand/marketing tasks (never a single choice).
- **Maintenance:** Update `AGENTS.md`, `README.md`, and `CHANGELOG.md` for any changes impacting the workflow or conventions.
