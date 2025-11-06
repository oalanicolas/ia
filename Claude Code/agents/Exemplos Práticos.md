# Exemplos Práticos

Casos reais de uso dos agentes, com código e resultados.

## Caso 1: Startup Criando MVP em 2 Semanas

### Contexto
Marketplace B2B, 2 desenvolvedores, 2 semanas de prazo.

### Como Fizemos

**Com solution-architect:**
```
"Preciso de um MVP de marketplace B2B onde empresas
podem vender produtos para outras empresas. Funcionalidades:
- Cadastro de empresas vendedoras e compradoras
- Catálogo de produtos com busca
- Carrinho e pedidos
- Dashboard básico
Tenho 2 desenvolvedores e 2 semanas. O que sugere?"
```

**Resposta do Agente:**
```
Arquitetura MVP Recomendada:

BACKEND:
- FastAPI (desenvolvimento rápido)
- PostgreSQL (relacional, robusto)
- JWT para auth simples
- S3 para imagens

FRONTEND:
- Next.js (SSR, SEO)
- Tailwind (desenvolvimento rápido)
- Zustand (state simples)

SIMPLIFICAÇÕES PARA MVP:
- Pagamento manual (apenas registro)
- Sem chat em tempo real
- Email básico com templates
- Deploy em Railway/Render

DIVISÃO DO TRABALHO:
Dev 1: Backend + DB
Dev 2: Frontend + Integração
Semana 1: Core features
Semana 2: Polish + Deploy
```

**Com fastapi-pro:**
```
"Implemente a estrutura base da API do marketplace
com os models e endpoints principais"
```

**Código Gerado:**
```python
# models.py
from sqlalchemy import Column, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum

class UserType(enum.Enum):
    BUYER = "buyer"
    SELLER = "seller"
    BOTH = "both"

class Company(Base):
    __tablename__ = "companies"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    type = Column(Enum(UserType))

    products = relationship("Product", back_populates="company")
    orders = relationship("Order", foreign_keys="[Order.buyer_id]")

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float)
    company_id = Column(String, ForeignKey("companies.id"))

    company = relationship("Company", back_populates="products")

# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import schemas
import crud
import models
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="B2B Marketplace API")

@app.post("/companies/", response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    return crud.create_company(db=db, company=company)

@app.get("/products/", response_model=List[schemas.Product])
def list_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)
```

###  Resultado
- MVP entregue em 12 dias
- 3 empresas piloto usando
- Investimento seed conseguido

## Caso 2: Empresa Migrando para Cloud

###  Situação
Empresa com sistema monolítico quer migrar para cloud.

###  Agentes Utilizados
1. `cloud-architect` - Estratégia de migração
2. `kubernetes-architect` - Orquestração
3. `devops-troubleshooter` - Resolução de problemas
4. `observability-engineer` - Monitoramento

###  Implementação

**Com cloud-architect:**
```
"Temos um monolito Django com 500k usuários/mês
rodando em servidor próprio. Como migrar para AWS
minimizando downtime e custos?"
```

**Plano Gerado:**
```
FASE 1 - LIFT & SHIFT (2 semanas)
- EC2 para aplicação
- RDS para PostgreSQL
- S3 para arquivos
- CloudFront como CDN

FASE 2 - OTIMIZAÇÃO (1 mês)
- Auto Scaling Groups
- ElastiCache para Redis
- SQS para filas
- Lambda para jobs

FASE 3 - MODERNIZAÇÃO (3 meses)
- Containerização com ECS
- Microserviços graduais
- API Gateway
- EventBridge

CUSTOS ESTIMADOS:
- Atual: $2000/mês (servidor dedicado)
- AWS Fase 1: $800/mês
- AWS Fase 3: $1200/mês (com redundância)
```

###  Resultado
- Migração sem downtime
- Redução de 40% nos custos
- Performance 3x melhor
- Escalabilidade automática

## Caso 3: Auditoria de Segurança Urgente

###  Situação
Empresa descobriu possível vazamento de dados.

###  Agentes Utilizados
1. `security-auditor` - Auditoria completa
2. `devops-troubleshooter` - Análise de logs
3. `code-reviewer` - Review de código

###  Ação Imediata

**Com security-auditor:**
```
"Suspeita de vazamento de dados. Sistema em Node.js
com MongoDB. Por onde começar a investigação?"
```

**Checklist de Emergência:**
```
AÇÕES IMEDIATAS (1 hora):
□ Rotacionar todas as chaves/secrets
□ Revisar logs de acesso últimas 72h
□ Verificar usuários com acessos anormais
□ Backup imediato do estado atual
□ Ativar logs detalhados

ANÁLISE (4 horas):
□ SQL Injection points
□ NoSQL Injection em MongoDB
□ Autenticação/Autorização
□ Logs de API calls
□ Verificar dependências vulneráveis

CÓDIGO VULNERÁVEL ENCONTRADO:
// VULNERÁVEL - NoSQL Injection
app.post('/login', (req, res) => {
  db.users.findOne({
    username: req.body.username,
    password: req.body.password  // PROBLEMA!
  })
})

// CORREÇÃO
app.post('/login', (req, res) => {
  db.users.findOne({
    username: String(req.body.username),
    password: hashPassword(String(req.body.password))
  })
})
```

###  Resultado
- Vulnerabilidade identificada em 2 horas
- Patch aplicado em 4 horas
- Nenhum dado foi vazado
- Implementação de WAF e monitoring

## Caso 4: Otimização de Performance

###  Situação
E-commerce com lentidão em Black Friday.

###  Agentes Utilizados
1. `devops-troubleshooter` - Diagnóstico
2. `performance-engineer` - Otimização
3. `database-architect` - Otimização DB

###  Diagnóstico e Solução

**Com devops-troubleshooter:**
```
"Site caindo com 10k usuários simultâneos.
Normal é 500. Usando React + Node + MySQL."
```

**Análise:**
```
GARGALOS IDENTIFICADOS:

1. DATABASE (70% do problema)
- Queries N+1 no ORM
- Falta de índices críticos
- Conexões não pooladas

2. BACKEND (20% do problema)
- Sem cache de API
- Processamento síncrono
- Memory leaks

3. FRONTEND (10% do problema)
- Bundle de 5MB
- Imagens não otimizadas
- Sem lazy loading

SOLUÇÕES APLICADAS:

-- Índices críticos
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);

-- Cache Redis
const cached = await redis.get(`product:${id}`);
if (cached) return JSON.parse(cached);

-- Query optimization
// Antes: 100 queries
const orders = await Order.findAll();
for (let order of orders) {
  order.user = await User.findById(order.userId);
}

// Depois: 1 query
const orders = await Order.findAll({
  include: [User]
});
```

###  Resultado
- Site suportando 50k usuários
- Tempo de resposta: 3s → 200ms
- Zero downtime na Black Friday
- Vendas aumentaram 300%

## Caso 5: Desenvolvimento de Feature Complexa

###  Situação
Adicionar sistema de recomendação com IA.

###  Agentes Utilizados
1. `ai-engineer` - Sistema de recomendação
2. `ml-engineer` - Pipeline de ML
3. `prompt-engineer` - Otimização

###  Implementação

**Com ai-engineer:**
```
"Criar sistema de recomendação de produtos
usando histórico de compras e embeddings."
```

**Sistema Criado:**
```python
# recommendation_system.py
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import openai
from typing import List
import redis
import json

class RecommendationEngine:
    def __init__(self):
        self.redis_client = redis.Redis()
        self.embedding_model = "text-embedding-ada-002"

    def get_product_embedding(self, product: dict) -> List[float]:
        """Gera embedding do produto"""
        text = f"{product['name']} {product['description']} {product['category']}"

        # Cache check
        cached = self.redis_client.get(f"emb:{product['id']}")
        if cached:
            return json.loads(cached)

        # Generate embedding
        response = openai.Embedding.create(
            input=text,
            model=self.embedding_model
        )
        embedding = response['data'][0]['embedding']

        # Cache for 7 days
        self.redis_client.setex(
            f"emb:{product['id']}",
            604800,
            json.dumps(embedding)
        )

        return embedding

    def get_recommendations(self, user_id: str, limit: int = 10):
        """Recomenda produtos baseado no histórico"""
        # Get user history
        user_products = self.get_user_purchased_products(user_id)

        if not user_products:
            return self.get_popular_products(limit)

        # Calculate user preference vector
        user_embeddings = [self.get_product_embedding(p) for p in user_products]
        user_vector = np.mean(user_embeddings, axis=0)

        # Get all products
        all_products = self.get_all_products()

        # Calculate similarities
        similarities = []
        for product in all_products:
            if product['id'] not in [p['id'] for p in user_products]:
                prod_embedding = self.get_product_embedding(product)
                sim = cosine_similarity([user_vector], [prod_embedding])[0][0]
                similarities.append((product, sim))

        # Sort and return top N
        similarities.sort(key=lambda x: x[1], reverse=True)
        return [p[0] for p in similarities[:limit]]

# API endpoint
@app.get("/recommendations/{user_id}")
async def get_recommendations(user_id: str, limit: int = 10):
    engine = RecommendationEngine()
    recommendations = engine.get_recommendations(user_id, limit)
    return {"recommendations": recommendations}
```

###  Resultado
- CTR aumentou 45%
- Vendas cruzadas +60%
- Tempo no site +25%
- ROI de 8x no primeiro mês

## Caso 6: Refatoração de Código Legado

###  Situação
Sistema de 10 anos em PHP precisa modernização.

###  Agentes Utilizados
1. `code-reviewer` - Análise do código
2. `backend-architect` - Nova arquitetura
3. `test-automator` - Testes para refatoração

###  Estratégia

**Com code-reviewer:**
```
"Analise este código PHP legado e sugira
estratégia de modernização sem reescrever tudo"
```

**Análise e Plano:**
```
PROBLEMAS IDENTIFICADOS:
- SQL direto no código (SQL Injection)
- Sem separação MVC
- PHP 5.6 (sem suporte)
- Zero testes
- 500+ arquivos misturados

ESTRATÉGIA DE REFATORAÇÃO:

FASE 1 - ESTABILIZAÇÃO (1 mês)
1. Adicionar composer e autoload
2. Criar camada de abstração DB
3. Adicionar logs estruturados
4. Testes para funcionalidades críticas

FASE 2 - MODERNIZAÇÃO (2 meses)
1. Migrar para PHP 8.1
2. Implementar Repository Pattern
3. Adicionar Service Layer
4. API REST gradual

FASE 3 - MICROSERVIÇOS (6 meses)
1. Extrair módulo de pagamento
2. Extrair módulo de usuários
3. Event-driven com RabbitMQ

CÓDIGO EXEMPLO:

// ANTES (SQL Injection vulnerável)
$result = mysql_query(
    "SELECT * FROM users WHERE email = '$_POST[email]'"
);

// FASE 1 (PDO seguro)
$stmt = $pdo->prepare("SELECT * FROM users WHERE email = ?");
$stmt->execute([$_POST['email']]);

// FASE 2 (Repository Pattern)
class UserRepository {
    public function findByEmail(string $email): ?User {
        $stmt = $this->db->prepare(
            "SELECT * FROM users WHERE email = :email"
        );
        $stmt->execute(['email' => $email]);
        $data = $stmt->fetch();
        return $data ? User::fromArray($data) : null;
    }
}

// FASE 3 (Service Layer)
class AuthService {
    public function authenticate(string $email, string $password): ?User {
        $user = $this->userRepo->findByEmail($email);
        if (!$user || !$this->verifyPassword($password, $user->password)) {
            $this->eventDispatcher->dispatch(new LoginFailedEvent($email));
            return null;
        }
        $this->eventDispatcher->dispatch(new LoginSuccessEvent($user));
        return $user;
    }
}
```

###  Resultado
- Zero vulnerabilidades de segurança
- Performance 5x melhor
- Manutenibilidade aumentada
- Deploy automatizado
- Cobertura de testes: 85%

## Templates Prontos

###  Template: API REST Completa

```bash
# Instale os agentes
npx claude-code-templates@latest --stack=api

# Use este prompt:
"Crie uma API REST completa para [SEU_DOMÍNIO] com:
- CRUD completo
- Autenticação JWT
- Validação de dados
- Testes automatizados
- Documentação Swagger
- Docker pronto

Tecnologias: [Python/Node/Go] + PostgreSQL"
```

###  Template: Dashboard Admin

```bash
# Instale os agentes
npx claude-code-templates@latest --stack=frontend

# Use este prompt:
"Crie um dashboard administrativo com:
- Login/Logout
- Gráficos e métricas
- Tabelas com filtros
- CRUD de entidades
- Responsive design
- Dark mode

Tecnologias: React + TypeScript + Tailwind"
```

###  Template: E-commerce

```bash
# Instale os agentes
npx claude-code-templates@latest --stack=fullstack

# Use este prompt:
"Crie um e-commerce com:
- Catálogo de produtos
- Carrinho de compras
- Checkout
- Painel admin
- Integração pagamento

Full-stack: Next.js + Prisma + PostgreSQL"
```

## Métricas de Sucesso

###  Resultados Reais de Usuários

| Projeto | Tempo Economizado | Qualidade |
|---------|------------------|-----------|
| API REST | 2 semanas → 2 dias | 95% coverage |
| Dashboard | 3 semanas → 3 dias | 0 bugs críticos |
| E-commerce | 2 meses → 2 semanas | Production-ready |
| Migração Cloud | 3 meses → 3 semanas | Zero downtime |
| Segurança | 1 semana → 4 horas | 100% vulnerabilidades |

## Lições Aprendidas

###  O que funciona
1. Combinar múltiplos agentes
2. Ser específico nos requisitos
3. Iterar em pequenos passos
4. Pedir explicações
5. Validar com testes

###  O que evitar
1. Tentar fazer tudo de uma vez
2. Pular a fase de arquitetura
3. Ignorar sugestões de segurança
4. Não fazer testes
5. Deploy sem revisão

---

*"Estes exemplos são de projetos reais. Use como inspiração e adapte para suas necessidades!"* 