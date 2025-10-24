# QA Report: Story #[número] - [Título]

**QA Engineer:** [Nome ou QA Agent]
**Data:** [YYYY-MM-DD]
**Story:** `PRPs/bmad-output/stories/[projeto]/story-[número].md`
**Dev Notes:** `PRPs/bmad-output/implementations/story-[número]-dev-notes.md`
**Build/Commit:** [hash ou versão testada]

**Status Final:** ✅ APROVADA / ⚠️ APROVADA com Ressalvas / ❌ REPROVADA

---

## 📋 Resumo Executivo

[Parágrafo resumindo o estado geral da implementação, qualidade do código, e se atende os requisitos]

**Decisão:**
[Explicação clara da decisão de aprovar/reprovar e principais motivos]

---

## ✅ Validação de Critérios de Aceitação

### CA1: [Descrição do Critério]
**Status:** ✅ Passou / ❌ Falhou

**Como foi testado:**
1. [Passo 1 do teste]
2. [Passo 2 do teste]
3. [Passo 3 do teste]

**Resultado Obtido:**
[O que aconteceu durante o teste]

**Resultado Esperado:**
[O que deveria ter acontecido]

**Evidência:**
[Screenshot, log, ou descrição da evidência]

**Notas:**
[Observações adicionais se houver]

---

### CA2: [Descrição do Critério]
**Status:** ✅ Passou

[...]

---

### CA3: [Descrição do Critério]
**Status:** ❌ Falhou

[... detalhes do falha]

---

## 🧪 Testes Automatizados

### Testes Unitários
- **Arquivo:** `tests/unit/feature.test.ts`
- **Total de testes:** 12
- **Passando:** 12 ✅
- **Falhando:** 0
- **Cobertura:** 87% ✅
- **Alvo:** > 80%
- **Status Geral:** ✅ Adequado

**Observações:**
[Comentários sobre qualidade dos testes, se aplicável]

### Testes de Integração
- **Arquivo:** `tests/integration/flow.test.ts`
- **Total de testes:** 3
- **Passando:** 3 ✅
- **Falhando:** 0
- **Status Geral:** ✅ Adequado

### Linter & Type-Check
- **Linter:** ✅ 0 errors, 0 warnings
- **Type-check:** ✅ Passou sem erros
- **Build:** ✅ Sucesso

---

## 🔍 Revisão de Código

### Qualidade Geral
| Aspecto | Avaliação | Nota |
|---------|-----------|------|
| Legibilidade | ✅ Boa / ⚠️ Regular / ❌ Ruim | [Comentário] |
| Manutenibilidade | ✅ Boa / ⚠️ Regular / ❌ Ruim | [Comentário] |
| Seguiu Padrões | ✅ Sim / ⚠️ Parcial / ❌ Não | [Comentário] |
| Documentação | ✅ Adequada / ⚠️ Insuficiente / ❌ Ausente | [Comentário] |
| Complexidade | ✅ Baixa / ⚠️ Média / ❌ Alta | [Comentário] |
| Duplicação | ✅ Mínima / ⚠️ Alguma / ❌ Muita | [Comentário] |

### ✅ Pontos Positivos
- [Aspecto bem implementado 1]
- [Código limpo e bem estruturado]
- [Bom tratamento de erros]
- [Testes abrangentes]

### 💡 Áreas de Melhoria (Não-bloqueantes)
- [Sugestão de melhoria 1]
- [Sugestão de melhoria 2]

### ⚠️ Code Smells (se houver)
- [Code smell identificado] - **Severidade:** Baixa/Média/Alta
  - **Localização:** [Arquivo:linha]
  - **Sugestão:** [Como melhorar]

---

## 🧪 Testes Funcionais Manuais

### Caso de Teste 1: [Nome do Caso]
**Objetivo:** [O que está sendo testado]

**Pré-condições:**
- [Pré-condição 1]
- [Pré-condição 2]

**Passos:**
1. [Passo 1]
2. [Passo 2]
3. [Passo 3]

**Resultado Esperado:**
[O que deveria acontecer]

**Resultado Obtido:**
[O que realmente aconteceu]

**Status:** ✅ Passou / ❌ Falhou

**Evidência:**
[Screenshot, log, ou descrição]

---

### Caso de Teste 2: Teste de Erro
[...]

---

### Caso de Teste 3: Edge Case
[...]

---

## 🔒 Validação de Segurança

### Validação de Inputs
- **Status:** ✅ Adequado / ⚠️ Parcial / ❌ Insuficiente
- **Detalhes:**
  - [x] Inputs são validados no backend
  - [x] Inputs são sanitizados
  - [x] Tipos são verificados
  - [Observação se houver]

### Autenticação/Autorização
- **Status:** ✅ OK / ⚠️ Revisar / ❌ Problema / N/A
- **Detalhes:** [Específicos da implementação]

### Proteções Implementadas
- [x] **SQL Injection:** Protegido (prepared statements/ORM)
- [x] **XSS:** Protegido (sanitização)
- [ ] **CSRF:** N/A para esta story
- [x] **Rate Limiting:** Implementado onde necessário

### Dados Sensíveis
- **Status:** ✅ Protegidos adequadamente
- **Detalhes:** [Como dados sensíveis são tratados]

---

## ⚡ Validação de Performance

### Tempo de Resposta
| Endpoint/Função | Tempo Medido | Expectativa | Status |
|-----------------|--------------|-------------|--------|
| [Nome] | [Xms] | < [Yms] | ✅ OK / ❌ Lento |
| [Nome] | [Xms] | < [Yms] | ✅ OK |

### Otimizações
- **Database Queries:** ✅ Eficientes / ⚠️ Melhoráveis / ❌ Problema
  - [Comentário sobre queries]
- **N+1 Queries:** ✅ Não detectado / ❌ Encontrado
- **Caching:** ✅ Implementado / N/A
- **Lazy Loading:** ✅ Implementado / N/A

### Observações de Performance
[Comentários adicionais sobre performance]

---

## 🐛 Bugs Encontrados

### Bug #1 - [Severidade: CRÍTICA / ALTA / MÉDIA / BAIXA]
**Título:** [Descrição curta do bug]

**Descrição Detalhada:**
[O que está errado]

**Passos para Reproduzir:**
1. [Passo 1]
2. [Passo 2]
3. [Bug ocorre]

**Resultado Esperado:**
[O que deveria acontecer]

**Resultado Atual:**
[O que acontece]

**Evidência:**
```
[Log de erro, screenshot, ou descrição detalhada]
```

**Bloqueante:** ✅ Sim / ❌ Não
**Impacto:** [Descrição do impacto]

---

### Bug #2 - [Severidade]
[...]

---

## ⚠️ Ressalvas e Observações

### Ressalva 1: [Título]
**Descrição:** [O que foi observado]
**Bloqueante:** ❌ Não
**Recomendação:** [O que fazer]

### Ressalva 2: [Título]
[...]

---

## 💡 Recomendações

### Para Esta Story
1. [Recomendação de melhoria 1]
2. [Recomendação de melhoria 2]

### Para Próximas Stories
1. [Padrão a seguir que funcionou bem]
2. [Sugestão para evitar problemas futuros]

### Débito Técnico Identificado
- [Item de débito técnico] - **Prioridade:** [Baixa/Média/Alta]

---

## 📊 Checklist Final

### Funcionalidade
- [x] Todos critérios de aceitação atendidos
- [x] Casos felizes funcionando
- [x] Casos de erro tratados adequadamente
- [x] Edge cases considerados e testados

### Código
- [x] Segue padrões do projeto
- [x] Código legível e bem estruturado
- [x] Sem code smells graves
- [x] Documentação inline adequada
- [x] Sem código duplicado excessivo

### Testes
- [x] Testes unitários adequados
- [x] Cobertura > 80%
- [x] Testes de integração (quando aplicável)
- [x] Todos testes passando
- [x] Testes bem escritos e manuteníveis

### Qualidade
- [x] Linter: 0 errors
- [x] Type-check: Passou
- [x] Build: Sucesso
- [x] Performance aceitável
- [x] Sem memory leaks

### Segurança
- [x] Inputs validados e sanitizados
- [x] Proteções básicas implementadas
- [x] Dados sensíveis protegidos (se aplicável)
- [x] Autenticação/Autorização OK (se aplicável)

### UX/Usabilidade (se aplicável)
- [ ] Interface intuitiva
- [ ] Feedback visual adequado
- [ ] Mensagens de erro claras
- [ ] Loading states implementados
- [ ] Responsive (mobile, tablet, desktop)

---

## 🎯 Decisão Final

**Status:** ✅ APROVADA / ⚠️ APROVADA com Ressalvas / ❌ REPROVADA

### Justificativa
[Explicação detalhada da decisão]

### Se APROVADA:
✅ Story está completa e pronta para produção

**Próximo Passo:**
- Story #[número+1]: [título] ou
- Deploy para [ambiente]

### Se APROVADA com Ressalvas:
⚠️ Story funciona mas há melhorias não-bloqueantes sugeridas

**Débitos Técnicos Criados:**
- [Link para débito técnico 1]
- [Link para débito técnico 2]

**Próximo Passo:**
- Story #[número+1]: [título]

### Se REPROVADA:
❌ Bugs bloqueantes impedem aprovação

**Bugs Bloqueantes:**
1. [Bug #X - Descrição]
2. [Bug #Y - Descrição]

**Próximo Passo:**
- Dev deve corrigir bugs listados
- Após correção, executar `/qa story-[número]` novamente

---

## 📝 Histórico de Testes

| Data | QA | Status | Bugs Encontrados | Notas |
|------|----|----|------------------|-------|
| [Data 1] | [Nome] | ❌ Reprovada | 2 críticos | [Nota] |
| [Data 2] | [Nome] | ✅ Aprovada | 0 | Bugs corrigidos |

---

## 📎 Anexos

### Screenshots
[Links ou referências para screenshots relevantes]

### Logs
```
[Logs importantes capturados durante teste]
```

### Metrics/Performance Data
[Dados de performance se relevantes]

---

**Template Version:** 1.0
**Assinatura QA:** [Nome] - [Data]
**Aprovado para:** [Produção / Próxima Story]

