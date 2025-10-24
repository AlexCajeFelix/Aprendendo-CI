# Melhores Práticas para Cursor

Este documento contém as melhores práticas para usar PRPs com o Cursor IDE, baseado no sistema PRPs-agentic-eng.

## 🎯 Princípios Fundamentais

### 1. Contexto é Rei
- **Sempre forneça contexto abrangente** nos PRPs
- **Inclua exemplos de código existente** do projeto
- **Documente armadilhas conhecidas** e limitações
- **Use palavras-chave específicas** do codebase

### 2. Validação Executável
- **Forneça comandos que a IA pode executar** para validar
- **Inclua testes automatizados** sempre que possível
- **Configure linting e formatação** automáticos
- **Defina critérios de sucesso claros**

### 3. Implementação Progressiva
- **Comece simples e valide** antes de complicar
- **Quebre tarefas complexas** em etapas menores
- **Valide cada etapa** antes de prosseguir
- **Itere rapidamente** com feedback contínuo

## 🚀 Comandos do Cursor

### Comandos Principais

#### `/create-prp`
Cria PRPs abrangentes com pesquisa e contexto completo.
```bash
/create-prp sistema de autenticação com JWT
```

#### `/execute-prp`
Executa PRPs contra o codebase atual.
```bash
/execute-prp PRPs/sistema-autenticacao.md
```

#### `/planning-create`
Cria documentos de planejamento com diagramas.
```bash
/planning-create arquitetura de microserviços
```

#### `/spec-create`
Cria especificações técnicas detalhadas.
```bash
/spec-create API REST para gerenciamento de pedidos
```

### Comandos de Revisão

#### `/review-code`
Revisão abrangente de qualidade de código.
```bash
/review-code src/components/
```

#### `/review-git`
Revisa mudanças staged e unstaged.
```bash
/review-git staged
```

#### `/refactor-simple`
Refatorações simples e seguras.
```bash
/refactor-simple extrair função de validação
```

### Comandos de Utilidade

#### `/create-pr`
Cria Pull Requests no GitHub.
```bash
/create-pr "Implementa sistema de notificações"
```

#### `/prime-context`
Prepara contexto completo do projeto.
```bash
/prime-context full
```

#### `/onboarding`
Processo de onboarding para novos membros.
```bash
/onboarding developer
```

#### `/debug`
Workflow estruturado de debug.
```bash
/debug "componente não está renderizando"
```

## 📋 Estrutura de PRPs Eficazes

### 1. Cabeçalho Informativo
```markdown
# [Nome do Projeto/Feature]

**Tipo:** [Tipo específico]
**Complexidade:** [Baixa/Média/Alta]
**Tempo Estimado:** [Estimativa realista]
**Versão:** 1.0
```

### 2. Objetivo Claro
```markdown
## 🎯 Objetivo

[Descrição concisa do que será construído]

### Por que é necessário?
- [Motivo 1]
- [Motivo 2]

### Critérios de Sucesso
- [ ] [Critério mensurável 1]
- [ ] [Critério mensurável 2]
```

### 3. Contexto Abrangente
```markdown
## 🧠 Todo Contexto Necessário

### Documentação & Referências
- **url:** https://exemplo.com/docs
  **por que:** [Por que esta documentação é importante]

- **arquivo:** src/exemplo/existing-code.ts
  **por que:** [Padrão existente a seguir]

### Armadilhas Conhecidas
# CRÍTICO: [Armadilha importante]
# IMPORTANTE: [Consideração importante]
```

### 4. Blueprint de Implementação
```markdown
## 🏗️ Blueprint de Implementação

### Etapa 1: [Nome da Etapa]
```pseudocode
1. Criar estrutura básica
2. Implementar funcionalidade principal
3. Adicionar validações
4. Criar testes
```
```

### 5. Loop de Validação
```markdown
## 🔄 Loop de Validação

### Nível 1: Sintaxe & Estilo
```bash
npm run lint
npm run type-check
```

### Nível 2: Testes
```bash
npm test
npm run test:coverage
```

### Nível 3: Integração
```bash
npm run dev
# Testar funcionalidade manualmente
```
```

## 🎨 Padrões de Código

### 1. Estrutura Consistente
- Use estrutura de pastas padronizada
- Mantenha arquivos pequenos e focados
- Organize imports de forma consistente
- Documente interfaces e tipos

### 2. Nomenclatura Clara
- Use nomes descritivos para funções e variáveis
- Siga convenções do projeto existente
- Evite abreviações desnecessárias
- Use constantes para valores mágicos

### 3. Tratamento de Erros
- Implemente tratamento de erros robusto
- Use tipos de erro específicos
- Forneça mensagens de erro úteis
- Registre erros para debugging

### 4. Testes Abrangentes
- Teste casos felizes e de erro
- Use mocks para dependências externas
- Mantenha cobertura de testes alta
- Teste comportamento, não implementação

## 🔧 Configuração do Projeto

### 1. Estrutura Recomendada
```
projeto/
├── .cursor/
│   ├── commands/          # Comandos personalizados
│   ├── rules              # Regras do projeto
│   └── instructions       # Instruções para IA
├── PRPs/
│   ├── templates/         # Templates de PRP
│   ├── examples/          # Exemplos práticos
│   ├── scripts/           # Scripts de execução
│   └── ai_docs/          # Documentação para IA
├── src/                   # Código fonte
├── tests/                 # Testes
└── docs/                  # Documentação
```

### 2. Arquivos de Configuração
- `.cursor/rules` - Regras específicas do projeto
- `.cursor/instructions` - Instruções para agentes
- `config/templates.json` - Configuração de templates
- `CLAUDE.md` - Guias específicos do projeto

### 3. Scripts de Desenvolvimento
```json
{
  "scripts": {
    "dev": "npm run dev",
    "build": "npm run build",
    "test": "npm test",
    "lint": "npm run lint",
    "type-check": "npm run type-check",
    "format": "npm run format"
  }
}
```

## 🧪 Estratégias de Teste

### 1. Testes Unitários
- Teste funções isoladamente
- Use mocks para dependências
- Mantenha testes simples e focados
- Teste casos extremos

### 2. Testes de Integração
- Teste fluxos completos
- Use banco de dados de teste
- Simule APIs externas
- Valide contratos de API

### 3. Testes E2E
- Teste jornadas críticas do usuário
- Use dados de teste realistas
- Automatize cenários principais
- Valide performance básica

## 📊 Métricas de Qualidade

### 1. Código
- Cobertura de testes > 80%
- Complexidade ciclomática baixa
- Duplicação de código < 5%
- Tempo de build < 2 minutos

### 2. Performance
- Tempo de carregamento < 3s
- Bundle size otimizado
- Lazy loading implementado
- Cache configurado adequadamente

### 3. Segurança
- Validação de inputs rigorosa
- Autenticação segura
- Headers de segurança configurados
- Dados sensíveis protegidos

## 🚨 Problemas Comuns e Soluções

### 1. PRP Muito Genérico
**Problema**: PRP não fornece contexto suficiente
**Solução**: 
- Inclua exemplos específicos do projeto
- Documente padrões existentes
- Liste armadilhas conhecidas
- Forneça referências diretas

### 2. Validação Inadequada
**Problema**: Comandos de validação não executam
**Solução**:
- Teste comandos antes de incluir no PRP
- Use comandos que existem no projeto
- Forneça comandos alternativos
- Documente pré-requisitos

### 3. Implementação Incompleta
**Problema**: IA não implementa tudo conforme especificado
**Solução**:
- Quebre em etapas menores
- Valide cada etapa antes de prosseguir
- Use exemplos mais específicos
- Inclua critérios de aceitação claros

### 4. Código de Baixa Qualidade
**Problema**: Código gerado não segue padrões
**Solução**:
- Configure linting automático
- Inclua exemplos de código existente
- Defina padrões claros no PRP
- Revise e corrija iterativamente

## 🎯 Dicas Avançadas

### 1. Uso de Contexto
- Use arquivos específicos como referência
- Inclua padrões de código existentes
- Documente convenções do projeto
- Forneça exemplos de uso real

### 2. Iteração Eficiente
- Comece com MVP e evolua
- Valide frequentemente
- Use feedback loops curtos
- Documente decisões importantes

### 3. Colaboração
- Compartilhe PRPs com a equipe
- Documente decisões arquiteturais
- Mantenha templates atualizados
- Colete feedback continuamente

### 4. Manutenção
- Revise PRPs periodicamente
- Atualize templates conforme necessário
- Remova informações obsoletas
- Melhore baseado em experiência

## 📚 Recursos Adicionais

### Documentação
- [Estrutura de PRPs](../docs/prp-structure.md)
- [Integração com Cursor](../docs/cursor-integration.md)
- [Guias de Setup](../docs/setup.md)

### Exemplos
- [Exemplos Práticos](../examples/)
- [Templates Disponíveis](../templates/)
- [Casos de Uso Reais](../examples/)

### Ferramentas
- [Scripts de Execução](../scripts/)
- [Validador de PRPs](../scripts/validator.py)
- [Gerador de Templates](../scripts/template_generator.py)

---

**Lembre-se**: O objetivo é implementação bem-sucedida em uma única passada através de contexto abrangente. PRPs bem escritos economizam tempo e produzem código de alta qualidade.
