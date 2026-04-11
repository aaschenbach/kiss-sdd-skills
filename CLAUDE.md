# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A collection of AI skills (for Codex, Gemini CLI, and Claude Code) that automate the product lifecycle following the KISS principle. Skills are invoked with the `$kiss-` prefix in Codex and Gemini CLI, and with the `/kiss-` prefix in Claude Code.

## Validation

```bash
python quick_validate.py
```

This checks that every skill folder under `skills/` starts with `kiss-`, contains a `SKILL.md` with a `name:` field matching the folder name, and has both `agents/openai.yaml` and `agents/gemini.yaml`.

## Skill structure

Each skill lives under `skills/<kiss-skill-name>/` and must contain:
- `SKILL.md` — the skill definition with `name:` frontmatter matching the folder name
- `agents/openai.yaml` — Codex agent config
- `agents/gemini.yaml` — Gemini CLI agent config
- `references/` — reference documents and templates consumed by the skill

`openai.yaml` and `gemini.yaml` must be kept in parity.

For Claude Code, the npm installer (`kiss-sdd-skills-cli`) generates a single `.md` file per skill by concatenating `SKILL.md` with all files in `references/`, and places it in `~/.claude/commands/` as a slash command.

## Architecture

The skills implement a staged product lifecycle pipeline:

| Stage | Skill | Output location |
|-------|-------|-----------------|
| Discovery / PRD | `kiss-estrategista-de-produto` | `dev-docs/01-produto/` |
| Brand (optional) | `kiss-posicionamento-de-marca` | `dev-docs/01-produto/brand-direction.md` |
| Architecture | `kiss-arquiteto-de-sistemas` | `dev-docs/02-arquitetura/` |
| Backlog | `kiss-backlog-de-produto` | `dev-docs/03-backlog/` |
| Task breakdown | `kiss-detalhador-de-tarefas` | `dev-docs/04-tarefas/FXXTYY-slug.md` |
| Execution | `kiss-executor-de-entrega` | `dev-docs/05-execucao/FXXTYY-slug.execution.md` |
| QA | `kiss-especialista-de-qa` | `dev-docs/06-qa/` |
| Full orchestration | `kiss-orquestrador-de-produto` | all of the above |

`kiss-orquestrador-de-produto` coordinates the full flow without replacing the specialized skills.

## Conventions

- All skill folder names and their `name:` fields in `SKILL.md` must use the `kiss-` prefix.
- Task item identifiers follow the pattern `FXXTYY-slug-do-item` (e.g., `F02T01-cadastro-e-login`).
- The kanban board at `dev-docs/03-backlog/kanban.md` uses states: `todo | ready | in_progress | blocked | review | done`.
- Each skill has a corresponding execution report file per item: `FXXTYY-slug.execution.md` (one cumulative report per item, not per developer).
- The project language (Portuguese or other) must be decided early and propagated across all phases and commit messages.
- Brand/marketing steps are optional and must not block architecture, backlog, or execution phases.

## Contributing

- Sync with `main` before starting (`git pull`), work in a short-lived branch (`feat/name`), and open a PR — avoid committing directly to `main` for relevant changes.
- When modifying a skill, keep `SKILL.md`, all reference files, and both agent YAML files consistent.
- When a cross-cutting convention changes, propagate it to all affected skills and update `AGENTS.md`, `README.md`, and `README.en.md`.
