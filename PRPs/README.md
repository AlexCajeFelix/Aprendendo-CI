# PRPs (Product Requirement Prompts)

Este diretório contém os Product Requirement Prompts - uma metodologia para desenvolvimento assistido por IA que garante implementação bem-sucedida em uma única passada através de contexto abrangente.

## 🎯 O que são PRPs?

PRPs são prompts estruturados que fornecem contexto completo para IA gerar código de alta qualidade. Eles incluem:

- **Objetivo claro**: O que precisa ser construído
- **Contexto abrangente**: Documentação, exemplos, armadilhas conhecidas
- **Blueprint de implementação**: Tarefas e pseudocódigo
- **Loop de validação**: Testes executáveis

## 📁 Estrutura

```
PRPs/
├── templates/           # Templates de PRPs
├── examples/           # Exemplos práticos
├── scripts/            # Scripts de execução
├── ai_docs/           # Documentação para IA
└── completed/         # PRPs finalizados
```

## 🚀 Como Usar

### 1. Criando um PRP

```bash
# Copiar um template
cp templates/prp_base.md PRPs/minha-feature.md

# Preencher com suas informações
# Ou usar o comando do Cursor: /create-prp
```

### 2. Executando um PRP

```bash
# Modo interativo (recomendado para desenvolvimento)
python scripts/prp_runner.py --prp minha-feature --interactive

# Modo headless (para CI/CD)
python scripts/prp_runner.py --prp minha-feature --output-format json
```

### 3. Usando Comandos do Cursor

- `/create-prp` - Gerar PRP abrangente com pesquisa
- `/execute-prp` - Executar PRP contra codebase
- `/planning-create` - Criar documentos de planejamento
- `/spec-create` - Criação avançada de especificações
- `/spec-execute` - Executar especificações

## 📋 Melhores Práticas

### 1. Contexto é Rei
- Inclua TODA documentação necessária
- Forneça exemplos de código existente
- Liste armadilhas conhecidas
- Use palavras-chave do codebase

### 2. Loops de Validação
- Forneça testes executáveis
- Inclua comandos de lint que a IA pode executar
- Defina critérios de sucesso claros

### 3. Informação Densa
- Use padrões específicos do projeto
- Inclua referências diretas a arquivos
- Mencione convenções de código

### 4. Sucesso Progressivo
- Comece simples, valide, depois melhore
- Quebre tarefas complexas em etapas
- Valide cada etapa antes de prosseguir

## 🎨 Tipos de PRPs

### PRP Base
Template completo com todas as seções necessárias para desenvolvimento full-stack.

### PRP de Especificação
Focado em documentação detalhada e planejamento.

### PRP de Planejamento
Inclui diagramas e fluxos de trabalho.

### PRP de Refatoração
Especializado em melhorias de código existente.

## 📚 Recursos Incluídos

### Documentação IA (ai_docs/)
- `cursor_best_practices.md` - Melhores práticas para Cursor
- `code_patterns.md` - Padrões de código comuns
- `testing_patterns.md` - Estratégias de teste
- `architecture_patterns.md` - Padrões arquiteturais

### Scripts (scripts/)
- `prp_runner.py` - Executor principal de PRPs
- `template_generator.py` - Gerador de templates
- `validator.py` - Validador de PRPs

### Exemplos (examples/)
- Exemplos de PRPs bem-sucedidos
- Casos de uso reais
- Templates personalizados

## 🔧 Configuração

### Variáveis de Ambiente
```env
PRP_DEFAULT_TEMPLATE=prp_base
PRP_OUTPUT_DIR=./output
PRP_VALIDATION_ENABLED=true
```

### Configuração do Projeto
Edite `config/templates.json` para personalizar templates disponíveis.

## 📖 Próximos Passos

1. Leia [Como Criar PRPs Eficazes](../docs/prp-creation-guide.md)
2. Explore os [Exemplos Práticos](./examples/)
3. Configure seus primeiros comandos do Cursor
4. Comece criando seu primeiro PRP

## 🤝 Contribuindo

1. Teste novos templates com projetos reais
2. Documente casos de uso bem-sucedidos
3. Compartilhe melhorias nos scripts
4. Mantenha a documentação atualizada

---

**Lembre-se**: O objetivo é implementação bem-sucedida em uma única passada através de contexto abrangente. PRPs bem escritos economizam tempo e produzem código de alta qualidade.
