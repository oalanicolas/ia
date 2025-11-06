---
description: Audit completo de segurança
allowed-tools: Read, Grep, Bash(npm audit:*), Bash(pip check:*), WebSearch
argument-hint: [foco específico ou scan completo]
---

# Security Audit

Análise completa de vulnerabilidades e riscos de segurança.

## Escopo: ${ARGUMENTS:-scan completo}

## Checklist de Segurança

### 1. OWASP Top 10

**A01: Broken Access Control**
- [ ] Verificar autenticação em todas rotas
- [ ] Validar autorização por recurso
- [ ] Checar CORS configuration

**A02: Cryptographic Failures**
- [ ] Buscar senhas em texto plano
- [ ] Verificar uso de HTTPS
- [ ] Algoritmos de hash seguros

**A03: Injection**
- [ ] SQL Injection
- [ ] Command Injection
- [ ] XSS (Cross-Site Scripting)
- [ ] Template Injection

**A04: Insecure Design**
- [ ] Rate limiting implementado
- [ ] Validação de entrada
- [ ] Princípio do menor privilégio

### 2. Análise de Código

**Buscar por**:
```grep patterns
- password|secret|key|token
- eval\(|exec\(
- innerHTML|dangerouslySetInnerHTML
- raw SQL queries
- TODO|FIXME|HACK
```

### 3. Dependências

**Verificar vulnerabilidades**:
- NPM: `npm audit`
- Python: `pip-audit` ou `safety check`
- Ruby: `bundle audit`
- Consultar CVE database

### 4. Configuração

**Arquivos sensíveis**:
- [ ] .env não está no git
- [ ] Secrets não hardcoded
- [ ] Configs de prod seguras
- [ ] Debug desabilitado em prod

### 5. Infraestrutura

**Headers de Segurança**:
- [ ] Content-Security-Policy
- [ ] X-Frame-Options
- [ ] X-Content-Type-Options
- [ ] Strict-Transport-Security

### 6. Relatório

**Classificar por severidade**:
- 🔴 **Crítico**: Correção imediata
- 🟡 **Alto**: Correção urgente
- 🟢 **Médio**: Planejar correção
- ⚪ **Baixo**: Boas práticas

**Para cada vulnerabilidade**:
- Descrição do risco
- Impacto potencial
- Como corrigir
- Código de exemplo

Foco: $ARGUMENTS