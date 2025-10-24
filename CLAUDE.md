# CLAUDE.md - Guias do Projeto PRP

Este arquivo contém diretrizes específicas para o projeto PRP, baseado no sistema PRPs-agentic-eng adaptado para Cursor.

## 🎯 Princípios do Projeto

### Filosofia de Desenvolvimento
- **Contexto é Rei**: Sempre forneça contexto abrangente
- **Implementação em Uma Passada**: Objetivo é sucesso na primeira tentativa
- **Validação Executável**: Comandos que a IA pode executar e corrigir
- **Progressão Incremental**: Começar simples e evoluir
- **Agentes Especializados**: Roles bem definidos colaborando (integração BMAD)

### Qualidade de Código
- **Código Limpo**: Legível, bem estruturado e documentado
- **Testes Abrangentes**: Cobertura mínima de 80%
- **Performance**: Otimizado para produção
- **Segurança**: Validação rigorosa e proteção de dados

## 🏗️ Arquitetura do Projeto

### Estrutura de Diretórios
```
PRP/
├── .cursor/                 # Configurações do Cursor
│   ├── commands/           # Comandos personalizados
│   ├── rules              # Regras do projeto
│   └── instructions       # Instruções para agentes
├── PRPs/                   # Product Requirement Prompts
│   ├── templates/         # Templates de PRP
│   ├── examples/          # Exemplos práticos
│   ├── scripts/           # Scripts de execução
│   └── ai_docs/          # Documentação para IA
├── config/                 # Configurações do projeto
├── docs/                   # Documentação
└── tools/                  # Ferramentas auxiliares
```

### Tecnologias Principais
- **Python**: Scripts de automação e execução
- **Markdown**: Documentação e PRPs
- **JSON**: Configurações e templates
- **Bash**: Comandos de validação

## 🤖 Integração BMAD - Agentes Especializados

### Sistema de Agentes

O PRP agora inclui 6 agentes especializados inspirados no [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD):

**Fase de Planejamento** (Sequencial):
1. **Analyst** (`/analyst`) - Análise de requisitos → Brief
2. **PM** (`/pm`) - Especificação de produto → PRD
3. **Architect** (`/architect`) - Arquitetura técnica → Architecture Doc

**Fase de Desenvolvimento** (Iterativo):
4. **Scrum Master** (`/scrum-master` ou `/sm`) - Quebra em stories → Development Stories
5. **Dev** (`/dev`) - Implementação → Código + Dev Notes
6. **QA** (`/qa`) - Validação → QA Reports

### Quando Usar BMAD vs PRP Tradicional

**Use BMAD Workflow quando**:
- Projeto novo do zero
- Precisa de planejamento robusto
- Projeto grande/complexo
- Quer separation of concerns
- Trabalhando com equipe (cada agente = role)

**Use PRP Tradicional quando**:
- Feature bem definida
- Projeto pequeno/médio
- Já tem arquitetura definida
- Quer implementação rápida

**São compatíveis!** Pode usar BMAD para planejar e PRP para features individuais.

### Documentação BMAD

- **[Integração BMAD](docs/bmad-integration.md)** - Guia completo de uso
- **[Sistema Automático](docs/bmad-auto-system.md)** - Workflow automático entre agentes
- **[Guia de Agentes](PRPs/ai_docs/bmad-agents-guide.md)** - Para IAs
- **Arquivos de Agentes**: `.cursor/agents/` - Definições completas
- **Comandos**: `.cursor/commands/` - Comandos slash
- **Templates**: `PRPs/templates/bmad/` - Templates dos documentos
- **Outputs**: `PRPs/bmad-output/` - Onde outputs são salvos
- **Scripts**: `PRPs/scripts/` - Scripts de automação e coordenação

## 📋 Padrões de PRP

### Estrutura Obrigatória
1. **Cabeçalho**: Metadados claros
2. **Objetivo**: Descrição concisa do que será construído
3. **Contexto**: Informações abrangentes e específicas
4. **Blueprint**: Plano de implementação detalhado
5. **Validação**: Comandos executáveis para validação

### Seções Recomendadas
- **Por que**: Justificativa e motivação
- **Critérios de Sucesso**: Métricas mensuráveis
- **Armadilhas Conhecidas**: Problemas a evitar
- **Exemplos**: Código e uso prático
- **Entregáveis**: Lista de itens a serem entregues

### Qualidade de Contexto
- **Específico**: Use exemplos do projeto atual
- **Abrangente**: Inclua toda informação necessária
- **Atualizado**: Mantenha informações relevantes
- **Executável**: Comandos que realmente funcionam

## 🔧 Configuração de Desenvolvimento

### Pré-requisitos
- Python 3.8+
- Node.js 18+ (para projetos web)
- Git configurado
- Cursor IDE

### Comandos Essenciais
```bash
# Executar PRP
python PRPs/scripts/prp_runner.py --prp PRPs/meu-prp.md --interactive

# Gerar template
python PRPs/scripts/template_generator.py --type web-application --output PRPs/novo-prp.md

# Validar PRP
python PRPs/scripts/validator.py PRPs/meu-prp.md --report
```

### Variáveis de Ambiente
```env
# Configurações do projeto
PRP_DEFAULT_TEMPLATE=prp_base
PRP_OUTPUT_DIR=./output
PRP_VALIDATION_ENABLED=true

# Configurações do Cursor
CURSOR_AGENT_ENABLED=true
CURSOR_AGENT_NAME=PRP Generator
```

## 🧪 Estratégia de Testes

### Validação de PRPs
- **Estrutura**: Verificar seções obrigatórias
- **Conteúdo**: Validar qualidade e completude
- **Comandos**: Testar comandos de validação
- **Contexto**: Verificar especificidade

### Testes de Execução
- **Sintaxe**: Linting e type-checking
- **Funcionalidade**: Testes unitários
- **Integração**: Testes de integração
- **Performance**: Validação de performance

### Critérios de Aceitação
- **Funcionalidade**: Todas as funcionalidades implementadas
- **Qualidade**: Código limpo e bem testado
- **Performance**: Métricas dentro dos limites
- **Documentação**: Código documentado adequadamente

## 📊 Métricas de Qualidade

### PRPs
- **Completude**: Todas as seções obrigatórias preenchidas
- **Especificidade**: Contexto específico do projeto
- **Executabilidade**: Comandos de validação funcionais
- **Clareza**: Objetivos e critérios bem definidos

### Código Gerado
- **Cobertura de Testes**: Mínimo 80%
- **Complexidade**: Ciclomática baixa
- **Duplicação**: Menos de 5% de código duplicado
- **Performance**: Tempo de execução aceitável

### Processo
- **Tempo de Execução**: PRPs executados em tempo esperado
- **Taxa de Sucesso**: Alta taxa de implementação bem-sucedida
- **Iterações**: Poucas iterações necessárias
- **Feedback**: Processo de melhoria contínua

## 🚨 Troubleshooting

### Problemas Comuns

#### PRP Muito Genérico
**Sintomas**: IA não entende contexto específico
**Solução**: 
- Inclua exemplos específicos do projeto
- Documente padrões existentes
- Liste armadilhas conhecidas

#### Comandos de Validação Falham
**Sintomas**: Comandos não executam ou falham
**Solução**:
- Teste comandos antes de incluir
- Forneça comandos alternativos
- Documente pré-requisitos

#### Implementação Incompleta
**Sintomas**: IA não implementa tudo conforme especificado
**Solução**:
- Quebre em etapas menores
- Valide cada etapa
- Use exemplos mais específicos

#### Código de Baixa Qualidade
**Sintomas**: Código não segue padrões do projeto
**Solução**:
- Configure linting automático
- Inclua exemplos de código existente
- Defina padrões claros

### Logs e Debugging
- **Logs de Execução**: `prp_execution_report.json`
- **Relatórios de Validação**: Saída do validator.py
- **Logs do Cursor**: Console do Cursor IDE

## 🔄 Processo de Melhoria

### Revisão de PRPs
1. **Análise de Execução**: Revisar relatórios de execução
2. **Identificação de Gaps**: Encontrar informações faltantes
3. **Atualização de Templates**: Melhorar templates baseado em experiência
4. **Documentação**: Atualizar guias e exemplos

### Feedback Loop
1. **Coleta**: Reunir feedback de usuários
2. **Análise**: Identificar padrões e problemas
3. **Implementação**: Fazer melhorias nos templates
4. **Validação**: Testar melhorias com casos reais

### Versionamento
- **Templates**: Versionar mudanças significativas
- **Scripts**: Manter compatibilidade com versões anteriores
- **Documentação**: Atualizar conforme necessário
- **Configurações**: Versionar mudanças de configuração

## 📚 Recursos e Referências

### Documentação Interna
- [Estrutura de PRPs](docs/prp-structure.md)
- [Integração com Cursor](docs/cursor-integration.md)
- [Melhores Práticas](PRPs/ai_docs/cursor_best_practices.md)
- [Exemplos Práticos](PRPs/examples/)

### Recursos Externos
- [PRPs-agentic-eng](https://github.com/Wirasm/PRPs-agentic-eng) - Repositório original
- [Cursor Documentation](https://cursor.sh/docs) - Documentação do Cursor
- [Claude Code](https://claude.ai/code) - Documentação do Claude Code

### Ferramentas
- **Scripts**: `PRPs/scripts/` - Automação e validação
- **Templates**: `PRPs/templates/` - Templates de PRP
- **Comandos**: `.cursor/commands/` - Comandos do Cursor

## 🎯 Roadmap

### Próximas Funcionalidades
- [ ] Integração com GitHub Actions
- [ ] Templates para mais tipos de projeto
- [ ] Métricas avançadas de qualidade
- [ ] Interface web para gerenciamento

### Melhorias Planejadas
- [ ] Validação automática de PRPs
- [ ] Geração automática de templates
- [ ] Integração com mais IDEs
- [ ] Comunidade de templates

---

**Instruções para IA**: Use este arquivo como referência para entender o contexto do projeto, padrões estabelecidos e melhores práticas. Sempre siga os princípios de contexto abrangente, implementação progressiva e validação executável.
