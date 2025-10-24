# Configuração Inicial

Este guia te ajudará a configurar o ambiente para usar PRPs genéricos com o Cursor.

## 📋 Pré-requisitos

- Cursor IDE instalado
- Git configurado
- Acesso ao GitHub (para agentes em segundo plano)

## 🚀 Instalação

### 1. Clone o Repositório
```bash
git clone <seu-repositorio>
cd PRP
```

### 2. Configuração do Cursor

#### Configurar Agentes em Segundo Plano
1. Abra as configurações do Cursor
2. Vá para "Background Agents"
3. Configure um novo agente com as seguintes propriedades:
   - Nome: "PRP Generator"
   - Descrição: "Gera código baseado em PRPs"
   - Instruções: Use o conteúdo de `.cursor/instructions`

#### Configurar Regras do Projeto
1. Certifique-se de que o arquivo `.cursor/rules` está sendo lido
2. As regras serão aplicadas automaticamente aos agentes

### 3. Estrutura de Diretórios
```
PRP/
├── .cursor/                 # Configurações do Cursor
│   ├── rules               # Regras do projeto
│   └── instructions        # Instruções para agentes
├── templates/               # Templates de PRPs
├── examples/               # Exemplos práticos
├── docs/                   # Documentação
├── tools/                  # Ferramentas auxiliares
└── config/                 # Configurações do projeto
```

## ⚙️ Configuração Avançada

### Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
# Configurações do Cursor
CURSOR_AGENT_ENABLED=true
CURSOR_AGENT_NAME=PRP Generator

# Configurações do Projeto
DEFAULT_TEMPLATE=web-application
DEFAULT_LANGUAGE=typescript
```

### Configuração de Templates
Edite o arquivo `config/templates.json` para personalizar os templates disponíveis.

## 🧪 Teste da Configuração

### 1. Teste Básico
1. Abra um template em `templates/`
2. Preencha com informações de teste
3. Use o agente para gerar código
4. Verifique se o resultado atende às expectativas

### 2. Teste Avançado
1. Crie um PRP personalizado
2. Execute com diferentes configurações
3. Valide a qualidade do código gerado
4. Ajuste as configurações conforme necessário

## 🔧 Personalização

### Adicionando Novos Templates
1. Crie um novo arquivo em `templates/`
2. Siga a estrutura padrão definida
3. Documente o template adequadamente
4. Teste com casos de uso reais

### Configurando Linguagens Específicas
1. Edite as regras em `.cursor/rules`
2. Adicione configurações específicas da linguagem
3. Configure linters e formatters apropriados
4. Teste com projetos reais

## 📚 Próximos Passos

Após a configuração inicial:
1. Leia [Estrutura de PRPs](prp-structure.md)
2. Explore os [Exemplos Práticos](../examples/README.md)
3. Configure sua primeira integração com Cursor
4. Comece a criar seus próprios PRPs

## ❓ Problemas Comuns

### Agente não responde
- Verifique se o agente está ativado
- Confirme se as instruções estão corretas
- Teste com um PRP mais simples

### Código gerado incompleto
- Revise o PRP para mais detalhes
- Verifique se todas as seções obrigatórias estão preenchidas
- Use exemplos mais específicos

### Configurações não aplicadas
- Reinicie o Cursor após mudanças nas configurações
- Verifique se os arquivos estão no local correto
- Confirme as permissões de leitura dos arquivos
