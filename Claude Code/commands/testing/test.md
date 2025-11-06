---
description: Executa suite de testes com coverage
allowed-tools: Bash(npm test:*), Bash(npm run:*), Bash(pytest:*), Bash(jest:*), Bash(vitest:*)
argument-hint: [arquivo ou padrão]
---

# Rodar Testes com Coverage

Execute testes automatizados e gere relatório de cobertura.

## Instruções

1. Identifique o framework de testes do projeto:
   - Node.js: Jest, Vitest, Mocha
   - Python: pytest, unittest
   - Ruby: RSpec
   - Go: go test

2. Execute os testes apropriados:
   - Se houver `package.json`: verifique scripts de test
   - Se houver `pytest.ini` ou `setup.cfg`: use pytest
   - Se especificado arquivo: `$ARGUMENTS`

3. Gere relatório de coverage se disponível

4. Analise resultados:
   - Testes passando/falhando
   - Cobertura de código
   - Sugestões de melhorias

5. Se houver falhas, mostre:
   - Mensagens de erro
   - Stack traces relevantes
   - Sugestões de correção

Target específico: $ARGUMENTS