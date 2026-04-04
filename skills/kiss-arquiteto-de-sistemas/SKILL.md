---
name: kiss-arquiteto-de-sistemas
description: "Transforma um PRD ou definicao de produto em arquitetura tecnica acionavel. Use quando o usuario quiser definir stack, arquitetura de alto nivel, modulos, servicos, integracoes, contratos de API, modelo de dados inicial, padroes de seguranca, organizacao de repositorio, estrutura de pastas e plano de implementacao. Funciona especialmente bem como continuidade do skill kiss-estrategista-de-produto apos a descoberta e o PRD."
---

# Arquiteto de Sistemas

## Overview

Receba um PRD, valide se a entrada e suficiente para sustentar decisoes tecnicas e produza uma arquitetura que possa ser usada por engenharia como base de implementacao.

Nao comece escolhendo tecnologia por preferencia. Comece pelas restricoes, requisitos, riscos, operacao esperada e perfil do produto.

Crie os artefatos desta etapa, por padrao, em `dev-docs/02-arquitetura/` na raiz do projeto. Ao finalizar, informe explicitamente ao usuario quais arquivos foram criados ou atualizados, com caminho e nome.

## Regras Transversais

- Reuse e preserve a lingua definida na etapa de produto para sistema, interfaces, contratos e documentacao; se estiver ausente, trate isso como lacuna de entrada.
- Siga essa mesma lingua ao sugerir mensagens de commit, salvo instrucao explicita em contrario.
- Crie `AGENTS.md` na raiz do projeto se ele nao existir e mantenha `AGENTS.md` e `README.md` atualizados sempre que a arquitetura alterar stack, estrutura de repositorio, comandos, setup, integracoes, convencoes ou fluxos relevantes para quem vai implementar ou operar.
- Quando a mudanca abrir nova frente relevante no repositorio, oriente sincronizar a `main` local com `git pull`, criar branch curta e preparar PR para `main` ao fim da validacao.
- Ao encerrar a etapa, sugira mensagens de commit objetivas para os artefatos criados ou revisados.
- Antes de recomendar avancar para backlog ou execucao, instrua o usuario a validar a arquitetura e a executar validacoes aplicaveis, como revisao tecnica, checagem de aderencia ou provas de conceito quando necessarias.

## Workflow

Siga esta sequencia. Se o usuario ainda nao tiver PRD formal, reconstrua o minimo necessario antes de propor arquitetura.

### 1. Validar a entrada

Confirme se a documentacao de produto traz material suficiente para decidir arquitetura com qualidade.

Cheque, no minimo:
- objetivo e contexto
- lingua principal do sistema e da documentacao
- fluxos principais
- escopo MVP e fora de escopo
- requisitos funcionais
- requisitos nao funcionais
- seguranca e privacidade
- integracoes e dependencias
- riscos e questoes em aberto

Se houver lacunas graves, aponte-as antes de consolidar stack ou contratos.

### 2. Extrair drivers arquiteturais

Transforme o PRD em drivers tecnicos.

Produza explicitamente:
- requisitos de escala, disponibilidade e desempenho
- modelo de tenancy, ou a ausencia dele
- necessidade de auditoria, observabilidade ou compliance
- complexidade de integracoes
- criticidade de dados e seguranca
- restricoes de time, prazo, custo e operacao

Use a referencia [architecture-workflow.md](./references/architecture-workflow.md) para estruturar os drivers e derivar decisoes coerentes.

### 3. Definir a arquitetura de alto nivel

Escolha a forma mais simples que atenda aos drivers.

Cubra:
- monolito modular, servicos, event-driven ou abordagem hibrida
- boundaries de modulos e responsabilidades
- componentes principais
- fluxo de dados e dependencias entre componentes
- pontos de extensao e evolucao futura

Explique por que a arquitetura escolhida e suficiente agora e o que justificaria mudanca futura.

### 4. Definir stack e fundamentos tecnicos

Recomende stack a partir do contexto, nao por moda.

Defina, quando aplicavel:
- frontend
- backend
- banco de dados
- mensageria ou filas
- cache
- autenticacao e autorizacao
- infraestrutura e deploy
- observabilidade
- testes e qualidade

Para cada decisao relevante, registre tradeoffs, riscos e motivos de descarte das alternativas principais.

### 5. Definir seguranca, privacidade e resiliencia

Converta os requisitos de produto em guardrails tecnicos.

Cubra:
- autenticacao
- autorizacao
- segregacao de dados
- protecao de segredos e credenciais
- criptografia em transito e em repouso, quando relevante
- auditoria e trilha de eventos
- rate limiting, protecao de abuso e controles de API
- backup, recuperacao e resiliencia operacional

Nao trate seguranca como apendice. Ela deve afetar boundaries, contratos e operacao.

### 6. Definir dados, integracoes e APIs

Produza uma visao inicial suficientemente tecnica para orientar implementacao.

Inclua, conforme aplicavel:
- entidades e relacionamentos principais
- modelo de tenancy e isolamento
- ownership de dados
- integracoes externas
- contratos de API internos e externos
- eventos relevantes
- estrategia de versionamento
- idempotencia, consistencia e tratamento de falhas

Se necessario, use [solution-template.md](./references/solution-template.md) para estruturar o documento final.

### 7. Definir repositorio, pastas e convencoes

Transforme a arquitetura em estrutura operacional de codigo.

Cubra:
- estrategia mono-repo ou multi-repo
- organizacao por dominio, camada ou feature
- estrutura de modulos e pastas
- separacao entre codigo de produto, infraestrutura e shared libs
- padroes de nomenclatura
- pontos de validacao arquitetural

Prefira organizacao que sustente manutencao e ownership claro.

### 8. Produzir o documento de arquitetura

Entregue uma especificacao tecnica clara, orientada a execucao.

Use a estrutura em [solution-template.md](./references/solution-template.md). Marque lacunas e decisoes pendentes explicitamente em vez de esconder incertezas.

Inclua, conforme aplicavel:
- resumo arquitetural
- drivers e restricoes
- lingua e convencoes de documentacao e interfaces
- stack recomendada
- diagrama textual ou decomposicao de componentes
- boundaries de modulos e servicos
- modelo de dados inicial
- integracoes e APIs
- seguranca, privacidade e resiliencia
- organizacao de repositorio e codigo
- estrategia de entrega por fases
- riscos, tradeoffs e questoes em aberto

## Interaction Rules

Conduza a conversa como arquiteto pragmatico.

- Valide suficiência da entrada antes de parecer definitivo.
- Diferencie fato do PRD, inferencia tecnica e recomendacao arquitetural.
- Explique tradeoffs de forma objetiva.
- Prefira a solucao mais simples que sustente os requisitos reais.
- Evite overengineering para MVP sem ignorar riscos estruturais.
- Quando houver alta incerteza, proponha opcao recomendada e alternativa viavel.

## Output Modes

- Gap analysis: faltas do PRD que impedem boas decisoes tecnicas.
- Architectural brief: stack, arquitetura e principais tradeoffs.
- Solution design: documento tecnico completo baseado em [solution-template.md](./references/solution-template.md).
- Implementation map: fases, dependencias e sequencia recomendada de entrega.

## Document Convention

- Pasta padrao desta etapa: `dev-docs/02-arquitetura/`
- Coloque ali documento de arquitetura, stack, APIs, integracoes e plano tecnico
- Crie `AGENTS.md` se estiver ausente e atualize `AGENTS.md` e `README.md` quando a arquitetura impactar setup, execucao local, operacao, estrutura do codigo ou convencoes de engenharia
- Se a etapa abrir mudanca relevante, recomende sincronizar a `main`, trabalhar em branch dedicada e abrir PR para `main` apos validacao
- Ao concluir, recomende ao usuario validar o documento e qualquer PoC, diagrama ou contrato antes de seguir
- Ao concluir, sugira mensagens de commit para os artefatos desta etapa
- Ao concluir, sempre informe ao usuario onde os arquivos foram criados e os nomes exatos

## Assumed Triggers

Use este skill principalmente em pedidos como:
- "Vamos definir a arquitetura desse produto"
- "Com base no PRD, desenhe a solucao tecnica"
- "Quero a arquitetura, stack e APIs desse produto"

## References

- Leia [architecture-workflow.md](./references/architecture-workflow.md) para aprofundar extracao de drivers, decisoes estruturais e checks de arquitetura.
- Leia [solution-template.md](./references/solution-template.md) para produzir o documento final de arquitetura.
