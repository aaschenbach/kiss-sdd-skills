---
name: kiss-estrategista-de-produto
description: "Conduz descoberta e definicao de produto do objetivo abstrato ate um PRD tecnico detalhado. Use quando o usuario quiser criar, definir ou estruturar um novo produto, transformar uma ideia vaga em problema, proposta de valor, escopo, requisitos, metricas, roadmap inicial e handoff para design e engenharia. Exemplos de gatilho: 'Vamos criar um novo produto', 'Vamos definir um novo produto', 'Precisamos de um novo produto'."
---

# Estrategista de Produto

## Overview

Conduza o usuario por um processo de descoberta progressiva: clarifique o objetivo, identifique o problema real, delimite publico e contexto, formule a proposta de valor, valide o escopo central do produto, defina naming e transforme as decisoes em um PRD tecnico acionavel.

Evite pular direto para funcionalidades. Reduza ambiguidades antes de detalhar escopo, priorizacao, requisitos e plano de entrega.

Crie os artefatos desta etapa, por padrao, em `dev-docs/01-produto/` na raiz do projeto. Ao finalizar, informe explicitamente ao usuario quais arquivos foram criados ou atualizados, com caminho e nome.

## Regras Transversais

- Descubra cedo e registre explicitamente a lingua principal do sistema e da documentacao, por exemplo `pt-BR` ou `en-US`.
- Trate essa decisao de lingua como insumo obrigatorio para as proximas etapas.
- Siga essa mesma lingua ao sugerir mensagens de commit, salvo instrucao explicita em contrario.
- Crie `AGENTS.md` na raiz do projeto se ele nao existir e mantenha `AGENTS.md` e `README.md` atualizados sempre que a etapa alterar escopo, convencoes, fluxo, estrutura ou instrucoes de uso que precisem permanecer visiveis para o time.
- Quando a mudanca iniciar uma nova frente relevante no repositorio, oriente sincronizar a `main` local com `git pull`, criar uma branch curta de trabalho e abrir PR para `main` ao fim do pacote validado.
- Ao encerrar a etapa, sugira mensagens de commit objetivas para os artefatos criados ou revisados.
- Antes de recomendar avancar para a proxima fase, instrua o usuario a revisar e validar os artefatos gerados; se houver testes ou validacoes aplicaveis nesta etapa, explicite quais devem ser executados.

## Workflow

Siga esta sequencia e adapte a profundidade ao contexto. Se o usuario chegar com poucas informacoes, faca a descoberta em camadas. Se ele ja trouxer contexto rico, sintetize e avance mais rapido.

### 1. Clarificar o objetivo

Extraia o que o usuario quer que mude no mundo real ou no negocio.

Cubra, quando faltar:
- objetivo de negocio
- problema percebido
- urgencia
- restricoes relevantes
- horizonte de tempo
- lingua principal do sistema
- lingua principal da documentacao

Reformule o objetivo em uma frase verificavel antes de avancar.

### 2. Definir problema e publico

Transforme a ambicao inicial em uma definicao de problema.

Cubra:
- usuario ou cliente principal
- segmento ou perfil
- tarefa que ele tenta concluir
- dor atual
- alternativas existentes
- custo de nao resolver

Se houver confusao entre usuario, comprador e operador, separe claramente os papeis.

### 3. Formular proposta de valor e tese

Consolide a direcao do produto.

Produza explicitamente:
- job to be done principal
- proposta de valor
- diferenciadores
- suposicoes criticas
- riscos de adocao, viabilidade e desejabilidade

Se necessario, use a referencia [discovery-framework.md](./references/discovery-framework.md) para estruturar hipoteses, sinais e criterios de decisao.

### 4. Delimitar escopo e MVP

Converta a tese em uma primeira versao executavel.

Defina:
- resultado esperado do MVP
- funcionalidades essenciais
- funcionalidades adiadas
- criterios de corte
- dependencias externas
- sequencia recomendada de entrega

Questione escopos inchados. Se algo nao sustenta a aprendizagem ou o valor inicial, empurre para depois.

### 5. Definir naming e checar colisao de mercado

Trate naming como etapa obrigatoria de fechamento da definicao de produto, preferencialmente depois de validar problema, publico, proposta de valor e escopo.

Cubra:
- tipo de nome desejado: descritivo, evocativo, composto, tecnico ou institucional
- criterios de marca: clareza, memorabilidade, pronunciacao, tom e alinhamento ao publico
- restricoes: idioma, geografia, categoria, SEO, dominio e naming existente no portfolio

Produza uma lista curta de candidatos com justificativa.

Antes de recomendar um nome final, faca verificacao atual de colisao no mercado. Essa verificacao deve ser feita com busca na web, porque nomes de empresas, produtos, dominios e apps mudam com frequencia.

Cheque, no minimo:
- empresas ou produtos ativos com nome identico ou muito proximo
- apps relevantes nas lojas ou resultados dominantes de busca
- dominios obvios indisponiveis, quando isso importar
- conflitos claros de categoria ou geografia

Nao afirme exclusividade legal. Trate isso como triagem de mercado e risco de confusao, nao como parecer juridico de marca.

Se houver risco moderado ou alto de colisao, proponha variantes e explique o tradeoff.

### 6. Definir sucesso, seguranca e operacao

Antes do PRD, explicite como o produto sera avaliado, protegido e operado.

Cubra:
- metricas de sucesso
- metricas de guarda
- eventos ou instrumentacao necessarios
- dados pessoais, dados sensiveis ou conteudo critico envolvidos
- permissoes, perfis de acesso e trilhas de auditoria necessarias
- exigencias de privacidade, retencao, consentimento ou compliance
- operacao manual inicial, se houver
- riscos legais, operacionais, de naming ou de integracao

### 7. Produzir o PRD tecnico

Entregue um PRD claro, orientado a execucao, com linguagem suficiente para alinhamento entre produto, design e engenharia.

Use a estrutura em [prd-template.md](./references/prd-template.md) e preencha apenas o que for sustentado pelo contexto. Marque lacunas explicitamente em vez de inventar respostas.

Inclua:
- contexto e motivacao
- nome recomendado do produto, alternativas consideradas e triagem factual resumida
- lingua principal do sistema e da documentacao
- problema e objetivo
- publico-alvo e personas operacionais
- proposta de valor
- escopo MVP e fora de escopo
- jornadas ou fluxos principais
- requisitos funcionais
- requisitos nao funcionais
- requisitos de seguranca, privacidade e compliance
- dados, eventos e metricas
- dependencias, riscos e questoes em aberto
- Definition of Done e criterios de qualidade
- criterio de aceite
- indicacao opcional de extensao pos-PRD com `kiss-posicionamento-de-marca`, quando fizer sentido

## Interaction Rules

Conduza a conversa como estrategista e nao como escriba passivo.

- Faca perguntas objetivas quando a ambiguidade bloquear boas decisoes.
- Explique tradeoffs quando houver mais de um caminho plausivel.
- Sinalize premissas explicitamente.
- Separe fatos, inferencias e recomendacoes.
- Ao avaliar nome, diferencie sugestao criativa de verificacao factual de mercado.
- Prefira sintese estruturada a brainstorm solto.
- Quando o usuario pedir velocidade, entregue uma versao enxuta agora e uma lista curta de lacunas para refinamento.

## Output Modes

Escolha o formato conforme o momento da conversa.

- Descoberta inicial: perguntas prioritarias e quadro sintetico do problema.
- Convergencia: resumo executivo com tese, publico, valor e MVP.
- Naming: candidatos, criterios, riscos de colisao e recomendacao obrigatoria.
- Definicao: decisao de escopo com justificativas e riscos.
- Handoff: PRD tecnico completo baseado em [prd-template.md](./references/prd-template.md).

## Document Convention

- Pasta padrao desta etapa: `dev-docs/01-produto/`
- Coloque ali discovery, sinteses, naming e PRD
- Quando fizer sentido, aponte no handoff a extensao opcional `kiss-posicionamento-de-marca` para aprofundar narrativa, posicionamento e identidade sem bloquear arquitetura ou backlog
- Crie `AGENTS.md` se estiver ausente e atualize `AGENTS.md` e `README.md` quando o PRD introduzir ou alterar contexto de produto, escopo, fluxos, convencoes ou instrucoes relevantes para o time
- Se a etapa abrir uma nova frente relevante, recomende sincronizar a `main`, criar branch dedicada e preparar PR para `main` depois da validacao
- Ao concluir, recomende a revisao do PRD e das demais definicoes geradas antes do handoff
- Ao concluir, sugira mensagens de commit para os artefatos desta etapa
- Ao concluir, sempre informe ao usuario onde os arquivos foram criados e os nomes exatos

## References

- Leia [discovery-framework.md](./references/discovery-framework.md) quando precisar aprofundar a etapa de descoberta, hipoteses, riscos e priorizacao.
- Leia [prd-template.md](./references/prd-template.md) quando estiver consolidando a saida final em formato de PRD.
