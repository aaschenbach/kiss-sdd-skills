---
name: kiss-especialista-de-qa
description: "Estrutura a etapa de QA com foco em cobertura funcional, validacao operacional e roteiros de testes manuais executaveis. Use quando o usuario quiser criar, revisar ou consolidar um roteiro manual final em pt-BR, transformar implementacao real em fluxo de teste ponta a ponta, mapear validacoes, erros, permissoes, isolamento, evidencias e fluxos API-first, ou preparar handoff de qualidade apos a execucao."
---

# Especialista de QA

## Overview

Receba o contexto funcional e tecnico ja implementado, reconcilie documentacao e comportamento real do sistema e produza artefatos de QA prontos para execucao humana.

O foco principal deste skill e transformar a implementacao existente em um roteiro de testes manuais detalhado, rastreavel e operacional. Se o pedido vier em formato mais aberto, preserve a disciplina de QA e conduza a saida para um artefato utilizavel, com escopo, massa, evidencias e resultados esperados.

Este skill atua depois de discovery, arquitetura, backlog, detalhamento e execucao. Ele nao substitui planejamento de produto nem implementacao.

Crie os artefatos desta etapa, por padrao, em `dev-docs/06-qa/` na raiz do projeto. Ao finalizar, informe explicitamente ao usuario quais arquivos foram criados ou atualizados, com caminho e nome.

## Regras Transversais

- Preserve a lingua definida para sistema e documentacao; se o contexto estiver ambiguo, registre a lacuna antes de consolidar o artefato.
- Siga essa mesma lingua ao sugerir mensagens de commit, salvo instrucao explicita em contrario.
- Crie `AGENTS.md` na raiz do projeto se ele nao existir e mantenha `AGENTS.md` e `README.md` atualizados sempre que a etapa de QA introduzir convencoes operacionais, artefatos, handoffs ou orientacoes de uso que devam permanecer visiveis no projeto.
- Quando a etapa iniciar uma nova frente relevante, oriente sincronizar a `main` local com `git pull`, criar branch curta e abrir PR para `main` ao fim do pacote validado.
- Ao encerrar a etapa, sugira mensagens de commit objetivas para os artefatos criados ou revisados.
- Antes de recomendar encerramento da entrega, instrua o usuario a revisar o roteiro, validar a cobertura e confirmar se o handoff de QA esta pronto para execucao.
- Quando houver acompanhamento operacional, reconcilie `dev-docs/03-backlog/kanban.md` e os relatorios `.execution.md` para garantir que o item testado tenha status, evidencias e pendencias coerentes.

## Workflow

### 1. Validar as entradas

Confirme se existem insumos suficientes para produzir um artefato de QA confiavel.

Cheque, no minimo:
- PRD, backlog, tarefa detalhada ou relato de execucao, quando existirem
- implementacao real ou documentacao operacional vigente
- lingua principal do sistema e da documentacao
- ambiente disponivel para teste
- seeds oficialmente suportados
- regras de permissao, isolamento e fluxos API-first relevantes

Se faltar material critico, liste as lacunas antes de consolidar o roteiro.

### 2. Reconstruir a verdade do sistema

Antes de escrever, reconcilie o comportamento real do produto a partir do minimo necessario:
- documentacao funcional vigente
- rotas web e API implementadas
- telas, templates e fluxos reais
- testes automatizados relevantes
- relatorios de execucao, changelog ou notas operacionais

Se houver divergencia entre documentacao antiga e implementacao atual, privilegie a implementacao real e registre a discrepancia.

Use [qa-workflow.md](./references/qa-workflow.md) para conduzir essa reconciliacao.

### 3. Definir ambiente, massa e estrategia

Antes de descrever os casos, estabeleca:
- como subir e limpar o ambiente
- quais migracoes e seeds sao suportadas
- qual massa base sera criada durante o proprio roteiro
- quais usuarios, departamentos, entidades e valores concretos serao reutilizados
- quais evidencias devem ser coletadas

Evite massa implicita, seeds nao suportados e placeholders vagos.

### 4. Montar o roteiro operacional

Produza um fluxo executavel de ponta a ponta com ordem operacional real.

Cubra, conforme aplicavel:
- preparacao de ambiente
- smoke inicial
- onboarding ou acesso inicial
- autenticacao
- administracao e configuracoes
- jornadas principais por perfil
- validacoes, erros e permissoes
- seguranca e isolamento
- fluxos API-first
- checklist final de evidencias

Cada bloco principal deve explicitar `Precondicao`, `Dados`, `Passos` e `Resultado esperado`.

### 5. Revisar cobertura e prontidao

Antes de concluir, revise:
- se o artefato esta em formato final e nao intermediario
- se todos os dados citados sao concretos e executaveis
- se nao ha placeholders ou instrucoes vagas
- se a ordem dos passos respeita pre-condicoes reais
- se validacoes negativas, permissao e isolamento estao cobertos
- se o template final foi seguido

Use [test-flow-template.md](./references/test-flow-template.md) para consolidar a saida final.

## Interaction Rules

- Produza roteiro operacional, nao plano de teste abstrato, salvo instrucao explicita do usuario.
- Use apenas comportamentos, campos, rotas e telas que existam no sistema real ou estejam claramente definidos no contexto entregue.
- Parta sempre de ambiente limpo ou explicite a preparacao minima necessaria.
- Nao use placeholders como `<id>`, `<email>` ou similares.
- Quando um valor dinamico for inevitavel, instrua explicitamente o testador a capturar o valor real e reutiliza-lo nos passos seguintes.
- Sempre explicite usuarios, papeis, departamentos, valores validos, valores invalidos e evidencias esperadas.
- Sempre diferencie fluxo principal, matriz transversal e checklist final.
- Se o pedido vier como "revisar QA" ou "avaliar cobertura", responda apontando lacunas concretas e, quando fizer sentido, proponha ou entregue o roteiro ajustado.

## Output Modes

- Roteiro manual final: fluxo completo pronto para execucao humana.
- Revisao de cobertura QA: avaliacao de lacunas, riscos e inconsistencias.
- Handoff de QA: consolidacao de ambiente, massa, roteiro e evidencias para validacao final.

## Document Convention

- Pasta padrao desta etapa: `dev-docs/06-qa/`
- Nome sugerido para o principal artefato: `roteiro-de-testes-manuais.md` ou nome equivalente alinhado ao item ou modulo validado
- Quando houver `dev-docs/03-backlog/kanban.md` e `dev-docs/05-execucao/*.execution.md`, reconcilie status, evidencias e pendencias relevantes
- Crie `AGENTS.md` se estiver ausente e atualize `AGENTS.md` e `README.md` quando a etapa introduzir novas convencoes operacionais ou novo handoff do fluxo
- Se a mudanca for relevante no repositorio, recomende sincronizar a `main`, usar branch dedicada e abrir PR para `main` apos revisao
- Ao concluir, recomende revisao final do roteiro antes da execucao
- Ao concluir, sugira mensagens de commit para os artefatos desta etapa
- Ao concluir, sempre informe ao usuario onde os arquivos foram criados e os nomes exatos

## Assumed Triggers

Use este skill principalmente em pedidos como:
- "Crie o roteiro de testes manuais dessa implementacao"
- "Revise a cobertura de QA desse fluxo"
- "Transforme a implementacao atual em um roteiro de validacao final"
- "Prepare o handoff de QA depois da execucao"

## References

- Leia [qa-workflow.md](./references/qa-workflow.md) para orientar a analise de ambiente, massa, cobertura e revisao final.
- Leia [test-flow-template.md](./references/test-flow-template.md) para produzir o roteiro manual final.
