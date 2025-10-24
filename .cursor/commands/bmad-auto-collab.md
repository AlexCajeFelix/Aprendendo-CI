---
description: Executa workflow BMAD colaborativo com revisão entre agentes
tags: [bmad, collaborative, review, agents, workflow]
---

# Comando: /bmad-auto-collab

## 📋 Descrição

Executa o **workflow BMAD colaborativo** onde os 6 agentes se revisam mutuamente após cada etapa, com aprovação do usuário em pontos críticos e implementação REAL de código.

## 🎯 Diferença do `/bmad-auto` Normal

| Aspecto | `/bmad-auto` | `/bmad-auto-collab` |
|---------|--------------|---------------------|
| **Revisão** | Sem revisão entre agentes | Todos revisam cada etapa |
| **Aprovação** | Automático | Usuário aprova cada etapa |
| **Iterações** | Uma vez por etapa | Múltiplas iterações com feedback |
| **Código** | Simulado | REAL (arquivos criados) |
| **Feedback** | Não tem | Feedback consolidado |

## 💻 Como Usar

```
/bmad-auto-collab "Descrição do projeto"
```

### Exemplos:

```
/bmad-auto-collab "Sistema de gerenciamento de tarefas pessoais"

/bmad-auto-collab "API REST para e-commerce com autenticação JWT"

/bmad-auto-collab "Dashboard de métricas em tempo real"
```

## 🔄 Workflow Colaborativo

### Fase 1: Planejamento com Revisão

#### 1. Analyst Cria Brief
```
🔄 Analyst trabalhando...
✅ Brief criado

👥 REVISÃO COLABORATIVA:
   🔍 PM revisando...
   ✅ PM: "Requisitos claros, sugiro adicionar métricas"
   
   🔍 Architect revisando...
   ✅ Architect: "Viável tecnicamente, sem bloqueadores"
   
   🔍 Dev revisando...
   ⚠️  Dev: "Falta detalhes sobre APIs externas"
   
   🔍 QA revisando...
   ✅ QA: "Requisitos testáveis"

❓ DECISÃO:
   a) Aceitar e continuar
   b) Melhorar com feedback
   c) Cancelar workflow

→ Usuário escolhe: b) Melhorar

🔁 Analyst melhora Brief (Iteração 2)...
✅ Aprovado!
```

#### 2. PM Cria PRD
```
🔄 PM trabalhando...
✅ PRD criado

👥 REVISÃO COLABORATIVA:
   (Todos os agentes revisam)

❓ DECISÃO:
→ Usuário aprova
```

#### 3. Architect Define Arquitetura
```
🔄 Architect trabalhando...
✅ Arquitetura definida

👥 REVISÃO COLABORATIVA:
   (Todos os agentes revisam)

❓ DECISÃO:
→ Usuário aprova
```

### Fase 2: Criação de Stories

#### 4. Scrum Master Cria Stories
```
🔄 Scrum Master trabalhando...
✅ Stories criadas

👥 REVISÃO COLABORATIVA:
   (Todos os agentes revisam)

❓ DECISÃO:
→ Usuário aprova
```

### Fase 3: Desenvolvimento (Opcional)

#### 5. Implementação de Código REAL

```
❓ Deseja implementar código agora?
   a) Sim, implementar código real
   b) Não, apenas documentação

→ Usuário escolhe: a) Sim

📁 Onde criar o projeto?
   Caminho (Enter para 'projects/meu-projeto'):

→ Usuário: projects/task-manager/

✅ Projeto será criado em: /path/to/projects/task-manager/

❓ Confirmar? (s/n): s

🚀 Implementando stories...

📝 Story #001: Project Setup
   💻 Dev implementando...
   ✅ Código implementado
   
   👥 REVISÃO DE CÓDIGO:
      🔍 QA revisando...
      ✅ QA: Testes passando, qualidade OK
      
      🔍 Architect revisando...
      ✅ Architect: Segue padrões da arquitetura
      
      🔍 PM revisando...
      ✅ PM: Atende requisitos do PRD
   
   ❓ Código aprovado?
      a) Sim, continuar
      b) Não, corrigir
   
   → Usuário: a) Sim
   ✅ Story #001 aprovada!

(Repete para cada story)
```

## 📤 Output

### Documentos Gerados:
```
PRPs/bmad-output/
├── briefs/
│   └── [projeto]-brief.md
├── prds/
│   └── [projeto]-prd.md
├── architecture/
│   └── [projeto]-architecture.md
└── stories/
    └── [projeto]/
        ├── index.md
        ├── story-001-*.md
        └── story-002-*.md
```

### Logs de Revisão:
```
PRPs/bmad-output/.workflow/
├── [projeto]-workflow.json
└── reviews/
    ├── analyst-create_brief-iter1.json
    ├── analyst-create_brief-iter2.json
    ├── pm-create_prd-iter1.json
    ├── architect-create_architecture-iter1.json
    └── scrum-master-create_stories-iter1.json
```

### Código Implementado (se habilitado):
```
projects/[projeto]/
├── src/
│   ├── components/
│   ├── services/
│   └── utils/
├── tests/
├── package.json
└── README.md
```

## ⚙️ Configuração do Agente

Este comando executa:
- **Script**: `PRPs/scripts/bmad_collaborative_workflow.py`
- **Modo**: Colaborativo com revisões
- **Aprovação**: Manual em cada etapa
- **Implementação**: Código real (opcional)

## 💡 Quando Usar

### ✅ Use `/bmad-auto-collab` quando:
- Projeto crítico que precisa de qualidade máxima
- Quer feedback de múltiplas perspectivas
- Quer controle sobre cada etapa
- Precisa implementar código real
- Tempo não é crítico (mais lento por revisar tudo)

### ❌ Use `/bmad-auto` normal quando:
- Projeto simples ou prototipo
- Quer resultado rápido
- Não precisa de revisões múltiplas
- Apenas documentação (sem código)

## 🎯 Benefícios do Modo Colaborativo

### 1. Qualidade Superior
- **Múltiplas perspectivas** em cada documento
- **Feedback especializado** de cada agente
- **Iterações** até atingir qualidade desejada
- **Redução de erros** por revisão antecipada

### 2. Contexto Compartilhado
- **Todos os agentes** conhecem todo o projeto
- **Alinhamento** desde o início
- **Menos retrabalho** por mal-entendidos

### 3. Implementação Real
- **Código funcional** criado
- **Arquivos reais** no sistema
- **Testes executados** de verdade
- **Projeto pronto** para rodar

### 4. Rastreabilidade
- **Logs completos** de todas revisões
- **Histórico de iterações**
- **Justificativas** de decisões
- **Transparência total**

## ⚠️ Considerações

### Tempo
- **Mais lento** que modo automático
- Cada etapa precisa de aprovação
- Múltiplas iterações possíveis

### Interação
- **Requer atenção** do usuário
- Decisões em cada etapa
- Não pode deixar rodando sozinho

### Complexidade
- **Mais complexo** de usar
- Mais decisões a tomar
- Precisa entender feedbacks

## 📊 Exemplo de Execução Completa

```bash
# Via Cursor
/bmad-auto-collab "Sistema de gerenciamento de tarefas"

# Via Script
python3 PRPs/scripts/bmad_collaborative_workflow.py "Sistema de tarefas"

# Com nome específico
python3 PRPs/scripts/bmad_collaborative_workflow.py --project task-manager "Sistema de tarefas"
```

### Output Esperado:

```
======================================================================
🤝 BMAD Collaborative Workflow - Sistema de Revisão Colaborativa
======================================================================

📁 Projeto: task-manager
📝 Descrição: Sistema de gerenciamento de tarefas
⏰ Iniciado: 14:30:15

======================================================================


📋 FASE 1: PLANEJAMENTO COLABORATIVO
----------------------------------------------------------------------

🔄 ANALYST - Iteração 1
   📋 Tarefa: Criar Brief com análise de requisitos completa
   ✅ Output criado

   👥 REVISÃO COLABORATIVA:
      🔍 PM revisando...
      🔍 Architect revisando...
      🔍 Dev revisando...
      🔍 QA revisando...

   📊 FEEDBACKS:
   ------------------------------------------------------------
   ✅ PM:
      Requisitos claros e bem estruturados
      💡 Sugiro adicionar métricas de sucesso específicas
   
   ✅ Architect:
      Tecnicamente viável, sem bloqueadores identificados
   
   ⚠️  Dev:
      Revisado sob perspectiva de Software Development
      💡 Falta detalhes sobre integração com APIs externas
   
   ✅ QA:
      Requisitos são testáveis
   ------------------------------------------------------------

   ❓ DECISÃO:
      a) Aceitar e continuar
      b) Melhorar com feedback
      c) Cancelar workflow

   Escolha (a/b/c): b

   🔁 Melhorando com feedback... (Iteração 2)

[... continua para cada agente ...]

🎉 WORKFLOW COLABORATIVO COMPLETO!
======================================================================

📁 Projeto: task-manager
⏰ Concluído: 15:45:22

📊 Resumo:
   • Etapas completadas: 4
   • Revisões realizadas: 28
   • Stories implementadas: 3
   • Código em: /projects/task-manager/

📁 Documentos e logs salvos em:
   • Workflow state: PRPs/bmad-output/.workflow/task-manager-workflow.json
   • Revisões: PRPs/bmad-output/.workflow/reviews/

======================================================================
```

## 🔧 Troubleshooting

### Problema: Muitas iterações
**Solução**: Seja mais específico na descrição inicial

### Problema: Feedbacks contraditórios
**Solução**: Escolha "Melhorar" e agente balanceará feedbacks

### Problema: Quer pular revisão
**Solução**: Use `/bmad-auto` normal em vez de `/bmad-auto-collab`

## 📚 Referências

- **Script**: `PRPs/scripts/bmad_collaborative_workflow.py`
- **Template de Revisão**: `PRPs/templates/bmad/review-template.md`
- **Documentação**: `docs/bmad-collaborative-mode.md`
- **Guia de Agentes**: `PRPs/ai_docs/bmad-agents-guide.md`

---

**🤝 Workflow Colaborativo**: Qualidade máxima com revisão de múltiplas perspectivas e aprovação do usuário em cada etapa!

