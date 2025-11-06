---
description: Gera documentação automática do código
allowed-tools: Read, Write, Grep
argument-hint: [arquivo, diretório ou tipo de doc]
---

# Gerador de Documentação

Crie documentação profissional automaticamente.

## Target: ${ARGUMENTS:-projeto completo}

## Tipos de Documentação

### 1. README.md
Se não existe ou está incompleto, gerar:
- Título e descrição
- Features principais
- Instalação
- Como usar
- Exemplos
- Configuração
- Contribuindo
- Licença

### 2. API Documentation
Para backend/bibliotecas:
- Endpoints disponíveis
- Parâmetros e tipos
- Responses esperadas
- Exemplos de requisição
- Códigos de erro

### 3. JSDoc/DocStrings
Para funções sem documentação:
```javascript
/**
 * Descrição da função
 * @param {tipo} nome - Descrição
 * @returns {tipo} Descrição
 * @example
 * // Como usar
 */
```

### 4. Arquitetura
Documentar:
- Estrutura de pastas
- Fluxo de dados
- Decisões técnicas
- Padrões utilizados
- Diagramas (se apropriado)

### 5. Guias

**Getting Started**
- Setup do ambiente
- Primeiro exemplo funcionando
- Troubleshooting comum

**Contributing**
- Como reportar bugs
- Como submeter PRs
- Estilo de código
- Testes necessários

### 6. Changelog
Se existe histórico:
- Versões e datas
- Features adicionadas
- Bugs corrigidos
- Breaking changes

## Processo

1. **Análise**: Identificar o que precisa de documentação
2. **Extração**: Coletar informações do código
3. **Geração**: Criar documentação apropriada
4. **Formatação**: Markdown limpo e organizado
5. **Exemplos**: Adicionar casos de uso práticos

## Output

Gerar arquivos:
- README.md (principal)
- API.md (se aplicável)
- CONTRIBUTING.md (se projeto open source)
- Inline docs no código

Target: $ARGUMENTS