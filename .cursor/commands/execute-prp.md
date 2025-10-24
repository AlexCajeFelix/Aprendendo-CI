# Executar PRP

Executa um PRP (Product Requirement Prompt) contra o codebase atual, implementando todas as funcionalidades especificadas.

## Argumentos: $ARGUMENTS

Forneça o caminho para o arquivo PRP. Exemplo:
- `PRPs/sistema-autenticacao.md`
- `PRPs/componente-carrinho.md`
- `PRPs/api-usuarios.md`

## Como usar

1. **Leia o PRP completo** e analise todos os requisitos
2. **Analise o codebase atual** para entender a estrutura
3. **Implemente seguindo o blueprint** definido no PRP
4. **Execute comandos de validação** conforme especificado
5. **Corrija erros encontrados** e valide novamente
6. **Documente o código** conforme necessário

## Processo de execução

### Etapa 1: Análise
- Ler e entender o PRP
- Analisar estrutura do projeto
- Identificar dependências necessárias

### Etapa 2: Implementação
- Seguir blueprint de implementação
- Criar arquivos e componentes
- Implementar funcionalidades

### Etapa 3: Validação
- Executar comandos de lint/type-check
- Executar testes unitários
- Executar testes de integração
- Validar critérios de sucesso

### Etapa 4: Correção
- Corrigir erros encontrados
- Otimizar código se necessário
- Garantir qualidade

## Exemplo de uso

```
/execute-prp PRPs/sistema-autenticacao.md
```

## Requisitos

- PRP deve estar bem estruturado
- Contexto deve ser abrangente
- Blueprint deve ser detalhado
- Loop de validação deve ser executável

## Saída esperada

- Código implementado conforme especificação
- Todos os testes passando
- Critérios de sucesso atendidos
- Código documentado e limpo
- PRP marcado como concluído
