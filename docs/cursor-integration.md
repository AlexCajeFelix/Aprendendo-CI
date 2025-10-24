# Integração com Cursor

Este documento explica como integrar os PRPs com as funcionalidades do Cursor IDE, especialmente com agentes em segundo plano.

## 🤖 Configuração de Agentes em Segundo Plano

### 1. Criando um Agente PRP

No Cursor, vá para as configurações e crie um novo agente em segundo plano:

```json
{
  "name": "PRP Code Generator",
  "description": "Gera código de alta qualidade baseado em PRPs estruturados",
  "instructions": "Você é um especialista em desenvolvimento de software. Sua tarefa é gerar código limpo, bem estruturado e pronto para produção baseado nos PRPs fornecidos. Sempre siga as melhores práticas, inclua testes quando apropriado e documente o código adequadamente.",
  "rules": [
    "Sempre responda em português brasileiro",
    "Gere código completo e funcional",
    "Inclua comentários explicativos",
    "Siga as convenções do projeto especificadas no PRP",
    "Priorize qualidade sobre velocidade",
    "Valide sempre o código gerado"
  ],
  "tools": [
    "code_generation",
    "file_creation",
    "testing",
    "documentation"
  ]
}
```

### 2. Configuração de Contexto

Configure o agente para ter acesso aos templates e configurações:

```json
{
  "context_files": [
    ".cursor/rules",
    ".cursor/instructions",
    "docs/prp-structure.md",
    "templates/**/*.md"
  ],
  "workspace_aware": true,
  "auto_save": true
}
```

## 📋 Workflow de Uso

### 1. Preparação do PRP
1. Escolha um template apropriado em `templates/`
2. Preencha todas as seções obrigatórias
3. Revise e refine o conteúdo
4. Salve o arquivo com nome descritivo

### 2. Execução com Agente
1. Abra o PRP no Cursor
2. Selecione o agente "PRP Code Generator"
3. Execute o comando de geração
4. Monitore o progresso em tempo real

### 3. Validação e Iteração
1. Revise o código gerado
2. Execute testes se disponíveis
3. Faça ajustes no PRP se necessário
4. Re-execute se precisar de melhorias

## ⚙️ Configurações Avançadas

### Personalização por Tipo de Projeto

#### Para Projetos React/Next.js
```json
{
  "framework_rules": {
    "react": {
      "use_functional_components": true,
      "prefer_hooks": true,
      "include_prop_types": true,
      "use_css_modules": true
    }
  }
}
```

#### Para Projetos Node.js/Express
```json
{
  "framework_rules": {
    "express": {
      "use_middleware": true,
      "error_handling": "centralized",
      "validation": "joi_or_yup",
      "logging": "winston_or_pino"
    }
  }
}
```

#### Para Projetos Python/Django
```json
{
  "framework_rules": {
    "django": {
      "use_class_based_views": true,
      "include_serializers": true,
      "use_migrations": true,
      "include_admin": true
    }
  }
}
```

### Configuração de Qualidade

```json
{
  "quality_standards": {
    "code_coverage": ">= 80%",
    "linting": "enabled",
    "formatting": "prettier_or_black",
    "type_checking": "enabled",
    "security_scan": "enabled"
  }
}
```

## 🔧 Comandos Úteis

### Comandos de Atalho no Cursor

Crie comandos personalizados para facilitar o uso:

```json
{
  "commands": [
    {
      "name": "Generate from PRP",
      "command": "cursor.generateFromPRP",
      "shortcut": "Ctrl+Shift+G"
    },
    {
      "name": "Validate PRP",
      "command": "cursor.validatePRP",
      "shortcut": "Ctrl+Shift+V"
    },
    {
      "name": "Open Template",
      "command": "cursor.openTemplate",
      "shortcut": "Ctrl+Shift+T"
    }
  ]
}
```

### Scripts de Automação

Crie scripts para automatizar tarefas comuns:

```bash
#!/bin/bash
# scripts/generate-from-prp.sh

PRP_FILE=$1
OUTPUT_DIR=$2

if [ -z "$PRP_FILE" ] || [ -z "$OUTPUT_DIR" ]; then
    echo "Uso: $0 <arquivo-prp> <diretorio-saida>"
    exit 1
fi

# Valida o PRP
cursor validate-prp "$PRP_FILE"

# Gera o código
cursor generate-code --prp "$PRP_FILE" --output "$OUTPUT_DIR"

# Executa testes se disponíveis
if [ -f "$OUTPUT_DIR/package.json" ]; then
    cd "$OUTPUT_DIR" && npm test
fi
```

## 📊 Monitoramento e Métricas

### Configuração de Logs

```json
{
  "logging": {
    "level": "info",
    "file": "logs/prp-generator.log",
    "format": "json",
    "retention": "30d"
  }
}
```

### Métricas de Qualidade

Configure métricas para monitorar a qualidade do código gerado:

```json
{
  "metrics": {
    "code_quality": {
      "complexity": "monitor",
      "duplication": "monitor",
      "maintainability": "monitor"
    },
    "performance": {
      "build_time": "track",
      "test_execution": "track",
      "bundle_size": "track"
    }
  }
}
```

## 🔄 Integração com CI/CD

### GitHub Actions

Crie workflows para validar PRPs automaticamente:

```yaml
name: Validate PRP
on:
  pull_request:
    paths:
      - 'templates/**/*.md'
      - 'examples/**/*.md'

jobs:
  validate-prp:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Validate PRP Structure
        run: |
          python scripts/validate_prp.py ${{ github.event.pull_request.changed_files }}
      - name: Generate Test Code
        run: |
          cursor generate-test --prp ${{ github.event.pull_request.changed_files }}
```

### Validação Automática

Script para validar estrutura de PRPs:

```python
# scripts/validate_prp.py
import os
import re
import sys

def validate_prp_structure(file_path):
    """Valida se um arquivo PRP segue a estrutura correta"""
    required_sections = [
        "# ",  # Cabeçalho
        "## 🎯 Contexto do Projeto",
        "## ⚙️ Requisitos Funcionais",
        "## 🔧 Requisitos Técnicos",
        "## 📦 Entregáveis Esperados"
    ]
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    missing_sections = []
    for section in required_sections:
        if section not in content:
            missing_sections.append(section)
    
    if missing_sections:
        print(f"❌ {file_path}: Seções faltando: {missing_sections}")
        return False
    else:
        print(f"✅ {file_path}: Estrutura válida")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python validate_prp.py <arquivo-prp>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Arquivo não encontrado: {file_path}")
        sys.exit(1)
    
    is_valid = validate_prp_structure(file_path)
    sys.exit(0 if is_valid else 1)
```

## 🎯 Melhores Práticas

### Para Desenvolvedores
1. **Seja específico**: Quanto mais detalhes no PRP, melhor o código gerado
2. **Use exemplos**: Inclua exemplos concretos de uso e comportamento
3. **Defina critérios claros**: Especifique exatamente o que constitui "pronto"
4. **Itere**: Use feedback do código gerado para melhorar o PRP

### Para Agentes
1. **Valide inputs**: Sempre verifique se o PRP está bem formado
2. **Gere código completo**: Não deixe funcionalidades pela metade
3. **Inclua testes**: Sempre que apropriado, inclua testes automatizados
4. **Documente**: Adicione comentários e documentação adequada

### Para Projetos
1. **Padronize**: Use templates consistentes para projetos similares
2. **Versionie**: Mantenha controle de versão dos templates
3. **Colete feedback**: Monitore a qualidade do código gerado
4. **Melhore continuamente**: Atualize templates baseado na experiência
