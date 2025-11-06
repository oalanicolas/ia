---
description: Refatora código mantendo funcionalidade
allowed-tools: Read, Edit, Write
argument-hint: [arquivo ou função]
---

# Refatoração Inteligente

Melhore a qualidade do código sem alterar comportamento.

## Target: ${ARGUMENTS:-arquivo atual}

## Processo de Refatoração

### 1. Análise Inicial
- Leia o código target
- Identifique problemas:
  - Duplicação de código
  - Funções muito grandes
  - Nomes confusos
  - Lógica complexa
  - Acoplamento alto

### 2. Técnicas de Refatoração

**Extract Method**
- Funções > 20 linhas
- Blocos com comentário explicativo
- Código duplicado

**Rename Variable/Function**
- Nomes não descritivos
- Abreviações confusas
- Convenções inconsistentes

**Simplify Conditionals**
- IFs aninhados profundos
- Condições complexas
- Early returns

**Remove Dead Code**
- Código comentado antigo
- Funções não utilizadas
- Imports desnecessários

### 3. Implementação
- Faça uma mudança por vez
- Mantenha testes passando
- Preserve comportamento original

### 4. Melhorias Aplicadas
Liste:
- O que foi refatorado
- Por que era necessário
- Benefícios obtidos

### 5. Validação
- Testes continuam passando
- Funcionalidade preservada
- Código mais limpo e legível

Target: $ARGUMENTS