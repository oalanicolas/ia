---
description: Code review completo com segurança e qualidade
allowed-tools: Read, Grep, Bash(eslint:*), Bash(pylint:*), Bash(rubocop:*)
argument-hint: [arquivo ou diretório]
---

# Code Review Profissional

Análise completa de código focando em qualidade, segurança e melhores práticas.

## Alvo: ${ARGUMENTS:-todo o projeto}

## Checklist de Review

### 1. Análise Estática
- Executar linters disponíveis (ESLint, Pylint, etc)
- Verificar formatação e estilo
- Detectar code smells

### 2. Segurança
- [ ] Verificar inputs não sanitizados
- [ ] Buscar credenciais hardcoded
- [ ] Validar autenticação/autorização
- [ ] Checar vulnerabilidades OWASP Top 10
- [ ] Revisar dependências desatualizadas

### 3. Performance
- [ ] Identificar queries N+1
- [ ] Loops desnecessários
- [ ] Operações bloqueantes
- [ ] Uso eficiente de memória
- [ ] Caching apropriado

### 4. Arquitetura
- [ ] Separação de responsabilidades
- [ ] Princípios SOLID
- [ ] Padrões de projeto apropriados
- [ ] Modularização adequada

### 5. Manutenibilidade
- [ ] Nomenclatura clara
- [ ] Documentação de funções complexas
- [ ] Testes adequados
- [ ] Tratamento de erros
- [ ] Logs apropriados

### 6. Sugestões de Melhoria
Forneça:
- Problemas críticos (deve corrigir)
- Melhorias importantes (deveria corrigir)
- Sugestões menores (poderia melhorar)

Target: $ARGUMENTS