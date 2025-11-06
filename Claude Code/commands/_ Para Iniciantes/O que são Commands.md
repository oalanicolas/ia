# O que são Commands no Claude Code

Commands são atalhos personalizados que automatizam tarefas repetitivas no desenvolvimento.

## Conceito Simples

Imagine que toda vez que você faz commit, precisa:
1. Verificar o que mudou
2. Escrever uma mensagem
3. Fazer o commit

Com um command `/commit`, você faz tudo em um comando só.

## Como Funcionam

1. **Você cria** um arquivo `.md` com instruções
2. **Coloca** na pasta `.claude/commands/`
3. **Usa** digitando `/nome-do-command`

## Exemplo Real

Arquivo: `.claude/commands/ola.md`
```markdown
---
description: Diz olá
---

Olá! Como posso ajudar hoje?
```

Uso: Digite `/ola` no chat

## Por Que Usar?

- **Economiza tempo**: Um comando faz várias coisas
- **Padroniza**: Todos na equipe fazem igual
- **Evita erros**: Processo sempre correto
- **Documenta**: Commands são documentação viva

## Commands vs Comandos Normais

**Sem command:**
```
"Por favor, verifique os testes, depois faça build,
e se tudo passar, faça deploy para staging"
```

**Com command:**
```
/deploy staging
```

## Tipos de Commands

### 1. Simples
Apenas texto/instruções

### 2. Com Argumentos
Aceita parâmetros: `/fix 123`

### 3. Com Bash
Executa comandos: `!`git status``

### 4. Com Arquivos
Lê arquivos: `@package.json`

## Próximos Passos

1. Leia [[Como Criar Commands]]
2. Veja [[IA/Claude Code/commands/_Para Iniciantes/Exemplos Simples]]
3. Crie [[Seu Primeiro Command]]

---

*Commands transformam tarefas complexas em simples.*