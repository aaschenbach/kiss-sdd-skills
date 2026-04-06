---
name: kiss-executor-de-entrega
description: "Executa o desenvolvimento de um item de backlog detalhado com seguranca operacional e rastreabilidade. Use quando o usuario quiser implementar uma tarefa ou a proxima tarefa desbloqueada com base no PRD, arquitetura, backlog, arquivo `FXXTYY-slug-do-item.md` e relatorio `FXXTYY-slug-do-item.execution.md`, validando cada passo antes de avancar."
---

# Executor de Entrega

## Overview

Execute desenvolvimento de forma controlada, uma tarefa por vez por padrao, usando os artefatos anteriores como fonte de verdade e atualizando um relatorio acumulativo de execucao por item.

Este skill nao define produto, arquitetura, backlog nem breakdown. Ele consome esses artefatos e conduz implementacao segura.

Considere como local padrao dos artefatos:
- `dev-docs/01-produto/`
- `dev-docs/02-arquitetura/`
- `dev-docs/03-backlog/`
- `dev-docs/04-tarefas/`
- `dev-docs/05-execucao/`

Ao finalizar, informe explicitamente ao usuario quais arquivos foram criados ou atualizados, com caminho e nome.

## Regras Transversais

- Preserve a lingua definida para sistema e documentacao tambem nos artefatos produzidos durante a execucao; se isso estiver ambiguo, registre a lacuna antes de seguir.
- Siga essa mesma lingua ao sugerir mensagens de commit, salvo instrucao explicita em contrario.
- Crie `AGENTS.md` na raiz do projeto se ele nao existir e mantenha `AGENTS.md` e `README.md` atualizados sempre que a implementacao alterar setup, execucao, ambiente, comandos, fluxos operacionais, troubleshooting ou convencoes relevantes para quem vai manter o projeto.
- Antes de iniciar uma nova frente relevante, verifique se o projeto utiliza controle de versionamento (Git); em caso positivo, **garanta** a sincronizacao da `main` local com `git pull` e a criacao de uma branch curta de trabalho (ex: `task/FXXTYY-slug`) para isolar as mudancas.
- Se o Git nao estiver presente, ignore os passos de versionamento e siga com a execucao local direta.
- Ao encerrar cada rodada ou pacote seguro de execucao, sugira mensagens de commit objetivas alinhadas ao que foi implementado.
- Antes de seguir para a proxima tarefa ou fase, instrua o usuario a executar os testes e validacoes aplicaveis, ou valide voce mesmo quando estiver no escopo da execucao.

## Execution Model

Use dois arquivos por item:
- `dev-docs/04-tarefas/FXXTYY-slug-do-item.md`: plano detalhado do item
- `dev-docs/05-execucao/FXXTYY-slug-do-item.execution.md`: relatorio acumulativo de execucao

Quando existir acompanhamento operacional, use tambem:
- `dev-docs/03-backlog/kanban.md`: board simples de status do item

Regra padrao:
- execute uma tarefa por vez
- valide antes de seguir
- atualize o relatorio apos cada tarefa

Se o usuario nao especificar qual fase ou tarefa deve ser executada, apresente a sequencia sugerida, mais logica e adequada com base no progresso atual e dependencias, para que ele decida.

Modos de execucao:
- manual: o usuario indica a tarefa, como `T2`
- guiado: execute a proxima tarefa desbloqueada
- sequencial: execute varias tarefas em ordem, validando a cada etapa

Se o usuario ja especificou um item de backlog mas nao o modo, use `guiado`.

## Workflow

### 0. Preparar Git (Sync & Branch)

Antes de qualquer acao, verifique se o ambiente utiliza Git (ex: `git rev-parse --is-inside-work-tree`).
- Se houver Git:
    - Sincronize com a branch principal (`git checkout main && git pull`).
    - Crie ou mova para uma branch de trabalho (ex: `git checkout -b task/FXXTYY-slug`).
- Se nao houver Git:
    - Continue a execucao diretamente no sistema de arquivos local.

### 1. Validar os insumos

Antes de codar, confirme a existencia e a coerencia de:
- PRD ou documento de produto relevante
- arquitetura ou documento tecnico relevante
- backlog ou item de backlog correspondente
- `dev-docs/03-backlog/kanban.md`, quando o projeto estiver usando board operacional
- lingua principal do sistema e da documentacao, quando relevante para codigo, UI e artefatos
- arquivo `FXXTYY-slug-do-item.md`
- arquivo `FXXTYY-slug-do-item.execution.md`, se ja existir
- estado atual do repositorio
- branch atual e estrategia de branch ou PR quando a mudanca for relevante

Se faltarem insumos criticos, pare e aponte o bloqueio.
Se o item existir no backlog mas nao tiver linha correspondente no `kanban.md`, reconcilie o board antes de iniciar a execucao.

### 2. Determinar a unidade de execucao

Escolha a unidade de trabalho:
- tarefa especifica, como `T2`
- proxima tarefa desbloqueada
- intervalo seguro, como `T1` ate `T3`

Nunca execute tarefa bloqueada por `depends on`.

Se o arquivo estiver inconsistente com o relatorio de execucao ou com o codigo atual, reconcilie antes de seguir.

### 3. Ler contexto antes da implementacao

Leia o minimo necessario para executar com qualidade:
- objetivo do item
- criterio de aceite
- impacto de seguranca e privacidade
- dependencias da tarefa
- validacao esperada
- decisoes arquiteturais e restricoes relevantes

Use [execution-workflow.md](./references/execution-workflow.md) para orientar a checagem de prontidao antes da implementacao.

### 4. Implementar a tarefa

Execute a tarefa de forma rastreavel.

Para cada tarefa:
- confirme objetivo e limite de escopo
- implemente apenas o necessario
- respeite arquitetura, seguranca e privacidade
- evite pular para tarefas futuras
- registre desvios relevantes do plano

Quando iniciar execucao real do item, atualize o `kanban.md` para `in_progress`.

Se descobrir que a tarefa esta mal definida, pare, registre e proponha ajuste em vez de improvisar silenciosamente.

### 5. Validar a tarefa

Antes de marcar como concluida, execute as validacoes aplicaveis:
- validacao funcional
- testes automatizados relevantes
- checagens de seguranca e permissao
- checagens de privacidade e dados sensiveis
- validacao de observabilidade, logs ou auditoria
- revisao de impacto em tarefas dependentes
- validacao ou atualizacao de `AGENTS.md` e `README.md`, quando a mudanca afetar uso, setup, manutencao ou operacao do projeto

Nao avance se a tarefa falhar em validacoes criticas.

### 6. Atualizar o relatorio de execucao

Registre o resultado em `FXXTYY-slug-do-item.execution.md` usando [execution-report-template.md](./references/execution-report-template.md).

Atualize, no minimo:
- tarefa executada
- status
- atualizacao no `kanban.md`, quando aplicavel
- o que foi implementado
- arquivos ou modulos afetados
- validacoes executadas
- falhas ou pendencias
- ajustes de plano
- licoes aprendidas
- proxima tarefa recomendada

Use um unico relatorio acumulativo por item, nao um relatorio por dev.

### 7. Decidir o proximo passo

Ao fim de cada execucao, conclua com uma decisao explicita:
- pronto para a proxima tarefa
- bloqueado
- precisa refinar o item
- precisa voltar para backlog ou arquitetura
- **pronto para encerrar e abrir Pull Request**: quando o pacote de tarefas ou o item estiver validado e o ambiente usar Git.

Se houver Git:
- Confirme com o usuario se ele deseja abrir o Pull Request agora.
- Se autorizado, ofereca-se para realizar a abertura do PR (se o GitHub CLI estiver disponivel) ou forneca o comando/orientacao necessario.
- Em caso de execucao sequencial (múltiplas tarefas), o PR deve ser aberto apos a conclusao e validacao do conjunto completo.

Mapeamento recomendado de status no `kanban.md`:
- `in_progress` ao iniciar execucao
- `blocked` quando houver impedimento real
- `review` quando a implementacao estiver pronta e aguardando validacao final
- `done` quando o item estiver concluido e validado

Use [execution-workflow.md](./references/execution-workflow.md) para decidir se pode seguir.

## Interaction Rules

- Execute uma tarefa por vez por padrao.
- So execute varias em sequencia quando as dependencias estiverem claras e o risco for baixo.
- Preserve rastreabilidade entre backlog, tarefa, codigo e relatorio.
- Preserve consistencia entre backlog, `kanban.md` e relatorio de execucao.
- Sempre reflita seguranca e privacidade nas validacoes.
- Nao trate sucesso parcial como tarefa concluida.
- Registre licoes aprendidas e ajustes quando mudarem a proxima execucao.

## Output Modes

- Single task execution: executa uma tarefa especifica.
- Next safe step: executa a proxima tarefa desbloqueada.
- Sequential run: executa uma sequencia curta com validacao em cada etapa.
- Execution review: le o relatorio e recomenda o proximo passo.

## Document Convention

- Pasta de detalhamento lida por este skill: `dev-docs/04-tarefas/`
- Pasta do board operacional: `dev-docs/03-backlog/`
- Pasta de relatorios de execucao: `dev-docs/05-execucao/`
- Um relatorio acumulativo por item, no formato `FXXTYY-slug-do-item.execution.md`
- Quando houver `kanban.md`, atualize-o junto com o relatorio de execucao
- Crie `AGENTS.md` se estiver ausente e atualize `AGENTS.md` e `README.md` quando necessario, registrando isso no relatorio de execucao
- Quando o Git for detectado, **garanta** a sincronizacao da `main` no inicio e o uso de branch dedicada.
- Ao concluir a execucao em ambiente Git, abra Pull Request para `main` (se autorizado pelo usuario) apos a validacao final do item ou pacote de tarefas.
- Ao concluir, deixe explicito quais testes e validacoes foram executados e quais ainda precisam ser rodados pelo usuario
- Ao concluir, sugira mensagens de commit para codigo, documentacao e relatorio quando aplicavel
- Ao concluir, sempre informe ao usuario onde os arquivos foram criados ou os nomes dos arquivos atualizados

## Assumed Triggers

Use este skill principalmente em pedidos como:
- "Execute a tarefa T2 do arquivo F02T01-cadastro-e-login.md"
- "Execute a proxima tarefa desbloqueada desse item"
- "Implemente esse item em sequencia, validando cada passo"

## References

- Leia [execution-workflow.md](./references/execution-workflow.md) para o protocolo de execucao e decisao de avancar ou parar.
- Leia [execution-report-template.md](./references/execution-report-template.md) para atualizar o relatorio por item.
