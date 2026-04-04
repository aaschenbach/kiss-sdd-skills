# Backlog Framework

Use este material para converter PRD e arquitetura em backlog priorizado.

## Sequencia recomendada

1. Ler objetivo e MVP
2. Mapear fluxos principais
3. Identificar capacidades necessarias
4. Separar funcionalidade de enablers
5. Definir hierarquia do backlog
6. Priorizar
7. Cortar releases

## 1. Ler objetivo e MVP

Extraia:
- objetivo de negocio
- publico prioritario
- problema central
- resultado esperado do MVP

Sem isso, o backlog vira lista de pedidos soltos.

## 2. Mapear fluxos principais

Para cada fluxo principal:
- qual resultado ele produz
- quem inicia
- qual dependencia tecnica relevante existe
- o que precisa existir para o fluxo ser considerado pronto

## 3. Identificar capacidades necessarias

Converta o material de entrada em blocos de capacidade:
- onboarding
- autenticacao
- gestao de dados
- fluxo transacional
- relatorios
- notificacoes
- administracao
- observabilidade
- compliance

Use nomes aderentes ao dominio do produto, nao force categorias genericas se nao fizer sentido.

## 4. Separar funcionalidade de enablers

Classifique cada item como:
- funcionalidade voltada ao usuario
- enabler tecnico
- item de seguranca ou compliance
- item operacional

Se um item nao entrega valor sozinho, mas viabiliza entrega segura ou escalavel, ele continua valido como backlog.

Para cada item, cheque explicitamente:
- impacto de seguranca: none, low, medium ou high
- impacto de privacidade: none, low, medium ou high
- necessidade de enabler adicional de seguranca, privacidade, auditoria ou compliance

## 5. Definir hierarquia do backlog

Estrutura recomendada:
- epico: bloco de valor ou capacidade relevante
- feature: recorte entregavel dentro do epico
- historia: item planejavel com criterio de aceite
- enabler: item tecnico ou estrutural necessario

## 6. Priorizar

Priorize por:
- valor para o usuario ou negocio
- reducao de risco
- dependencia tecnica
- desbloqueio de outras entregas
- urgencia externa

Evite priorizar apenas por facilidade tecnica.

## 7. Cortar releases

Monte ao menos:
- MVP
- proxima release
- backlog posterior

Deixe explicito:
- o que ficou de fora
- por que ficou de fora
- quais dependencias impedem antecipacao
- quais itens de seguranca e privacidade precisam entrar cedo para evitar risco estrutural

## Estrutura de sintese recomendada

- Logica de priorizacao
- MVP
- Release seguinte
- Epicos
- Features
- Historias
- Enablers
- Dependencias
- Itens prontos para detalhamento
