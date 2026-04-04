---
name: kiss-detalhador-de-tarefas
description: "Transforma um item de backlog em tarefas tecnicas executaveis. Use quando o usuario quiser decompor uma historia, feature ou enabler em subtarefas, sequencia de implementacao, dependencias, testes esperados, Definition of Done e pontos de atencao para engenharia. Funciona especialmente bem como continuidade do skill kiss-backlog-de-produto."
---

# Detalhador de Tarefas

## Overview

Receba um item de backlog ja definido, preserve seu objetivo e decomponha-o em trabalho tecnico implementavel sem perder contexto de valor, risco e qualidade.

Este skill opera depois da priorizacao. Nao o use para desenhar o backlog inteiro.

O padrao preferencial e produzir um arquivo por item de backlog detalhado, usando o nome do item no formato `FXXTYY-slug-do-item.md`. Dentro desse arquivo, enumere as tarefas como `T1`, `T2`, `T3` e subtarefas como `T2.1`, `T2.2` quando necessario.

Crie os artefatos desta etapa, por padrao, em `dev-docs/04-tarefas/` na raiz do projeto. Ao finalizar, informe explicitamente ao usuario quais arquivos foram criados ou atualizados, com caminho e nome.

## Regras Transversais

- Preserve no detalhamento a lingua definida para sistema e documentacao; se a entrada nao trouxer isso, sinalize a lacuna.
- Siga essa mesma lingua ao sugerir mensagens de commit, salvo instrucao explicita em contrario.
- Crie `AGENTS.md` na raiz do projeto se ele nao existir e mantenha `AGENTS.md` e `README.md` atualizados sempre que o detalhamento introduzir instrucoes de execucao, convencoes de desenvolvimento, setup, validacao ou operacao que devam permanecer visiveis no projeto.
- Quando a etapa iniciar uma nova frente relevante, oriente sincronizar a `main` local com `git pull`, criar branch curta e abrir PR para `main` ao fim do pacote validado.
- Ao encerrar a etapa, sugira mensagens de commit objetivas para os artefatos criados ou revisados.
- Antes de recomendar avancar para execucao, instrua o usuario a validar o breakdown, os testes esperados e os artefatos gerados.
- Quando o item ficar pronto para execucao, atualize ou instrua atualizar `dev-docs/03-backlog/kanban.md` para status `ready`.
- Se o `kanban.md` estiver ausente ou inconsistente para o item, reconcilie o board antes de concluir o detalhamento.

## Workflow

### 1. Validar o item de entrada

Confirme se o item de backlog esta suficientemente definido para ser quebrado em tarefas.

Cheque:
- objetivo do item
- criterio de aceite
- dependencias
- lingua principal do sistema e da documentacao, quando isso afetar implementacao e artefatos
- restricoes tecnicas relevantes
- riscos ou requisitos de seguranca, privacidade e qualidade

Se o item ainda estiver vago, produza perguntas de esclarecimento antes de decompor.

Antes de seguir, confirme que existe uma linha correspondente no `kanban.md` para o item. Se nao existir, crie ou reconcilie a linha usando o identificador do backlog.

### 2. Identificar impacto tecnico

Mapeie quais partes do sistema serao afetadas.

Cubra:
- frontend
- backend
- banco de dados
- APIs e integracoes
- observabilidade
- seguranca
- testes
- migracoes ou operacao

Use [task-breakdown-framework.md](./references/task-breakdown-framework.md) para orientar a decomposicao.

### 3. Quebrar em tarefas

Crie tarefas que possam ser executadas de forma clara por engenharia.

Prefira tarefas:
- com ownership compreensivel
- pequenas o suficiente para planejamento
- ordenadas por dependencia
- escritas em linguagem de execucao

Se houver necessidade, separe tarefas por trilha:
- produto ou UX
- frontend
- backend
- dados
- DevOps ou plataforma
- seguranca ou compliance

Cada tarefa deve ser referenciavel de forma inequivoca. Para cada tarefa, inclua:
- identificador, como `T1`
- titulo curto e objetivo
- objetivo da tarefa
- dependencia de outras tarefas, quando houver
- validacao esperada
- criterio de conclusao

Se houver impacto de seguranca ou privacidade, reflita isso em tarefas explicitas ou checks obrigatorios de validacao. Nao deixe esse aspecto apenas implícito no texto.

### 4. Definir qualidade e verificacao

Para cada conjunto de tarefas, explicite:
- testes necessarios
- checks de seguranca
- checks de privacidade
- validacoes de seguranca ou permissao
- observabilidade minima
- Definition of Done da entrega
- riscos tecnicos e pontos de rollback

Nao deixe qualidade implicita.

### 5. Produzir a sequencia de implementacao

Monte uma ordem recomendada de execucao.

Inclua:
- pre-requisitos
- tarefas desbloqueadoras
- tarefas paralelizaveis
- verificacoes intermediarias
- ponto de integracao final

### 6. Produzir o detalhamento final

Use [task-template.md](./references/task-template.md) para consolidar a saida.

Inclua, conforme aplicavel:
- resumo do item
- lingua e convencoes operacionais herdadas
- referencia ao `kanban.md` quando houver acompanhamento operacional
- impactos tecnicos
- tarefas
- subtarefas
- dependencias
- testes e verificacoes
- DoD
- riscos
- sequencia recomendada

Por padrao, produza um unico documento por item de backlog detalhado. So divida em mais de um arquivo quando o item estiver excessivamente grande, envolver trilhas quase independentes ou exigir ownership separado por time.

Quando o item estiver detalhado, com dependencias de execucao suficientemente claras e sem bloqueio estrutural aberto, marque o item como `ready` no `kanban.md`.

## Interaction Rules

- Preserve a rastreabilidade com o item de backlog original.
- Nao invente escopo novo sem sinalizar.
- Diferencie tarefa de implementacao, tarefa de validacao e tarefa operacional.
- Sempre reflita impacto de seguranca e privacidade no breakdown, ainda que apenas como validacao obrigatoria.
- Se o item estiver grande demais, recomende quebrar antes em backlog.
- Prefira decomposicao que facilite paralelismo sem aumentar acoplamento.
- Estruture a saida para que o usuario possa pedir ao Codex algo como "execute T2 do arquivo F02T01-cadastro-e-login.md".

## Output Modes

- Quick breakdown: tarefas principais.
- Engineering breakdown: tarefas com dependencias e testes.
- Delivery checklist: resumo pronto para execucao.

## Document Convention

- Pasta padrao desta etapa: `dev-docs/04-tarefas/`
- Um arquivo por item detalhado, no formato `FXXTYY-slug-do-item.md`
- Quando houver `dev-docs/03-backlog/kanban.md`, mantenha a linha do item consistente e marque `ready` ao finalizar o detalhamento executavel
- Nao trate ausencia de linha no board como detalhe opcional quando o projeto estiver usando acompanhamento operacional
- Crie `AGENTS.md` se estiver ausente e atualize `AGENTS.md` e `README.md` quando o detalhamento explicitar comandos, fluxos de trabalho ou validacoes que precisem ser reaproveitados
- Se a mudanca for relevante no repositorio, recomende sincronizar a `main`, usar branch dedicada e abrir PR para `main` apos revisao
- Ao concluir, recomende validar o breakdown e confirmar testes e checks antes da implementacao
- Ao concluir, sugira mensagens de commit para os artefatos desta etapa
- Ao concluir, sempre informe ao usuario onde os arquivos foram criados e os nomes exatos

## Assumed Triggers

Use este skill principalmente em pedidos como:
- "Detalhe as tarefas dessa historia"
- "Quebre esse item de backlog em tarefas tecnicas"
- "Prepare a implementacao dessa feature com testes e DoD"

## References

- Leia [task-breakdown-framework.md](./references/task-breakdown-framework.md) para orientar a decomposicao.
- Leia [task-template.md](./references/task-template.md) para produzir a saida final.
