---
description: Executa workflow BMAD completo automaticamente com comunicação entre agentes
tags: [bmad, auto, workflow, full, agents]
---

# Comando: /bmad-auto

## 📋 Descrição

Executa o **workflow BMAD completo automaticamente** onde os 6 agentes se comunicam entre si, passando contexto e executando próximas etapas sem intervenção manual.

## 🎯 Quando Usar

Use este comando quando:
- Quiser executar todo o workflow BMAD de uma vez
- Precisar de projeto completo do zero
- Quiser que agentes se comuniquem automaticamente
- Preferir automação total vs execução manual

## 💻 Como Usar

```
/bmad-auto [descrição-do-projeto]
```

### Exemplos:

```
/bmad-auto Sistema de gerenciamento de tarefas pessoais

/bmad-auto API REST para e-commerce com autenticação

/bmad-auto Dashboard de métricas em tempo real
```

## 🔄 Workflow Automático

**O comando executa automaticamente:**

### Fase 1: Planejamento (Sequencial)
```
1. 🤖 Analyst analisa requisitos → cria Brief
2. 🤖 PM lê Brief → cria PRD  
3. 🤖 Architect lê PRD → define Arquitetura
```

### Fase 2: Desenvolvimento (Iterativo)
```
4. 🤖 Scrum Master lê tudo → cria Development Stories
5. 🤖 Loop automático:
   - Dev implementa story
   - QA valida story
   - Próxima story...
```

## 📤 Output

O sistema cria automaticamente:

**Documentos de Planejamento:**
- `PRPs/bmad-output/briefs/[projeto]-brief.md`
- `PRPs/bmad-output/prds/[projeto]-prd.md`
- `PRPs/bmad-output/architecture/[projeto]-architecture.md`

**Development Stories:**
- `PRPs/bmad-output/stories/[projeto]/index.md`
- `PRPs/bmad-output/stories/[projeto]/story-001-*.md`
- `PRPs/bmad-output/stories/[projeto]/story-002-*.md`
- etc...

**Implementações:**
- `PRPs/bmad-output/implementations/story-*-dev-notes.md`
- `PRPs/bmad-output/qa-reports/story-*-qa-report.md`

**Logs do Workflow:**
- `PRPs/bmad-output/.workflow/[projeto]-workflow-state.json`
- `PRPs/bmad-output/.workflow/handoffs/handoff-*.json`

## 🎭 O que Acontece Automaticamente

1. **Analyst** recebe descrição e cria Brief completo
2. **PM** lê Brief e cria PRD detalhado
3. **Architect** lê PRD e define arquitetura técnica
4. **Scrum Master** lê tudo e cria stories implementáveis
5. **Dev** implementa cada story com código e testes
6. **QA** valida cada implementação
7. **Sistema** coordena comunicação entre agentes

## ⚙️ Configuração do Agente

Este comando usa:
- **Script**: `PRPs/scripts/bmad_full_auto.py`
- **Coordenação**: Sistema de handoff entre agentes
- **Monitoramento**: Estado do workflow em tempo real
- **Output**: Estrutura completa de documentos

## 💡 Vantagens do Modo Automático

### ✅ Benefícios
- **Zero intervenção manual** - Tudo executado automaticamente
- **Comunicação entre agentes** - Contexto passado automaticamente
- **Workflow completo** - Do Brief até código implementado
- **Logs detalhados** - Rastreabilidade completa
- **Estado persistente** - Pode ser pausado e retomado

### ⚠️ Considerações
- **Tempo**: Workflow completo pode levar tempo
- **Debugging**: Mais complexo debugar se algo der errado
- **Flexibilidade**: Menos controle sobre cada etapa individual

## 🎨 Comparação: Manual vs Automático

| Aspecto | Manual (`/analyst` → `/pm` → ...) | Automático (`/bmad-auto`) |
|---------|-----------------------------------|---------------------------|
| **Controle** | Total controle sobre cada etapa | Execução automática |
| **Tempo** | Mais lento (pausas manuais) | Mais rápido (contínuo) |
| **Debugging** | Fácil debugar cada etapa | Logs para debugging |
| **Flexibilidade** | Pode parar e ajustar | Executa até o final |
| **Comunicação** | Manual entre agentes | Automática entre agentes |

## 🔧 Opções Avançadas

### Modo Silencioso (Sem Pausas)
```bash
# Via script direto (sem comando Cursor):
python PRPs/scripts/bmad_full_auto.py "Meu projeto" --auto-approve
```

### Verificar Estado do Workflow
```bash
python PRPs/scripts/bmad_orchestrator.py --project meu-projeto
```

### Workflow Personalizado
Edite `PRPs/scripts/bmad_full_auto.py` para customizar:
- Ordem dos agentes
- Critérios de handoff
- Validações entre etapas

## 📊 Exemplo de Execução

```
🤖 BMAD Full Automático - Iniciando Workflow
============================================================
📁 Projeto: task-manager
📝 Descrição: Sistema de gerenciamento de tarefas pessoais
⏰ Iniciado em: 14:30:15

📋 FASE 1: PLANEJAMENTO
------------------------------------------------------------
🔄 Executando ANALYST...
   ✅ ANALYST concluído. Pressione Enter para continuar...
   📄 Output: PRPs/bmad-output/briefs/task-manager-brief.md

🔄 Executando PM...
   ✅ PM concluído. Pressione Enter para continuar...
   📄 Output: PRPs/bmad-output/prds/task-manager-prd.md

🔄 Executando ARCHITECT...
   ✅ ARCHITECT concluído. Pressione Enter para continuar...
   📄 Output: PRPs/bmad-output/architecture/task-manager-architecture.md

✅ Planejamento Completo!

💻 FASE 2: DESENVOLVIMENTO
------------------------------------------------------------
🔄 Executando SCRUM-MASTER...
   ✅ SCRUM-MASTER concluído. Pressione Enter para continuar...
   📄 Output: PRPs/bmad-output/stories/task-manager/index.md

📝 Encontradas 3 stories
🔄 Processando Story 1/3: story-001-exemplo.md
   💻 Dev implementando...
   ✅ QA validando...
   ✅ Story 1 completa. Pressione Enter para próxima...

🎉 WORKFLOW BMAD COMPLETO!
============================================================
📁 Projeto: task-manager
⏰ Concluído em: 14:35:22
📊 Etapas completadas: 4
```

## 🚀 Próximos Passos

Após execução completa:
1. **Revisar outputs** gerados em `PRPs/bmad-output/`
2. **Testar implementação** se código foi gerado
3. **Usar orchestrator** para verificar status
4. **Iterar** se necessário com workflow manual

## 🤝 Modo Colaborativo (Alternativa)

Para **revisão entre agentes** e **aprovação do usuário**:

```bash
/bmad-auto-collab "Descrição do projeto"
```

**Diferenças**:
- ✅ Todos os agentes revisam cada etapa
- ✅ Usuário aprova cada decisão
- ✅ Múltiplas iterações com feedback
- ✅ Implementação REAL de código
- ⚠️ Mais lento (requer interação)

📖 [Documentação Completa do Modo Colaborativo](docs/bmad-collaborative-mode.md)

## 📚 Referências

- **Script**: `PRPs/scripts/bmad_full_auto.py`
- **Orchestrator**: `PRPs/scripts/bmad_orchestrator.py`
- **Documentação**: `docs/bmad-integration.md`
- **Handoffs**: `PRPs/bmad-output/.workflow/handoffs/`

---

**🚀 Workflow BMAD Automático**: Do Brief até código implementado, sem intervenção manual!

