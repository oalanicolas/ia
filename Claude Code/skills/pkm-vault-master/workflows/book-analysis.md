# Workflow: Análise de Livros e Priorização de Perfis de Autores

## Objetivo

Analisar a biblioteca de livros do vault, avaliar o nível de profundidade de cada resumo, e identificar quais autores devem ser priorizados para criação de perfis.

---

## Níveis de Profundidade de Livros

| Nível | Nome | Palavras | Descrição |
|-------|------|----------|-----------|
| 1 | **STUB** | <200 | Apenas metadata básica, precisa desenvolvimento urgente |
| 2 | **BÁSICO** | 200-500 | Template parcial, falta conteúdo substantivo |
| 3 | **INTERMEDIÁRIO** | 500-1500 | Template completo mas superficial |
| 4 | **COMPLETO** | 1500-3000 | Template completo e detalhado |
| 5 | **EXEMPLAR** | 3000+ | Muito detalhado, serve como referência |

---

## Seções Esperadas (Template de Livro)

Cada livro deve conter as seguintes seções:

1. **IP** - Ideia Principal (1-2 parágrafos)
2. **PQ** - Para quem é? (bullet list de perfis)
3. **IMP** - Como o Livro me Impactou (narrativa pessoal)
4. **SUM** - Sumário (Ideias Chave estruturadas)
5. **CIT** - Citações Preferidas (3+ citações diretas)
6. **CRIT** - Críticas (análise honesta)
7. **VL** - Mencionado em Vida Lendária (cross-reference)

**Livro completo = 7/7 seções + 1500+ palavras**

---

## Critérios de Priorização para Perfis de Autores

### Fatores de Prioridade (peso)

1. **Múltiplos livros no vault** (3x)
   - Indica relevância recorrente na biblioteca

2. **Profundidade do resumo** (2x)
   - Livros com resumos extensos (3000+) mostram maior engajamento

3. **Alinhamento temático** (2x)
   - Desenvolvimento pessoal, produtividade, negócios, filosofia

4. **Citações em Vida Lendária** (2x)
   - Mencionado em episódios do podcast

5. **Impacto histórico do autor** (1x)
   - Influência no campo de conhecimento

### Fórmula de Prioridade

```
Score = (Num_Livros × 3) + (Palavras_Total / 1000 × 2) + (Tema_Alinhado × 2) + (Citações_VL × 2) + (Impacto × 1)
```

---

## Comando de Execução

### Passo 1: Scan de Livros

```bash
cd "/Users/oalanicolas/Library/Mobile Documents/iCloud~md~obsidian/Documents/mentelendaria"

for file in Livros/*.md "Recursos/Livros"/*.md; do
  [ -f "$file" ] || continue
  name=$(basename "$file" .md)
  [[ "$name" == "INDEX" ]] && continue
  words=$(wc -w < "$file" 2>/dev/null | tr -d ' ')
  author=$(grep -E "^autor:|^author:" "$file" 2>/dev/null | head -1 | sed 's/.*: *//' | tr -d '"[]')

  # Verificar seções
  sections=""
  grep -q "Ideia Principal" "$file" && sections="${sections}IP,"
  grep -q "Para quem" "$file" && sections="${sections}PQ,"
  grep -q "Como.*Impactou" "$file" && sections="${sections}IMP,"
  grep -q "Sumário\|Ideias Chave" "$file" && sections="${sections}SUM,"
  grep -q "Citações" "$file" && sections="${sections}CIT,"
  grep -q "Críticas" "$file" && sections="${sections}CRIT,"
  grep -q "Vida Lendária" "$file" && sections="${sections}VL,"

  echo "$author|$name|$words|$sections"
done
```

### Passo 2: Verificar Perfis Existentes

```bash
ls -d "Autores & Pensadores"/*/ 2>/dev/null | while read dir; do
  author=$(basename "$dir")
  files=$(ls "$dir"/*.md 2>/dev/null | wc -l)
  echo "$author: $files arquivos"
done
```

### Passo 3: Gerar Relatório

Salvar em: `_reports/YYYYMMDD_HHMM_book_analysis.md`

---

## Template de Relatório

```markdown
# Análise de Livros e Perfis de Autores

**Data:** [DATA]
**Total de Livros:** [N]
**Perfis Existentes:** [N]

## Distribuição por Nível

| Nível | Quantidade | % |
|-------|------------|---|
| Stub | X | Y% |
| Básico | X | Y% |
| Intermediário | X | Y% |
| Completo | X | Y% |
| Exemplar | X | Y% |

## Autores com Perfil

[Lista de autores que já têm perfil + seus livros no vault]

## Prioridades para Novos Perfis

### Alta Prioridade
[Autores com múltiplos livros e/ou resumos exemplares]

### Média Prioridade
[Autores com 1 livro completo e tema alinhado]

### Baixa Prioridade
[Autores com resumos superficiais]

## Livros que Precisam Desenvolvimento

### Nível 1 - STUB (urgente)
[Lista de livros com <200 palavras]

### Nível 2 - BÁSICO
[Lista de livros com 200-500 palavras]

## Próximos Passos

1. [ ] Desenvolver livros stub prioritários
2. [ ] Criar perfil de [AUTOR 1]
3. [ ] Criar perfil de [AUTOR 2]
```

---

## Integração com Outros Workflows

- **Após criar perfil de autor:** Atualizar `/Autores & Pensadores/INDEX.md`
- **Após desenvolver livro:** Atualizar `/Livros/INDEX.md` e `/atualizacoes.md`
- **Cruzar com episódios VL:** Verificar `/Vida Lendária/Episódios VL/ÍNDICE_LIVROS.md`

---

## Gatilhos para Re-análise

Executar este workflow quando:
- Adicionar 5+ novos livros ao vault
- Criar novo perfil de autor (verificar livros relacionados)
- Planejar próximos episódios do Vida Lendária
- Revisar estratégia de conteúdo trimestral
