---
name: kiss-orquestrador-de-produto
description: "Orquestra o fluxo completo da ideia inicial ate execucao e handoff de QA. Use quando o usuario quiser conduzir, em sequencia, discovery de produto, PRD, arquitetura tecnica, backlog priorizado, detalhamento de tarefas, execucao e validacao de qualidade, aproveitando como base os skills kiss-estrategista-de-produto, kiss-arquiteto-de-sistemas, kiss-backlog-de-produto, kiss-detalhador-de-tarefas, kiss-executor-de-entrega e kiss-especialista-de-qa."
---

# Orquestrador de Produto

## Overview

Coordene o fluxo ponta a ponta sem substituir os skills especializados. Este skill existe para guiar a passagem entre artefatos, validar suficiência entre etapas e impedir que o processo avance com lacunas perigosas.

Pense nele como maestro do processo, nao como autor unico de todos os outputs.

Use como convencao padrao de artefatos na raiz do projeto:
- `dev-docs/01-produto/`
- `dev-docs/02-arquitetura/`
- `dev-docs/03-backlog/`
- `dev-docs/04-tarefas/`
- `dev-docs/05-execucao/`
- `dev-docs/06-qa/`

Ao final de cada fase, informe explicitamente ao usuario onde os arquivos foram criados ou atualizados, com caminho e nome.

## Regras Transversais

- Descubra ou confirme cedo a lingua principal do sistema e da documentacao e propague essa decisao entre as fases; se faltar, trate como lacuna de handoff.
- Siga essa mesma lingua ao sugerir mensagens de commit ao fim das fases, salvo instrucao explicita em contrario.
- Crie `AGENTS.md` na raiz do projeto se ele nao existir e mantenha `AGENTS.md` e `README.md` atualizados sempre que qualquer fase alterar escopo, arquitetura, setup, fluxo, convencoes ou orientacoes de uso que precisem permanecer acessiveis.
- Trate `kiss-posicionamento-de-marca` como extensao opcional apos o PRD ou em momento posterior, sem bloquear arquitetura, backlog, detalhamento, execucao ou QA.
- Quando o fluxo abrir uma nova frente relevante, oriente sincronizar a `main` local com `git pull`, criar branch curta por trabalho e abrir PR para `main` ao fim do pacote validado.
- Ao encerrar cada fase, sugira mensagens de commit objetivas para os artefatos criados ou revisados.
- Antes de liberar avancar para a fase seguinte, instrua o usuario a revisar, validar artefatos e executar testes ou checks aplicaveis daquela fase.

## Workflow

### 1. Identificar ponto de partida

Descubra em que estado o trabalho esta.

Cheque:
- ideia vaga sem descoberta
- descoberta parcial
- PRD ja existente
- arquitetura ja existente
- backlog parcial
- board operacional existente em `dev-docs/03-backlog/kanban.md`
- item pronto para detalhamento
- lingua principal do sistema e da documentacao, quando ja definida

Se ja existirem artefatos, reutilize-os. Nao reconstrua etapas sem necessidade.

### 2. Escolher o modo de execucao

Use um destes modos:
- `full-flow`: da ideia inicial ate backlog e detalhamento inicial
- `ate-prd`: discovery e PRD
- `ate-arquitetura`: PRD e arquitetura
- `ate-backlog`: PRD, arquitetura e backlog
- `detalhar-mvp`: pega backlog pronto e detalha apenas itens selecionados

Se o usuario nao especificar modo, escolha o menor modo que satisfaca o pedido sem gerar trabalho desnecessario.

### 3. Executar discovery e PRD

Quando faltar definicao de produto suficiente, conduza a etapa usando o skill `kiss-estrategista-de-produto`.

Objetivo desta fase:
- clarificar problema, publico, proposta de valor e MVP
- mapear naming, riscos, seguranca e privacidade
- produzir PRD tecnico suficientemente claro para handoff

Nao siga para arquitetura se o PRD ainda estiver fraco em escopo, fluxos, restricoes ou requisitos criticos.

Se fizer sentido para o pedido, sinalize ao fim desta fase a opcao de acionar `kiss-posicionamento-de-marca` para produzir direcao de marca baseada no PRD, sem transformar isso em gate do fluxo principal.

### 4. Executar arquitetura tecnica

Quando existir PRD suficientemente claro, conduza a etapa usando o skill `kiss-arquiteto-de-sistemas`.

Objetivo desta fase:
- extrair drivers arquiteturais
- definir stack
- definir arquitetura de alto nivel
- definir seguranca, privacidade, tenancy, dados, integracoes e APIs
- estruturar repositorio, modulos e plano de implementacao

Se a arquitetura depender de decisoes ainda abertas no PRD, pare, sinalize e volte uma etapa.

### 5. Executar backlog de produto

Quando produto e arquitetura estiverem suficientemente definidos, conduza a etapa usando o skill `kiss-backlog-de-produto`.

Objetivo desta fase:
- transformar PRD e arquitetura em epicos, features, historias e enablers
- priorizar
- cortar MVP e releases seguintes
- nomear itens prontos para detalhamento no formato `FXXTYY-slug-do-item`
- inicializar `kanban.md` assim que os itens priorizados forem definidos, sem esperar a etapa inteira terminar
- manter `todo` como padrao quando ainda houver proxima acao util no item e reservar `blocked` para impedimento real e atual
- explicitar impacto de seguranca e privacidade em cada item

Nao siga para detalhamento amplo se o backlog ainda estiver grande demais, mal priorizado ou sem dependencias claras.

### 6. Executar detalhamento de tarefas

Quando houver itens prontos para execucao, conduza a etapa usando o skill `kiss-detalhador-de-tarefas`.

Objetivo desta fase:
- gerar um arquivo por item no formato `FXXTYY-slug-do-item.md`
- quebrar em tarefas `T1`, `T2`, `T3`
- marcar itens prontos como `ready` no `kanban.md`
- explicitar dependencias, validacoes, DoD, seguranca, privacidade e testes

Por padrao, detalhe apenas:
- itens do MVP
- itens explicitamente escolhidos pelo usuario
- itens desbloqueadores de arquitetura ou entrega

Evite detalhar tudo cedo demais.

### 7. Executar QA e handoff final

Quando houver implementacao pronta ou pacote validavel, conduza a etapa usando o skill `kiss-especialista-de-qa`.

Objetivo desta fase:
- consolidar ambiente, massa e evidencias de validacao
- produzir roteiro manual final ou revisao de cobertura QA
- reconciliar backlog, `kanban.md` e relatorios `.execution.md` com o estado real da validacao
- preparar handoff final de qualidade sem inventar comportamento nao implementado

Nao trate QA como etapa abstrata. Se houver entrega validavel, transforme isso em artefato executavel.

### 8. Consolidar o handoff

Ao fim de cada fase, deixe claro:
- o que foi produzido
- o que esta pronto para a proxima fase
- o que ainda bloqueia avancar
- quais decisoes permanecem em aberto
- quais validacoes ou testes precisam acontecer antes da proxima fase
- quais mensagens de commit sao recomendadas para registrar a fase
- se a mudanca pede branch dedicada, commit e PR para `main`
- como backlog, `kanban.md` e relatorios de execucao se reconciliam no estado atual
- por que cada item do board esta como `todo` ou `blocked`, sem tratar dependencia planejada como bloqueio por padrao

Use [handoff-checklist.md](./references/handoff-checklist.md) para checar suficiência entre etapas.

## Orchestration Rules

- Reutilize artefatos existentes antes de recriar conteudo.
- Nao pule etapa quando a qualidade do insumo nao sustentar a proxima.
- Pare explicitamente diante de lacunas bloqueantes.
- Prefira produzir pouco e consistente a produzir o fluxo inteiro com premissas fracas.
- Quando houver incerteza, entregue a fase atual e liste o minimo necessario para seguir.
- Se o usuario pedir velocidade, execute ate o ponto de maior valor com menor risco estrutural.

## Output Modes

- Flow assessment: diagnostico do estado atual e proxima etapa recomendada.
- Phase execution: execucao de uma fase especifica.
- Full orchestration: sequencia completa ate execucao e handoff de QA.
- MVP execution pack: backlog, detalhamento, execucao e QA dos itens centrais do MVP.

## Document Convention

- Produto: `dev-docs/01-produto/`
- Extensao opcional de marca: `dev-docs/01-produto/brand-direction.md`
- Arquitetura: `dev-docs/02-arquitetura/`
- Backlog: `dev-docs/03-backlog/`
- Board operacional: `dev-docs/03-backlog/kanban.md`
- Tarefas: `dev-docs/04-tarefas/`
- Execucao: `dev-docs/05-execucao/`
- QA: `dev-docs/06-qa/`
- Crie `AGENTS.md` se estiver ausente e atualize `AGENTS.md` e `README.md` quando qualquer fase mudar informacoes estruturais, operacionais ou de uso
- Quando a mudanca for relevante, recomende sincronizar a `main`, usar branch dedicada e abrir PR para `main` no handoff final
- Ao concluir qualquer fase, explicite validacoes pendentes antes do avancar
- Ao concluir qualquer fase, sugira mensagens de commit para os artefatos gerados
- Ao concluir qualquer fase, sempre informe ao usuario a localizacao e o nome dos arquivos gerados

## Assumed Triggers

Use este skill principalmente em pedidos como:
- "Quero seguir da ideia ate o planejamento de execucao"
- "Conduza todo o fluxo de produto, arquitetura, entrega e QA"
- "Use os artefatos existentes e avance para as proximas etapas"

## References

- Leia [handoff-checklist.md](./references/handoff-checklist.md) para validar se cada etapa esta pronta para entregar a proxima.
