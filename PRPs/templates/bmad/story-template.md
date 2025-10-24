# Story #[número]: [Título Descritivo]

**Épico:** [Nome do épico pai]
**Prioridade:** P0-MVP / P1-Important / P2-Nice-to-have
**Estimativa:** 2h / 4h / 8h
**Status:** Todo / In Progress / Done / Blocked
**Dependências:** [Story #X, Story #Y] ou [Nenhuma]
**Criada em:** [YYYY-MM-DD]

---

## 🎯 Objetivo

[Uma frase clara e concisa do que será implementado nesta story]

---

## 📋 Contexto Completo

### Do Brief (Por quê)
> **Seção:** [Nome da seção do Brief]
>
> [Trecho relevante do Brief explicando a necessidade de negócio e motivação]

### Do PRD (O quê)
> **Feature:** [Nome da feature no PRD]
>
> **Descrição:**
> [Requisitos funcionais específicos desta story extraídos do PRD]
>
> **Critérios de Aceitação do PRD:**
> - [ ] [Critério do PRD 1]
> - [ ] [Critério do PRD 2]

### Da Arquitetura (Como)
> **Componente:** [Nome do componente arquitetural]
>
> **Padrão Arquitetural:**
> [Decisões arquiteturais relevantes - stack, padrões, estrutura]
>
> **Tecnologias Específicas:**
> - [Tecnologia 1]
> - [Tecnologia 2]

---

## 💻 Tarefas de Implementação

### Tarefa 1: [Descrição específica]
**Arquivo:** `src/path/to/file.ts`
**Ação:** [Criar novo / Modificar existente]

**Descrição detalhada:**
[O que fazer neste arquivo]

**Código de Referência / Skeleton:**
```typescript
// Exemplo de estrutura esperada
interface Example {
  id: string;
  name: string;
}

export const doSomething = (data: Example): void => {
  // Implementação aqui
};
```

**Notas:**
- IMPORTANTE: [Armadilha ou consideração crítica]
- TIP: [Dica útil]

### Tarefa 2: [Descrição específica]
**Arquivo:** `src/path/to/another-file.ts`
[...]

### Tarefa 3: [Descrição específica]
[...]

---

## ✅ Critérios de Aceitação (Testáveis)

Estes são os critérios que o QA Agent irá validar:

- [ ] **CA1**: [Critério específico e testável]
  - **Como testar**: [Passos para validar]
  - **Resultado esperado**: [O que deve acontecer]

- [ ] **CA2**: [Critério específico e testável]
  - **Como testar**: [Passos para validar]
  - **Resultado esperado**: [O que deve acontecer]

- [ ] **CA3**: [Critério testável para caso de erro]
  - **Como testar**: [Passos com input inválido]
  - **Resultado esperado**: [Erro tratado corretamente]

---

## 🧪 Testes Esperados

### Testes Unitários

**Arquivo de teste:** `tests/unit/feature.test.ts`

**Casos a testar:**
```typescript
describe('[Nome do componente/função]', () => {
  describe('[Funcionalidade específica]', () => {
    it('deve [comportamento esperado]', () => {
      // Arrange
      const input = ...;
      
      // Act
      const result = ...;
      
      // Assert
      expect(result).toBe(...);
    });

    it('deve [outro comportamento]', () => {
      // Test
    });
  });

  describe('Error cases', () => {
    it('deve lançar erro quando [condição inválida]', () => {
      // Test
    });
  });
});
```

**Cobertura esperada:** > 80% para código desta story

### Testes de Integração (se aplicável)

**Arquivo de teste:** `tests/integration/flow.test.ts`

**Cenários a testar:**
1. [Cenário de integração 1]
2. [Cenário de integração 2]

---

## 📝 Notas de Implementação

### ⚠️ IMPORTANTE
- [Armadilha conhecida que deve ser evitada]
- [Consideração crítica para esta implementação]

### 💡 DICAS
- [Dica útil para implementação]
- [Padrão a seguir do código existente]

### 🔗 REFERÊNCIAS
- **Código Existente**: `src/path/to/similar-code.ts` - [Seguir este padrão]
- **Documentação**: [Link para doc relevante]

### 🔒 SEGURANÇA
- [Validação de input necessária]
- [Proteção contra [tipo de ataque]]

### ⚡ PERFORMANCE
- [Consideração de performance]
- [Otimização recomendada]

---

## 🔄 Definition of Done

Esta story está completa quando:

- [ ] **Código** implementado conforme especificação
- [ ] **Testes unitários** escritos e passando
- [ ] **Testes de integração** (se aplicável) escritos e passando
- [ ] **Linter** sem errors ou warnings
- [ ] **Type-check** passando (TypeScript)
- [ ] **Build** sucesso sem errors
- [ ] **Código reviewed** (auto-review ou por QA)
- [ ] **Documentação inline** adequada (comentários, JSDoc)
- [ ] **Performance** aceitável (sem lentidão óbvia)
- [ ] **Critérios de aceitação** todos validados
- [ ] **Dev notes** criadas
- [ ] **QA Report** aprovado

---

## 🔗 Referências e Contexto

### Documentos de Planejamento
- **Brief**: `PRPs/bmad-output/briefs/[projeto]-brief.md` (seção [X])
- **PRD**: `PRPs/bmad-output/prds/[projeto]-prd.md` (feature [Y])
- **Architecture**: `PRPs/bmad-output/architecture/[projeto]-architecture.md` (componente [Z])

### Código Relacionado
- [Arquivo 1] - [Relação]
- [Arquivo 2] - [Relação]

### Issues/Bugs Relacionados
- [Issue #X] - [Descrição]

---

## 🔀 Fluxo de Trabalho

### Para Implementar (Dev Agent):
```bash
# Use o comando:
/dev PRPs/bmad-output/stories/[projeto]/story-[número]-[titulo].md
```

### Após Implementação (QA Agent):
```bash
# Use o comando:
/qa story-[número]
```

### Próxima Story
**Story #[número+1]**: [título]
**Depende desta?**: [Sim/Não]
**Bloqueada até**: [Esta story estar completa / Nenhuma]

---

## 📊 Tracking

**Iniciada em:** [Data quando Dev começou]
**Tempo real gasto:** [Horas]
**Concluída em:** [Data quando QA aprovou]

**Desvios do estimado:**
[Se demorou mais/menos que estimado, explicar por quê]

---

**Template Version:** 1.0
**Última atualização:** [Data]

