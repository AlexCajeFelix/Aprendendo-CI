---
description: Valida qualidade de implementação de story
tags: [bmad, qa, testing, validation, quality]
---

# Comando: /qa

## 📋 Descrição

Ativa o **QA Agent** para realizar validação completa de qualidade em uma implementação, testando funcionalidade, código, performance e segurança.

## 🎯 Quando Usar

Use este comando quando:
- Dev Agent completou implementação de uma story
- Todos testes automatizados estão passando
- Dev notes foram criadas
- Story está pronta para validação final

## 💻 Como Usar

```
/qa [caminho-da-story ou número]
```

### Exemplos:

```
/qa PRPs/bmad-output/stories/ecommerce/story-001-setup.md

/qa story-015

/qa 015  # Apenas número
```

## 🔄 Workflow

**Fase**: Desenvolvimento (3/3 - Última etapa!)

```
Analyst → PM → Architect → Scrum Master → Dev → [VOCÊ ESTÁ AQUI]
```

### Pré-requisitos:
- Story implementada pelo Dev Agent
- Dev notes criadas
- Testes automatizados passando
- Build sucesso

### Próximo Passo:
Após QA aprovar, story está completa! Próxima story ou deploy se todas completas.

## 📤 Output

O QA criará:
- **QA Report** em `PRPs/bmad-output/qa-reports/story-[número]-qa-report.md`
- Status: ✅ Aprovada / ⚠️ Ressalvas / ❌ Reprovada
- Lista de bugs encontrados (se houver)
- Sugestões de melhoria
- Validação completa de critérios

## 🎭 O que o QA Faz

1. **Revisa** story e dev notes
2. **Executa** testes automatizados
3. **Revisa** código (qualidade, padrões, segurança)
4. **Testa** funcionalidade manualmente
5. **Valida** cada critério de aceitação
6. **Verifica** performance e segurança
7. **Documenta** achados em report
8. **Decide**: Aprovar, Aprovar com Ressalvas, ou Reprovar

## ⚙️ Configuração do Agente

Este comando carrega:
- Personalidade: QA Engineer Senior
- Input: Story + Dev Notes
- Template: `PRPs/templates/bmad/qa-report-template.md`
- Output: `PRPs/bmad-output/qa-reports/`
- Contexto: Story + implementação + testes

## 💡 Dicas

- QA testa o que Dev implementou contra a story
- Critérios de aceitação são obrigatórios
- Bugs críticos são bloqueantes
- Sugestões não-bloqueantes são bem-vindas
- Foque em qualidade, não perfeccionismo

## 🎯 O que QA Valida

### Funcionalidade
- ✅ Todos critérios de aceitação
- ✅ Casos felizes funcionando
- ✅ Casos de erro tratados
- ✅ Edge cases considerados

### Código
- ✅ Padrões do projeto seguidos
- ✅ Legibilidade e manutenibilidade
- ✅ Sem code smells graves
- ✅ Documentação adequada

### Testes
- ✅ Unitários adequados (>80%)
- ✅ Integração quando aplicável
- ✅ Todos passando
- ✅ Qualidade dos testes

### Qualidade Geral
- ✅ Linter e type-check passando
- ✅ Build sucesso
- ✅ Performance aceitável
- ✅ Segurança básica

## 📊 Possíveis Resultados

### ✅ APROVADA
```
✅ Story #[número] APROVADA!

📄 QA Report: PRPs/bmad-output/qa-reports/story-[número]-qa-report.md

🎉 Story completa e pronta para deploy!

📊 Resumo:
- Critérios: ✅ Todos atendidos
- Testes: ✅ Passando
- Código: ✅ Qualidade adequada
- Performance: ✅ Dentro do esperado

➡️ Próximo: Story #[X] ou Deploy
```

### ⚠️ APROVADA com Ressalvas
```
⚠️ Story #[número] APROVADA com ressalvas

📄 QA Report: PRPs/bmad-output/qa-reports/story-[número]-qa-report.md

✅ Funcionalidade OK, mas melhorias sugeridas

📊 Resumo:
- Funcionalidade: ✅ OK
- Sugestões: 3 melhorias não-bloqueantes
- Débito Técnico: Documentado

➡️ Próximo: Story #[X] (ressalvas não bloqueiam)
```

### ❌ REPROVADA
```
❌ Story #[número] REPROVADA

📄 QA Report: PRPs/bmad-output/qa-reports/story-[número]-qa-report.md

🐛 Bugs bloqueantes encontrados: 2

Bugs:
1. [CRÍTICO] - [Descrição]
2. [ALTO] - [Descrição]

➡️ Próximo: Dev precisa corrigir bugs, depois re-teste com `/qa`
```

## ⚠️ Importante

- QA não altera código - apenas valida
- QA pode reprovar se bugs críticos
- Melhorias não-bloqueantes não reprovam
- QA documenta tudo no report
- Decisões baseadas em critérios objetivos

## 🔄 Ciclo de Correção

Se reprovada:
1. Dev lê QA report
2. Dev corrige bugs
3. Dev atualiza dev notes
4. QA re-testa com `/qa` novamente
5. Repete até aprovar

## 📚 Referências

- Agente: `.cursor/agents/qa.md`
- Template: `PRPs/templates/bmad/qa-report-template.md`
- Guia: `docs/bmad-integration.md`

---

**Workflow BMAD**: QA é o checkpoint final. Story aprovada = story completa e pronta para deploy!

