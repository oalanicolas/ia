# Exemplos Práticos de Commands

Casos reais de uso dos commands no dia a dia.

## 🚀 Workflow de Feature Nova

### Situação
Você vai implementar uma nova feature de login.

### Commands Usados

```bash
# 1. Criar branch da feature
/branch feat add-login-system

# 2. Verificar status antes de começar
/status

# 3. Após implementar, revisar código
/review src/auth/

# 4. Rodar testes
/test

# 5. Fazer commit
/commit

# 6. Deploy para staging
/deploy staging
```

### Tempo Economizado
- Sem commands: ~15 minutos de comandos manuais
- Com commands: 2 minutos

## 🐛 Correção de Bug em Produção

### Situação
Bug crítico reportado na issue #423.

### Commands Usados

```bash
# 1. Entender e corrigir o bug
/fix 423

# 2. Verificar segurança da correção
/security

# 3. Rodar testes específicos
/test src/api/users.test.js

# 4. Deploy emergencial
/deploy production hotfix
```

### Resultado
Bug corrigido e em produção em 10 minutos.

## 📊 Otimização de Performance

### Situação
Aplicação está lenta, precisa otimizar.

### Commands Usados

```bash
# 1. Identificar gargalos
/optimize src/

# 2. Aplicar refatoração
/refactor src/utils/dataProcessor.js

# 3. Verificar melhorias
/test --performance

# 4. Documentar mudanças
/docs performance-improvements
```

### Ganho
- 40% de melhoria na performance
- Código mais limpo
- Documentado automaticamente

## 🔒 Auditoria de Segurança

### Situação
Antes de lançar nova versão, verificar segurança.

### Commands Usados

```bash
# 1. Scan completo
/security

# 2. Revisar código sensível
/review src/auth/ src/api/

# 3. Atualizar dependências vulneráveis
/fix vulnerabilities

# 4. Gerar relatório
/docs security-audit
```

### Benefício
- 5 vulnerabilidades encontradas e corrigidas
- Relatório completo gerado
- Compliance garantida

## 📝 Documentação de API

### Situação
API cresceu, precisa de documentação atualizada.

### Commands Usados

```bash
# 1. Gerar docs da API
/docs api

# 2. Revisar e melhorar
/review API.md

# 3. Commit da documentação
/commit docs
```

### Resultado
- API totalmente documentada
- Exemplos práticos incluídos
- Markdown pronto para publicar

## 🔄 Refatoração de Código Legado

### Situação
Código antigo precisa modernização.

### Commands Usados

```bash
# 1. Analisar código atual
/review src/legacy/

# 2. Refatorar por partes
/refactor src/legacy/userManager.js

# 3. Garantir funcionamento
/test src/legacy/

# 4. Otimizar se necessário
/optimize

# 5. Documentar mudanças
/commit refactor
```

### Impacto
- Código 50% menor
- Mais testável
- Manutenção facilitada

## 🎯 Debug de Problema Complexo

### Situação
Erro intermitente difícil de reproduzir.

### Commands Usados

```bash
# 1. Investigar o problema
/debug "usuário não consegue fazer login às vezes"

# 2. Adicionar logs estratégicos
/fix add-debug-logs

# 3. Monitorar em staging
/deploy staging

# 4. Identificar e corrigir
/fix race-condition-login

# 5. Validar correção
/test auth --stress
```

### Resolução
- Bug race condition identificado
- Corrigido com mutex apropriado
- Teste de stress adicionado

## 🚢 Deploy Sexta-feira

### Situação
Deploy importante na sexta (sim, eu sei...).

### Commands Usados

```bash
# 1. Review completo antes
/review

# 2. Segurança dupla checada
/security

# 3. Todos os testes
/test --all

# 4. Deploy com rollback preparado
/deploy production --with-rollback

# 5. Monitoramento pós-deploy
/status --monitor
```

### Resultado
- Deploy sem incidentes
- Rollback não foi necessário
- Final de semana salvo

## 💡 Criação de POC Rápida

### Situação
Precisa validar ideia com POC.

### Commands Usados

```bash
# 1. Setup inicial
/setup

# 2. Implementação rápida
(desenvolvimento manual)

# 3. Documentar POC
/docs poc-overview

# 4. Preparar apresentação
/commit poc-ready
```

### Tempo Total
- 2 horas do conceito ao POC funcional

## 🎓 Onboarding de Dev Novo

### Situação
Novo desenvolvedor no time.

### Commands para Compartilhar

```bash
# Setup inicial
/setup

# Entender o projeto
/docs

# Ver status atual
/status

# Rodar testes para validar
/test

# Primeiro commit
/commit
```

### Benefício
- Onboarding em 30 minutos
- Dev produtivo no dia 1

## Métricas de Produtividade

### Com Commands

- ⏱️ **Tempo economizado**: ~2 horas/dia
- 🎯 **Tarefas automatizadas**: 15+
- 📈 **Aumento produtividade**: 40%
- 😊 **Redução de stress**: Inestimável

### Tarefas Mais Aceleradas

1. **Commits**: 5min → 30s
2. **Deploy**: 20min → 2min
3. **Code Review**: 30min → 5min
4. **Bug Fix**: 1h → 15min
5. **Documentação**: 2h → 15min

## Commands Combinados

### Super Workflow

```bash
# Morning Routine
/status && /test && /todo

# Pre-Deploy
/review && /security && /test --all && /deploy

# End of Day
/commit && /status && /todo --tomorrow
```

## Customizações por Projeto

### Frontend React
- `/component` - Cria componente com testes
- `/storybook` - Adiciona story
- `/css` - Otimiza CSS

### Backend Node
- `/endpoint` - Novo endpoint com docs
- `/migration` - Database migration
- `/seed` - Seed database

### DevOps
- `/scale` - Auto-scaling
- `/monitor` - Setup monitoring
- `/backup` - Backup automático

## Dicas de Ouro

### 1. Comece Pequeno
Não crie 50 commands de uma vez.

### 2. Itere
Melhore commands conforme usa.

### 3. Compartilhe
Bons commands valem ouro.

### 4. Documente
`description` clara é essencial.

### 5. Combine
Commands podem chamar outros.

## Conclusão

Commands transformam desenvolvimento:
- Tarefas chatas → Automáticas
- Processos longos → Instantâneos
- Erros comuns → Impossíveis

Comece com 3 commands hoje.
Em uma semana, você não vive sem eles.

---

*Exemplos reais que provam: commands são superpoderes.*