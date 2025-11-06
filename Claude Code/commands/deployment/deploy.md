---
description: Build, testes e deploy completo
allowed-tools: Bash(npm run:*), Bash(docker:*), Bash(git push:*), Bash(vercel:*), Bash(netlify:*), Bash(gh:*)
argument-hint: [ambiente: staging|production]
---

# Deploy Completo

Execute build, testes e deploy para o ambiente especificado.

## Ambiente alvo: ${1:-staging}

## Checklist de Deploy

1. **Verificar branch atual**
   !`git branch --show-current`

2. **Verificar se há mudanças não commitadas**
   !`git status --short`

3. **Executar testes** (se existirem)
   - Rodar suite de testes
   - Verificar se todos passam

4. **Build do projeto**
   - Node.js: `npm run build` ou `npm run build:${1}`
   - Python: preparar requirements.txt
   - Docker: build da imagem se houver Dockerfile

5. **Deploy por plataforma**:

   **Vercel/Netlify:**
   - Push para branch apropriada
   - Ou use CLI se disponível

   **Docker/K8s:**
   - Build e tag da imagem
   - Push para registry
   - Update deployment

   **GitHub Pages:**
   - Build e push para gh-pages

   **Heroku/Railway:**
   - Push para remote apropriado

6. **Verificações pós-deploy**:
   - Verificar se aplicação está online
   - Testar endpoints principais
   - Verificar logs por erros

7. **Notificar conclusão**

Ambiente: $ARGUMENTS