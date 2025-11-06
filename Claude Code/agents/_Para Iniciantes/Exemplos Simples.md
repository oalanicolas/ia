# Exemplos Simples

Casos práticos para começar agora.

## Exemplo 1: Função Python

### Sem Agente
```python
def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)
```

### Com python-pro
```python
def calcular_desconto(preco: float, percentual: float) -> float:
    """
    Calcula o desconto sobre um preço.

    Args:
        preco: Valor original
        percentual: Percentual de desconto (0-100)

    Returns:
        Preço com desconto aplicado

    Raises:
        ValueError: Se percentual < 0 ou > 100
    """
    if not 0 <= percentual <= 100:
        raise ValueError("Percentual deve estar entre 0 e 100")

    if preco < 0:
        raise ValueError("Preço não pode ser negativo")

    desconto = preco * (percentual / 100)
    return round(preco - desconto, 2)
```

**Diferenças:**
- Type hints
- Docstring completa
- Validação de entrada
- Tratamento de erros
- Arredondamento correto

## Exemplo 2: Componente React

### Sem Agente
```jsx
function TodoItem({todo}) {
  return (
    <div>
      <input type="checkbox" checked={todo.done}/>
      <span>{todo.text}</span>
    </div>
  )
}
```

### Com frontend-developer
```jsx
import React, { memo } from 'react';
import PropTypes from 'prop-types';

const TodoItem = memo(({ todo, onToggle, onDelete }) => {
  const handleToggle = () => {
    onToggle(todo.id);
  };

  const handleDelete = () => {
    onDelete(todo.id);
  };

  return (
    <div className="todo-item">
      <input
        type="checkbox"
        checked={todo.done}
        onChange={handleToggle}
        aria-label={`Mark ${todo.text} as ${todo.done ? 'incomplete' : 'complete'}`}
      />
      <span className={todo.done ? 'todo-done' : ''}>
        {todo.text}
      </span>
      <button
        onClick={handleDelete}
        aria-label={`Delete ${todo.text}`}
      >
        Delete
      </button>
    </div>
  );
});

TodoItem.propTypes = {
  todo: PropTypes.shape({
    id: PropTypes.string.isRequired,
    text: PropTypes.string.isRequired,
    done: PropTypes.bool.isRequired
  }).isRequired,
  onToggle: PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired
};

TodoItem.displayName = 'TodoItem';

export default TodoItem;
```

**Diferenças:**
- Memoização para performance
- PropTypes para validação
- Acessibilidade (aria-labels)
- Handlers separados
- CSS classes condicionais

## Exemplo 3: Endpoint API

### Sem Agente
```python
@app.post("/users")
def create_user(name, email):
    user = {"name": name, "email": email}
    users.append(user)
    return user
```

### Com backend-architect + python-pro
```python
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from typing import Optional
import re

router = APIRouter()

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime

@router.post("/users", response_model=UserResponse, status_code=201)
async def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new user.

    Returns:
        201: User created successfully
        400: Invalid input data
        409: Email already exists
    """
    # Check if email exists
    existing = db.query(User).filter(User.email == user_data.email).first()
    if existing:
        raise HTTPException(status_code=409, detail="Email already registered")

    # Create user
    user = User(**user_data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)

    return user
```

**Diferenças:**
- Validação com Pydantic
- Status codes corretos
- Tratamento de duplicatas
- Documentação automática
- Injeção de dependências
- Async/await

## Exemplo 4: Teste

### Sem Agente
```python
def test_soma():
    assert soma(2, 2) == 4
```

### Com test-automator
```python
import pytest
from unittest.mock import Mock, patch

class TestCalculadora:
    """Testes para funções de cálculo."""

    @pytest.mark.parametrize("a,b,expected", [
        (2, 2, 4),
        (0, 5, 5),
        (-1, 1, 0),
        (0.1, 0.2, 0.3),
        (1000000, 1, 1000001)
    ])
    def test_soma_valores_validos(self, a, b, expected):
        """Testa soma com diferentes tipos de valores."""
        result = soma(a, b)
        assert result == pytest.approx(expected)

    def test_soma_tipo_incorreto(self):
        """Testa que TypeError é levantado para tipos incorretos."""
        with pytest.raises(TypeError):
            soma("2", 2)

    def test_soma_overflow(self):
        """Testa comportamento com números muito grandes."""
        import sys
        max_int = sys.maxsize
        result = soma(max_int, 1)
        assert result == max_int + 1
```

**Diferenças:**
- Testes parametrizados
- Casos extremos
- Testes de erro
- Organização em classes
- Documentação

## Como Usar Estes Exemplos

1. **Compare** - Veja as diferenças
2. **Entenda** - Por que o agente fez assim?
3. **Pratique** - Tente reproduzir
4. **Adapte** - Use no seu projeto

## Padrão que Emerge

Os agentes sempre adicionam:
- **Validação** - Entrada e saída
- **Documentação** - Código auto-explicativo
- **Tratamento de erros** - Casos extremos
- **Performance** - Otimizações
- **Manutenibilidade** - Código limpo

## Seu Turno

Pegue um código seu simples e peça para um agente melhorar. Compare e aprenda!