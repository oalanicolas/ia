# Claude Code Skills 🎯

Bem-vindo à minha coleção pessoal de **Claude Skills**!

## O que é uma Claude Skill?

Uma **Claude Skill** é uma pasta contendo instruções, scripts e recursos que o Claude carrega dinamicamente para se tornar especialista em tarefas específicas. É como dar ao Claude um manual de procedimentos para tarefas que você executa com frequência.

As skills ensinam ao Claude como completar tarefas de forma **repetível e consistente**. Seja:
- Criar documentos com sua marca pessoal ou da empresa
- Analisar dados usando seus próprios workflows
- Automatizar tarefas recorrentes
- Executar procedimentos técnicos especializados
- Gerar conteúdo em tom ou estilo específicos

Cada skill é **autocontida em uma pasta** com um arquivo `SKILL.md` que contém as instruções e metadados que o Claude usa.

## 📚 Esta Pasta

Esta é a **minha coleção pessoal de skills favoritos** - aqueles que uso com frequência e considero mais valiosos para meu workflow. Aqui você encontra skills que já testei, refinei e que realmente funcionam bem.

## 📖 Para Saber Mais

- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

---

## Skills vs MCP: Qual a Diferença?

Se você está descobrindo Claude Skills, provavelmente já ouviu falar em **MCP (Model Context Protocol)**. São tecnologias complementares, mas com propósitos diferentes.

### 📊 Tabela Comparativa

| Aspecto | **Claude Skills** | **MCP (Model Context Protocol)** |
|---------|------------------|--------------------------------|
| **Propósito** | Expertise em tarefas específicas | Integração com dados e APIs externos |
| **Portabilidade** | Funciona em Claude.ai, Code e API | Requer configuração de servidor |
| **Execução de Código** | Pode executar scripts | Fornece ferramentas e recursos |
| **Eficiência de Tokens** | 30-50 tokens até ser ativada | Varia conforme implementação |
| **Melhor Para** | Tarefas repetitivas, workflows documentação | Acesso a bancos de dados, APIs |

### 🎯 Quando Usar Cada Uma?

**Use Claude Skills quando:**
- Você tem procedimentos que repete frequentemente
- Quer manter instruções complexas sincronizadas
- Precisa aplicar um tom, estilo ou brand específicos
- Quer automatizar workflows com scripts executáveis

**Use MCP quando:**
- Precisa integrar com APIs externas (Slack, GitHub, etc.)
- Quer conectar a bancos de dados
- Necessita de ferramentas que consultam informações em tempo real
- Está construindo agentes que precisam acessar sistemas externos

### 🔄 Podem Trabalhar Juntas?

**Sim!** De fato, as skills podem criar servidores MCP. Você pode usar uma skill para **guiar a criação de um MCP** quando precisar de integrações mais complexas.

---

# Sobre Esta Coleção

Esta pasta contém uma coleção curada de skills que demonstram o que é possível com o sistema de skills do Claude. Os exemplos variam de aplicações criativas (arte, design) a tarefas técnicas (testes web, geração de servidores) até workflows empresariais (comunicações, branding).

Cada skill é **autocontida em sua própria pasta** com um arquivo `SKILL.md` contendo as instruções e metadados que o Claude utiliza. Aqui você encontra inspiração para suas próprias skills e entende diferentes padrões e abordagens.

## ⚠️ Aviso Importante

**Estas skills são fornecidas para fins demonstrativos e educacionais.** Sempre teste skills completamente em seu próprio ambiente antes de depender delas para tarefas críticas. As implementações e comportamentos podem variar conforme o contexto de uso.

---

## 🔗 Minhas Fontes de Referência

Aqui estão os repositórios e recursos que frequentemente consulto para descobrir e aprender novas skills:

1. **[Awesome Claude Skills (travisvn)](https://github.com/travisvn/awesome-claude-skills)**
   - A mais completa coleção curada de Claude Skills da comunidade
   - Documentação detalhada sobre cada skill
   - Seções sobre criação, segurança e best practices

2. **[Awesome Claude Skills (BehiSecc)](https://github.com/BehiSecc/awesome-claude-skills)**
   - Outra perspectiva curada da comunidade
   - Foco em skills práticas e úteis

3. **[MCP Servers - Anthropic Skills](https://mcpservers.org/claude-skills/anthropic/pdf)**
   - Catálogo de servidores MCP que integram com skills
   - Referência para skills avançadas que precisam de integração

---

# Estrutura de uma Skill

Criar uma skill é simples - é apenas uma pasta com um arquivo `SKILL.md` contendo frontmatter YAML e instruções.

Exemplo básico:

```markdown
---
name: minha-skill
description: Uma descrição clara do que essa skill faz e quando usar
---

# Minha Skill

Aqui vão as instruções que o Claude seguirá quando esta skill estiver ativa.

## Exemplos
- Exemplo de uso 1
- Exemplo de uso 2

## Diretrizes
- Diretriz 1
- Diretriz 2
```

**Campos obrigatórios do frontmatter:**
- `name` - Identificador único para sua skill (minúsculo, hífens para espaços)
- `description` - Descrição completa do que a skill faz e quando usar

Para mais detalhes, veja [Como criar custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills).

---

## 💡 Próximos Passos

Se você está descobrindo skills ou quer aprender mais:

1. **Explore as fontes de referência** acima (Awesome Claude Skills)
2. **Teste skills existentes** em Claude.ai ou Claude Code
3. **Crie sua primeira skill** para uma tarefa que você repete frequentemente
4. **Refine conforme necessário** - as melhores skills evoluem com o uso

---

**Última atualização:** Novembro 2025