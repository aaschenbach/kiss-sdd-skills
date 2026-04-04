# AGENTS

Guia operacional para manutencao deste repositorio de skills.

## Escopo

- Este repositorio concentra skills de produto, arquitetura, backlog, detalhamento e execucao para uso no Codex.
- Mudancas em qualquer skill devem preservar consistencia entre `SKILL.md`, referencias associadas e documentacao raiz.

## Regras de Atualizacao

- Atualize `README.md` quando a mudanca afetar fluxo, uso, convencoes, instalacao, artefatos ou expectativas de handoff.
- Atualize este `AGENTS.md` quando a mudanca afetar regras operacionais transversais, responsabilidades, guardrails de manutencao ou convencoes para agentes.
- **Multi-Plataforma:** Mantenha sempre a paridade entre `agents/openai.yaml` e `agents/gemini.yaml` em cada skill.
- Se um novo requisito transversal surgir, propague-o para todas as skills impactadas e para os templates ou referencias relevantes.
- Para mudancas relevantes, sincronize com `main`, trabalhe em branch dedicada e preserve o merge para PR em vez de commit direto recorrente em `main`.

## Validacao Minima

- Validar os skills alterados com `quick_validate.py`.
- Revisar diffs para garantir consistencia entre skills, templates e `README.md`.
- Quando aplicavel, confirmar que os artefatos instruem validacao antes da proxima fase e sugerem mensagens de commit.
- Confirmar que as instrucoes de branch, `pull`, commit e PR estao coerentes com o fluxo minimo do repositorio.
- Confirmar que todo skill publicado por este repositorio usa o prefixo canonico `kiss-` tanto no nome da pasta quanto no campo `name` do `SKILL.md`.
- Quando houver acompanhamento operacional, confirmar consistencia entre backlog consolidado, `kanban.md` e relatorio de execucao por item.
- Quando houver skill de marca ou marketing, confirmar que cada entregavel relevante apresenta multiplas opcoes reais e comparaveis, em vez de proposta unica fechada.
- Confirmar que mensagens de commit sugeridas seguem o mesmo idioma principal definido para sistema e documentacao, salvo instrucao explicita em contrario.

## Convencoes Transversais

- Todos os skills publicados por este repositorio devem usar o prefixo `kiss-`.
- A lingua principal do sistema e da documentacao deve ser definida cedo e propagada entre as fases.
- Mensagens de commit sugeridas devem seguir a mesma lingua principal adotada na documentacao e nos artefatos do projeto, salvo instrucao explicita em contrario.
- Etapas opcionais de marca e marketing devem complementar o PRD sem bloquear arquitetura, backlog, detalhamento ou execucao.
- Skills de marca e marketing devem entregar sempre mais de uma opcao por modulo relevante, como posicionamento, pitch, tagline, logo e paleta.
- Identificadores de item devem usar o padrao `FXXTYY-slug-do-item`, com fase estavel e numeracao unica dentro da fase.
- O acompanhamento operacional deve usar `dev-docs/03-backlog/kanban.md` como board simples de status, com estados `todo | ready | in_progress | blocked | review | done`.
- Cada fase deve orientar atualizacao de `AGENTS.md` e `README.md` quando necessario.
- Cada fase deve orientar validacao de artefatos e testes antes do proximo handoff.
- Cada fase deve sugerir mensagens de commit ao encerrar.
- Antes de iniciar nova frente relevante, orientar sincronizacao com `main` via `git pull`.
- Quando a mudanca for relevante, orientar branch dedicada e PR para `main`.
