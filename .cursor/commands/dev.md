---
description: Implementa código baseado em Development Story
tags: [bmad, development, implementation, coding]
---

# Comando: /dev

## 📋 Descrição

Ativa o **Dev Agent** para implementar código de alta qualidade baseado em uma Development Story específica.

## 🎯 Quando Usar

Use este comando quando:
- Scrum Master já criou Development Stories
- Estiver pronto para implementar uma story específica
- Tiver verificado que dependências da story estão completas
- Quiser implementar código seguindo especificação completa

## 💻 Como Usar

```
/dev [caminho-da-story]
```

### Exemplos:

```
/dev PRPs/bmad-output/stories/ecommerce/story-001-setup.md

/dev PRPs/bmad-output/stories/payment-api/story-015-create-payment-endpoint.md

/dev story-003  # Se estiver no diretório de stories
```

## 🔄 Workflow

**Fase**: Desenvolvimento (2/3)

```
Analyst → PM → Architect → Scrum Master → [VOCÊ ESTÁ AQUI] → QA
```

### Pré-requisitos:
- Development Story criada pelo Scrum Master
- Dependências da story (outras stories) implementadas
- Ambiente de desenvolvimento configurado

### Próximo Passo:
Após o Dev implementar e validar, use `/qa` para testar e validar a implementação.

## 📤 Output

O Dev criará:
- **Código funcional** nos arquivos especificados na story
- **Testes** unitários e de integração
- **Dev Notes** em `PRPs/bmad-output/implementations/story-[número]-dev-notes.md`
- Documentação inline e comentários
- Validação completa (lint, tests, build)

## 🎭 O que o Dev Faz

1. **Lê** a Development Story completamente
2. **Entende** contexto de Brief/PRD/Arquitetura embutido
3. **Implementa** funcionalidades conforme especificação
4. **Escreve** testes unitários e de integração
5. **Valida** lint, type-check, testes
6. **Documenta** código e decisões de implementação
7. **Cria** dev notes com resultados
8. **Prepara** para QA

## ⚙️ Configuração do Agente

Este comando carrega:
- Personalidade: Software Developer Senior
- Input: Development Story específica
- Template: `PRPs/templates/bmad/dev-notes-template.md`
- Output: Código + `PRPs/bmad-output/implementations/`
- Contexto: Story + Arquitetura + código existente

## 💡 Dicas

- Leia a story completamente antes de começar
- Verifique que dependências estão implementadas
- Siga padrões e estruturas da Arquitetura
- Implemente testes junto com código
- Execute validadores frequentemente
- Documente decisões importantes
- Teste casos felizes E casos de erro

## ⚠️ Importante

- **Siga a story** - Não invente requisitos
- **Escreva testes** - Não é opcional
- **Valide tudo** - Lint, types, tests antes de finalizar
- **Documente desvios** - Se mudar algo da story, explique
- **Code quality** - Código limpo e manutenível

## 🔄 Comandos de Validação

O Dev Agent executará:

```bash
# Linting
npm run lint

# Type checking
npm run type-check

# Testes
npm test

# Build
npm run build
```

Todos devem passar antes de considerar story completa.

## ✅ Definition of Done

Uma story está completa quando:
- [x] Código implementado conforme especificação
- [x] Testes unitários escritos e passando
- [x] Testes integração (se aplicável) passando
- [x] Sem linter errors
- [x] Type-safe (TypeScript)
- [x] Código documentado adequadamente
- [x] Build sucesso
- [x] Dev notes criadas
- [x] Pronta para QA

## 🎉 Após Implementação

Quando Dev completar:

```
✅ Story #[número] implementada!

📄 Dev Notes: PRPs/bmad-output/implementations/story-[número]-dev-notes.md

🧪 Próximo Passo: Use `/qa story-[número]` para validação

📊 Status:
- Lint: ✅
- Type-check: ✅
- Tests: ✅ 15/15
- Build: ✅
```

## 📚 Referências

- Agente: `.cursor/agents/dev.md`
- Template: `PRPs/templates/bmad/dev-notes-template.md`
- Guia: `docs/bmad-integration.md`

---

**Workflow BMAD**: Dev implementa com contexto completo da story. QA valida para garantir qualidade!

