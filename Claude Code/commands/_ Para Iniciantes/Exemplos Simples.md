# Exemplos Simples de Commands

Commands práticos para você começar hoje.

## 1. Daily - Standup Diário

`.claude/commands/daily.md`
```markdown
---
description: Prepara resumo para daily standup
allowed-tools: Bash(git log:*)
---

# Daily Standup

## Ontem
Commits de ontem:
!`git log --since=yesterday --oneline --author=$(git config user.name)`

## Hoje
Listar 3 principais tarefas para hoje baseado no que está em progresso.

## Bloqueios
Algum impedimento identificado?
```

## 2. Clean - Limpar Projeto

`.claude/commands/clean.md`
```markdown
---
description: Limpa arquivos temporários e cache
allowed-tools: Bash(rm:*), Bash(find:*)
---

# Limpeza do Projeto

1. Remover node_modules se muito grande
2. Limpar cache (npm, pip, etc)
3. Deletar arquivos .log
4. Remover builds antigas
5. Mostrar quanto espaço foi liberado
```

## 3. Setup - Configurar Ambiente

`.claude/commands/setup.md`
```markdown
---
description: Configura ambiente de desenvolvimento
allowed-tools: Bash(npm:*), Write
---

# Setup do Ambiente

## 1. Instalar dependências
- Se existe package.json: npm install
- Se existe requirements.txt: pip install

## 2. Criar .env
Criar arquivo .env com variáveis básicas:
- DATABASE_URL
- API_KEY (placeholder)
- NODE_ENV=development

## 3. Verificar instalação
- Rodar teste básico
- Confirmar que servidor inicia
```

## 4. Todo - Listar Tarefas

`.claude/commands/todo.md`
```markdown
---
description: Lista TODOs no código
allowed-tools: Grep
---

# Buscar TODOs

Procure por:
- TODO
- FIXME
- HACK
- XXX

Organize por prioridade e arquivo.
Sugira quais resolver primeiro.
```

## 5. Prettier - Formatar Código

`.claude/commands/prettier.md`
```markdown
---
description: Formata código do projeto
allowed-tools: Bash(prettier:*), Bash(black:*), Bash(rubocop:*)
argument-hint: [arquivo ou pasta]
---

# Formatar Código

Target: ${ARGUMENTS:-.}

1. Detectar linguagem/framework
2. Usar ferramenta apropriada:
   - JS/TS: prettier
   - Python: black
   - Ruby: rubocop

3. Mostrar arquivos modificados
```

## 6. Branch - Criar Branch

`.claude/commands/branch.md`
```markdown
---
description: Cria branch com nome padrão
argument-hint: [tipo] [descrição]
allowed-tools: Bash(git:*)
---

# Criar Branch

Tipo: $1 (feat/fix/chore)
Descrição: $2

Criar branch: $1/$2
Exemplo: feat/add-login

!`git checkout -b $1/$2`
```

## 7. Version - Bump Version

`.claude/commands/version.md`
```markdown
---
description: Atualiza versão do projeto
argument-hint: [major|minor|patch]
allowed-tools: Edit, Bash(npm version:*)
---

# Bump Version

Tipo: ${1:-patch}

1. Se package.json existe:
   npm version $1

2. Se não, procurar version em:
   - setup.py
   - Cargo.toml
   - version.txt

3. Criar commit de versão
```

## 8. Env - Checar Variáveis

`.claude/commands/env.md`
```markdown
---
description: Verifica variáveis de ambiente
allowed-tools: Read, Grep
---

# Verificar Ambiente

1. Ler .env.example
2. Comparar com .env
3. Listar variáveis faltando
4. Sugerir valores padrão
5. Alertar sobre secrets expostos
```

## 9. Lint - Verificar Código

`.claude/commands/lint.md`
```markdown
---
description: Roda linter do projeto
allowed-tools: Bash(eslint:*), Bash(pylint:*)
---

# Lint Check

1. Identificar linter:
   - package.json scripts
   - .eslintrc
   - .pylintrc

2. Executar lint
3. Resumir problemas por tipo
4. Sugerir fixes automáticos
```

## 10. Help - Documentação Rápida

`.claude/commands/help.md`
```markdown
---
description: Mostra como usar função/comando
argument-hint: [comando ou função]
---

# Ajuda Rápida

Sobre: $1

1. Se é comando npm: mostrar do package.json
2. Se é função: buscar JSDoc/docstring
3. Se é CLI tool: mostrar --help
4. Dar exemplo de uso prático
```

## Como Usar

1. **Copie** o exemplo que precisa
2. **Cole** em `.claude/commands/nome.md`
3. **Customize** para seu projeto
4. **Use** com `/nome`

## Dica Pro

Comece com 2-3 commands simples que você usa sempre.
Depois vá adicionando conforme a necessidade.

## Próximo Passo

Crie [[Seu Primeiro Command]] agora!

---

*Exemplos práticos para você começar em 2 minutos.*