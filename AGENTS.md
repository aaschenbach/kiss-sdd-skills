# AGENTS.md

Instrucoes para agentes que trabalham neste repositorio.

## Sobre o repositorio

- Este repositorio mantem skills do ecossistema KISS para discovery, arquitetura, backlog, detalhamento, execucao e orquestracao.
- O codigo-fonte principal fica em `skills/`.
- A documentacao raiz relevante fica em `README.md`, `README.en.md`, `CHANGELOG.md`, `CLAUDE.md`, `GEMINI.md` e neste arquivo.

## Estrutura esperada das skills

Cada skill publicada neste repositorio deve:

- usar o prefixo `kiss-` no nome da pasta;
- usar o mesmo nome da pasta no campo `name` do `SKILL.md`;
- manter `agents/openai.yaml` e `agents/gemini.yaml` em paridade;
- manter referencias e templates coerentes com o `SKILL.md`.

Estrutura tipica:

- `skills/<kiss-skill>/SKILL.md`
- `skills/<kiss-skill>/agents/openai.yaml`
- `skills/<kiss-skill>/agents/gemini.yaml`
- `skills/<kiss-skill>/references/`

## Fluxo do produto refletido nas skills

O repositorio representa este fluxo:

1. `kiss-estrategista-de-produto`
2. `kiss-posicionamento-de-marca` opcional
3. `kiss-arquiteto-de-sistemas`
4. `kiss-backlog-de-produto`
5. `kiss-detalhador-de-tarefas`
6. `kiss-executor-de-entrega`
7. `kiss-orquestrador-de-produto` como coordenador do fluxo ponta a ponta

Ao alterar uma skill, preserve compatibilidade com esse encadeamento.

## Convencoes transversais

- A lingua principal do sistema e da documentacao deve ser definida cedo e propagada entre fases, artefatos e mensagens de commit sugeridas.
- Skills de marca e marketing devem sempre oferecer multiplas opcoes reais e comparaveis, nunca uma unica proposta fechada.
- Etapas de marca e marketing complementam o PRD e nao devem bloquear arquitetura, backlog, detalhamento ou execucao.
- Identificadores de item seguem o padrao `FXXTYY-slug-do-item`.
- O board operacional padrao fica em `dev-docs/03-backlog/kanban.md`.
- Os estados aceitos no kanban sao `todo | ready | in_progress | blocked | review | done`.
- Cada fase deve orientar validacao antes do proximo handoff.
- Cada fase deve sugerir mensagem de commit ao encerrar.

## Regras de manutencao

- Atualize `README.md` e `README.en.md` quando a mudanca afetar fluxo, instalacao, uso, convencoes, artefatos ou handoff.
- Atualize este `AGENTS.md` quando a mudanca alterar regras operacionais, guardrails, responsabilidades ou convencoes transversais.
- Se surgir um requisito transversal novo, propague-o para todas as skills, referencias e templates impactados.
- Nao deixe divergencia entre `openai.yaml` e `gemini.yaml`.
- Nao altere apenas uma etapa do fluxo se isso quebrar a continuidade das etapas seguintes.

## Fluxo de Git esperado

- Antes de iniciar uma frente relevante, sincronize com `main` via `git pull`.
- Para mudancas relevantes, trabalhe em branch dedicada.
- Prefira abrir PR para `main` em vez de acumular alteracoes diretamente em `main`.
- Ao concluir, revise os diffs antes de propor commit.

## Validacao minima

Sempre que alterar skills ou convencoes relacionadas:

1. Rode `python quick_validate.py`.
2. Revise o diff para conferir consistencia entre `SKILL.md`, referencias, YAMLs e documentacao raiz.
3. Confirme que nomes de pasta e campo `name` seguem o prefixo `kiss-`.
4. Confirme que instrucoes de branch, `pull`, commit e PR continuam coerentes com o fluxo minimo do repositorio.
5. Quando houver backlog operacional, confirme consistencia entre backlog consolidado, `kanban.md` e relatorios `.execution.md`.

## Checklist rapido para agentes

Antes de encerrar uma mudanca, confirme:

- a skill alterada continua consistente internamente;
- a documentacao raiz foi atualizada se necessario;
- a paridade multi-plataforma foi preservada;
- a validacao minima foi executada;
- a resposta final inclui proximo passo ou mensagem de commit sugerida quando aplicavel.
