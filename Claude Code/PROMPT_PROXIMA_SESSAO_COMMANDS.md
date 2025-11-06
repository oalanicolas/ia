# Prompt para Próxima Sessão - Organizar /commands

Ver: [[README|Documentação dos Agents já organizados]]

## Contexto

Acabamos de organizar a pasta `/agents` do Claude Code com:
- 31 agentes documentados com código completo
- Pasta `Iniciantes/` com guias didáticos
- Estrutura limpa e mínima de arquivos
- Baseado em documentação oficial da Anthropic
- Linguagem direta, sem robôs, sem emojis excessivos

## Objetivo da Próxima Sessão

Fazer o mesmo para a pasta `/commands`:

1. **Documentar commands existentes** com código completo
2. **Criar estrutura organizada** por categoria/uso
3. **Pasta Iniciantes/** com guias básicos
4. **Baseado em fontes oficiais** (não copiar, apenas referenciar)
5. **Mínimo de arquivos** para máxima clareza

## Estilo de Comunicação

**Manter meu estilo:**
- Direto ao ponto, sem enrolação
- Conversacional mas profissional
- Exemplos práticos, não teoria
- Sem emojis excessivos
- Código comentado em português, mas código em inglês

## Estrutura Esperada

```
commands/
├── README.md                 → Guia principal
├── Exemplos Práticos.md      → Casos de uso reais
├── Iniciantes/               → Para quem está começando
│   ├── O que são Commands
│   ├── Como Criar
│   ├── Exemplos Simples
│   └── Primeiro Command
├── [categorias]/             → Commands organizados
│   ├── git/
│   ├── testing/
│   ├── deployment/
│   └── etc/
```

## Informações Importantes sobre Commands

Commands no Claude Code são atalhos personalizados que:
- Automatizam tarefas repetitivas
- Combinam múltiplas operações
- Podem chamar agentes específicos
- São configuráveis via `/` no chat

## Exemplos de Commands Úteis

- `/test` - Roda todos os testes
- `/deploy` - Faz deploy completo
- `/review` - Review de código com security
- `/refactor` - Refatora código selecionado
- `/explain` - Explica código complexo

## Referências para Consultar

1. [Claude Code Commands Documentation](https://docs.anthropic.com/claude-code/commands)
2. [Best Practices for Commands](https://www.anthropic.com/engineering/claude-code-best-practices#commands)
3. Verificar pasta atual `/commands` para ver o que já existe

## Checklist para a Sessão

- [ ] Listar commands existentes na pasta
- [ ] Pesquisar documentação oficial sobre commands
- [ ] Criar estrutura de categorias baseada no que existe
- [ ] Documentar cada command com:
  - Descrição clara
  - Código completo
  - Exemplo de uso
  - Quando usar/não usar
- [ ] Criar guia para iniciantes
- [ ] Criar exemplos práticos testados
- [ ] Manter mínimo de arquivos
- [ ] Usar linguagem direta e clara

## Primeiro Comando da Sessão

```
Vamos organizar a pasta /commands do Claude Code seguindo o mesmo padrão que usamos para /agents.
Primeiro, liste o que existe atualmente na pasta commands e depois pesquise a documentação oficial
sobre Claude Code commands para basear nossa documentação.
```

## Notas

- Priorizar commands mais úteis/usados
- Incluir workflow de criação de commands customizados
- Mostrar como commands podem chamar agentes
- Exemplos reais de automação

---

*Use este prompt no início da próxima sessão para continuar o trabalho de organização.*