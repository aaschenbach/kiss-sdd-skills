---
name: kiss-posicionamento-de-marca
description: "Transforma um PRD ou definicao de produto em um documento de posicionamento de marca e direcao de marketing inicial. Use quando o usuario quiser, logo apos o PRD ou em qualquer outro momento, explorar opcoes de pitch, taglines, significado do nome, posicionamento, voz, mensagens principais, conceitos de logotipo, paletas de cores e direcao visual sem fechar uma unica resposta definitiva."
---

# Posicionamento de Marca

## Overview

Receba um PRD ou definicao de produto, preserve a estrategia do produto e produza um documento de marca orientado a opcoes, comparacoes e escolha posterior.

Esta skill nao substitui o PRD, nao substitui design final e nao bloqueia arquitetura, backlog ou execucao. Ela complementa o trabalho de produto com narrativa, identidade e direcao visual inicial.

Crie os artefatos desta etapa, por padrao, em `dev-docs/01-produto/` na raiz do projeto. Ao finalizar, informe explicitamente ao usuario quais arquivos foram criados ou atualizados, com caminho e nome.

## Regras Transversais

- Reutilize a lingua definida no PRD para narrativa, exemplos e artefatos de marca; se a lingua do sistema ou da documentacao estiver ausente, trate isso como lacuna de entrada.
- Siga essa mesma lingua ao sugerir mensagens de commit, salvo instrucao explicita em contrario.
- Trate esta etapa como opcional e nao como gate para `kiss-arquiteto-de-sistemas`, `kiss-backlog-de-produto` ou `kiss-detalhador-de-tarefas`.
- Crie `AGENTS.md` na raiz do projeto se ele nao existir e mantenha `AGENTS.md` e `README.md` atualizados sempre que a etapa alterar fluxo, artefatos, convencoes de handoff ou instrucoes duradouras.
- Quando a mudanca abrir nova frente relevante no repositorio, oriente sincronizar a `main` local com `git pull`, criar branch curta e preparar PR para `main` ao fim da validacao.
- Ao encerrar a etapa, sugira mensagens de commit objetivas para os artefatos criados ou revisados.
- Toda recomendacao de marca ou marketing deve ser apresentada em multiplas opcoes comparaveis. Nao entregue pitch unico, tagline unica, logo unico, paleta unica ou posicionamento unico como resposta fechada.
- Sempre que o usuario pedir uma decisao final, preserve ao menos duas alternativas viaveis antes de recomendar uma preferencia.

## Workflow

### 1. Validar a entrada

Confirme se existe base suficiente para propor marca com coerencia.

Cheque, no minimo:
- PRD completo, PRD parcial ou definicao de produto equivalente
- nome atual, nomes alternativos ou lacuna explicita de naming
- publico prioritario
- proposta de valor
- diferenciais percebidos
- lingua principal do sistema e da documentacao
- contexto competitivo ou sinais de categoria, quando existirem

Se faltarem elementos criticos, explicite as lacunas antes de fechar qualquer direcao.

### 2. Extrair os fundamentos de marca

Converta o produto em materia-prima de posicionamento.

Explicite:
- categoria percebida
- promessa central
- tensao de mercado ou problema simbolico resolvido
- personalidade esperada da marca
- sinais de credibilidade
- riscos de interpretacao

Use [marketing-options-framework.md](./references/marketing-options-framework.md) para organizar a analise.

### 3. Escolher os modulos de saida

Ative apenas os modulos sustentados pelo contexto e desejados pelo usuario.

Modulos recomendados:
- plataformas de posicionamento
- mensagens centrais e pilares
- sugestoes de pitch
- sugestoes de tagline
- interpretacoes do significado do nome, quando possivel
- voz e tom
- conceitos de logotipo
- paletas de cores do sistema
- direcao visual inicial
- mensagens de landing page ou hero section

Nao force todos os modulos quando o contexto nao sustentar esse nivel de definicao.

### 4. Produzir opcoes comparaveis

Para cada modulo ativado:
- entregue mais de uma opcao
- nomeie claramente cada alternativa
- explique racional, sinais que reforca e riscos
- diferencie opcoes mais conservadoras, aspiracionais ou ousadas quando isso ajudar a decisao

Regra obrigatoria:
- nunca responder com apenas uma sugestao por entregavel
- minimo recomendado de tres opcoes por entregavel principal
- se o contexto for fraco, reduzir profundidade, nao reduzir variedade

### 5. Traduzir posicionamento em sistema de marca

Quando houver direcao visual, conecte narrativa e forma.

Inclua conforme aplicavel:
- conceitos de simbolo ou logotipo em mais de uma direcao
- familias de formas, metaforas e referencias
- direcao tipografica
- paletas com justificativa semantica e funcional
- relacao entre paleta, legibilidade, acessibilidade e percepcao de categoria
- coerencia entre logo, produto e mensagens

Nao fingir que isso substitui design profissional final. Entregar briefing e direcao, nao arte final.

### 6. Consolidar o documento final

Use [brand-direction-template.md](./references/brand-direction-template.md) para produzir o documento de saida.

Inclua, conforme aplicavel:
- resumo da base de produto utilizada
- criterios de marca
- opcoes de posicionamento
- opcoes de pitch e tagline
- significado do nome, quando possivel
- opcoes de voz e mensagens
- opcoes de logo
- opcoes de paleta
- recomendacao preferencial com tradeoffs
- proximos testes ou validacoes

### 7. Encerrar com handoff claro

Ao concluir:
- informe arquivos criados ou atualizados
- deixe claro que arquitetura e backlog podem seguir independentemente
- recomende como escolher ou validar as opcoes com stakeholders
- sugira mensagens de commit

## Interaction Rules

- Preserve aderencia ao PRD e nao invente posicionamento incompativel com o produto.
- Diferencie fato do produto, inferencia de marca e recomendacao criativa.
- Trate marca como sistema de escolhas, nao como inspiracao solta.
- Sempre ofereca alternativas suficientes para comparacao real.
- Quando houver naming fraco ou provisiorio, sinalize como isso limita significado, narrativa e logo.
- Evite jargao publicitario vazio; priorize clareza, memorabilidade e coerencia.

## Output Modes

- Brand gap analysis: lacunas do PRD que impedem uma boa direcao de marca.
- Messaging options: opcoes de pitch, tagline, voz e mensagens.
- Visual direction pack: opcoes de logo, paleta e direcao visual.
- Full brand direction: documento completo em `dev-docs/01-produto/brand-direction.md`.

## Document Convention

- Pasta padrao desta etapa: `dev-docs/01-produto/`
- Documento principal recomendado: `dev-docs/01-produto/brand-direction.md`
- O PRD continua sendo a referencia principal de produto e esta etapa deve apontar para ele explicitamente
- Crie `AGENTS.md` se estiver ausente e atualize `AGENTS.md` e `README.md` quando a etapa introduzir novos artefatos, convencoes de marketing ou handoffs opcionais
- Se a etapa abrir mudanca relevante, recomende sincronizar a `main`, trabalhar em branch dedicada e abrir PR para `main` apos validacao
- Ao concluir, recomende revisao das opcoes com stakeholders antes de fechar direcao unica
- Ao concluir, sugira mensagens de commit para os artefatos desta etapa
- Ao concluir, sempre informe ao usuario onde os arquivos foram criados e os nomes exatos

## Assumed Triggers

Use este skill principalmente em pedidos como:
- "Depois do PRD, quero explorar posicionamento de marca"
- "Use o PRD para sugerir pitch, tagline e logo"
- "Quero um documento de direcao de marca para esse produto"
- "Com base no PRD, monte opcoes de narrativa e identidade visual"

## References

- Leia [marketing-options-framework.md](./references/marketing-options-framework.md) para estruturar fundamentos, modulos e comparacao entre alternativas.
- Leia [brand-direction-template.md](./references/brand-direction-template.md) para produzir o documento final.
