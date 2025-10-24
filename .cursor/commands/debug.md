# Workflow de Debug

Executa processo estruturado de debug, identificando e resolvendo problemas no código.

## Argumentos: $ARGUMENTS

Descreva o problema encontrado. Exemplo:
- "erro de compilação no componente X"
- "funcionalidade Y não está funcionando"
- "performance lenta na página Z"
- ou deixe vazio para análise geral

## Como usar

1. **Identifique o problema** e sintomas
2. **Analise logs** e mensagens de erro
3. **Reproduza o problema** consistentemente
4. **Isole a causa** raiz
5. **Implemente solução** adequada
6. **Valide correção** com testes

## Processo de debug

### Etapa 1: Identificação
- Descrever problema claramente
- Identificar sintomas observados
- Localizar onde ocorre
- Determinar impacto

### Etapa 2: Análise
- Examinar logs e erros
- Analisar código relacionado
- Verificar dependências
- Identificar padrões

### Etapa 3: Reprodução
- Criar cenário mínimo
- Isolar variáveis
- Documentar passos
- Confirmar consistência

### Etapa 4: Investigação
- Usar ferramentas de debug
- Adicionar logs temporários
- Verificar estado dos dados
- Analisar fluxo de execução

### Etapa 5: Solução
- Implementar correção
- Testar solução
- Validar impacto
- Documentar mudanças

### Etapa 6: Validação
- Executar testes
- Verificar funcionalidade
- Confirmar performance
- Revisar código

## Exemplo de uso

```
/debug "componente de login não está validando senha"
```

## Saída esperada

- Análise detalhada do problema
- Causa raiz identificada
- Solução implementada
- Testes validando correção
- Documentação da correção
- Prevenção de problemas similares
