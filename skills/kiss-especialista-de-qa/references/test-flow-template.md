# QA Test Flow Template

## 1. Objetivo

[[descrever o objetivo do roteiro de QA no contexto real do sistema]]

## 2. Escopo e Premissas

- [[descrever o ambiente base]]
- [[descrever os seeds realmente suportados]]
- [[descrever a politica de massa funcional]]
- [[descrever limitacoes relevantes do ambiente]]
- [[descrever quando usar UI e quando usar HTTP manual]]

## 3. Preparacao do Ambiente

### [[identificador do bloco de preparacao]]

**Precondicao**

- [[descrever a precondicao minima]]

**Dados**

- [[listar dados, ou declarar que nao ha dados adicionais]]

**Passos**

1. [[descrever o primeiro passo executavel]]
2. [[descrever o segundo passo executavel]]
3. [[continuar ate fechar a preparacao]]

**Resultado esperado**

- [[descrever os resultados verificaveis da preparacao]]

## 4. Convencoes do Roteiro

- [[descrever a estrategia de sessoes e perfis]]
- [[descrever o padrao de evidencia]]
- [[descrever como registrar IDs e URLs reais]]
- [[descrever regras operacionais do roteiro]]

## 5. Dados de Teste Base

| Campo | Valor |
|---|---|
| [[campo]] | `[[valor concreto]]` |
| [[campo]] | `[[valor concreto]]` |
| [[campo]] | `[[valor concreto]]` |

## 6. Roteiro Principal

### [[identificador e nome do bloco]]

**Precondicao**

- [[descrever a precondicao real]]

**Dados**

- [[listar usuario, perfil, departamento, valores validos, valores invalidos, textos, prioridades, datas ou declarar explicitamente que nao ha dados adicionais]]

**Passos**

1. [[abrir rota ou tela concreta]]
2. [[clicar em acao concreta]]
3. [[preencher campo concreto com valor concreto]]
4. [[confirmar acao]]
5. [[validar mensagem, resposta ou mudanca de estado]]

**Resultado esperado**

- [[descrever o efeito funcional esperado]]
- [[descrever o comportamento de validacao, persistencia ou auditoria esperado]]

### [[identificador e nome do bloco]]

**Precondicao**

- [[descrever a precondicao real]]

**Dados**

- [[listar os dados concretos usados neste bloco]]

**Passos**

1. [[navegar]]
2. [[preencher]]
3. [[salvar]]
4. [[validar]]

**Resultado esperado**

- [[descrever o resultado esperado]]

### [[repetir o bloco acima para todos os casos principais do roteiro]]

## 7. Matriz de Validacoes e Erros

| Area | Casos obrigatorios |
|---|---|
| [[area]] | [[listar os erros e validacoes concretos]] |
| [[area]] | [[listar os erros e validacoes concretos]] |
| [[area]] | [[listar os erros e validacoes concretos]] |

## 8. Matriz de Permissoes

| Acao | [[perfil 1]] | [[perfil 2]] | [[perfil 3]] | [[perfil 4]] |
|---|---|---|---|---|
| [[acao concreta]] | [[sim ou nao]] | [[sim ou nao]] | [[sim ou nao]] | [[sim ou nao]] |
| [[acao concreta]] | [[sim ou nao]] | [[sim ou nao]] | [[sim ou nao]] | [[sim ou nao]] |

## 9. Matriz de Transicoes de Status

### [[perfil ou capacidade]]

- `[[status_origem]] -> [[status_destino]]`
- `[[status_origem]] -> [[status_destino]]`

### [[perfil ou capacidade]]

- `[[status_origem]] -> [[status_destino]]`
- `[[status_origem]] -> [[status_destino]]`

## 10. Matriz de Filtros, Busca e Paginacao

### [[contexto 1]]

- `[[filtro_ou_parametro]]`
- `[[filtro_ou_parametro]]`
- `[[filtro_ou_parametro]]`

### [[contexto 2]]

- `[[filtro_ou_parametro]]`
- `[[filtro_ou_parametro]]`
- `[[filtro_ou_parametro]]`

[[incluir instrucao para executar ao menos um caso positivo e um negativo por filtro quando aplicavel]]

## 11. Matriz de Seguranca e Isolamento

[[escrever uma lista objetiva de testes manuais de autorizacao, isolamento e nao vazamento]]

**Resultado esperado**

- [[descrever o comportamento de bloqueio esperado]]
- [[descrever o comportamento de nao vazamento esperado]]

## 12. Fluxos API-First Obrigatorios

### [[identificador e nome do fluxo API-first]]

**Precondicao**

- [[descrever a precondicao]]

**Dados**

- [[descrever os dados concretos]]

**Passos**

1. [[executar chamada HTTP concreta]]
2. [[registrar a resposta]]
3. [[repetir com cenario invalido, se aplicavel]]

**Resultado esperado**

- [[descrever o resultado esperado]]

### [[repetir para cada fluxo API-first obrigatorio]]

## 13. Checklist Final de Evidencias

- [[evidencia obrigatoria 1]]
- [[evidencia obrigatoria 2]]
- [[evidencia obrigatoria 3]]
- [[evidencia obrigatoria 4]]
- [[evidencia obrigatoria 5]]

## 14. Revisao Final Antes de Entregar

- [[confirmar que todos os blocos principais usam Precondicao, Dados, Passos e Resultado esperado]]
- [[confirmar que nao existem placeholders residuais no documento final]]
- [[confirmar que todos os usuarios, perfis e departamentos citados sao concretos]]
- [[confirmar que IDs dinamicos sao capturados como valor real durante a execucao]]
- [[confirmar que o documento reflete a implementacao real]]
- [[confirmar que erros, permissoes, isolamento e fluxos API-first foram cobertos]]
