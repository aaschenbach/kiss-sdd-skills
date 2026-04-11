# QA Workflow

## 1. Objetivo da etapa

Transformar implementacao real e artefatos tecnicos existentes em um pacote de QA executavel, com foco em validacao manual, rastreabilidade, evidencias e cobertura funcional.

## 2. Entradas recomendadas

- PRD ou definicao funcional vigente
- documento de arquitetura ou restricoes tecnicas
- backlog e item detalhado quando houver
- relatorio `.execution.md` ou diff recente da entrega
- rotas web e API implementadas
- telas, templates e fluxos reais
- testes automatizados relevantes
- documentacao operacional do ambiente

## 3. Regras obrigatorias

- Escrever em portugues do Brasil quando esta for a lingua do projeto.
- Privilegiar a implementacao real quando houver divergencia com documentacao antiga.
- Produzir artefato final executavel, nao texto exploratorio.
- Partir de ambiente limpo e seeds oficialmente suportados.
- Nao depender de massa oculta ou configuracoes manuais nao documentadas.
- Nao usar placeholders vagos.
- Explicitar sempre resultado esperado e evidencia minima.

## 4. Reconstrucao da verdade do sistema

Antes de escrever o roteiro:

1. Confirmar quais fluxos existem de fato.
2. Identificar campos, rotas, respostas HTTP, mensagens e regras reais.
3. Mapear quais perfis podem executar cada acao.
4. Verificar isolamento, seguranca, validacoes negativas e trilhas paralelas.
5. Registrar divergencias entre o que esta documentado e o que esta implementado.

## 5. Preparacao do ambiente

Definir com precisao:

- como subir a aplicacao
- migracoes necessarias
- seeds suportados
- contas iniciais disponiveis
- dados que precisam ser criados durante o roteiro
- limites conhecidos do ambiente

Se o ambiente nao for reproduzivel, sinalizar a lacuna antes de concluir o artefato.

## 6. Massa base recomendada

Antes de escrever os casos, definir um conjunto pequeno e reutilizavel de dados:

- tenant ou organizacao principal
- admin principal
- usuarios secundarios por perfil
- departamentos ou agrupamentos
- entidades centrais do fluxo, como tickets, pedidos, cadastros ou registros
- valores invalidos para testes negativos

Essa massa deve ser concreta, repetivel e suficiente para cobrir jornada principal, erros, permissoes, isolamento e operacao.

## 7. Estrutura do roteiro

O roteiro final deve seguir, quando aplicavel, esta ordem:

1. Objetivo
2. Escopo e premissas
3. Preparacao do ambiente
4. Convencoes do roteiro
5. Dados de teste base
6. Roteiro principal
7. Matriz de validacoes e erros
8. Matriz de permissoes
9. Matriz de transicoes de status
10. Matriz de filtros, busca e paginacao
11. Matriz de seguranca e isolamento
12. Fluxos API-first obrigatorios
13. Checklist final de evidencias
14. Revisao final antes de entregar

## 8. Estrutura de cada bloco principal

Cada bloco principal deve conter:

- titulo claro
- `Precondicao`
- `Dados`
- `Passos`
- `Resultado esperado`

## 9. Padrões de escrita

### Fazer

- Usar instrucoes concretas e verificaveis.
- Nomear rotas, telas, campos e acoes de forma explicita.
- Definir valores validos e invalidos reais.
- Explicar quando trocar perfil, abrir nova sessao ou registrar um identificador dinamico.
- Relacionar cada bloco a um resultado observavel.

### Nao fazer

- Nao escrever "testar cadastro" ou "validar tela" genericamente.
- Nao assumir conhecimento oral do testador.
- Nao descrever funcionalidades hipoteticas.
- Nao misturar roteiro operacional com brainstorming de qualidade.

## 10. Cobertura minima recomendada

Cobrir, conforme aplicavel ao contexto:

- onboarding ou preparacao inicial
- autenticacao, logout e recuperacao de acesso
- configuracoes administrativas
- jornadas principais por perfil
- validacoes e erros
- permissoes
- filtros, busca e paginacao
- seguranca e isolamento
- fluxos API-first
- checklist final de evidencias

## 11. Revisao final

Antes de concluir:

- conferir se nao ha placeholders
- conferir se todos os passos sao executaveis
- conferir se os dados sao concretos
- conferir se a ordem esta coerente
- conferir se erros, permissao e isolamento foram cobertos
- conferir se as evidencias esperadas estao explicitas

## 12. Integracao com o fluxo KISS

- Consumir artefatos de `dev-docs/01-produto/` a `dev-docs/05-execucao/` quando existirem.
- Produzir artefatos de QA em `dev-docs/06-qa/`.
- Reconciliar backlog, kanban e relatorios de execucao quando a etapa de QA revelar gaps ou bloqueios.
- Preparar handoff final de validacao sem bloquear indevidamente backlog, detalhamento ou execucao quando a etapa de QA for complementar.
