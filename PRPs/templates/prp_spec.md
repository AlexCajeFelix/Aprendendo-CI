# [Nome da Especificação]

**Tipo:** Especificação Técnica
**Complexidade:** [Baixa/Média/Alta]
**Tempo Estimado:** [Estimativa em horas]
**Versão:** 1.0

## 📋 Visão Geral

### Objetivo
[Descrição clara do que será especificado]

### Escopo
- **Incluído:** [O que está incluído na especificação]
- **Excluído:** [O que não está incluído na especificação]

### Stakeholders
- **Product Owner:** [Nome]
- **Tech Lead:** [Nome]
- **Desenvolvedores:** [Nomes]
- **QA:** [Nome]

## 🎯 Requisitos Funcionais

### RF001 - [Nome do Requisito]
**Descrição:** [Descrição detalhada]
**Prioridade:** [Alta/Média/Baixa]
**Critérios de Aceitação:**
- [ ] [Critério 1]
- [ ] [Critério 2]
- [ ] [Critério 3]

### RF002 - [Nome do Requisito]
**Descrição:** [Descrição detalhada]
**Prioridade:** [Alta/Média/Baixa]
**Critérios de Aceitação:**
- [ ] [Critério 1]
- [ ] [Critério 2]
- [ ] [Critério 3]

## 🔧 Requisitos Não Funcionais

### Performance
- **Tempo de Resposta:** [Especificação]
- **Throughput:** [Especificação]
- **Disponibilidade:** [Especificação]

### Segurança
- **Autenticação:** [Especificação]
- **Autorização:** [Especificação]
- **Criptografia:** [Especificação]

### Usabilidade
- **Interface:** [Especificação]
- **Acessibilidade:** [Especificação]
- **Responsividade:** [Especificação]

## 🏗️ Arquitetura

### Visão Geral
```
[Diagrama de arquitetura em texto ou referência para diagrama]
```

### Componentes Principais
1. **[Componente 1]**
   - Responsabilidade: [O que faz]
   - Interface: [Como se comunica]
   - Dependências: [Do que depende]

2. **[Componente 2]**
   - Responsabilidade: [O que faz]
   - Interface: [Como se comunica]
   - Dependências: [Do que depende]

### Fluxo de Dados
```
[Descrição do fluxo de dados entre componentes]
```

## 📊 Modelo de Dados

### Entidades Principais
```typescript
// Exemplo de modelo de dados
interface User {
  id: string;
  name: string;
  email: string;
  createdAt: Date;
  updatedAt: Date;
}

interface Product {
  id: string;
  name: string;
  price: number;
  category: string;
  inStock: boolean;
}
```

### Relacionamentos
- [Descrição dos relacionamentos entre entidades]

### Regras de Negócio
1. **[Regra 1]:** [Descrição]
2. **[Regra 2]:** [Descrição]
3. **[Regra 3]:** [Descrição]

## 🔌 APIs e Interfaces

### Endpoints REST
```
GET    /api/users          # Listar usuários
POST   /api/users          # Criar usuário
GET    /api/users/:id      # Buscar usuário por ID
PUT    /api/users/:id      # Atualizar usuário
DELETE /api/users/:id      # Deletar usuário
```

### Contratos de API
```typescript
// Exemplo de contrato
interface CreateUserRequest {
  name: string;
  email: string;
  password: string;
}

interface CreateUserResponse {
  id: string;
  name: string;
  email: string;
  createdAt: string;
}
```

### Validações
- [Lista de validações necessárias]

## 🧪 Estratégia de Testes

### Testes Unitários
- **Cobertura Mínima:** 80%
- **Ferramentas:** Jest, Vitest
- **Foco:** Lógica de negócio

### Testes de Integração
- **Ferramentas:** Supertest, Cypress
- **Foco:** APIs e fluxos completos

### Testes E2E
- **Ferramentas:** Playwright, Cypress
- **Foco:** Jornadas críticas do usuário

### Cenários de Teste
1. **[Cenário 1]:** [Descrição]
2. **[Cenário 2]:** [Descrição]
3. **[Cenário 3]:** [Descrição]

## 🚀 Plano de Implementação

### Fase 1: [Nome da Fase]
**Duração:** [Estimativa]
**Entregáveis:**
- [ ] [Entregável 1]
- [ ] [Entregável 2]

### Fase 2: [Nome da Fase]
**Duração:** [Estimativa]
**Entregáveis:**
- [ ] [Entregável 1]
- [ ] [Entregável 2]

### Fase 3: [Nome da Fase]
**Duração:** [Estimativa]
**Entregáveis:**
- [ ] [Entregável 1]
- [ ] [Entregável 2]

## 📦 Entregáveis

### Código
- [ ] [Arquivo/Componente 1]
- [ ] [Arquivo/Componente 2]
- [ ] [Arquivo/Componente 3]

### Documentação
- [ ] README técnico
- [ ] Documentação da API
- [ ] Guia de deployment
- [ ] Manual do usuário

### Testes
- [ ] Suite de testes unitários
- [ ] Suite de testes de integração
- [ ] Suite de testes E2E
- [ ] Relatório de cobertura

## ✅ Critérios de Aceitação

### Funcionalidade
- [ ] Todos os requisitos funcionais implementados
- [ ] Todos os requisitos não funcionais atendidos
- [ ] Performance dentro dos limites especificados

### Qualidade
- [ ] Código revisado e aprovado
- [ ] Testes passando com cobertura mínima
- [ ] Documentação completa e atualizada

### Deploy
- [ ] Aplicação deployada em ambiente de staging
- [ ] Testes de smoke passando
- [ ] Aprovado para produção

## 🔍 Riscos e Mitigações

### Riscos Técnicos
1. **[Risco 1]**
   - **Probabilidade:** [Alta/Média/Baixa]
   - **Impacto:** [Alto/Médio/Baixo]
   - **Mitigação:** [Como mitigar]

2. **[Risco 2]**
   - **Probabilidade:** [Alta/Média/Baixa]
   - **Impacto:** [Alto/Médio/Baixo]
   - **Mitigação:** [Como mitigar]

### Riscos de Negócio
1. **[Risco 1]**
   - **Probabilidade:** [Alta/Média/Baixa]
   - **Impacto:** [Alto/Médio/Baixo]
   - **Mitigação:** [Como mitigar]

## 📚 Referências

### Documentação Técnica
- [Link para documentação do framework]
- [Link para documentação da API]
- [Link para padrões de arquitetura]

### Exemplos e Padrões
- [Link para exemplo similar]
- [Link para padrão de design]
- [Link para biblioteca de componentes]

### Ferramentas e Tecnologias
- [Link para documentação da ferramenta]
- [Link para guia de configuração]
- [Link para melhores práticas]

---

**Instruções para IA:**
1. Analise todos os requisitos e especificações
2. Implemente seguindo exatamente a arquitetura definida
3. Crie testes para todos os cenários especificados
4. Documente o código conforme os padrões estabelecidos
5. Valide se todos os critérios de aceitação foram atendidos
