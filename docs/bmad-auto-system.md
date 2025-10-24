# Sistema BMAD Full Automático

Este documento detalha o **Sistema BMAD Full Automático** - uma extensão avançada que permite execução completa do workflow BMAD onde os agentes se comunicam automaticamente entre si.

## 🎯 Visão Geral

O Sistema BMAD Full Automático implementa **comunicação automática entre agentes**, eliminando a necessidade de intervenção manual entre etapas. Os agentes passam contexto automaticamente e executam o workflow completo do Brief até código implementado.

### Diferenças do Sistema Manual

| Aspecto | Manual (`/analyst` → `/pm` → ...) | Automático (`/bmad-auto`) |
|---------|-----------------------------------|---------------------------|
| **Comunicação** | Manual entre agentes | Automática via handoffs |
| **Execução** | Etapa por etapa | Workflow completo |
| **Tempo** | Mais lento (pausas) | Mais rápido (contínuo) |
| **Controle** | Total sobre cada etapa | Automático com logs |
| **Debugging** | Fácil (etapa por etapa) | Via logs e monitoramento |
| **Uso Ideal** | Features específicas | Projetos completos |

## 🚀 Como Usar

### Comando Principal

```bash
/bmad-auto "Descrição do seu projeto"
```

### Exemplos Práticos

```bash
# Sistema de gerenciamento de tarefas
/bmad-auto "Sistema web para gerenciar tarefas pessoais com autenticação e dashboard"

# API REST
/bmad-auto "API REST para e-commerce com JWT, CRUD de produtos e carrinho"

# Dashboard de métricas
/bmad-auto "Dashboard em tempo real para métricas de negócio com gráficos interativos"
```

### Via Script Direto

```bash
# Execução básica
python PRPs/scripts/bmad_full_auto.py "Descrição do projeto"

# Com nome específico
python PRPs/scripts/bmad_full_auto.py "Sistema de vendas" --project sales-system

# Modo silencioso (sem pausas)
python PRPs/scripts/bmad_full_auto.py "API REST" --auto-approve
```

### Via Orchestrator

```bash
# Execução automática via orchestrator
python PRPs/scripts/bmad_orchestrator.py --auto "Meu projeto"

# Com nome específico
python PRPs/scripts/bmad_orchestrator.py --auto "API REST" --project-name api
```

## 🔄 Workflow Automático

### Fase 1: Planejamento (Sequencial)

```
1. 🤖 Analyst
   Input: Descrição do projeto
   Processo: Analisa requisitos, stakeholders, objetivos
   Output: Brief completo
   Handoff: → PM

2. 🤖 PM (Product Manager)
   Input: Brief do Analyst
   Processo: Cria PRD com user stories e critérios de aceitação
   Output: Product Requirement Document
   Handoff: → Architect

3. 🤖 Architect
   Input: Brief + PRD
   Processo: Define arquitetura técnica, stack, padrões
   Output: Documento de Arquitetura
   Handoff: → Scrum Master
```

### Fase 2: Desenvolvimento (Iterativo)

```
4. 🤖 Scrum Master
   Input: Brief + PRD + Arquitetura
   Processo: Quebra em Development Stories implementáveis
   Output: Stories organizadas
   Handoff: → Dev (primeira story)

5. 🤖 Loop Dev → QA (para cada story):
   a. Dev recebe story
   b. Dev implementa código + testes
   c. Dev cria Dev Notes
   d. QA valida implementação
   e. QA cria QA Report
   f. Se aprovado: próxima story
   g. Se reprovado: volta para Dev
```

## 📁 Estrutura de Outputs

### Documentos de Planejamento

```
PRPs/bmad-output/
├── briefs/
│   └── [projeto]-brief.md          # Brief do Analyst
├── prds/
│   └── [projeto]-prd.md            # PRD do PM
└── architecture/
    └── [projeto]-architecture.md   # Arquitetura do Architect
```

### Development Stories

```
PRPs/bmad-output/stories/[projeto]/
├── index.md                        # Índice de stories
├── story-001-[nome].md             # Story 1
├── story-002-[nome].md             # Story 2
└── story-003-[nome].md             # Story 3
```

### Implementações e Validações

```
PRPs/bmad-output/
├── implementations/
│   ├── story-001-[projeto]-dev-notes.md    # Dev Notes
│   ├── story-002-[projeto]-dev-notes.md
│   └── story-003-[projeto]-dev-notes.md
└── qa-reports/
    ├── story-001-[projeto]-qa-report.md     # QA Reports
    ├── story-002-[projeto]-qa-report.md
    └── story-003-[projeto]-qa-report.md
```

### Logs e Monitoramento

```
PRPs/bmad-output/.workflow/
├── [projeto]-workflow-state.json           # Estado do workflow
└── handoffs/
    ├── handoff-1234567890-system-to-analyst.json
    ├── handoff-1234567891-analyst-to-pm.json
    └── handoff-1234567892-pm-to-architect.json
```

## 🤖 Sistema de Comunicação Entre Agentes

### Handoffs Automáticos

O sistema implementa **handoffs automáticos** onde cada agente:

1. **Recebe input** do agente anterior
2. **Processa** conforme sua especialização
3. **Cria output** estruturado
4. **Gera handoff** para próximo agente
5. **Atualiza estado** do workflow

### Coordenação de Agentes

```python
# Exemplo de handoff automático
handoff = {
    "from": "analyst",
    "to": "pm",
    "workflow_id": "task-manager-1234567890",
    "data": {
        "project_name": "task-manager",
        "brief_file": "PRPs/bmad-output/briefs/task-manager-brief.md"
    },
    "status": "ready"
}
```

### Monitoramento em Tempo Real

O sistema monitora:
- **Estado do workflow** (qual etapa está ativa)
- **Handoffs pendentes** (aguardando processamento)
- **Progresso de stories** (implementadas vs pendentes)
- **Logs detalhados** (para debugging)

## 📊 Monitoramento e Debugging

### Verificar Status

```bash
# Status geral do projeto
python PRPs/scripts/bmad_orchestrator.py

# Status de projeto específico
python PRPs/scripts/bmad_orchestrator.py --project meu-projeto

# Status em JSON
python PRPs/scripts/bmad_orchestrator.py --json
```

### Logs do Workflow

```bash
# Ver estado do workflow
cat PRPs/bmad-output/.workflow/[projeto]-workflow-state.json

# Ver handoffs
ls -la PRPs/bmad-output/.workflow/handoffs/

# Ver handoff específico
cat PRPs/bmad-output/.workflow/handoffs/handoff-*-analyst-to-pm.json
```

### Debugging

Se algo der errado:

1. **Verificar logs** em `PRPs/bmad-output/.workflow/`
2. **Verificar handoffs** pendentes
3. **Usar orchestrator** para diagnosticar
4. **Executar manualmente** etapa específica se necessário

## 🛠️ Scripts e Ferramentas

### Scripts Principais

- **`bmad_full_auto.py`** - Execução automática completa
- **`bmad_agent_coordinator.py`** - Sistema de coordenação entre agentes
- **`bmad_orchestrator.py`** - Monitoramento e diagnóstico
- **`bmad_demo_auto.py`** - Demonstração do sistema

### Comandos Úteis

```bash
# Demonstração do sistema
python PRPs/scripts/bmad_demo_auto.py

# Iniciar coordenador de agentes
python PRPs/scripts/bmad_agent_coordinator.py --start

# Ver workflows ativos
python PRPs/scripts/bmad_agent_coordinator.py --list

# Status de workflow específico
python PRPs/scripts/bmad_agent_coordinator.py --status workflow-id
```

## 🎯 Casos de Uso

### Ideal para Sistema Automático

✅ **Use `/bmad-auto` quando:**
- Projeto novo do zero
- Precisa de planejamento completo
- Quer execução rápida
- Projeto pequeno/médio
- Não precisa de controle granular
- Quer ver resultado final rapidamente

### Ideal para Sistema Manual

✅ **Use comandos individuais quando:**
- Feature específica
- Precisa de controle total
- Debugging detalhado
- Projeto grande/complexo
- Quer ajustar cada etapa
- Trabalhando com equipe

## 🔧 Configuração Avançada

### Personalizar Workflow

Edite `PRPs/scripts/bmad_full_auto.py` para:
- Alterar ordem dos agentes
- Modificar critérios de handoff
- Ajustar timeouts
- Customizar outputs

### Adicionar Novos Agentes

1. Criar definição em `.cursor/agents/`
2. Adicionar comando em `.cursor/commands/`
3. Atualizar `bmad_full_auto.py`
4. Testar integração

### Integração com APIs Reais

O sistema atual usa simulação. Para integração real:
1. Substituir `_simulate_agent_execution()` por chamadas reais
2. Implementar autenticação com APIs
3. Configurar webhooks para notificações
4. Adicionar retry logic robusto

## 🚀 Próximos Passos

### Melhorias Planejadas

- [ ] Integração real com APIs do Cursor
- [ ] Interface web para monitoramento
- [ ] Notificações em tempo real
- [ ] Retry logic avançado
- [ ] Métricas de performance
- [ ] Integração com CI/CD

### Contribuições

Para contribuir com o sistema automático:
1. Fork do repositório
2. Criar branch para feature
3. Implementar melhorias
4. Testar com projetos reais
5. Submeter pull request

## 📚 Referências

- **[Integração BMAD](bmad-integration.md)** - Documentação geral
- **[Guia de Agentes](PRPs/ai_docs/bmad-agents-guide.md)** - Para IAs
- **[Templates BMAD](PRPs/templates/bmad/)** - Templates dos documentos
- **[Scripts](PRPs/scripts/)** - Scripts de automação
- **[Comandos](.cursor/commands/)** - Comandos slash

---

**🤖 Sistema BMAD Full Automático**: Comunicação inteligente entre agentes para desenvolvimento ágil e eficiente!
