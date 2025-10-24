# BMAD Output Directory

Este diretório contém os outputs gerados pelos 6 agentes BMAD durante o workflow de desenvolvimento.

## 📂 Estrutura

```
bmad-output/
├── briefs/              # Outputs do Analyst (Brief de requisitos)
├── prds/                # Outputs do PM (Product Requirement Documents)
├── architecture/        # Outputs do Architect (Documentos de arquitetura)
├── stories/             # Outputs do Scrum Master (Development Stories)
│   └── [projeto]/      # Stories organizadas por projeto
│       ├── index.md    # Índice de todas as stories
│       ├── story-001-*.md
│       ├── story-002-*.md
│       └── ...
├── implementations/     # Outputs do Dev (Dev Notes)
└── qa-reports/         # Outputs do QA (QA Reports)
```

## 🔄 Fluxo de Documentos

### Fase de Planejamento (Sequencial)

1. **Analyst** → `briefs/[projeto]-brief.md`
   - Análise de requisitos
   - Stakeholders e personas
   - Casos de uso
   - Riscos e dependências

2. **PM** → `prds/[projeto]-prd.md`
   - Especificação detalhada de features
   - User stories
   - Critérios de aceitação
   - Roadmap e priorização

3. **Architect** → `architecture/[projeto]-architecture.md`
   - Stack tecnológico
   - Decisões arquiteturais
   - Design de componentes
   - Segurança e performance

### Fase de Desenvolvimento (Iterativo)

4. **Scrum Master** → `stories/[projeto]/story-*.md`
   - Stories de 2-8h cada
   - Contexto completo embutido
   - Tarefas de implementação
   - Critérios de aceitação

5. **Dev** → `implementations/story-[número]-dev-notes.md`
   - Código implementado
   - Decisões de implementação
   - Validação de critérios
   - Testes realizados

6. **QA** → `qa-reports/story-[número]-qa-report.md`
   - Validação de qualidade
   - Bugs encontrados (se houver)
   - Aprovação ou reprovação
   - Recomendações

## 🚀 Como Usar

### Verificar Status do Projeto

```bash
python PRPs/scripts/bmad_orchestrator.py
```

Mostra:
- Estado atual do projeto
- Documentos criados
- Próximo passo recomendado

### Criar Novo Projeto

1. **Inicie com Analyst**:
   ```bash
   /analyst Meu novo projeto
   ```

2. **Continue com PM**:
   ```bash
   /pm PRPs/bmad-output/briefs/meu-projeto-brief.md
   ```

3. **Defina Arquitetura**:
   ```bash
   /architect PRPs/bmad-output/prds/meu-projeto-prd.md
   ```

4. **Crie Stories**:
   ```bash
   /sm PRPs/bmad-output/architecture/meu-projeto-architecture.md
   ```

5. **Implemente (iterativo)**:
   ```bash
   /dev PRPs/bmad-output/stories/meu-projeto/story-001-setup.md
   /qa story-001
   /dev PRPs/bmad-output/stories/meu-projeto/story-002-auth.md
   /qa story-002
   # ... e assim por diante
   ```

## 📋 Convenções de Nomenclatura

### Briefs
- Formato: `[projeto]-brief.md`
- Exemplo: `task-manager-brief.md`

### PRDs
- Formato: `[projeto]-prd.md`
- Exemplo: `task-manager-prd.md`

### Architecture
- Formato: `[projeto]-architecture.md`
- Exemplo: `task-manager-architecture.md`

### Stories
- Formato: `story-[número]-[título-curto].md`
- Exemplo: `story-001-setup-projeto.md`
- Número: 3 dígitos com zero padding (001, 002, 003...)

### Dev Notes
- Formato: `story-[número]-dev-notes.md`
- Exemplo: `story-001-dev-notes.md`

### QA Reports
- Formato: `story-[número]-qa-report.md`
- Exemplo: `story-001-qa-report.md`

## 🎯 Melhores Práticas

### 1. Organização por Projeto

Mantenha cada projeto em seu próprio subdiretório em `stories/`:
```
stories/
├── ecommerce/
│   ├── index.md
│   ├── story-001-setup.md
│   └── ...
└── task-manager/
    ├── index.md
    ├── story-001-setup.md
    └── ...
```

### 2. Mantenha Documentos Atualizados

Se requisitos mudarem durante desenvolvimento:
1. Atualize o Brief
2. Atualize o PRD
3. Revise a Architecture se necessário
4. Scrum Master atualiza stories afetadas

### 3. Não Delete Documentos Antigos

Se fizer mudanças significativas:
- Mantenha versões antigas com sufixo `-v1`, `-v2`, etc
- Ou use controle de versão (git)

### 4. Use o Orchestrator

Antes de começar qualquer etapa:
```bash
python PRPs/scripts/bmad_orchestrator.py
```

Para verificar se pré-requisitos estão prontos.

## 📚 Documentação Relacionada

- **[Integração BMAD](../../docs/bmad-integration.md)** - Guia completo
- **[Guia de Agentes](../ai_docs/bmad-agents-guide.md)** - Para IAs
- **[Templates](../templates/bmad/)** - Templates usados pelos agentes

## 💡 Dicas

- **Stories muito grandes?** Scrum Master pode quebrar mais
- **QA reprovou?** Dev corrige e QA testa novamente
- **Mudou requisitos?** Volte ao Analyst e atualize Brief
- **Dúvidas no workflow?** Use o orchestrator para sugestões

---

**Este diretório é gerenciado automaticamente pelos agentes BMAD. Não edite manualmente a menos que seja necessário.**

