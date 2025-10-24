---
description: Quebra planejamento em Development Stories executáveis
tags: [bmad, development, stories, sprint]
aliases: [sm]
---

# Comando: /scrum-master (ou /sm)

## 📋 Descrição

Ativa o **Scrum Master Agent** para transformar Brief + PRD + Arquitetura em Development Stories implementáveis com contexto completo.

## 🎯 Quando Usar

Use este comando quando:
- Fase de planejamento está completa (Brief + PRD + Architecture)
- Precisar quebrar funcionalidades em tarefas implementáveis
- Quiser organizar trabalho em sprints
- Estiver pronto para começar implementação

## 💻 Como Usar

```
/scrum-master [caminho-da-arquitetura]

/sm [caminho-da-arquitetura]  # Alias curto
```

### Exemplos:

```
/sm PRPs/bmad-output/architecture/ecommerce-architecture.md

/scrum-master PRPs/bmad-output/architecture/payment-api-architecture.md

/sm  # Usa arquitetura mais recente automaticamente
```

## 🔄 Workflow

**Fase**: Desenvolvimento (1/3 - Início do desenvolvimento!)

```
Analyst → PM → Architect → [VOCÊ ESTÁ AQUI] → Dev → QA
```

### Pré-requisitos:
- Brief criado pelo Analyst
- PRD criado pelo PM
- Architecture criada pelo Architect

### Próximo Passo:
Após o Scrum Master criar as stories, use `/dev` para implementar cada uma.

## 📤 Output

O Scrum Master criará:
- **Development Stories** em `PRPs/bmad-output/stories/[projeto]/`
  - `story-001-setup-projeto.md`
  - `story-002-auth-basico.md`
  - `story-003-api-usuarios.md`
  - etc...
- **Index de Stories** em `index.md` com overview
- Stories priorizadas e sequenciadas
- Contexto completo embutido em cada story

## 🎭 O que o Scrum Master Faz

1. **Analisa** Brief, PRD e Arquitetura
2. **Identifica** épicos e features
3. **Quebra** em stories de 2-8h
4. **Prioriza** baseado em valor e dependências
5. **Sequencia** em ordem lógica de implementação
6. **Enriquece** cada story com contexto completo
7. **Documenta** critérios de aceitação
8. **Organiza** em sprints sugeridos

## ⚙️ Configuração do Agente

Este comando carrega:
- Personalidade: Scrum Master experiente
- Input: Brief + PRD + Architecture
- Template: `PRPs/templates/bmad/story-template.md`
- Output: `PRPs/bmad-output/stories/[projeto]/`
- Contexto: Todos documentos de planejamento

## 💡 Dicas

- Certifique-se que planejamento está completo
- Stories devem ter contexto auto-suficiente
- Comece com stories de fundação (setup, auth)
- Respeite dependências técnicas
- Cada story deve ser testável independentemente

## ⚠️ Importante

- Stories bem escritas economizam dias de trabalho
- Dev Agent deve ter TUDO que precisa na story
- Inclua trechos relevantes de Brief/PRD/Arch
- Forneça code skeletons para estruturas complexas
- Documente armadilhas conhecidas

## 📊 Estrutura Típica de Stories

1. **Setup & Fundação** (Stories 001-010)
   - Setup de projeto
   - Configurações
   - Database schema
   - Auth básico

2. **Features Core** (Stories 011-030)
   - Funcionalidades P0 do MVP
   - APIs principais
   - UI base

3. **Features Secundárias** (Stories 031-050)
   - Funcionalidades P1
   - Integrações
   - Refinamentos

4. **Polish & Optimization** (Stories 051+)
   - UI/UX improvements
   - Performance
   - Bug fixes

## 🎉 Marco Importante

Criar as stories significa que **desenvolvimento pode começar**!

Workflow de desenvolvimento:
1. `/sm` - Cria todas as stories (VOCÊ ESTÁ AQUI)
2. `/dev story-001` - Dev implementa story
3. `/qa story-001` - QA valida story
4. Repita para próxima story

## 📚 Referências

- Agente: `.cursor/agents/scrum-master.md`
- Template: `PRPs/templates/bmad/story-template.md`
- Guia: `docs/bmad-integration.md`

---

**Workflow BMAD**: Com stories criadas, o Dev Agent pode começar implementação incrementalmente, uma story por vez!

