---
description: Define arquitetura técnica do sistema
tags: [bmad, planning, architecture, technical]
---

# Comando: /architect

## 📋 Descrição

Ativa o **Architect Agent** para desenhar a arquitetura técnica completa do sistema, definindo COMO o produto será construído.

## 🎯 Quando Usar

Use este comando quando:
- Já tiver Brief (Analyst) e PRD (PM) criados
- Precisar definir stack tecnológico e arquitetura
- Quiser documentar decisões técnicas importantes
- Precisar de blueprint técnico antes do desenvolvimento

## 💻 Como Usar

```
/architect [caminho-do-prd]
```

### Exemplos:

```
/architect PRPs/bmad-output/prds/ecommerce-prd.md

/architect PRPs/bmad-output/prds/payment-api-prd.md

/architect  # Usa PRD mais recente automaticamente
```

## 🔄 Workflow

**Fase**: Planejamento (3/3 - Última etapa de planejamento!)

```
Analyst → PM → [VOCÊ ESTÁ AQUI] → Scrum Master → Dev → QA
```

### Pré-requisitos:
- Brief criado pelo Analyst
- PRD criado pelo PM

### Próximo Passo:
Após o Architect criar o documento de arquitetura, a **fase de planejamento está completa**! Use `/scrum-master` para começar a fase de desenvolvimento.

## 📤 Output

O Architect criará:
- **Documento de Arquitetura** em `PRPs/bmad-output/architecture/[projeto]-architecture.md`
- Decisões de arquitetura justificadas
- Stack tecnológico definido
- Design de componentes e camadas
- Estratégias de segurança, performance e escalabilidade
- Modelo de dados e fluxos

## 🎭 O que o Architect Faz

1. **Analisa** Brief e PRD para requisitos técnicos
2. **Define** arquitetura geral (monolito, microserviços, etc)
3. **Escolhe** stack tecnológico apropriado
4. **Desenha** componentes e suas interações
5. **Especifica** segurança, performance, escalabilidade
6. **Documenta** padrões e convenções de código
7. **Planeja** infraestrutura e DevOps
8. **Identifica** riscos arquiteturais

## ⚙️ Configuração do Agente

Este comando carrega:
- Personalidade: Arquiteto de Software Senior
- Input: Brief + PRD
- Template: `PRPs/templates/bmad/architecture-template.md`
- Output: `PRPs/bmad-output/architecture/`
- Contexto: Documentação técnica do projeto

## 💡 Dicas

- Revise Brief e PRD antes de começar
- Justifique escolhas tecnológicas importantes
- Documente trade-offs claramente
- Pense em evolução e escalabilidade
- Inclua diagramas (mesmo em texto)
- Especifique versões exatas de tecnologias
- Considere expertise do time

## ⚠️ Importante

- Arquitetura deve atender requisitos não-funcionais do Brief
- Escolhas devem ser justificadas, não arbitrárias
- Documente PORQUÊ de cada decisão importante
- Considere manutenibilidade a longo prazo
- Não sobre-engenharia - mantenha simples quando possível

## 🎉 Marco Importante

Completar a arquitetura significa que o **planejamento está finalizado**!

Você terá:
✅ Brief (Análise de requisitos)
✅ PRD (Especificação do produto)
✅ Architecture (Design técnico)

Próximo: Partir para implementação com `/scrum-master`

## 📚 Referências

- Agente: `.cursor/agents/architect.md`
- Template: `PRPs/templates/bmad/architecture-template.md`
- Guia: `docs/bmad-integration.md`

---

**Workflow BMAD**: Este é o último passo do planejamento. Com Brief + PRD + Arquitetura completos, o Scrum Master pode criar stories implementáveis!

