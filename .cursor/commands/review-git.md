# Revisar Mudanças Git

Revisa mudanças staged e unstaged no Git, analisando qualidade, impacto e conformidade com padrões.

## Argumentos: $ARGUMENTS

Especifique o tipo de revisão:
- `staged` - Revisar apenas arquivos staged
- `unstaged` - Revisar apenas arquivos unstaged  
- `all` - Revisar todas as mudanças (padrão)
- ou deixe vazio para revisar todas as mudanças

## Como usar

1. **Analise mudanças staged** no Git
2. **Analise mudanças unstaged** no Git
3. **Revise qualidade** do código alterado
4. **Verifique impacto** das mudanças
5. **Valide conformidade** com padrões
6. **Sugira melhorias** antes do commit

## Aspectos analisados

### Mudanças Staged
- Qualidade do código commitado
- Conformidade com padrões
- Completude das funcionalidades
- Qualidade dos commits
- Mensagens de commit

### Mudanças Unstaged
- Código não commitado
- Mudanças em desenvolvimento
- Arquivos temporários
- Configurações locais
- Arquivos de teste

### Análise de Impacto
- Arquivos modificados
- Linhas adicionadas/removidas
- Funcionalidades afetadas
- Dependências impactadas
- Testes necessários

### Qualidade e Padrões
- Formatação e estilo
- Convenções de nomenclatura
- Estrutura e organização
- Comentários e documentação
- Tratamento de erros

### Sugestões de Melhoria
- Refatorações necessárias
- Otimizações de performance
- Melhorias de segurança
- Adição de testes
- Documentação necessária

## Exemplo de uso

```
/review-git staged
```

## Saída esperada

- Resumo das mudanças analisadas
- Análise de qualidade do código
- Identificação de problemas
- Sugestões de melhorias
- Recomendações para commit
- Plano de ação para correções
