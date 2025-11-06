---
description: Analisa mudanças e cria commit com mensagem inteligente
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git add:*), Bash(git commit:*)
argument-hint: [tipo] [escopo] [descrição]
---

# Git Commit Inteligente

Analise as mudanças e crie um commit seguindo Conventional Commits.

## Status atual
!`git status --short`

## Mudanças
!`git diff --stat`

## Instruções

1. Analise todas as mudanças não commitadas
2. Identifique o tipo de mudança:
   - feat: nova funcionalidade
   - fix: correção de bug
   - docs: documentação
   - style: formatação
   - refactor: refatoração
   - test: testes
   - chore: manutenção

3. Se houver arquivos não rastreados importantes, adicione com `git add`
4. Crie commit com mensagem no formato: `tipo(escopo): descrição`
5. Mostre o resultado com `git log -1 --oneline`

Argumentos opcionais: $ARGUMENTS