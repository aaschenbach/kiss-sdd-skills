# Handoff Checklist

Use este checklist para decidir se o fluxo pode avancar sem comprometer qualidade.

## 1. Idea -> PRD

Pode avancar quando houver, no minimo:
- problema claro
- publico prioritario
- proposta de valor
- recorte de MVP
- lingua principal do sistema e da documentacao definida
- riscos e restricoes principais
- seguranca e privacidade mapeadas em nivel de produto

Bloqueios tipicos:
- objetivo abstrato demais
- publico mal definido
- escopo inflado
- ausencia de criterio de sucesso

## 2. PRD -> Arquitetura

Pode avancar quando houver, no minimo:
- fluxos principais
- requisitos funcionais
- requisitos nao funcionais
- lingua e convencoes relevantes para sistema e documentacao
- dependencias externas conhecidas
- requisitos de seguranca, privacidade e compliance
- decisoes de produto suficientemente claras para orientar tradeoffs tecnicos

Bloqueios tipicos:
- requisitos contraditorios
- ausencia de restricoes operacionais
- indefinicao sobre tenancy, integracoes ou dados sensiveis

## 3. Arquitetura -> Backlog

Pode avancar quando houver, no minimo:
- stack recomendada
- boundaries principais
- integracoes e APIs relevantes
- convencoes de repositorio e arquivos `AGENTS.md` e `README.md` criados ou atualizados quando necessario
- requisitos estruturais de seguranca e privacidade
- dependencias e riscos tecnicos relevantes

Bloqueios tipicos:
- arquitetura abstrata demais
- falta de clareza sobre enablers
- dependencia externa sem dono ou sem plano

## 4. Backlog -> Detalhamento

Pode avancar quando houver, no minimo:
- item priorizado
- objetivo claro
- criterio de aceite
- dependencias conhecidas
- `kanban.md` inicializado desde a definicao dos itens em acompanhamento operacional, quando aplicavel
- uso simples e coerente de `todo` versus `blocked`, com `blocked` restrito a impedimento real e atual
- testes e validacoes esperadas explicitados
- impacto de seguranca e privacidade classificado
- ordem sugerida de execucao

Bloqueios tipicos:
- item grande demais
- backlog sem corte de MVP
- falta de prioridade ou dependencia

## Estrutura de decisao recomendada

Ao final de cada fase, conclua com:
- status: pronto ou nao pronto
- lacunas bloqueantes
- proxima fase recomendada
- menor proximo passo util
- validacoes ou testes pendentes
- mensagens de commit sugeridas no mesmo idioma principal da documentacao e dos artefatos
- consistencia entre backlog, board operacional e relatorios de execucao, quando aplicavel
