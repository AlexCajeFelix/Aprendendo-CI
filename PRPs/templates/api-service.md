# [Nome do Serviço de API]

**Tipo:** Serviço de API REST/GraphQL
**Complexidade:** [Baixa/Média/Alta]
**Tempo Estimado:** [4-20 horas]
**Versão:** 1.0

## 🎯 Objetivo

Desenvolver um serviço de API robusto e escalável para [descrição do serviço].

### Por que este serviço é necessário?
- [Motivo 1]
- [Motivo 2]
- [Motivo 3]

### Critérios de Sucesso
- [ ] API bem documentada e testada
- [ ] Performance otimizada
- [ ] Segurança implementada
- [ ] Monitoramento configurado
- [ ] Deploy automatizado

## 📋 O que será construído

### Endpoints da API
- CRUD completo para entidades
- Autenticação e autorização
- Validação de dados
- Tratamento de erros padronizado
- Paginação e filtros
- Rate limiting

### Funcionalidades Principais
1. **[Funcionalidade 1]**
   - Descrição: [Detalhes da funcionalidade]
   - Endpoint: [Método] /api/[rota]
   - Critérios de aceitação: [Como validar se está funcionando]

2. **[Funcionalidade 2]**
   - Descrição: [Detalhes da funcionalidade]
   - Endpoint: [Método] /api/[rota]
   - Critérios de aceitação: [Como validar se está funcionando]

## 🧠 Todo Contexto Necessário

### Stack Tecnológico
- **Framework:** [Node.js/Express/FastAPI/Django/Spring Boot]
- **Banco de Dados:** [PostgreSQL/MySQL/MongoDB]
- **Cache:** [Redis/Memcached]
- **Documentação:** [Swagger/OpenAPI]

### Documentação & Referências

- **url:** https://framework.com/docs
  **por que:** Documentação oficial do framework escolhido

- **arquivo:** src/routes/existing-route.js
  **por que:** Padrão de rotas existente no projeto

- **doc:** https://openapi.org/specification
  **seção:** Especificação OpenAPI 3.0

### Armadilhas Conhecidas

# CRÍTICO: Implementar rate limiting para evitar abuso
# IMPORTANTE: Validar todos os inputs para segurança
# NOTA: Usar HTTPS em produção obrigatoriamente

### Padrões do Projeto

```javascript
// Exemplo de rota Express
const express = require('express');
const { validateInput } = require('../middleware/validation');
const { authenticate } = require('../middleware/auth');

router.get('/api/users', authenticate, async (req, res) => {
  try {
    const users = await UserService.getAll(req.query);
    res.json(users);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});
```

## 🏗️ Blueprint de Implementação

### Etapa 1: Configuração Base
```pseudocode
1. Configurar estrutura do projeto
2. Instalar dependências
3. Configurar banco de dados
4. Configurar ambiente de desenvolvimento
5. Configurar linting e testes
```

### Etapa 2: Estrutura da API
```pseudocode
1. Configurar servidor
2. Configurar middleware básico
3. Criar estrutura de rotas
4. Implementar tratamento de erros
5. Configurar CORS
```

### Etapa 3: Autenticação
```pseudocode
1. Implementar sistema de auth
2. Configurar JWT
3. Criar middleware de autenticação
4. Implementar autorização
5. Configurar refresh tokens
```

### Etapa 4: Endpoints
```pseudocode
1. Implementar CRUD básico
2. Adicionar validações
3. Implementar paginação
4. Adicionar filtros e busca
5. Configurar rate limiting
```

### Etapa 5: Qualidade
```pseudocode
1. Implementar testes
2. Configurar documentação
3. Adicionar logging
4. Configurar monitoramento
5. Otimizar performance
```

### Estrutura de Arquivos Esperada

```
api-service/
├── src/
│   ├── controllers/       # Controladores
│   ├── models/           # Modelos de dados
│   ├── routes/           # Definição de rotas
│   ├── middleware/       # Middlewares
│   ├── services/         # Lógica de negócio
│   ├── utils/           # Utilitários
│   ├── config/          # Configurações
│   └── types/           # Definições de tipos
├── tests/               # Testes
├── docs/                # Documentação
├── scripts/             # Scripts utilitários
└── docker/              # Configuração Docker
```

## 🔄 Loop de Validação

### Nível 1: Sintaxe & Estilo
```bash
# Verificar sintaxe e estilo
npm run lint
npm run type-check
npm run format

# Verificar dependências
npm audit
```

### Nível 2: Testes Unitários
```bash
# Executar testes
npm test
npm run test:coverage

# Verificar cobertura mínima (80%)
npm run test:coverage:check
```

### Nível 3: Teste de Integração
```bash
# Executar API em modo teste
npm run test:integration

# Testar endpoints principais
curl -X GET http://localhost:3000/api/health
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "password"}'
```

### Nível 4: Teste de Performance
```bash
# Teste de carga
npm run test:load

# Verificar métricas
# - Tempo de resposta < 200ms
# - Throughput > 100 req/s
# - Uso de memória < 512MB
```

## 📦 Entregáveis Esperados

### API Endpoints
- [ ] Endpoints CRUD completos
- [ ] Autenticação e autorização
- [ ] Validação de dados
- [ ] Paginação e filtros
- [ ] Tratamento de erros
- [ ] Rate limiting

### Funcionalidades
- [ ] Sistema de autenticação
- [ ] CRUD de entidades
- [ ] Busca e filtros
- [ ] Upload de arquivos
- [ ] Webhooks/notificações
- [ ] Cache implementado

### Qualidade
- [ ] Testes unitários (>80% cobertura)
- [ ] Testes de integração
- [ ] Testes de performance
- [ ] Documentação OpenAPI
- [ ] Logs estruturados
- [ ] Monitoramento

### Segurança
- [ ] Autenticação JWT
- [ ] Validação de inputs
- [ ] Rate limiting
- [ ] CORS configurado
- [ ] HTTPS obrigatório
- [ ] Headers de segurança

## ✅ Critérios de Qualidade

### Performance
- [ ] Tempo de resposta < 200ms (p95)
- [ ] Throughput > 100 req/s
- [ ] Uso de memória < 512MB
- [ ] CPU usage < 70%

### Segurança
- [ ] Autenticação segura
- [ ] Validação rigorosa
- [ ] Rate limiting implementado
- [ ] Headers de segurança
- [ ] Logs de auditoria

### Documentação
- [ ] OpenAPI/Swagger completo
- [ ] Exemplos de uso
- [ ] Códigos de erro documentados
- [ ] Guia de autenticação
- [ ] Changelog atualizado

### Monitoramento
- [ ] Health checks
- [ ] Métricas de performance
- [ ] Logs estruturados
- [ ] Alertas configurados
- [ ] Dashboard de monitoramento

## 📚 Exemplos e Referências

### Exemplo de Endpoint
```javascript
// GET /api/users
const getUsers = async (req, res) => {
  try {
    const { page = 1, limit = 10, search } = req.query;
    
    const users = await UserService.getAll({
      page: parseInt(page),
      limit: parseInt(limit),
      search
    });
    
    res.json({
      data: users.data,
      pagination: {
        page: parseInt(page),
        limit: parseInt(limit),
        total: users.total,
        pages: Math.ceil(users.total / limit)
      }
    });
  } catch (error) {
    res.status(500).json({ 
      error: 'Internal server error',
      message: error.message 
    });
  }
};
```

### Exemplo de Middleware
```javascript
// Middleware de validação
const validateUser = (req, res, next) => {
  const { name, email, password } = req.body;
  
  if (!name || !email || !password) {
    return res.status(400).json({
      error: 'Validation error',
      message: 'Name, email and password are required'
    });
  }
  
  if (!isValidEmail(email)) {
    return res.status(400).json({
      error: 'Validation error',
      message: 'Invalid email format'
    });
  }
  
  next();
};
```

## 🔧 Configuração de Desenvolvimento

### Pré-requisitos
- Node.js >= 18.0.0
- npm >= 8.0.0
- PostgreSQL/MySQL/MongoDB
- Redis (opcional)

### Comandos de Desenvolvimento
```bash
# Instalar dependências
npm install

# Executar em desenvolvimento
npm run dev

# Executar testes
npm test

# Build para produção
npm run build

# Executar em produção
npm start
```

### Variáveis de Ambiente
```env
# Servidor
PORT=3000
NODE_ENV=development

# Banco de dados
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Autenticação
JWT_SECRET=your-secret-key
JWT_EXPIRES_IN=24h

# Cache
REDIS_URL=redis://localhost:6379

# Rate limiting
RATE_LIMIT_WINDOW_MS=900000
RATE_LIMIT_MAX_REQUESTS=100
```

## 📝 Notas Adicionais

- Implementar health checks para monitoramento
- Configurar logs estruturados (JSON)
- Considerar implementação de cache
- Planejar estratégia de versionamento da API
- Configurar CI/CD para deploy automático

---

**Instruções para IA:**
1. Analise o contexto completo do projeto
2. Implemente seguindo o blueprint em etapas
3. Execute todos os comandos de validação
4. Corrija erros encontrados
5. Valide critérios de qualidade
6. Documente a API completamente
7. Configure monitoramento básico
