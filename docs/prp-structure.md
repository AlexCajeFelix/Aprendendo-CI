# Estrutura de PRPs

Este documento define a estrutura padrão para Product Requirement Prompts (PRPs) neste projeto.

## 📋 Estrutura Padrão

Todo PRP deve seguir esta estrutura para garantir consistência e qualidade:

### 1. Cabeçalho
```markdown
# [Nome do Projeto/Feature]

**Tipo:** [Tipo do PRP]
**Complexidade:** [Baixa/Média/Alta]
**Tempo Estimado:** [Estimativa em horas]
**Versão:** [Versão do template]
```

### 2. Contexto do Projeto
```markdown
## 🎯 Contexto do Projeto

### Descrição Geral
[Descrição clara e concisa do que será desenvolvido]

### Objetivos
- [Objetivo principal]
- [Objetivos secundários]

### Justificativa
[Por que este projeto/feature é necessário]
```

### 3. Requisitos Funcionais
```markdown
## ⚙️ Requisitos Funcionais

### Funcionalidades Principais
1. **[Funcionalidade 1]**
   - Descrição: [Detalhes da funcionalidade]
   - Critérios de aceitação: [Como validar se está funcionando]

2. **[Funcionalidade 2]**
   - Descrição: [Detalhes da funcionalidade]
   - Critérios de aceitação: [Como validar se está funcionando]

### Casos de Uso
- **Caso 1:** [Descrição do caso de uso]
- **Caso 2:** [Descrição do caso de uso]
```

### 4. Requisitos Técnicos
```markdown
## 🔧 Requisitos Técnicos

### Stack Tecnológico
- **Frontend:** [Tecnologias do frontend]
- **Backend:** [Tecnologias do backend]
- **Banco de Dados:** [Tipo de banco e tecnologias]
- **Infraestrutura:** [Ferramentas de deploy e CI/CD]

### Arquitetura
[Descrição da arquitetura desejada]

### Padrões de Código
- **Linguagem:** [Linguagem principal]
- **Framework:** [Framework utilizado]
- **Convenções:** [Convenções de código a seguir]
- **Testes:** [Estratégia de testes]
```

### 5. Estrutura de Arquivos
```markdown
## 📁 Estrutura de Arquivos

```
projeto/
├── src/
│   ├── components/     # Componentes reutilizáveis
│   ├── pages/         # Páginas da aplicação
│   ├── services/      # Serviços e APIs
│   ├── utils/         # Utilitários
│   └── types/         # Definições de tipos
├── tests/             # Testes automatizados
├── docs/              # Documentação
└── config/            # Configurações
```
```

### 6. Entregáveis Esperados
```markdown
## 📦 Entregáveis Esperados

### Código
- [ ] [Arquivo/Componente 1]
- [ ] [Arquivo/Componente 2]
- [ ] [Arquivo/Componente 3]

### Funcionalidades
- [ ] [Funcionalidade 1 implementada]
- [ ] [Funcionalidade 2 implementada]
- [ ] [Funcionalidade 3 implementada]

### Testes
- [ ] Testes unitários para [componente]
- [ ] Testes de integração para [funcionalidade]
- [ ] Testes e2e para [fluxo principal]

### Documentação
- [ ] README com instruções de uso
- [ ] Documentação da API
- [ ] Guia de contribuição
```

### 7. Critérios de Qualidade
```markdown
## ✅ Critérios de Qualidade

### Código
- [ ] Código limpo e bem estruturado
- [ ] Comentários explicativos onde necessário
- [ ] Seguindo convenções do projeto
- [ ] Sem código duplicado

### Performance
- [ ] Tempo de carregamento aceitável
- [ ] Uso eficiente de recursos
- [ ] Otimizações implementadas

### Segurança
- [ ] Validação de inputs
- [ ] Proteção contra vulnerabilidades conhecidas
- [ ] Gerenciamento seguro de dados sensíveis

### Usabilidade
- [ ] Interface intuitiva
- [ ] Feedback visual adequado
- [ ] Tratamento de erros
```

### 8. Exemplos e Referências
```markdown
## 📚 Exemplos e Referências

### Exemplos de Uso
```code
[Exemplo de código ou uso]
```

### Referências
- [Link para documentação relevante]
- [Exemplo similar em outro projeto]
- [Padrões de design utilizados]
```

## 🎨 Variações por Tipo

### PRP para Web Application
- Foco em componentes reutilizáveis
- Responsividade obrigatória
- SEO básico incluído
- Acessibilidade considerada

### PRP para API Service
- Documentação da API obrigatória
- Validação de dados rigorosa
- Tratamento de erros padronizado
- Logs estruturados

### PRP para Database Schema
- Normalização adequada
- Índices otimizados
- Constraints de integridade
- Migrations documentadas

### PRP para Microservice
- Comunicação entre serviços
- Monitoramento e observabilidade
- Configuração via ambiente
- Deploy independente

## 📝 Dicas para Preenchimento

### Seja Específico
- Use exemplos concretos
- Defina critérios de aceitação claros
- Especifique tecnologias exatas

### Forneça Contexto
- Explique o problema a ser resolvido
- Inclua limitações e restrições
- Mencione dependências externas

### Considere Casos Extremos
- Cenários de erro
- Dados inválidos
- Limites de performance
- Casos de uso não óbvios

## 🔄 Iteração e Melhoria

### Após a Primeira Execução
1. Revise o código gerado
2. Identifique gaps no PRP
3. Atualize o template
4. Execute novamente se necessário

### Versionamento
- Mantenha versões dos templates
- Documente mudanças significativas
- Colete feedback dos usuários
- Melhore continuamente
