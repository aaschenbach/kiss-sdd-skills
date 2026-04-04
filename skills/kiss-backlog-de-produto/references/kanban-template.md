# Kanban Template

Use este arquivo como board operacional simples em `dev-docs/03-backlog/kanban.md`.

## Regras

- Um item por linha.
- Use o identificador `FXXTYY-slug-do-item` como chave principal.
- Nao substitua o backlog consolidado por este board.
- Crie a linha do item assim que ele for definido no backlog com identificador estavel.
- Sempre que houver bloqueio, descreva em `observacoes ou bloqueio`.
- Sempre que houver mudanca relevante, atualize `ultima atualizacao` e `proxima acao`.

## Status canonicos

- `todo`: item priorizado e acompanhado desde o backlog, ainda nao detalhado para execucao, mas com alguma proxima acao viavel na fase atual
- `ready`: item detalhado e pronto para execucao
- `in_progress`: item em execucao
- `blocked`: item sem avancar na fase atual por dependencia externa, decisao pendente, aprovacao obrigatoria ou falha real
- `review`: item implementado aguardando validacao final, revisao ou fechamento operacional
- `done`: item concluido e validado

## Heuristica rapida para `todo` vs `blocked`

- Use `todo` quando o item ainda pode avancar em algo util agora, como detalhar tarefas, refinar criterios, preparar ambiente ou decompor dependencias.
- Use `blocked` quando nenhuma proxima acao relevante do proprio item pode avancar sem resolver antes um impedimento externo ou decisao obrigatoria.
- Dependencia planejada nao implica bloqueio por si so. Se o item apenas ainda nao chegou na vez, mantenha `todo`.

## Estrutura recomendada

| item | titulo | status | release | responsavel | ultima atualizacao | proxima acao | observacoes ou bloqueio |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F01T01-fundacao-de-autenticacao | Fundacao de autenticacao | todo | MVP |  | 2026-04-01 | Detalhar tarefas e criterios tecnicos | Depende de enabler interno, mas ja pode ser refinado |
| F01T02-onboarding-do-tenant | Onboarding do tenant | todo | MVP |  | 2026-04-01 | Quebrar fluxo, regras e validacoes | Implementacao depende da autenticacao, mas o item ainda pode ser detalhado |
| F01T03-integracao-com-provedor-x | Integracao com provedor X | blocked | MVP |  | 2026-04-01 | Cobrar aprovacao do provedor | Sem sandbox e sem credenciais homologadas; nao ha como avancar o item agora |
