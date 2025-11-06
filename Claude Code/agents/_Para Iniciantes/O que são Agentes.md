# O que são Agentes

Explicação simples para quem está começando.

## Analogia Simples

Pense nos agentes como **consultores especializados**.

**Sem agente:**
É como perguntar para um amigo inteligente - ele sabe de tudo um pouco.

**Com agente:**
É como contratar um especialista - ele sabe MUITO sobre aquela área específica.

## Na Prática

Claude normal:
```
Você: "Crie uma API"
Claude: "Vou criar uma API básica com Express..."
```

Com agente backend-architect:
```
Você: "Crie uma API"
Claude: "Vou projetar usando Clean Architecture, com camadas separadas,
autenticação JWT, rate limiting, cache Redis, documentação OpenAPI..."
```

## Por Que Usar?

1. **Qualidade** - Código profissional desde o início
2. **Aprendizado** - Veja como experts fariam
3. **Velocidade** - Menos idas e vindas
4. **Consistência** - Mesmo padrão sempre

## Como Funcionam

Cada agente tem três coisas:

1. **Personalidade** - Quem ele é
2. **Conhecimento** - O que sabe
3. **Ferramentas** - O que pode fazer

```javascript
{
  systemPrompt: "Você é um arquiteto backend...",
  tools: ["read_file", "write_file"],
  temperature: 0.7
}
```

## Tipos Principais

- **Arquitetos** - Desenham a estrutura
- **Desenvolvedores** - Escrevem o código
- **Auditores** - Procuram problemas
- **DevOps** - Fazem rodar em produção

## Primeiro Passo

1. Escolha um agente simples como `python-pro`
2. Faça uma tarefa pequena
3. Compare com o que você faria
4. Aprenda com a diferença

A partir daí, você vai entender quando e como usar cada um.