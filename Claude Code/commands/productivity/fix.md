---
description: Corrige issue específica do GitHub/GitLab
allowed-tools: Read, Edit, Write, Bash(gh issue:*), Bash(git:*), WebFetch
argument-hint: [número da issue ou URL]
---

# Fix Issue

Resolva uma issue específica do repositório.

## Issue: #$1

## Workflow

1. **Buscar detalhes da issue**
   - Se número fornecido: use `gh issue view $1`
   - Se URL: faça fetch da página
   - Entenda o problema reportado

2. **Criar branch para fix**
   ```bash
   git checkout -b fix-issue-$1
   ```

3. **Identificar arquivos afetados**
   - Busque por código mencionado na issue
   - Localize componentes relacionados

4. **Implementar correção**
   - Faça as mudanças necessárias
   - Mantenha mudanças focadas na issue
   - Adicione testes se necessário

5. **Validar correção**
   - Teste a solução
   - Verifique se não quebra nada
   - Confirme que resolve o problema

6. **Criar commit descritivo**
   ```bash
   git commit -m "fix: resolve issue #$1 - [descrição breve]"
   ```

7. **Preparar para PR** (se solicitado)
   - Push da branch
   - Sugestão de descrição do PR
   - Link para issue

Issue/URL: $ARGUMENTS