# Integração BMAD - Sistema de Agentes Especializados

## 🎯 Visão Geral

A integração BMAD adiciona ao PRP um sistema completo de **6 agentes especializados** inspirados no [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD), permitindo um workflow ágil completo de planejamento e desenvolvimento.

### O que é BMAD?

**BMAD** (Breakthrough Method for Agile AI-Driven Development) é uma metodologia que usa agentes especializados colaborando em um workflow estruturado para garantir implementação de alta qualidade.

### PRP + BMAD = Melhor dos Dois Mundos

- **PRP**: Templates estruturados com contexto rico e validação executável
- **BMAD**: Agentes especializados com roles bem definidos
- **Integração**: Workflow ágil completo mantendo os princípios do PRP

---

## 🤖 Os 6 Agentes BMAD

### Fase de Planejamento

#### 1. **Analyst** 📊
- **Comando**: `/analyst`
- **Função**: Análise de requisitos
- **Output**: Brief de projeto
- **Localização**: `PRPs/bmad-output/briefs/`

#### 2. **PM** (Product Manager) 📋
- **Comando**: `/pm`
- **Função**: Especificação de produto
- **Output**: PRD (Product Requirement Document)
- **Localização**: `PRPs/bmad-output/prds/`

#### 3. **Architect** 🏗️
- **Comando**: `/architect`
- **Função**: Arquitetura técnica
- **Output**: Documento de Arquitetura
- **Localização**: `PRPs/bmad-output/architecture/`

### Fase de Desenvolvimento

#### 4. **Scrum Master** 📝
- **Comando**: `/scrum-master` ou `/sm`
- **Função**: Quebrar planejamento em stories
- **Output**: Development Stories
- **Localização**: `PRPs/bmad-output/stories/[projeto]/`

#### 5. **Dev** (Developer) 💻
- **Comando**: `/dev`
- **Função**: Implementação de código
- **Output**: Código + Dev Notes
- **Localização**: `PRPs/bmad-output/implementations/`

#### 6. **QA** (Quality Assurance) ✅
- **Comando**: `/qa`
- **Função**: Validação de qualidade
- **Output**: QA Reports
- **Localização**: `PRPs/bmad-output/qa-reports/`

---

## 🔄 Workflows Disponíveis

### Workflow 1: Planejamento Sequencial

```
/analyst  →  /pm  →  /architect
```

**Quando usar**: Projetos novos que precisam de planejamento completo.

**Output**:
- Brief (análise)
- PRD (produto)
- Architecture (técnico)

### Workflow 2: Desenvolvimento Iterativo

```
/sm  →  /dev story-001  →  /qa story-001  →  /dev story-002  →  ...
```

**Quando usar**: Quando planejamento está completo e é hora de implementar.

**Output**:
- Stories (quebradas e priorizadas)
- Código implementado
- QA Reports de validação

### Workflow 3: Completo (Planning + Development)

```
Planejamento:
  /analyst  →  /pm  →  /architect

Desenvolvimento (iterativo):
  /sm  →  Loop: /dev story-X  →  /qa story-X
```

**Quando usar**: Projeto completo do zero até deploy.

---

## 📖 Como Usar: Passo a Passo

### Cenário: Novo Projeto do Zero

#### Passo 1: Iniciar Análise

```bash
/analyst Sistema de gerenciamento de tarefas com autenticação
```

O Analyst fará perguntas para entender o projeto e criará um Brief completo.

**Output**: `PRPs/bmad-output/briefs/task-manager-brief.md`

---

#### Passo 2: Criar PRD

```bash
/pm PRPs/bmad-output/briefs/task-manager-brief.md
```

O PM transforma o Brief em especificações detalhadas de produto com user stories.

**Output**: `PRPs/bmad-output/prds/task-manager-prd.md`

---

#### Passo 3: Definir Arquitetura

```bash
/architect PRPs/bmad-output/prds/task-manager-prd.md
```

O Architect desenha a solução técnica completa.

**Output**: `PRPs/bmad-output/architecture/task-manager-architecture.md`

**✅ Planejamento Completo!** Agora você tem:
- Por quê (Brief)
- O quê (PRD)
- Como (Architecture)

---

#### Passo 4: Criar Development Stories

```bash
/sm PRPs/bmad-output/architecture/task-manager-architecture.md
```

O Scrum Master quebra tudo em stories implementáveis de 2-8h cada.

**Output**: `PRPs/bmad-output/stories/task-manager/story-001-setup.md`, `story-002-auth.md`, etc.

---

#### Passo 5: Implementar Stories (Iterativo)

```bash
# Story 1: Setup
/dev PRPs/bmad-output/stories/task-manager/story-001-setup.md

# Após Dev completar:
/qa story-001

# Se aprovado, próxima story:
/dev PRPs/bmad-output/stories/task-manager/story-002-auth.md

# E assim por diante...
```

---

## 🎯 Diferenças: PRP Tradicional vs BMAD Workflow

| Aspecto | PRP Tradicional | BMAD Workflow |
|---------|-----------------|---------------|
| **Documento** | Um PRP único | Documentos separados por fase |
| **Agentes** | IA genérica | 6 agentes especializados |
| **Workflow** | Linear | Fases distintas (Plan → Dev) |
| **Contextualização** | Tudo no PRP | Contexto passado entre agentes |
| **Melhor para** | Features individuais | Projetos completos |
| **Complexidade** | Baixa/Média | Média/Alta |
| **Output** | Código direto | Brief → PRD → Arch → Stories → Código |

### Quando Usar Cada Um?

**Use PRP Tradicional quando**:
- Feature bem definida
- Projeto pequeno/médio
- Quer implementação rápida
- Já tem arquitetura definida

**Use BMAD Workflow quando**:
- Projeto novo do zero
- Projeto grande/complexo
- Precisa de planejamento robusto
- Quer separation of concerns
- Trabalhando com equipe (cada agente = role)

---

## 📂 Estrutura de Arquivos

```
PRPs/
├── templates/
│   ├── bmad/                    # Templates dos agentes BMAD
│   │   ├── brief-template.md
│   │   ├── prd-template.md
│   │   ├── architecture-template.md
│   │   ├── story-template.md
│   │   ├── dev-notes-template.md
│   │   └── qa-report-template.md
│   └── [templates PRP originais]
│
├── bmad-output/                 # Outputs dos agentes
│   ├── briefs/                  # Briefs do Analyst
│   ├── prds/                    # PRDs do PM
│   ├── architecture/            # Arquiteturas do Architect
│   ├── stories/                 # Stories do Scrum Master
│   │   └── [projeto]/
│   │       ├── index.md
│   │       ├── story-001-setup.md
│   │       ├── story-002-auth.md
│   │       └── ...
│   ├── implementations/         # Dev Notes do Dev
│   └── qa-reports/             # Reports do QA
│
└── ai_docs/
    └── bmad-agents-guide.md    # Guia de colaboração entre agentes
```

---

## 🎨 Fluxo de Contexto Entre Agentes

### Planning Phase

```
Analyst (Brief)
    ↓ [Brief completo passa para PM]
PM (PRD)
    ↓ [Brief + PRD passam para Architect]
Architect (Architecture)
```

### Development Phase

```
Scrum Master
    ↓ [Brief + PRD + Architecture → Stories]
Dev (implementa Story #X)
    ↓ [Story + Dev Notes → QA]
QA (valida Story #X)
    ↓ [Se aprovado, próxima story]
Dev (implementa Story #X+1)
    ...
```

**Chave**: Cada agente recebe contexto completo de agentes anteriores embutido nos documentos.

---

## 💡 Melhores Práticas

### 1. Planeje Antes de Implementar

Não pule direto para `/dev`. O workflow BMAD é desenhado para garantir que planejamento esteja sólido antes de código ser escrito.

### 2. Uma Story por Vez

Não tente implementar múltiplas stories em paralelo. O workflow é sequencial por motivo: cada story pode impactar as próximas.

### 3. QA Não é Opcional

Sempre execute `/qa` após `/dev`. É o checkpoint de qualidade que previne bugs em produção.

### 4. Documente Desvios

Se Dev precisar desviar da story, deve documentar no Dev Notes. QA vai validar se o desvio faz sentido.

### 5. Itere no Planejamento

Se durante desenvolvimento perceber que planejamento está incompleto, volte e atualize Brief/PRD/Arch.

---

## 🔧 Configuração

### Arquivos Importantes

- `.cursor/agents/` - Definições dos 6 agentes
- `.cursor/commands/` - Comandos slash para cada agente
- `config/agents.json` - Configuração centralizada
- `PRPs/templates/bmad/` - Templates que agentes usam

### Customização

Para customizar um agente:

1. Edite `.cursor/agents/[agente].md`
2. Ajuste instruções e regras conforme necessário
3. Mantenha estrutura de output compatível

---

## 📊 Exemplo Completo: E-commerce

### 1. Planning Phase

**Analyst** cria `ecommerce-brief.md`:
- Requisitos de negócio
- Personas (comprador, vendedor, admin)
- Casos de uso principais

**PM** cria `ecommerce-prd.md`:
- Features: Catálogo, Carrinho, Checkout, Admin
- User stories para cada feature
- MVP vs Future features

**Architect** cria `ecommerce-architecture.md`:
- Frontend: Next.js + TypeScript
- Backend: Node.js + Express
- Database: PostgreSQL
- Decisões de segurança, performance, etc

### 2. Development Phase

**Scrum Master** cria stories:
- `story-001-setup-projeto.md`
- `story-002-database-schema.md`
- `story-003-auth-basico.md`
- `story-004-api-produtos.md`
- `story-005-catalogo-frontend.md`
- ... total de 30 stories

**Dev + QA** implementam iterativamente:
```bash
# Sprint 1: Foundation
/dev story-001 → /qa story-001 ✅
/dev story-002 → /qa story-002 ✅
/dev story-003 → /qa story-003 ✅

# Sprint 2: Core Features
/dev story-004 → /qa story-004 ✅
/dev story-005 → /qa story-005 ⚠️ (Ressalvas, mas aprovado)
...
```

---

## 🎓 Recursos de Aprendizado

### Documentação

- **Este documento**: Guia de integração
- `PRPs/ai_docs/bmad-agents-guide.md`: Guia para IAs
- Arquivos `.cursor/agents/*.md`: Detalhes de cada agente
- Arquivos `.cursor/commands/*.md`: Como usar comandos

### Exemplos

- `PRPs/templates/bmad/`: Templates preenchidos
- `PRPs/bmad-output/`: Outputs de exemplo (quando disponíveis)

### BMAD Original

- [BMAD-METHOD no GitHub](https://github.com/bmad-code-org/BMAD-METHOD)
- Conceitos originais que inspiraram esta integração

---

## 🆚 Compatibilidade com PRP Original

**100% Compatível!**

Você pode usar:
- **Apenas PRP original**: Comandos `/create-prp`, `/execute-prp` continuam funcionando
- **Apenas BMAD workflow**: Use os 6 novos agentes
- **Híbrido**: Use BMAD para planejar, PRP para features individuais

**Exemplo Híbrido**:
1. Use BMAD para criar Brief, PRD, Architecture
2. Use Scrum Master para quebrar em stories
3. Use `/execute-prp` com stories individuais (compatível!)

---

## 🚀 Próximos Passos

Agora que entendeu a integração BMAD:

1. **Experimente**: Crie um projeto simples usando o workflow completo
2. **Compare**: Teste PRP original vs BMAD para ver diferenças
3. **Customize**: Ajuste agentes para seu estilo de trabalho
4. **Compartilhe**: Documente seus aprendizados

---

**Integração criada com ❤️ combinando o melhor de PRP e BMAD!**

