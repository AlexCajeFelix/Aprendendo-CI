# Dev Notes: Story #[número] - [Título]

**Dev:** [Nome ou Dev Agent]
**Data:** [YYYY-MM-DD]
**Status:** ✅ Completa / ⚠️ Parcial / ❌ Bloqueada
**Tempo Real:** [Xh] (Estimado: [Yh])

---

## ✅ O que Foi Implementado

### Arquivos Criados
- `src/path/file1.ts` - [Descrição breve do que este arquivo faz]
- `src/path/file2.tsx` - [Descrição breve do que este arquivo faz]
- `tests/unit/file1.test.ts` - [Testes unitários]

### Arquivos Modificados
- `src/path/existing-file.ts` - [O que mudou e por quê]
- `src/config/routes.ts` - [Adicionado rota para nova feature]

### Funcionalidades Implementadas
- [x] [Funcionalidade 1 conforme story]
- [x] [Funcionalidade 2 conforme story]
- [x] [Funcionalidade 3 conforme story]

### Pacotes Adicionados (se aplicável)
```json
{
  "dependencies": {
    "[package-name]": "^X.Y.Z" // [Por que foi adicionado]
  },
  "devDependencies": {
    "[package-name]": "^X.Y.Z" // [Por que foi adicionado]
  }
}
```

---

## 🧪 Testes Implementados

### Testes Unitários
**Arquivo:** `tests/unit/feature.test.ts`
- **Total de testes:** 12
- **Todos passando:** ✅ Sim
- **Cobertura:** 87%

**Casos testados:**
- [x] Happy path - [descrição]
- [x] Error case - [descrição]
- [x] Edge case - [descrição]

### Testes de Integração
**Arquivo:** `tests/integration/flow.test.ts`
- **Total de testes:** 3
- **Todos passando:** ✅ Sim

**Fluxos testados:**
- [x] [Fluxo end-to-end 1]
- [x] [Fluxo com erro]

---

## ✅ Validação de Critérios de Aceitação

### CA1: [Descrição do critério]
- **Status:** ✅ Validado
- **Como validei:** [Descrição de como testou]
- **Resultado:** [Conforme esperado]

### CA2: [Descrição do critério]
- **Status:** ✅ Validado
- **Como validei:** [Descrição de como testou]
- **Resultado:** [Conforme esperado]

### CA3: [Descrição do critério]
- **Status:** ✅ Validado
- **Como validei:** [Descrição de como testou]
- **Resultado:** [Conforme esperado]

---

## 🔧 Decisões de Implementação

### Decisão 1: [Título da decisão]
**Contexto:**
[Por que uma decisão foi necessária]

**Problema:**
[Qual era o desafio ou escolha a ser feita]

**Solução Implementada:**
[O que foi decidido e implementado]

**Alternativas Consideradas:**
1. [Alternativa 1] - [Por que foi descartada]
2. [Alternativa 2] - [Por que foi descartada]

**Justificativa:**
[Por que esta foi a melhor escolha]

### Decisão 2: [Título da decisão]
[...]

---

## ⚠️ Desvios da Story

> Se houve qualquer desvio da story original, documente aqui

### Desvio 1: [Descrição]
**Original na Story:**
[O que estava especificado]

**Implementado:**
[O que foi feito de diferente]

**Motivo:**
[Por que foi necessário desviar]

**Impacto:**
[Qual o impacto desta mudança]

**Aprovado por:**
[Se foi discutido/aprovado]

---

## 📝 Notas de Implementação

### 💡 Aprendizados
- [Algo que aprendi durante implementação]
- [Insight útil para próximas stories]

### ⚠️ IMPORTANTE - Para Próximos Devs
- **CRITICAL**: [Informação crítica que próximos devs precisam saber]
- **IMPORTANT**: [Consideração importante]
- **TIP**: [Dica útil]

### 🐛 Gotchas Encontrados
- [Armadilha que encontrei e como resolvi]
- [Comportamento não-óbvio que descobri]

### 🔧 Configurações Adicionadas
```javascript
// Exemplo de configuração que foi necessária
export const config = {
  // ...
};
```

---

## 🚧 Débito Técnico / TODOs

> Itens que não são bloqueantes mas deveriam ser melhorados no futuro

- [ ] **[Prioridade]**: [Descrição do débito técnico]
  - **Razão**: [Por que ficou pendente]
  - **Impacto**: [Baixo/Médio/Alto]
  - **Sugestão**: [Como resolver]

- [ ] **[Prioridade]**: [Outro item]
  - [...]

---

## 🔄 Validações Executadas

### Linting
```bash
npm run lint
```
**Resultado:** ✅ 0 errors, 0 warnings

### Type Checking
```bash
npm run type-check
```
**Resultado:** ✅ Passou sem erros

### Testes Unitários
```bash
npm run test:unit
```
**Resultado:** ✅ 12/12 testes passando

### Testes de Integração
```bash
npm run test:integration
```
**Resultado:** ✅ 3/3 testes passando

### Build
```bash
npm run build
```
**Resultado:** ✅ Build concluído com sucesso

### Teste Manual
**Cenário:** [O que testou manualmente]
**Resultado:** ✅ Funcionando conforme esperado

---

## 📊 Métricas de Código

### Complexidade
- **Ciclomática média:** [X] (alvo: < 10)
- **Funções > 50 linhas:** [X] (alvo: 0)

### Cobertura de Testes
- **Statements:** 87%
- **Branches:** 82%
- **Functions:** 90%
- **Lines:** 86%
- **Alvo:** > 80% ✅

### Performance (se aplicável)
- **Tempo de resposta:** [Xms]
- **Dentro do esperado:** ✅ Sim

---

## 🔗 Próximos Passos

### Para QA
Story está pronta para validação. Use:
```bash
/qa story-[número]
```

**Checklist pré-QA:**
- [x] Todos critérios de aceitação implementados
- [x] Testes passando
- [x] Linter e type-check ok
- [x] Build sucesso
- [x] Teste manual OK
- [x] Dev notes completas

### Próxima Story
- **Story #[número+1]**: [título]
- **Depende desta:** [Sim/Não]
- **Pronta para começar:** [Sim/Não]

---

## 📎 Anexos

### Screenshots (se UI)
[Links ou descrições de screenshots relevantes]

### Logs Relevantes
```
[Logs importantes durante desenvolvimento/teste]
```

### Commits Relacionados
- [commit hash] - [mensagem do commit]
- [commit hash] - [mensagem do commit]

---

## 🎯 Resumo para QA

**Status Geral:** ✅ Pronto para QA

**Pontos de Atenção:**
- [Ponto 1 que QA deve focar]
- [Ponto 2 que QA deve focar]

**Casos de Teste Sugeridos:**
1. [Teste 1 que QA deve executar]
2. [Teste 2 que QA deve executar]
3. [Teste 3 - especialmente casos de erro]

---

**Template Version:** 1.0
**Assinatura Dev:** [Nome] - [Data]

