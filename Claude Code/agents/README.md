# Agentes Claude Code

Guia prático e direto sobre como usar agentes para desenvolver melhor e mais rápido.

## O Que São Agentes

Agentes são versões especializadas do Claude configuradas para tarefas específicas.

A diferença? Em vez de um Claude genérico, você tem um especialista que já sabe exatamente o que fazer.

**Exemplo prático:**
- Claude normal: "Vou criar uma API básica..."
- Agente backend-architect: "Vou projetar seguindo REST, com JWT, rate limiting, cache, OpenAPI..."

## Como Usar

### 1. Estrutura Básica

Cada agente precisa de:
```javascript
{
  systemPrompt: "Quem é e o que sabe fazer",
  tools: ["ferramentas que pode usar"],
  temperature: 0.7
}
```

### 2. Arquivo CLAUDE.md

Crie na raiz do projeto com contexto que o Claude deve sempre considerar:

```markdown
# CLAUDE.md
Projeto FastAPI com PostgreSQL.
Python 3.11, poetry para dependências.
Convenções: snake_case, type hints, docstrings em português.
```

### 3. Workflow que Funciona

A Anthropic testou e comprovou esta ordem:

1. **Research** - "pesquise o projeto e entenda X"
2. **Planning** - "planeje como implementar Y"
3. **Implementation** - "agora implemente"
4. **Testing** - "crie testes para validar"

Pular os dois primeiros é o erro mais comum.

### 4. Comandos Think

Peça para o Claude pensar quando precisar de análise profunda:

- `think` - análise rápida
- `think hard` - análise profunda
- `think harder` - múltiplas alternativas
- `ultrathink` - máximo de análise

## Para Iniciantes

Se está começando, veja a pasta **`Iniciantes/`** primeiro. Tem tudo explicado passo a passo.

## Agentes Disponíveis

Temos 31 agentes organizados em categorias. Os mais usados:

1. **backend-architect** - Projeta arquitetura de sistemas
2. **python-pro** - Desenvolvimento Python profissional
3. **frontend-developer** - React e interfaces modernas
4. **security-auditor** - Encontra vulnerabilidades
5. **deployment-engineer** - CI/CD e deploy

Veja a lista completa em cada pasta:
- `architecture/` - 10 agentes de arquitetura
- `backend/` - 3 especialistas em backend
- `frontend/` - 7 para interfaces
- `devops/` - 3 para infraestrutura
- `security/` - 2 para segurança
- `ai-ml/` - 3 para IA

## Exemplo Prático

Criando uma API do zero:

```bash
# 1. Arquitetura
"backend-architect: projete uma API de e-commerce"

# 2. Implementação
"python-pro: implemente usando FastAPI"

# 3. Testes
"test-automator: crie testes completos"

# 4. Segurança
"security-auditor: verifique vulnerabilidades"

# 5. Deploy
"deployment-engineer: configure CI/CD"
```

## Test-Driven Development (TDD)

O workflow favorito da Anthropic:

```bash
# 1. Testes primeiro
"Escreva testes para [feature]. NÃO implemente ainda."

# 2. Implementação mínima
"Implemente apenas o necessário para passar os testes."

# 3. Refatoração
"Melhore o código mantendo testes verdes."
```

## Dicas Importantes

**O que funciona:**
- Sempre pesquise antes de implementar
- Use comandos think para decisões complexas
- Combine múltiplos agentes
- Escreva testes primeiro

**O que evitar:**
- Pular direto para código
- Usar agente errado para a tarefa
- Não validar com testes
- Configurações genéricas demais

## Criando Seus Agentes

Exemplo de agente customizado:

```javascript
// meu-agente.js
module.exports = {
  systemPrompt: `Você é especialista em [área].
    Sempre considere [princípios].
    Use [ferramentas].`,
  tools: ['read_file', 'write_file'],
  temperature: 0.7
}
```

## Links Úteis

- [Documentação Oficial Claude Agent SDK](https://docs.anthropic.com/claude-agent-sdk)
- [Best Practices da Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Exemplos no GitHub](https://github.com/anthropics/claude-agent-sdk)

---

*A diferença entre um desenvolvedor mediano e um excepcional é saber usar as ferramentas certas.*