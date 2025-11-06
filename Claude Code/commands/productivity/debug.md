---
description: Debug avançado para encontrar e corrigir bugs
allowed-tools: Read, Edit, Bash(node:*), Bash(python:*), Grep
argument-hint: [descrição do erro ou arquivo]
---

# Debug Avançado

Encontre e corrija bugs complexos sistematicamente.

## Problema: $ARGUMENTS

## Estratégia de Debug

### 1. Reproduzir o Bug
- Entenda o comportamento esperado vs atual
- Identifique passos para reproduzir
- Colete mensagens de erro/logs

### 2. Isolar o Problema
- **Busque por padrões de erro**
  - Stack traces
  - Mensagens de log
  - Comportamento anormal

- **Técnicas de isolamento**:
  - Binary search (comentar metade do código)
  - Git bisect (se bug foi introduzido recentemente)
  - Adicionar logs/breakpoints estratégicos

### 3. Análise de Causa Raiz

**Checklist comum de bugs**:
- [ ] Null/undefined não tratado
- [ ] Off-by-one em loops
- [ ] Race conditions (async)
- [ ] Mutação indevida de estado
- [ ] Tipo incorreto de dados
- [ ] Caso edge não coberto
- [ ] Dependência quebrada
- [ ] Configuração incorreta

### 4. Implementar Correção
- Corrija o problema na raiz
- Não apenas os sintomas
- Adicione validações preventivas

### 5. Prevenir Regressão
- Adicione teste para o bug
- Documente o caso edge
- Melhore tratamento de erros

### 6. Verificar Correção
- Bug não reproduz mais
- Outros testes continuam passando
- Nenhum efeito colateral

Descrição: $ARGUMENTS