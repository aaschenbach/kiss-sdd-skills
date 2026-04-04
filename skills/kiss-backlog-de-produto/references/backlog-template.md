# Backlog Template

## 1. Resumo

- Objetivo do backlog
- Artefatos de entrada utilizados
- Lingua principal do sistema e da documentacao
- Logica de priorizacao
- Lacunas ou premissas assumidas
- Arquivo operacional associado: `dev-docs/03-backlog/kanban.md`

## 2. Recorte de releases

### MVP

- Itens incluidos
- Itens excluidos
- Justificativa

### Release seguinte

- Itens candidatos
- Dependencias

## 3. Epicos

Para cada epico:
- nome
- objetivo
- valor entregue
- dependencias principais

## 4. Features

Para cada feature:
- nome
- epico relacionado
- descricao
- prioridade
- dependencias

## 5. Historias ou itens funcionais

Para cada item:
- titulo
- feature relacionada
- objetivo
- criterio de aceite
- impacto de seguranca: `none | low | medium | high`
- impacto de privacidade: `none | low | medium | high`
- riscos ou observacoes

## 6. Enablers tecnicos

Para cada enabler:
- titulo
- objetivo tecnico
- motivo
- dependencia que desbloqueia
- relacao com seguranca, privacidade, auditoria ou compliance, se houver

## 7. Dependencias e bloqueios

- dependencia
- impacto
- item afetado
- acao sugerida

## 8. Itens prontos para detalhamento

- item no formato `FXXTYY-slug-do-item`
- fase estavel associada, como `F01` ou `F02`
- motivo de estar pronto
- dependencias resolvidas ou pendentes

## 9. Board operacional

- Crie ou atualize `dev-docs/03-backlog/kanban.md`
- Crie cada linha assim que o item priorizado receber identificador
- Inicialize itens priorizados como `todo` por padrao
- Mantenha `todo` quando ainda existir proxima acao util de detalhamento, refinamento ou preparacao, mesmo com dependencia mapeada
- Use `blocked` somente quando o item ja nascer sem avancar na fase atual por dependencia externa, decisao pendente, aprovacao obrigatoria ou impedimento real
- Nao marque como `blocked` apenas porque outro item vem antes na ordem ou porque existe dependencia sequencial planejada
- Mantenha o board consistente com os identificadores do backlog
