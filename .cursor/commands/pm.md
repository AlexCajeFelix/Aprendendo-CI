---
description: Cria Product Requirement Document (PRD) detalhado
tags: [bmad, planning, prd, product]
---

# Comando: /pm

## 📋 Descrição

Ativa o **PM Agent** (Product Manager) para transformar o Brief em um PRD (Product Requirement Document) detalhado com especificações funcionais completas.

## 🎯 Quando Usar

Use este comando quando:
- Já tiver um Brief criado pelo Analyst
- Precisar especificar EXATAMENTE o que será construído
- Quiser definir MVP e roadmap
- Precisar criar user stories e critérios de aceitação

## 💻 Como Usar

```
/pm [caminho-do-brief]
```

### Exemplos:

```
/pm PRPs/bmad-output/briefs/ecommerce-brief.md

/pm PRPs/bmad-output/briefs/payment-api-brief.md

/pm  # Usa o Brief mais recente automaticamente
```

## 🔄 Workflow

**Fase**: Planejamento (2/3)

```
Analyst → [VOCÊ ESTÁ AQUI] → Architect → Scrum Master → Dev → QA
```

### Pré-requisito:
Brief criado pelo Analyst em `PRPs/bmad-output/briefs/`

### Próximo Passo:
Após o PM criar o PRD, use `/architect` para definir a arquitetura técnica.

## 📤 Output

O PM criará:
- **PRD completo** em `PRPs/bmad-output/prds/[projeto]-prd.md`
- Especificações funcionais detalhadas
- User stories com critérios de aceitação
- Roadmap e priorização (MVP, Phase 2, etc)
- Critérios de sucesso mensuráveis

## 🎭 O que o PM Faz

1. **Analisa** o Brief do Analyst
2. **Define** visão e escopo do produto
3. **Especifica** cada funcionalidade com detalhes
4. **Cria** user stories e critérios de aceitação
5. **Prioriza** features (MVP vs future)
6. **Documenta** fluxos de usuário
7. **Define** métricas de sucesso

## ⚙️ Configuração do Agente

Este comando carrega:
- Personalidade: Product Manager experiente
- Input: Brief do Analyst
- Template: `PRPs/templates/bmad/prd-template.md`
- Output: `PRPs/bmad-output/prds/`
- Contexto: Brief + documentação do projeto

## 💡 Dicas

- Certifique-se que o Brief está completo antes de começar
- Seja específico em critérios de aceitação
- Pense no usuário final em cada feature
- Defina claramente o que é MVP
- Documente o que está fora do escopo
- Use exemplos concretos sempre que possível

## ⚠️ Importante

- O PM NÃO define implementação técnica (isso é do Architect)
- O PRD foca no QUE será construído, não no COMO
- Critérios de aceitação devem ser testáveis pelo QA
- Cada feature deve ter valor claro para o usuário

## 📚 Referências

- Agente: `.cursor/agents/pm.md`
- Template: `PRPs/templates/bmad/prd-template.md`
- Guia: `docs/bmad-integration.md`

---

**Workflow BMAD**: O PRD é a especificação definitiva do produto. O Architect usará isso para definir a arquitetura técnica.

