# Architecture Workflow

Use este material para converter o PRD em decisoes tecnicas coerentes.

## Sequencia recomendada

1. Validar entrada
2. Extrair drivers arquiteturais
3. Escolher forma arquitetural
4. Definir stack
5. Definir seguranca e resiliencia
6. Definir dados, integracoes e APIs
7. Estruturar repositorio e codigo
8. Planejar implementacao

## 1. Validar entrada

Antes de decidir arquitetura, confirme:
- problema e objetivo claros
- fluxos principais identificados
- escopo MVP definido
- requisitos nao funcionais minimamente descritos
- risco e compliance conhecidos
- dependencias externas mapeadas

Se faltar material critico, produza uma lista de lacunas bloqueantes.

## 2. Extrair drivers arquiteturais

Derive drivers a partir do PRD:
- volume esperado
- latencia toleravel
- frequencia de uso
- necessidade de multi-tenancy
- sensibilidade dos dados
- necessidade de trilha de auditoria
- complexidade de integracoes
- expectativa de crescimento
- maturidade do time
- restricoes de prazo e custo

Sem drivers claros, a decisao de stack vira opiniao.

Cheque explicitamente tenancy:
- o produto e single-tenant ou multi-tenant?
- tenant representa empresa, workspace, conta ou outra unidade?
- o isolamento precisa ser logico ou fisico?
- ha configuracao, branding, billing, quotas ou auditoria por tenant?
- autorizacao muda por tenant?

Se isso estiver indefinido, registre como decisao arquitetural pendente.

## 3. Escolher forma arquitetural

Comece simples.

Perguntas uteis:
- monolito modular resolve o problema atual?
- ha necessidade real de servicos separados?
- existe processamento assincrono relevante?
- o dominio exige desacoplamento forte desde o inicio?

Regra pratica:
- prefira monolito modular para MVP salvo restricao real
- introduza mensageria quando houver necessidade concreta
- separe servicos quando houver ownership, escala ou risco operacional distintos

## 4. Definir stack

Escolha stack com base em:
- adequacao ao problema
- produtividade do time
- maturidade operacional
- ecossistema e manutencao
- custo de operacao

Para cada decisao importante, registre:
- opcao escolhida
- motivo
- alternativa considerada
- custo ou risco da escolha

## 5. Definir seguranca e resiliencia

Cheque:
- modelo de identidade
- perfis e autorizacao
- isolamento entre tenants, se houver
- segredos e configuracoes
- logs e auditoria
- estrategia de backup e recuperacao
- comportamento sob falha de integracao
- controles contra abuso

## 6. Definir dados, integracoes e APIs

Produza:
- entidades principais
- modelo de tenancy e regra de isolamento
- ownership por modulo
- contratos entre componentes
- integrações externas e pontos de falha
- padrao de API
- eventos relevantes
- estrategia de versionamento

## 7. Estruturar repositorio e codigo

Escolha a estrutura que mais reduz acoplamento acidental.

Decisoes comuns:
- mono-repo vs multi-repo
- organizacao por dominio vs por camada
- shared libs minimas
- convencoes de testes, contratos e observabilidade

## 8. Planejar implementacao

Divida por fatias que entreguem valor e reduzam risco:
- fundacao tecnica
- fluxo principal
- integracoes essenciais
- seguranca e observabilidade
- expansoes posteriores

## Estrutura de sintese recomendada

- Drivers arquiteturais
- Arquitetura recomendada
- Stack
- Seguranca e resiliencia
- Dados e APIs
- Estrutura de codigo
- Fases de implementacao
- Riscos e pendencias
