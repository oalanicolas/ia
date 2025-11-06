# Seu Primeiro Projeto com Agentes

Tutorial prático: vamos criar uma API de TODO list do zero.

## O que vamos construir

Uma API simples com:
- Criar tarefa
- Listar tarefas
- Marcar como concluída
- Deletar tarefa

## Passo 1: Arquitetura

Use o `backend-architect`:

```
"projete uma API REST de TODO list com:
- CRUD de tarefas
- PostgreSQL para dados
- Autenticação simples
Use FastAPI"
```

O agente vai criar:
- Estrutura de pastas
- Modelos de dados
- Endpoints planejados

## Passo 2: Implementação

Use o `python-pro`:

```
"implemente a API que foi projetada com:
- FastAPI
- SQLAlchemy
- Pydantic para validação"
```

Você vai receber:
```python
# main.py
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from typing import List

app = FastAPI()

@app.post("/tasks/")
async def create_task(task: TaskCreate):
    # Implementação completa
    pass

@app.get("/tasks/")
async def list_tasks():
    # Implementação completa
    pass
```

## Passo 3: Testes

Use o `test-automator`:

```
"crie testes para todos os endpoints da API de tarefas"
```

Vai gerar:
```python
def test_create_task():
    response = client.post("/tasks/", json={
        "title": "Estudar Python",
        "completed": False
    })
    assert response.status_code == 201
```

## Passo 4: Segurança

Use o `security-auditor`:

```
"verifique vulnerabilidades na API de tarefas"
```

O agente vai:
- Checar SQL injection
- Validar autenticação
- Verificar CORS
- Sugerir melhorias

## Passo 5: Deploy

Use o `deployment-engineer`:

```
"configure Docker e GitHub Actions para deploy da API"
```

Você recebe:
- Dockerfile
- docker-compose.yml
- .github/workflows/deploy.yml

## Resultado Final

Em menos de 1 hora você tem:
- API completa e funcional
- Testes automatizados
- Segurança validada
- Deploy configurado

## O que você aprendeu

1. **Workflow correto** - Research → Plan → Code → Test
2. **Agente certo para cada tarefa**
3. **Código profissional** desde o início
4. **Best practices** aplicadas automaticamente

## Exercícios

Agora tente sozinho:

### Fácil
Adicione um campo "description" nas tarefas

### Médio
Implemente categorias para as tarefas

### Difícil
Adicione autenticação com JWT

## Dicas

- Sempre peça explicações: "explique por que fez assim"
- Compare com seu código: o que está diferente?
- Itere: "melhore X mantendo Y"
- Teste tudo antes de confiar

## Próximo Projeto

Depois deste, tente:
1. Blog com comentários
2. Chat em tempo real
3. E-commerce simples

Cada projeto te ensina algo novo sobre como usar agentes efetivamente.