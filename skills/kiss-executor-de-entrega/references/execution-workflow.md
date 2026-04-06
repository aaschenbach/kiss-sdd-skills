# Execution Workflow

Use este material para executar com seguranca a partir de um item detalhado.

## Sequencia recomendada

0. Preparar Git (Sync & Branch)
1. Validar insumos
2. Escolher tarefa
3. Confirmar dependencias
4. Implementar
5. Validar
6. Atualizar relatorio
7. Decidir o proximo passo / Abrir Pull Request

## 0. Preparar Git (Sync & Branch)

Verifique se o projeto utiliza Git (ex: `git rev-parse --is-inside-work-tree`).

**Se houver Git:**
1. Sincronize: `git checkout main && git pull`
2. Prepare Branch: `git checkout -b task/FXXTYY-slug`
   - Se estiver executando multiplas tarefas, use uma branch unica para o conjunto.

**Se nao houver Git:**
- Ignore este passo e continue a execucao local direta.

## 1. Validar insumos

Confirme:
- o arquivo `FXXTYY-slug-do-item.md` existe
- o relatorio `FXXTYY-slug-do-item.execution.md` existe ou pode ser criado
- o `dev-docs/03-backlog/kanban.md` existe ou pode ser atualizado quando houver acompanhamento operacional
- a tarefa escolhida existe
- o estado do codigo nao contradiz o plano
- o item ainda esta alinhado ao backlog e a arquitetura

Se houver acompanhamento operacional e a linha do item nao existir no board, reconcilie o `kanban.md` antes de executar qualquer tarefa.

## 2. Escolher tarefa

Modos:
- manual: o usuario indica `Tn`
- guiado: escolher a proxima tarefa sem dependencias pendentes
- sequencial: executar um conjunto pequeno e seguro

Preferencia:
- use uma tarefa por vez
- execute varias apenas quando a validacao entre elas for simples e o risco for baixo

## 3. Confirmar dependencias

Antes de implementar, cheque:
- `depends on` resolvido
- pre-requisitos tecnicos prontos
- ausencia de bloqueio por decisao pendente
- seguranca e privacidade cobertas no plano

Se houver bloqueio, nao improvise. Registre no relatorio.
Se o bloqueio for real para o item, sincronize o board com status `blocked`.

## 4. Implementar

Implemente apenas o escopo da tarefa atual.

Durante a execucao, registre:
- desvios de plano
- descoberta tecnica relevante
- necessidade de ajuste em tarefa futura

Ao iniciar a execucao de um item, sincronize o board para `in_progress` quando houver `kanban.md`.

## 5. Validar

No minimo, cheque:
- funcionalidade esperada
- testes aplicaveis
- permissoes e seguranca
- privacidade e dados
- logs, auditoria ou observabilidade quando relevantes

## 6. Atualizar relatorio

Use um relatorio unico por item.

Cada rodada deve registrar:
- data ou contexto da execucao
- tarefa executada
- status
- implementacao realizada
- validacoes
- pendencias
- licoes aprendidas

## 7. Decidir o proximo passo / Abrir Pull Request

Conclua sempre com uma destas saidas:
- proxima tarefa liberada
- bloqueado por dependencia
- precisa revisar o plano
- precisa voltar para backlog ou arquitetura

### Conclusao de Item ou Pacote (PR Workflow)

Se a rodada encerrar a implementacao validada de um item ou conjunto de tarefas:
1. Sincronize o board para `review` ou `done`.
2. **Se houver Git:**
    - Execute `git add .` e sugira mensagens de commit claras.
    - **Apos confirmacao do usuario**, execute `git push` e abra o Pull Request para a `main`.
    - Se o GitHub CLI (`gh`) estiver disponivel, ofereca-se para criar o PR automaticamente: `gh pr create --title "FXXTYY-slug-do-item" --body "Implementacao validada do item."`.

## Regra de ouro

Nao avance para a proxima tarefa apenas porque a implementacao foi iniciada. Avance apenas quando a tarefa atual estiver concluida ou quando o desvio estiver claramente registrado e aceito.
