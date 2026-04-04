# K.I.S.S. SDD Skills

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Codex](https://img.shields.io/badge/Codex-Compatible-brightgreen)](https://github.com/google/codex)
[![Gemini](https://img.shields.io/badge/Gemini-Compatible-orange)](https://github.com/google/gemini-cli)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[English Version (README.en.md)](README.en.md)

Coleção de skills para IA que automatizam o ciclo de vida de produto (Discovery -> Arquitetura -> Execução) seguindo o princípio **KISS (Keep It Simple, Stupid)**.

## Funcionalidades

- **Estratégia & Discovery:** Transforma ideias em PRDs técnicos detalhados (`$kiss-estrategista-de-produto`).
- **Identidade de Marca:** Gera opções de posicionamento, pitch e branding inicial (`$kiss-posicionamento-de-marca`).
- **Arquitetura de Sistemas:** Converte PRDs em especificações de APIs, stack e modelos de dados (`$kiss-arquiteto-de-sistemas`).
- **Gestão de Backlog:** Cria e prioriza épicos, histórias e boards Kanban (`$kiss-backlog-de-produto`).
- **Detalhamento de Tarefas:** Decompõe histórias em tarefas técnicas executáveis (`$kiss-detalhador-de-tarefas`).
- **Execução de Entrega:** Implementa código com rastreabilidade e relatórios automáticos (`$kiss-executor-de-entrega`).
- **Orquestração:** Coordena o fluxo ponta a ponta entre todas as skills (`$kiss-orquestrador-de-produto`).

## Tecnologias

- **Linguagens:** Markdown (Instruções), Python (Validação), YAML (Configuração).
- **Ferramentas:** Otimizado para [Codex](https://github.com/google/codex) e [Gemini CLI](https://github.com/google/gemini-cli).

## Pré-requisitos

- **Codex** ou **Gemini CLI** instalado e configurado localmente.
- **Python 3.8+** (necessário apenas para o script de validação).

## Instalação

Você pode instalar as skills via clonagem de repositório (Git) ou baixando os arquivos manualmente.

### Opção A: Via Git (Recomendado)

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/alexandre-aschenbach/kiss-sdd-skills.git
   cd kiss-sdd-skills
   ```

2. **Execute o script de cópia:**

   **Para Codex (Windows/PowerShell):**
   ```powershell
   xcopy /E /I .\skills\* "$env:USERPROFILE\.codex\skills\"
   ```
   **Para Codex (macOS/Linux):**
   ```bash
   cp -R ./skills/* ~/.codex/skills/
   ```

   **Para Gemini CLI (Windows/PowerShell):**
   ```powershell
   xcopy /E /I .\skills\* "$env:USERPROFILE\.gemini\skills\"
   ```
   **Para Gemini CLI (macOS/Linux):**
   ```bash
   mkdir -p ~/.gemini/skills && cp -R ./skills/* ~/.gemini/skills/
   ```

### Opção B: Download ZIP (Manual)

1. Baixe o código-fonte em formato **[ZIP](https://github.com/alexandre-aschenbach/kiss-sdd-skills/archive/refs/heads/main.zip)**.
2. Extraia o conteúdo para uma pasta temporária.
3. Copie o conteúdo da pasta `skills/` para o diretório de skills da sua ferramenta:
   - **Codex:** `%USERPROFILE%\.codex\skills\` (Windows) ou `~/.codex/skills/` (Unix).
   - **Gemini CLI:** `%USERPROFILE%\.gemini\skills\` (Windows) ou `~/.gemini/skills/` (Unix).

### Validar a Instalação
Certifique-se de que a estrutura e os nomes das skills estão corretos:
```bash
python quick_validate.py
```

## Uso

Ative as skills diretamente no seu terminal (Codex ou Gemini CLI) usando o prefixo `$kiss-`:

```text
Use $kiss-estrategista-de-produto para transformar esta ideia em um PRD técnico.
```

### Fluxo de Trabalho Recomendado (Workflow)

O ciclo de vida ideal segue esta sequência:

1.  **Discovery:** `$kiss-estrategista-de-produto` -> Gera o PRD em `dev-docs/01-produto/`.
2.  **Branding:** `$kiss-posicionamento-de-marca` -> (Opcional) Define narrativa e identidade.
3.  **Arquitetura:** `$kiss-arquiteto-de-sistemas` -> Define APIs e modelo de dados.
4.  **Planejamento:** `$kiss-backlog-de-produto` -> Cria o `backlog.md` e o `kanban.md`.
5.  **Refinamento:** `$kiss-detalhador-de-tarefas` -> Cria arquivos de detalhamento `FXXTYY.md`.
6.  **Implementação:** `$kiss-executor-de-entrega` -> Executa tarefas e gera relatórios `.execution.md`.

## Contribuição

1. Sincronize sempre com a `main` antes de iniciar (`git pull`).
2. Crie uma branch curta para sua alteração (`feat/nome-da-feature`).
3. Mantenha a convenção de prefixo `kiss-` para todas as novas skills.
4. Envie um Pull Request detalhando as mudanças.

## Licença

Distribuído sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

> **Keep It Simple, Stupid:** Sistemas funcionam melhor se forem mantidos simples e diretos.
