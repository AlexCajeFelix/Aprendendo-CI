# Melhores Práticas para PRPs

Este documento apresenta as melhores práticas para criar e usar Product Requirement Prompts (PRPs) de forma eficaz.

## 📋 Estrutura e Organização

### 1. Seja Específico e Detalhado
**❌ Ruim:**
```
Implementar sistema de autenticação
```

**✅ Bom:**
```
Implementar sistema de autenticação com:
- Login via email/senha com validação JWT
- Registro de usuários com verificação de email
- Recuperação de senha via email com tokens seguros
- Middleware de autenticação para proteger rotas
- Rate limiting para prevenir ataques de força bruta
- Logs de auditoria para tentativas de login
```

### 2. Use Critérios de Aceitação Claros
**❌ Ruim:**
```
O usuário deve conseguir fazer login
```

**✅ Bom:**
```
Critérios de aceitação:
- [ ] Usuário pode fazer login com email/senha válidos
- [ ] Sistema retorna JWT token válido por 24 horas
- [ ] Login falha com credenciais incorretas
- [ ] Sistema bloqueia após 5 tentativas falhadas
- [ ] Logs de tentativas de login são gerados
```

### 3. Inclua Exemplos Concretos
**❌ Ruim:**
```
Criar formulário de contato
```

**✅ Bom:**
```
Criar formulário de contato com campos:
- Nome (obrigatório, mínimo 2 caracteres)
- Email (obrigatório, formato válido)
- Assunto (obrigatório, máximo 100 caracteres)
- Mensagem (obrigatório, mínimo 10 caracteres)
- Botão "Enviar" que valida dados e envia email
- Feedback visual de sucesso/erro
- Loading state durante envio
```

## 🎯 Foco e Escopo

### 1. Mantenha o Escopo Focado
- **Um PRP por funcionalidade principal**
- **Evite PRPs muito amplos** (ex: "Criar um sistema completo de e-commerce")
- **Quebre projetos grandes** em PRPs menores e gerenciáveis

### 2. Defina Limites Claros
```
Escopo INCLUÍDO:
- CRUD básico de produtos
- Sistema de categorias
- Busca por texto

Escopo EXCLUÍDO:
- Sistema de pagamentos
- Integração com gateways
- Relatórios avançados
```

### 3. Priorize Funcionalidades
```
Prioridade ALTA:
- Autenticação de usuários
- CRUD de produtos

Prioridade MÉDIA:
- Sistema de categorias
- Busca básica

Prioridade BAIXA:
- Filtros avançados
- Exportação de dados
```

## 🔧 Aspectos Técnicos

### 1. Especifique Tecnologias Exatas
**❌ Ruim:**
```
Usar React e Node.js
```

**✅ Bom:**
```
Stack Tecnológico:
- Frontend: React 18.2.0 + TypeScript 5.0
- Backend: Node.js 20.0 + Express 4.18
- Banco: PostgreSQL 15.0
- ORM: Prisma 5.0
- Estilização: Tailwind CSS 3.3
```

### 2. Defina Padrões de Código
```
Padrões de Código:
- Linguagem: TypeScript 5.0
- Framework: React 18 com hooks funcionais
- Convenções: ESLint + Prettier configurados
- Testes: Jest + Testing Library
- Estado: Zustand para estado global
- Roteamento: React Router 6.8
```

### 3. Inclua Considerações de Performance
```
Performance:
- Tempo de carregamento inicial < 3 segundos
- Lazy loading para componentes pesados
- Otimização de re-renders com React.memo
- Bundle size < 1MB gzipped
- Cache de dados com React Query
```

## 📚 Documentação e Exemplos

### 1. Forneça Exemplos de Código
```typescript
// Exemplo de componente principal
import React, { useState } from 'react';

interface TaskFormProps {
  onSubmit: (task: Task) => void;
}

export const TaskForm: React.FC<TaskFormProps> = ({ onSubmit }) => {
  const [title, setTitle] = useState('');
  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (title.trim()) {
      onSubmit({ title: title.trim(), completed: false });
      setTitle('');
    }
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Nova tarefa..."
        required
      />
      <button type="submit">Adicionar</button>
    </form>
  );
};
```

### 2. Inclua Casos de Uso Específicos
```
Casos de Uso:
1. Usuário cria nova tarefa:
   - Clica em "Nova Tarefa"
   - Preenche título obrigatório
   - Opcionalmente adiciona descrição
   - Salva e tarefa aparece na lista

2. Usuário marca tarefa como concluída:
   - Clica no checkbox da tarefa
   - Tarefa fica com visual de concluída
   - Contador de tarefas é atualizado
```

### 3. Documente Estados e Comportamentos
```
Estados do Componente:
- Loading: Mostra spinner durante carregamento
- Error: Exibe mensagem de erro com botão de retry
- Success: Mostra confirmação de sucesso
- Empty: Exibe mensagem quando não há dados
- Idle: Estado normal de interação
```

## 🛡️ Segurança e Qualidade

### 1. Considere Aspectos de Segurança
```
Segurança:
- Validação de inputs no frontend e backend
- Sanitização de dados de entrada
- Autenticação JWT com tokens seguros
- Rate limiting para prevenir abuso
- HTTPS obrigatório em produção
- Headers de segurança configurados
```

### 2. Defina Critérios de Qualidade
```
Critérios de Qualidade:
- Código TypeScript bem tipado
- Cobertura de testes >= 80%
- Componentes reutilizáveis
- Documentação inline adequada
- Performance otimizada
- Acessibilidade WCAG 2.1 AA
```

### 3. Inclua Tratamento de Erros
```
Tratamento de Erros:
- Try-catch em todas as operações async
- Mensagens de erro user-friendly
- Logs detalhados para debugging
- Fallbacks para falhas de rede
- Retry automático para operações críticas
```

## 📊 Métricas e Validação

### 1. Defina Métricas de Sucesso
```
Métricas de Sucesso:
- Tempo de desenvolvimento: < 16 horas
- Cobertura de testes: >= 80%
- Performance: < 3s tempo de carregamento
- Usabilidade: < 3 cliques para ação principal
- Bugs críticos: 0
```

### 2. Inclua Critérios de Validação
```
Validação:
- [ ] Funcionalidades principais testadas manualmente
- [ ] Testes automatizados passando
- [ ] Performance dentro dos limites
- [ ] Acessibilidade validada
- [ ] Segurança auditada
- [ ] Documentação completa
```

## 🔄 Iteração e Melhoria

### 1. Colete Feedback
- **Teste o PRP** gerando código e avaliando o resultado
- **Identifique gaps** entre o que foi solicitado e o que foi gerado
- **Refine o PRP** baseado na experiência

### 2. Versionamento
```
Versionamento:
- Mantenha histórico de mudanças no PRP
- Documente melhorias e correções
- Colete feedback de usuários
- Evolua templates baseado na experiência
```

### 3. Reutilização
```
Reutilização:
- Crie templates para casos comuns
- Documente padrões que funcionam bem
- Compartilhe PRPs bem-sucedidos
- Mantenha biblioteca de exemplos
```

## 🎨 Dicas Específicas por Tipo

### Web Applications
- **Foque na experiência do usuário**
- **Inclua wireframes ou mockups quando possível**
- **Especifique responsividade e acessibilidade**
- **Defina fluxos de navegação claros**

### APIs
- **Documente todos os endpoints com exemplos**
- **Especifique códigos de status HTTP**
- **Inclua schemas de request/response**
- **Defina estratégias de versionamento**

### Databases
- **Inclua diagramas ER quando complexo**
- **Especifique índices e constraints**
- **Defina estratégias de backup**
- **Considere migrações e versionamento**

### Microservices
- **Defina contratos de comunicação**
- **Especifique responsabilidades claras**
- **Inclua considerações de deployment**
- **Documente dependências entre serviços**

### Components
- **Inclua props interface bem definida**
- **Especifique estados visuais**
- **Documente casos de uso**
- **Considere acessibilidade**

## ⚠️ Erros Comuns a Evitar

### 1. PRP Muito Vago
```
❌ "Criar um sistema de usuários"
✅ "Criar API REST para CRUD de usuários com autenticação JWT"
```

### 2. Falta de Contexto
```
❌ "Implementar login"
✅ "Implementar sistema de login para aplicação web que permite acesso a área administrativa"
```

### 3. Critérios de Aceitação Ambíguos
```
❌ "Deve funcionar bem"
✅ "Deve carregar em menos de 2 segundos e suportar 100 usuários simultâneos"
```

### 4. Tecnologias Não Especificadas
```
❌ "Usar banco de dados moderno"
✅ "Usar PostgreSQL 15.0 com Prisma ORM"
```

### 5. Falta de Exemplos
```
❌ "Criar formulário"
✅ "Criar formulário com validação em tempo real, estados de loading e tratamento de erros"
```

## 🚀 Conclusão

PRPs eficazes são:
- **Específicos** e detalhados
- **Bem estruturados** e organizados
- **Focados** em um escopo claro
- **Técnicos** mas compreensíveis
- **Testáveis** e validáveis
- **Iterativos** e melhoráveis

Lembre-se: um bom PRP é a base para código de alta qualidade. Invista tempo na criação de PRPs bem estruturados e você colherá os benefícios na qualidade do código gerado.
