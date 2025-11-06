---
description: Otimiza performance do código
allowed-tools: Read, Edit, Bash(time:*), Bash(node --prof:*), Grep
argument-hint: [arquivo ou função específica]
---

# Otimização de Performance

Analise e melhore a performance do código.

## Target: ${ARGUMENTS:-análise geral}

## Análise de Performance

### 1. Identificar Gargalos

**Métricas a verificar**:
- Tempo de execução
- Uso de memória
- Operações I/O
- Queries de banco de dados
- Chamadas de API

### 2. Problemas Comuns

**JavaScript/TypeScript**:
- [ ] Loops dentro de loops (O(n²))
- [ ] Re-renders desnecessários (React)
- [ ] Bundle size grande
- [ ] Operações síncronas bloqueantes
- [ ] Memory leaks

**Python**:
- [ ] List comprehension vs loops
- [ ] Uso inadequado de pandas
- [ ] I/O não otimizado
- [ ] GIL bottlenecks

**Banco de Dados**:
- [ ] Queries N+1
- [ ] Missing indexes
- [ ] Over-fetching de dados
- [ ] Falta de cache

### 3. Otimizações Sugeridas

**Quick Wins**:
- Memoização de cálculos caros
- Lazy loading quando apropriado
- Debounce/throttle em eventos
- Cache de resultados

**Refatorações Maiores**:
- Algoritmos mais eficientes
- Estruturas de dados apropriadas
- Processamento assíncrono
- Workers/threads para tarefas pesadas

### 4. Implementar Melhorias
- Aplique uma otimização por vez
- Meça o impacto de cada mudança
- Documente trade-offs

### 5. Validação
- Compare métricas antes/depois
- Verifique que funcionalidade está preservada
- Teste com dados reais/volume

Target: $ARGUMENTS