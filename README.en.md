# K.I.S.S. SDD Skills

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Codex](https://img.shields.io/badge/Codex-Compatible-brightgreen)](https://github.com/google/codex)
[![Gemini](https://img.shields.io/badge/Gemini-Compatible-orange)](https://github.com/google/gemini-cli)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-blueviolet)](https://claude.ai/code)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[Versão em Português (README.md)](README.md)

Collection of AI skills that automate the product lifecycle (Discovery -> Architecture -> Execution -> QA) following the **KISS (Keep It Simple, Stupid)** principle.

## Features

- **Strategy & Discovery:** Turns ideas into detailed technical PRDs (`$kiss-estrategista-de-produto`).
- **Brand Identity:** Generates positioning, pitch, and early branding options (`$kiss-posicionamento-de-marca`).
- **Systems Architecture:** Converts PRDs into API specs, tech stacks, and data models (`$kiss-arquiteto-de-sistemas`).
- **Backlog Management:** Creates and prioritizes epics, stories, and Kanban boards (`$kiss-backlog-de-produto`).
- **Task Breakdown:** Decomposes stories into actionable technical tasks (`$kiss-detalhador-de-tarefas`).
- **Delivery Execution:** Implements code with traceability and automated reports (`$kiss-executor-de-entrega`).
- **Quality and QA:** Consolidates coverage and executable manual test scripts (`$kiss-especialista-de-qa`).
- **Orchestration:** Coordinates the end-to-end flow between all skills (`$kiss-orquestrador-de-produto`).

## Technologies

- **Languages:** Markdown (Instructions), Python (Validation), YAML (Configuration).
- **Tools:** Optimized for [Codex](https://github.com/google/codex), [Gemini CLI](https://github.com/google/gemini-cli), and [Claude Code](https://claude.ai/code).

## Prerequisites

- **Codex**, **Gemini CLI**, or **Claude Code** installed and configured locally.
- **Python 3.8+** (required only for the validation script).

## Installation

You can install the skills by cloning the repository (Git), npm or by downloading the files manually.

### Option A: Via npm (Simplest)

Install automatically using the CLI:

```bash
npx kiss-sdd-skills install codex
```

Or for Gemini:

```bash
npx kiss-sdd-skills install gemini
```

Or for Claude Code:

```bash
npx kiss-sdd-skills install claude
```

To install for all tools at once:

```bash
npx kiss-sdd-skills install all
```

You can also install it globally:

```bash
npm install -g kiss-sdd-skills
kiss-sdd-skills install codex
```

### Option B: Via Git (Recommended for development)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/alexandre-aschenbach/kiss-sdd-skills.git
   cd kiss-sdd-skills
   ```

2. **Run the copy command:**

   **For Codex (Windows/PowerShell):**
   ```powershell
   xcopy /E /I .\skills\* "$env:USERPROFILE\.codex\skills\"
   ```
   **For Codex (macOS/Linux):**
   ```bash
   cp -R ./skills/* ~/.codex/skills/
   ```

   **For Gemini CLI (Windows/PowerShell):**
   ```powershell
   xcopy /E /I .\skills\* "$env:USERPROFILE\.gemini\skills\"
   ```
   **For Gemini CLI (macOS/Linux):**
   ```bash
   mkdir -p ~/.gemini/skills && cp -R ./skills/* ~/.gemini/skills/
   ```

   **For Claude Code:** use the npm installer (`npx kiss-sdd-skills install claude`), as it generates command files in the correct format for `~/.claude/commands/`.

### Option C: ZIP Download (Manual)

1. Download the source code as a **[ZIP](https://github.com/alexandre-aschenbach/kiss-sdd-skills/archive/refs/heads/main.zip)**.
2. Extract the contents to a temporary folder.
3. Copy the contents of the `skills/` folder to your tool's skills directory:
   - **Codex:** `%USERPROFILE%\.codex\skills\` (Windows) or `~/.codex/skills/` (Unix).
   - **Gemini CLI:** `%USERPROFILE%\.gemini\skills\` (Windows) or `~/.gemini/skills/` (Unix).
   - **Claude Code:** use the npm installer (`npx kiss-sdd-skills install claude`), as it generates command files in the correct format for `~/.claude/commands/`.

### Validate Installation
Ensure the structure and skill names are correct:
```bash
python quick_validate.py
```

## Usage

Activate the skills directly in your terminal using the prefix for your tool:

| Tool | Prefix | Example |
|------|--------|---------|
| Codex | `$kiss-` | `$kiss-estrategista-de-produto` |
| Gemini CLI | `$kiss-` | `$kiss-estrategista-de-produto` |
| Claude Code | `/kiss-` | `/kiss-estrategista-de-produto` |

```text
Use $kiss-estrategista-de-produto to turn this idea into a technical PRD.
```

### Recommended Workflow

The ideal lifecycle follows this sequence:

1.  **Discovery:** `$kiss-estrategista-de-produto` -> Generates the PRD in `dev-docs/01-produto/`.
2.  **Branding:** `$kiss-posicionamento-de-marca` -> (Optional) Defines narrative and identity.
3.  **Architecture:** `$kiss-arquiteto-de-sistemas` -> Defines APIs and data models.
4.  **Planning:** `$kiss-backlog-de-produto` -> Creates `backlog.md` and `kanban.md`.
5.  **Refinement:** `$kiss-detalhador-de-tarefas` -> Creates `FXXTYY.md` breakdown files.
6.  **Implementation:** `$kiss-executor-de-entrega` -> Executes tasks and generates `.execution.md` reports.
7.  **QA:** `$kiss-especialista-de-qa` -> Consolidates the quality handoff and generates artifacts in `dev-docs/06-qa/`.

## Contribution

1. Always sync with `main` before starting (`git pull`).
2. Create a short branch for your change (`feat/feature-name`).
3. Maintain the `kiss-` prefix convention for all new skills.
4. Submit a Pull Request detailing the changes.

## License

Distributed under the **MIT** license. See [LICENSE](LICENSE) for more details.

---

> **Keep It Simple, Stupid:** Systems work best if they are kept simple rather than made complicated.
