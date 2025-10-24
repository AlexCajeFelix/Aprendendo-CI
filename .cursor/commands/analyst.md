---
description: Inicia análise de requisitos e cria Brief de projeto
tags: [bmad, planning, analysis]
---

# Comando: /analyst

## 📋 Descrição

Ativa o **Analyst Agent** para conduzir uma análise profunda de requisitos e criar um Brief de projeto estruturado.

## 🎯 Quando Usar

Use este comando quando:
- Estiver iniciando um novo projeto
- Precisar documentar requisitos de forma estruturada
- Quiser entender melhor o problema antes de definir soluções
- Precisar de um Brief para passar ao PM

## 💻 Como Usar

```
/analyst [descrição-breve-do-projeto]
```

### Exemplos:

```
/analyst Sistema de gerenciamento de pedidos para e-commerce

/analyst API REST para integração com gateway de pagamento

/analyst Dashboard analytics em tempo real com React
```

## 🔄 Workflow

**Fase**: Planejamento (1/3)

```
[VOCÊ ESTÁ AQUI] → PM → Architect → Scrum Master → Dev → QA
```

### Próximo Passo:
Após o Analyst criar o Brief, use `/pm` para gerar o PRD.

## 📤 Output

O Analyst criará:
- **Brief completo** em `PRPs/bmad-output/briefs/[projeto]-brief.md`
- Análise de requisitos funcionais e não-funcionais
- Identificação de riscos e dependências
- Casos de uso principais

## 🎭 O que o Analyst Faz

1. **Faz perguntas** para entender o contexto completo
2. **Investiga** requisitos funcionais e não-funcionais
3. **Identifica** stakeholders e usuários
4. **Documenta** restrições e limitações
5. **Captura** riscos e dependências
6. **Cria** Brief estruturado

## ⚙️ Configuração do Agente

Este comando carrega:
- Personalidade: Analista investigativo e metódico
- Template: `PRPs/templates/bmad/brief-template.md`
- Output: `PRPs/bmad-output/briefs/`
- Contexto: Arquivos de referência do projeto

## 💡 Dicas

- Seja específico na descrição inicial
- Responda às perguntas do Analyst com detalhes
- Mencione integrações e sistemas existentes
- Informe restrições conhecidas desde o início
- O Brief é a fundação - invista tempo aqui!

## 📚 Referências

- Agente: `.cursor/agents/analyst.md`
- Template: `PRPs/templates/bmad/brief-template.md`
- Guia: `docs/bmad-integration.md`

---

**Workflow BMAD**: Este é o primeiro passo do processo de planejamento. O Brief alimentará o PM e o Architect nas próximas etapas.

