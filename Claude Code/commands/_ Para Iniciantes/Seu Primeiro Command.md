# Seu Primeiro Command

Vamos criar um command do zero em 5 minutos.

## O que vamos fazer

Criar um command `/status` que mostra:
- Branch atual do git
- Mudanças pendentes
- Último commit
- Se testes estão passando

## Passo 1: Criar a Pasta

No terminal do seu projeto:

```bash
mkdir -p .claude/commands
```

## Passo 2: Criar o Arquivo

Crie `.claude/commands/status.md`:

```bash
touch .claude/commands/status.md
```

## Passo 3: Escrever o Command

Copie e cole este conteúdo:

```markdown
---
description: Mostra status completo do projeto
allowed-tools: Bash(git:*), Bash(npm test:*)
---

# Status do Projeto

## 📍 Branch Atual
!`git branch --show-current`

## 📝 Mudanças Pendentes
!`git status --short`

## 🕐 Último Commit
!`git log -1 --oneline`

## ✅ Testes
Verificar se existem testes e rodar se houver.

## 📊 Resumo
Forneça um resumo:
- Tudo limpo para commit?
- Branch está atualizada?
- Alguma ação recomendada?
```

## Passo 4: Testar

1. Abra o Claude Code no seu projeto
2. Digite `/status`
3. Veja a mágica acontecer!

## Passo 5: Personalizar

Agora customize para suas necessidades:

### Adicionar Mais Informações

```markdown
## 📦 Dependências
!`npm outdated`

## 🔍 TODOs
Buscar por TODO e FIXME no código
```

### Adicionar Argumentos

```markdown
---
argument-hint: [verbose]
---

Modo: ${1:-normal}

Se verbose, mostrar diff completo.
```

### Tornar Inteligente

```markdown
## 🤖 Análise Inteligente

Baseado no status:
- Se há mudanças: sugerir commit message
- Se branch divergiu: sugerir pull/merge
- Se testes falhando: identificar qual
```

## Exemplo Completo Melhorado

```markdown
---
description: Status inteligente do projeto
allowed-tools: Bash(git:*), Bash(npm:*), Grep
argument-hint: [verbose|simple]
---

# Status do Projeto

## 🚀 Quick Check

Branch: !`git branch --show-current`
Mudanças: !`git status --porcelain | wc -l` arquivos
Último commit: !`git log -1 --format="%h %s"`

## 📊 Análise Detalhada

### Git Status
!`git status`

### Verificações
1. ✅ Testes passando?
2. ✅ Lint sem erros?
3. ✅ Branch atualizada com main?
4. ✅ Sem conflitos de merge?

## 💡 Recomendações

Baseado no status atual, sugira próximos passos:
- Fazer commit se mudanças prontas
- Pull se branch desatualizada
- Resolver conflitos se existem
- Rodar testes se não rodaram recentemente

## 📝 Preparar Commit

Se há mudanças staged, sugerir mensagem de commit
seguindo Conventional Commits.
```

## Troubleshooting

### Command não aparece?
- Verifique se está em `.claude/commands/`
- Nome do arquivo deve terminar em `.md`
- Reinicie o Claude Code

### Erro ao executar?
- Verifique `allowed-tools` no frontmatter
- Comandos bash precisam de permissão

### Não faz o que esperava?
- Instruções devem ser claras e específicas
- Teste incrementalmente

## Próximos Commands para Criar

Depois do primeiro, tente estes:

1. **`/commit`** - Commit inteligente
2. **`/pr`** - Criar pull request
3. **`/deploy`** - Deploy automatizado
4. **`/fix`** - Corrigir issue específica
5. **`/review`** - Review de código

## Dicas Finais

### Comece Simples
Primeiro command = uma tarefa que você faz sempre

### Itere
Melhore o command conforme usa

### Compartilhe
Commands bons podem ajudar toda equipe

### Documente
`description` clara ajuda outros a entender

## Parabéns! 🎉

Você criou seu primeiro command!

Agora você pode:
- Criar quantos commands quiser
- Automatizar tarefas chatas
- Padronizar processos
- Economizar horas de trabalho

## Próximos Recursos

- [[../README|Ver todos os commands disponíveis]]
- [[Como Criar Commands|Aprender recursos avançados]]
- [[IA/Claude Code/commands/_Para Iniciantes/Exemplos Simples|Mais exemplos práticos]]

---

*Seu primeiro command em 5 minutos. Os próximos são ainda mais fáceis.*