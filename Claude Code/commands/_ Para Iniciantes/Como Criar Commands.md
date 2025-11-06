# Como Criar Commands

Guia passo a passo para criar seus próprios commands.

## 1. Estrutura Básica

Todo command é um arquivo `.md` com:

```markdown
---
description: O que o command faz
---

Instruções do que fazer
```

## 2. Onde Criar

**Para seu projeto:**
```bash
mkdir -p .claude/commands
```

**Para todos projetos:**
```bash
mkdir -p ~/.claude/commands
```

## 3. Anatomia de um Command

### Frontmatter (Opcional)
```yaml
---
description: Descrição curta
allowed-tools: Read, Write, Edit
argument-hint: [tipo] [mensagem]
model: sonnet
---
```

### Corpo (Obrigatório)
```markdown
# Título do Command

Instruções detalhadas do que fazer.

Pode incluir:
- Listas de tarefas
- Código para executar
- Referências a arquivos
```

## 4. Recursos Avançados

### Argumentos

**Todos os argumentos:**
```markdown
Processar: $ARGUMENTS
```

**Argumentos específicos:**
```markdown
Issue número: $1
Prioridade: $2
```

### Executar Bash
```markdown
Status atual:
!`git status`
```

### Referenciar Arquivos
```markdown
Analisar configuração:
@package.json
```

## 5. Exemplo Completo

Arquivo: `.claude/commands/pr.md`

```markdown
---
description: Cria PR com review automático
allowed-tools: Bash(git:*), Bash(gh:*)
argument-hint: [branch] [título]
---

# Criar Pull Request

## 1. Verificar branch
!`git branch --show-current`

## 2. Push das mudanças
!`git push -u origin HEAD`

## 3. Criar PR
Crie PR de current branch para main com título: $2

## 4. Auto-review
- Verificar testes passando
- Checar cobertura
- Validar lint

## 5. Adicionar descrição
Baseado no diff, escreva descrição clara do que mudou e por quê.
```

## 6. Testar seu Command

1. Salve o arquivo
2. Digite `/` no chat para ver lista
3. Use `/seu-command` para testar

## 7. Dicas Importantes

### DO ✅
- Nome descritivo e curto
- Instruções claras e específicas
- Documente argumentos esperados
- Teste antes de compartilhar

### DON'T ❌
- Nomes genéricos (test, run)
- Instruções vagas
- Assumir contexto
- Esquecer de documentar

## 8. Commands Úteis para Começar

### Hello World
```markdown
---
description: Meu primeiro command
---

Diga "Olá, mundo!" e mostre a data/hora atual.
```

### Status
```markdown
---
description: Mostra status do projeto
allowed-tools: Bash(git status:*), Bash(npm:*)
---

Mostre:
1. Branch atual
2. Mudanças pendentes
3. Último commit
4. Se há testes rodando
```

## Próximo Passo

Veja [[IA/Claude Code/commands/_Para Iniciantes/Exemplos Simples]] para mais inspiração!

---

*Criar commands é simples: arquivo .md com instruções.*