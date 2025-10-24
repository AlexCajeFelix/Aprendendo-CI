# PRP - Product Requirement Prompts

Sistema completo de Product Requirement Prompts baseado no [PRPs-agentic-eng](https://github.com/Wirasm/PRPs-agentic-eng), adaptado e otimizado para funcionar com o Cursor IDE.

## 🎯 O que são PRPs?

PRPs (Product Requirement Prompts) são prompts estruturados que fornecem contexto abrangente para IA gerar código de alta qualidade. Eles garantem implementação bem-sucedida em uma única passada através de:

- **Contexto abrangente** com documentação e exemplos
- **Blueprint de implementação** detalhado
- **Loop de validação** com comandos executáveis
- **Critérios de sucesso** claros e mensuráveis

## 🚀 Características Principais

### ✨ Sistema Completo
- **12 comandos do Cursor** pré-configurados
- **Templates de PRP** para diferentes tipos de projeto
- **Scripts de execução** e validação
- **Documentação abrangente** e exemplos práticos

### 🎨 Templates Incluídos
- **Aplicação Web Completa** - Frontend + Backend integrados
- **Serviço de API** - APIs REST/GraphQL robustas
- **Componente Frontend** - Componentes reutilizáveis
- **Schema de Banco** - Estruturas de dados otimizadas
- **Microserviço** - Arquitetura distribuída

### 🔧 Comandos do Cursor
- `/create-prp` - Criar PRPs abrangentes
- `/execute-prp` - Executar PRPs contra codebase
- `/planning-create` - Documentos de planejamento
- `/spec-create` - Especificações técnicas
- `/review-code` - Revisão de qualidade
- `/refactor-simple` - Refatorações seguras
- E mais 6 comandos especializados

### 🤖 **NOVO: Agentes BMAD Integrados**

Inspirado no [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD), agora o PRP inclui **6 agentes especializados** para workflow ágil completo:

#### Fase de Planejamento:
- **`/analyst`** - Analista de requisitos → cria Brief
- **`/pm`** - Product Manager → cria PRD  
- **`/architect`** - Arquiteto → define arquitetura técnica

#### Fase de Desenvolvimento:
- **`/scrum-master` ou `/sm`** - Quebra em Development Stories
- **`/dev`** - Developer → implementa código com testes
- **`/qa`** - QA Engineer → valida qualidade

**Workflow Completo**: `Analyst → PM → Architect → Scrum Master → Dev → QA`

#### 🚀 **Sistema Automático**:
- **`/bmad-auto`** - Executa workflow completo automaticamente
- **Comunicação entre agentes** - Handoffs automáticos
- **Zero intervenção manual** - Do Brief até código implementado

#### 🤝 **Sistema Colaborativo** (NOVO):
- **`/bmad-auto-collab`** - Workflow com revisão entre agentes
- **Todos revisam todos** - Feedback de múltiplas perspectivas
- **Aprovação do usuário** - Controle em cada etapa
- **Implementação real** - Código realmente criado

📖 [Documentação Completa da Integração BMAD](docs/bmad-integration.md)  
🤖 [Sistema BMAD Full Automático](docs/bmad-auto-system.md)  
🤝 [Sistema BMAD Colaborativo](docs/bmad-collaborative-mode.md)

## 📁 Estrutura do Projeto

```
PRP/
├── .cursor/                 # Configurações do Cursor
│   ├── commands/           # 12 comandos personalizados
│   ├── rules              # Regras do projeto
│   └── instructions       # Instruções para agentes
├── PRPs/                   # Product Requirement Prompts
│   ├── templates/         # Templates especializados
│   ├── examples/          # Exemplos práticos
│   ├── scripts/           # Scripts Python de execução
│   └── ai_docs/          # Documentação para IA
├── config/                 # Configurações JSON
├── docs/                   # Documentação detalhada
└── tools/                  # Ferramentas auxiliares
```

## 🛠️ Instalação e Configuração

### 1. Clone o Repositório
```bash
git clone <seu-repositorio>
cd PRP
```

### 2. Configure o Cursor
Os comandos já estão configurados em `.cursor/commands/`. Eles aparecerão automaticamente no Cursor quando você digitar `/`.

### 3. Configure Agentes (Opcional)
1. Abra configurações do Cursor
2. Vá para "Background Agents"
3. Configure agente com instruções de `.cursor/instructions`

### 4. Teste a Configuração
```bash
# Validar estrutura
python PRPs/scripts/validator.py PRPs/templates/prp_base.md

# Gerar exemplo
python PRPs/scripts/template_generator.py --type web-application --output PRPs/exemplo.md
```

## 🎯 Como Usar

### Criando um PRP
```bash
# Usar comando do Cursor
/create-prp sistema de autenticação com JWT

# Ou usar script diretamente
python PRPs/scripts/template_generator.py --description "sistema de autenticação" --output PRPs/auth.md
```

### Executando um PRP
```bash
# Modo interativo (recomendado)
python PRPs/scripts/prp_runner.py --prp PRPs/auth.md --interactive

# Modo headless (para CI/CD)
python PRPs/scripts/prp_runner.py --prp PRPs/auth.md --output-format json
```

### Usando Comandos do Cursor
1. Digite `/` no Cursor para ver comandos disponíveis
2. Selecione o comando desejado
3. Forneça argumentos quando solicitado
4. Acompanhe a execução e resultados

## 📋 Exemplos de Uso

### Exemplo 1: Aplicação Web
```bash
/create-prp "dashboard de métricas em tempo real com React e Node.js"
```
Resultado: PRP completo com contexto, blueprint e validações.

### Exemplo 2: API Service
```bash
/execute-prp PRPs/api-usuarios.md
```
Resultado: Implementação completa da API seguindo especificação.

### Exemplo 3: Componente Frontend
```bash
/refactor-simple "extrair componente de tabela para reutilização"
```
Resultado: Refatoração segura mantendo funcionalidade.

## 🎨 Templates Disponíveis

### Web Application
- **Complexidade**: Baixa/Média/Alta
- **Tempo**: 8-40 horas
- **Tecnologias**: React, Vue, Angular, Next.js, Node.js, Express, FastAPI, Django
- **Foco**: Aplicações completas com frontend e backend

### API Service
- **Complexidade**: Baixa/Média/Alta
- **Tempo**: 4-20 horas
- **Tecnologias**: Node.js, Express, FastAPI, Spring Boot, PostgreSQL, MongoDB
- **Foco**: APIs robustas e escaláveis

### Frontend Component
- **Complexidade**: Baixa/Média/Alta
- **Tempo**: 1-8 horas
- **Tecnologias**: React, Vue, Angular, TypeScript, CSS Modules
- **Foco**: Componentes reutilizáveis e bem testados

### Database Schema
- **Complexidade**: Baixa/Média/Alta
- **Tempo**: 2-12 horas
- **Tecnologias**: PostgreSQL, MySQL, MongoDB, SQLite
- **Foco**: Estruturas de dados otimizadas

### Microservice
- **Complexidade**: Média/Alta
- **Tempo**: 12-60 horas
- **Tecnologias**: Docker, Kubernetes, Node.js, Python, Go
- **Foco**: Arquitetura distribuída

## 🔧 Scripts Incluídos

### PRP Runner (`prp_runner.py`)
Executor principal de PRPs com suporte a:
- Modo interativo para desenvolvimento
- Modo headless para CI/CD
- Validação automática
- Relatórios detalhados

### Template Generator (`template_generator.py`)
Gerador de templates customizados com:
- Análise automática do projeto
- Personalização baseada na stack tecnológica
- Geração baseada em descrição
- Múltiplos formatos de saída

### Validator (`validator.py`)
Validador de PRPs com:
- Verificação de estrutura
- Validação de conteúdo
- Análise de qualidade
- Relatórios detalhados

## 📚 Documentação

### Guias Principais
- [Setup e Configuração](docs/setup.md)
- [Estrutura de PRPs](docs/prp-structure.md)
- [Integração com Cursor](docs/cursor-integration.md)
- [Melhores Práticas](docs/best-practices.md)

### Recursos para IA
- [Melhores Práticas para Cursor](PRPs/ai_docs/cursor_best_practices.md)
- [Padrões de Código](PRPs/ai_docs/code_patterns.md)
- [Estratégias de Teste](PRPs/ai_docs/testing_patterns.md)

### Exemplos Práticos
- [Exemplos por Tipo](PRPs/examples/)
- [Casos de Uso Reais](PRPs/examples/)
- [Templates Customizados](PRPs/templates/)

## 🎯 Benefícios

### Para Desenvolvedores
- **Implementação mais rápida** com contexto abrangente
- **Menos iterações** através de especificações claras
- **Código de maior qualidade** com validações automáticas
- **Aprendizado contínuo** através de exemplos práticos

### Para Equipes
- **Padronização** de processos de desenvolvimento
- **Documentação viva** através de PRPs
- **Colaboração melhorada** com especificações claras
- **Qualidade consistente** através de validações

### Para Projetos
- **Redução de bugs** através de especificações detalhadas
- **Manutenibilidade** através de código bem documentado
- **Escalabilidade** através de padrões estabelecidos
- **Onboarding acelerado** para novos membros

## 🔄 Workflow Recomendado

### 1. Planejamento
```bash
/planning-create "arquitetura do sistema de pagamentos"
```

### 2. Especificação
```bash
/spec-create "API REST para processamento de pagamentos"
```

### 3. Implementação
```bash
/execute-prp PRPs/api-pagamentos.md
```

### 4. Revisão
```bash
/review-code src/api/pagamentos/
```

### 5. Refatoração
```bash
/refactor-simple "otimizar validação de dados"
```

### 6. Deploy
```bash
/create-pr "Implementa sistema de pagamentos"
```

## 🤝 Contribuindo

### Como Contribuir
1. **Teste** com projetos reais
2. **Documente** casos de uso bem-sucedidos
3. **Compartilhe** melhorias nos templates
4. **Mantenha** a documentação atualizada

### Áreas de Contribuição
- **Templates**: Novos tipos de projeto
- **Scripts**: Melhorias na automação
- **Documentação**: Guias e exemplos
- **Comandos**: Novos comandos do Cursor

## 📄 Licença

MIT License - Veja [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

Baseado no excelente trabalho do [PRPs-agentic-eng](https://github.com/Wirasm/PRPs-agentic-eng) por [Wirasm](https://github.com/Wirasm).

## 📞 Suporte

- **Issues**: [GitHub Issues](https://github.com/seu-usuario/PRP/issues)
- **Discussões**: [GitHub Discussions](https://github.com/seu-usuario/PRP/discussions)
- **Documentação**: [Wiki do Projeto](https://github.com/seu-usuario/PRP/wiki)

---

**🚀 Comece agora**: Use `/create-prp` no Cursor para criar seu primeiro PRP e experimente o poder da implementação assistida por IA!
# Aprendendo-CI
# Aprendendo-CI
