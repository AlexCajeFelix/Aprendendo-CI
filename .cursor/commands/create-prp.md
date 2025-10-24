# Criar PRP Base

Gera um PRP (Product Requirement Prompt) abrangente com pesquisa e contexto completo.

## Argumentos: $ARGUMENTS

Forneça uma descrição do que você quer construir. Exemplo:
- "sistema de autenticação com JWT"
- "componente de carrinho de compras"
- "API REST para gerenciamento de usuários"

## Como usar

1. **Analise o projeto atual** para entender a estrutura e padrões
2. **Pesquise documentação relevante** das tecnologias utilizadas
3. **Crie um PRP estruturado** baseado no template base
4. **Inclua contexto abrangente** com exemplos e armadilhas conhecidas
5. **Defina blueprint de implementação** com etapas claras
6. **Configure loop de validação** com testes executáveis

## Template usado

O comando usa o template `PRPs/templates/prp_base.md` como base e personaliza com:
- Tecnologias específicas do projeto
- Padrões de código existentes
- Estrutura de arquivos atual
- Convenções estabelecidas

## Exemplo de uso

```
/create-prp sistema de notificações em tempo real com WebSocket
```

## Saída esperada

- PRP completo salvo em `PRPs/[nome-da-feature].md`
- Contexto abrangente incluído
- Blueprint de implementação detalhado
- Loop de validação configurado
- Pronto para execução com `/execute-prp`
