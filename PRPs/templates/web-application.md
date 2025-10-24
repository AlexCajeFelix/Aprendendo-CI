# [Nome da Aplicação Web]

**Tipo:** Aplicação Web Completa
**Complexidade:** [Baixa/Média/Alta]
**Tempo Estimado:** [8-40 horas]
**Versão:** 1.0

## 🎯 Objetivo

Desenvolver uma aplicação web completa com frontend e backend integrados.

### Por que esta aplicação é necessária?
- [Motivo 1]
- [Motivo 2]
- [Motivo 3]

### Critérios de Sucesso
- [ ] Interface responsiva e intuitiva
- [ ] Funcionalidades principais implementadas
- [ ] Performance otimizada
- [ ] Testes automatizados
- [ ] Deploy funcional

## 📋 O que será construído

### Frontend
- Interface de usuário moderna e responsiva
- Componentes reutilizáveis
- Gerenciamento de estado
- Roteamento e navegação
- Integração com APIs

### Backend
- API REST/GraphQL
- Autenticação e autorização
- Banco de dados integrado
- Validação de dados
- Tratamento de erros

### Funcionalidades Principais
1. **[Funcionalidade 1]**
   - Descrição: [Detalhes da funcionalidade]
   - Critérios de aceitação: [Como validar se está funcionando]

2. **[Funcionalidade 2]**
   - Descrição: [Detalhes da funcionalidade]
   - Critérios de aceitação: [Como validar se está funcionando]

## 🧠 Todo Contexto Necessário

### Stack Tecnológico
- **Frontend:** [React/Vue/Angular/Next.js/Nuxt.js]
- **Backend:** [Node.js/Express/FastAPI/Django]
- **Banco de Dados:** [PostgreSQL/MySQL/MongoDB]
- **Styling:** [Tailwind/CSS Modules/Styled Components]

### Documentação & Referências

- **url:** https://framework.com/docs
  **por que:** Documentação oficial do framework escolhido

- **arquivo:** src/components/existing-component.tsx
  **por que:** Padrão de componentes existente no projeto

- **doc:** https://ui-library.com/components
  **seção:** Componentes de UI disponíveis

### Armadilhas Conhecidas

# CRÍTICO: Implementar lazy loading para componentes grandes
# IMPORTANTE: Configurar CORS adequadamente no backend
# NOTA: Usar environment variables para configurações sensíveis

### Padrões do Projeto

```typescript
// Exemplo de componente React
interface ComponentProps {
  title: string;
  onAction: () => void;
}

const Component: React.FC<ComponentProps> = ({ title, onAction }) => {
  return (
    <div className="component">
      <h2>{title}</h2>
      <button onClick={onAction}>Action</button>
    </div>
  );
};
```

## 🏗️ Blueprint de Implementação

### Etapa 1: Configuração Base
```pseudocode
1. Configurar estrutura do projeto
2. Instalar dependências necessárias
3. Configurar ambiente de desenvolvimento
4. Configurar linting e formatação
5. Configurar testes
```

### Etapa 2: Backend Setup
```pseudocode
1. Criar estrutura da API
2. Configurar banco de dados
3. Implementar autenticação
4. Criar endpoints básicos
5. Configurar middleware
```

### Etapa 3: Frontend Setup
```pseudocode
1. Configurar roteamento
2. Criar layout base
3. Implementar componentes básicos
4. Configurar gerenciamento de estado
5. Integrar com API
```

### Etapa 4: Funcionalidades
```pseudocode
1. Implementar funcionalidades principais
2. Criar componentes específicos
3. Implementar validações
4. Adicionar tratamento de erros
5. Otimizar performance
```

### Estrutura de Arquivos Esperada

```
projeto/
├── frontend/
│   ├── src/
│   │   ├── components/     # Componentes reutilizáveis
│   │   ├── pages/         # Páginas da aplicação
│   │   ├── hooks/         # Custom hooks
│   │   ├── services/      # Serviços de API
│   │   ├── utils/         # Utilitários
│   │   ├── types/         # Definições de tipos
│   │   └── styles/        # Estilos globais
│   ├── public/            # Arquivos estáticos
│   └── package.json
├── backend/
│   ├── src/
│   │   ├── controllers/   # Controladores
│   │   ├── models/        # Modelos de dados
│   │   ├── routes/        # Rotas da API
│   │   ├── middleware/    # Middlewares
│   │   ├── services/      # Lógica de negócio
│   │   └── utils/         # Utilitários
│   └── package.json
├── shared/                # Código compartilhado
├── tests/                 # Testes integrados
└── docs/                  # Documentação
```

## 🔄 Loop de Validação

### Nível 1: Sintaxe & Estilo
```bash
# Frontend
npm run lint
npm run type-check
npm run format

# Backend
npm run lint
npm run type-check
npm run format
```

### Nível 2: Testes Unitários
```bash
# Frontend
npm test
npm run test:coverage

# Backend
npm test
npm run test:coverage
```

### Nível 3: Teste de Integração
```bash
# Executar aplicação completa
npm run dev

# Testar endpoints
curl -X GET http://localhost:3000/api/health
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "password"}'
```

### Nível 4: Teste E2E
```bash
# Executar testes E2E
npm run test:e2e

# Validar funcionalidades principais
# - Login/logout
# - CRUD de entidades
# - Responsividade
# - Performance
```

## 📦 Entregáveis Esperados

### Frontend
- [ ] Componentes principais implementados
- [ ] Páginas funcionais
- [ ] Roteamento configurado
- [ ] Gerenciamento de estado
- [ ] Integração com API
- [ ] Responsividade
- [ ] Acessibilidade básica

### Backend
- [ ] API REST/GraphQL funcional
- [ ] Autenticação implementada
- [ ] Banco de dados configurado
- [ ] Validação de dados
- [ ] Tratamento de erros
- [ ] Logs estruturados
- [ ] Documentação da API

### Testes
- [ ] Testes unitários (cobertura > 80%)
- [ ] Testes de integração
- [ ] Testes E2E para fluxos críticos
- [ ] Testes de performance

### Documentação
- [ ] README com instruções de setup
- [ ] Documentação da API
- [ ] Guia de contribuição
- [ ] Documentação de deploy

## ✅ Critérios de Qualidade

### Frontend
- [ ] Interface intuitiva e responsiva
- [ ] Componentes reutilizáveis
- [ ] Performance otimizada (Core Web Vitals)
- [ ] Acessibilidade (WCAG 2.1 AA)
- [ ] SEO básico implementado

### Backend
- [ ] API bem documentada
- [ ] Validação rigorosa de dados
- [ ] Tratamento de erros padronizado
- [ ] Logs estruturados
- [ ] Segurança implementada

### Performance
- [ ] Tempo de carregamento < 3s
- [ ] First Contentful Paint < 1.5s
- [ ] Largest Contentful Paint < 2.5s
- [ ] Cumulative Layout Shift < 0.1

### Segurança
- [ ] Autenticação segura
- [ ] Validação de inputs
- [ ] Proteção contra XSS/CSRF
- [ ] HTTPS configurado
- [ ] Dados sensíveis protegidos

## 📚 Exemplos e Referências

### Exemplo de Componente
```typescript
// Componente de formulário
import { useState } from 'react';
import { api } from '../services/api';

interface FormProps {
  onSubmit: (data: FormData) => void;
}

const Form: React.FC<FormProps> = ({ onSubmit }) => {
  const [formData, setFormData] = useState({});
  
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.post('/endpoint', formData);
      onSubmit(formData);
    } catch (error) {
      console.error('Erro ao enviar formulário:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Campos do formulário */}
    </form>
  );
};
```

### Exemplo de API
```typescript
// Endpoint de API
import { Request, Response } from 'express';
import { validateData } from '../utils/validation';

export const createItem = async (req: Request, res: Response) => {
  try {
    const validatedData = validateData(req.body);
    const item = await ItemService.create(validatedData);
    res.status(201).json(item);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};
```

## 🔧 Configuração de Desenvolvimento

### Pré-requisitos
- Node.js >= 18.0.0
- npm >= 8.0.0
- PostgreSQL/MySQL (para backend)
- Git

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

# Deploy
npm run deploy
```

### Variáveis de Ambiente
```env
# Frontend
REACT_APP_API_URL=http://localhost:3000
REACT_APP_ENV=development

# Backend
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
JWT_SECRET=your-secret-key
PORT=3000
NODE_ENV=development
```

## 📝 Notas Adicionais

- Implementar lazy loading para otimizar performance
- Configurar cache adequadamente
- Considerar implementação de PWA
- Planejar estratégia de SEO
- Configurar monitoramento e analytics

---

**Instruções para IA:**
1. Analise o contexto completo do projeto
2. Implemente seguindo o blueprint em etapas
3. Execute todos os comandos de validação
4. Corrija erros encontrados
5. Valide critérios de qualidade
6. Documente o código adequadamente
7. Teste funcionalidades end-to-end
