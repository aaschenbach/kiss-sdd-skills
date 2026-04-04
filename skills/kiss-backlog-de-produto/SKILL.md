---
name: kiss-backlog-de-produto
description: "Transforma PRD, arquitetura e restricoes de entrega em backlog de produto priorizado. Use quando o usuario quiser derivar epicos, features, historias, enablers tecnicos, dependencias, criterio de aceite e cortes de release a partir dos documentos produzidos pelos skills kiss-estrategista-de-produto e kiss-arquiteto-de-sistemas."
---

# Backlog de Produto

## Overview

Receba os artefatos de produto e arquitetura, converta-os em backlog executavel e preserve rastreabilidade entre objetivo, requisito, decisao tecnica e item de entrega.

Nao detalhe tarefas de implementacao aqui. Este skill termina no nivel de backlog pronto para priorizacao e planejamento.

Crie os artefatos desta etapa, por padrao, em `dev-docs/03-backlog/` na raiz do projeto. Ao finalizar, informe explicitamente ao usuario quais arquivos foram criados ou atualizados, com caminho e nome.

## Regras Transversais

- Preserve no backlog a lingua definida para sistema e documentacao; se esse contexto faltar, registre a lacuna antes de consolidar os itens.
- Siga essa mesma lingua ao sugerir mensagens de commit, salvo instrucao explicita em contrario.
- Crie `AGENTS.md` na raiz do projeto se ele nao existir e mantenha `AGENTS.md` e `README.md` atualizados sempre que a etapa mudar o plano visivel de entregas, convencoes de priorizacao, estrutura de artefatos ou orientacoes de uso relevantes para o time.
- Quando a etapa iniciar uma nova frente relevante, oriente sincronizar a `main` local com `git pull`, criar branch curta e abrir PR para `main` ao fim do pacote validado.
- Ao encerrar a etapa, sugira mensagens de commit objetivas para os artefatos criados ou revisados.
- Antes de recomendar avancar para detalhamento ou execucao, instrua o usuario a revisar o backlog, validar priorizacao e confirmar os artefatos gerados.
- Quando houver acompanhamento operacional, crie ou atualize `dev-docs/03-backlog/kanban.md` assim que os itens priorizados receberem identificador e mantenha consistencia entre backlog e board durante toda a etapa.

## Workflow

### 1. Validar as entradas

Confirme se existem insumos suficientes para montar backlog com qualidade.

Cheque, no minimo:
- PRD ou definicao de produto
- arquitetura ou restricoes tecnicas relevantes
- lingua principal do sistema e da documentacao
- MVP e fora de escopo
- dependencias e riscos conhecidos
- criterios de aceite ou Definition of Done em nivel de produto

Se faltar material critico, liste as lacunas antes de consolidar backlog.

### 2. Extrair unidades de valor

Transforme os documentos em resultados entregaveis.

Identifique:
- objetivos do produto
- fluxos principais
- capacidades necessarias
- restricoes de negocio
- restricoes tecnicas
- requisitos transversais como seguranca, observabilidade e compliance

Use [backlog-framework.md](./references/backlog-framework.md) para estruturar a decomposicao.

### 3. Estruturar o backlog

Organize em niveis claros:
- epicos
- features
- historias de usuario ou itens funcionais equivalentes
- enablers tecnicos
- itens de risco, compliance ou operacao quando forem necessarios para entrega real

Nao force formato agil ritualistico se o contexto pedir outra estrutura, mas mantenha hierarquia e rastreabilidade.

### 4. Definir criterio de pronto por item

Para cada item relevante de backlog, explicite:
- objetivo do item
- valor entregue
- pre-condicoes
- criterio de aceite
- impacto de seguranca
- impacto de privacidade
- riscos relevantes
- dependencias conhecidas

Nao quebre em tarefas tecnicas detalhadas. Isso pertence ao skill kiss-detalhador-de-tarefas.

### 5. Priorizar e cortar releases

Monte uma ordem de entrega coerente com valor, risco e dependencia.

Cubra:
- o que entra no MVP
- o que fica para release posterior
- enablers que precisam vir antes
- itens de seguranca e privacidade que nao podem ficar para depois sem elevar risco indevido
- itens bloqueados por decisao pendente
- caminho critico de entrega

Assim que um item priorizado receber identificador estavel `FXXTYY-slug-do-item`, crie ou atualize sua linha no `kanban.md`.

Regra de timing:
- nao espere concluir o backlog inteiro para iniciar o board
- use `todo` como estado padrao para item priorizado ainda nao detalhado, mesmo quando existir dependencia futura mapeada, desde que haja proxima acao viavel de refinamento, detalhamento ou preparacao
- use `blocked` apenas quando o item ja nascer sem avancar na fase atual por dependencia externa, decisao pendente, aprovacao obrigatoria ou outro impedimento real que paralisa a proxima acao
- nao use `blocked` apenas para indicar ordem de execucao, dependencia sequencial planejada ou trabalho que ainda nao entrou na vez
- se houver duvida, prefira `todo` com `proxima acao` explicita e detalhe o risco em `observacoes`
- exemplos:
- `todo`: item depende de um enabler da mesma release, mas ja pode ser detalhado ou ter criterios refinados
- `blocked`: item depende de aprovacao de provedor, definicao juridica ou acesso externo sem os quais nenhuma proxima acao util pode avancar
- atualize release, proxima acao e observacoes na mesma rodada em que o item for definido

### 6. Produzir o backlog final e reconciliar o board

Use [backlog-template.md](./references/backlog-template.md) para consolidar a saida.
Use [kanban-template.md](./references/kanban-template.md) para criar ou atualizar o board operacional simples.

Quando um item estiver pronto para ser detalhado pelo skill kiss-detalhador-de-tarefas, atribua um identificador estavel e ordenavel no formato `FXXTYY-slug-do-item`, em que:
- `FXX` representa a fase estavel de entrega, como `F01` ou `F02`
- `TYY` representa a ordem unica do item dentro da fase, como `T01` ou `T02`
- `slug-do-item` descreve claramente o item

Nao reutilize o mesmo identificador para itens diferentes. Se um item mudar de fase, gere um novo identificador e registre a substituicao explicitamente.

Exemplos:
- `F01T01-fundacao-de-autenticacao`
- `F01T02-onboarding-do-tenant`
- `F02T01-cadastro-e-login`

Inclua, conforme aplicavel:
- resumo da logica de priorizacao
- lingua e convencoes relevantes herdadas do produto
- epicos
- features
- historias
- enablers tecnicos
- dependencias
- riscos
- cortes de release
- itens prontos para detalhamento pelo skill kiss-detalhador-de-tarefas

No `kanban.md`, garanta para cada item priorizado:
- linha criada no momento em que o item foi definido
- status coerente com o estado atual, normalmente `todo` ou `blocked`
- release associada, quando conhecida
- proxima acao coerente com a fase atual
- observacoes de bloqueio ou dependencia, quando existirem
- uso de `blocked` restrito a impedimento real e atual, nao a dependencia planejada

## Interaction Rules

- Preserve o vinculo entre item de backlog e objetivo de produto.
- Diferencie backlog funcional de habilitadores tecnicos.
- Nao esconda dependencias ou bloqueios.
- Force um check explicito de seguranca e privacidade em cada item, mesmo que o resultado seja "sem impacto relevante".
- Evite backlog inchado por especulacao futura.
- Prefira itens pequenos o suficiente para planejamento, mas grandes o suficiente para manter contexto de valor.
- Para itens prontos para execucao, gere nomes estaveis que possam ser referenciados diretamente pelo Codex.
- Trate o `kanban.md` como acompanhamento corrente desde a definicao do backlog, nao como fechamento tardio da etapa.

## Output Modes

- Backlog skeleton: epicos e features iniciais.
- Prioritized backlog: backlog completo com ordem sugerida.
- Release cut: recorte de MVP e releases seguintes.
- Ready for breakdown: shortlist de itens prontos para o skill kiss-detalhador-de-tarefas.

## Document Convention

- Pasta padrao desta etapa: `dev-docs/03-backlog/`
- Coloque ali backlog consolidado, cortes de release, listas de itens prontos para detalhamento e `kanban.md`
- Crie `AGENTS.md` se estiver ausente e atualize `AGENTS.md` e `README.md` quando o backlog consolidar roadmap, convencoes de identificacao ou instrucoes de planejamento que precisem ficar acessiveis
- Se a mudanca for relevante no repositorio, recomende sincronizar a `main`, usar branch dedicada e abrir PR para `main` apos revisao
- Ao concluir, recomende revisao do backlog e validacao do corte de MVP antes do detalhamento
- Ao concluir, sugira mensagens de commit para os artefatos desta etapa
- Ao concluir, sempre informe ao usuario onde os arquivos foram criados e os nomes exatos

## Assumed Triggers

Use este skill principalmente em pedidos como:
- "Transforme esse PRD e a arquitetura em backlog"
- "Monte o backlog do produto com epicos, historias e dependencias"
- "Quero priorizar o backlog desse produto para o MVP"

## References

- Leia [backlog-framework.md](./references/backlog-framework.md) para orientar decomposicao, priorizacao e cortes.
- Leia [backlog-template.md](./references/backlog-template.md) para produzir o backlog final.
- Leia [kanban-template.md](./references/kanban-template.md) para inicializar ou atualizar o board operacional.
