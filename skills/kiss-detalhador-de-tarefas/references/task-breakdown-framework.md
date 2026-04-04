# Task Breakdown Framework

Use este material para quebrar um item de backlog em execucao tecnica.

## Sequencia recomendada

1. Entender o item
2. Mapear impacto tecnico
3. Definir tarefas base
4. Acrescentar validacao e qualidade
5. Ordenar execucao

## 1. Entender o item

Confirme:
- o que precisa ser entregue
- como saber se esta pronto
- o que nao faz parte
- quais riscos sao conhecidos

## 2. Mapear impacto tecnico

Pergunte:
- quais modulos ou servicos mudam?
- ha mudanca de contrato de API?
- ha alteracao de schema ou migracao?
- ha requisitos de seguranca ou auditoria?
- ha impacto em observabilidade ou operacao?

## 3. Definir tarefas base

Tipos comuns:
- analise ou refinamento tecnico
- implementacao frontend
- implementacao backend
- banco de dados e migracoes
- integracao externa
- configuracao de infraestrutura
- observabilidade
- documentacao tecnica

Nem todo item precisa de todos esses tipos.

Padrao de identificacao:
- use um arquivo por item de backlog, no formato `FXXTYY-slug-do-item.md`
- use `T1`, `T2`, `T3` para tarefas
- use `T2.1`, `T2.2` para subtarefas quando necessario

Cada tarefa deve deixar claro:
- titulo
- objetivo
- depends on
- validation
- done when

Se o item tiver impacto de seguranca ou privacidade, acrescente explicitamente:
- tarefa tecnica de protecao quando houver implementacao necessaria
- validacao de permissao, acesso, retencao, auditoria ou tratamento de dados sensiveis
- testes ou verificacoes correspondentes

## 4. Acrescentar validacao e qualidade

Cheque:
- testes unitarios ou equivalentes
- testes de integracao ou contrato
- verificacao manual critica
- validacao de permissao e seguranca
- validacao de privacidade e tratamento de dados
- monitoramento ou logs necessarios

## 5. Ordenar execucao

Organize por:
- dependencias
- desbloqueio tecnico
- possibilidade de paralelismo
- risco de integracao

## Estrutura de sintese recomendada

- Objetivo do item
- Impacto tecnico
- Tarefas
- Testes
- DoD
- Sequencia de execucao
