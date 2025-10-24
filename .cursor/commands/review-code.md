# Revisão Geral de Código

Executa uma revisão abrangente do código, analisando qualidade, performance, segurança e boas práticas.

## Argumentos: $ARGUMENTS

Forneça o escopo da revisão. Exemplo:
- `src/components/` (revisar componentes)
- `src/services/` (revisar serviços)
- `src/utils/` (revisar utilitários)
- ou deixe vazio para revisar todo o projeto

## Como usar

1. **Analise a estrutura** do código
2. **Revise qualidade** e boas práticas
3. **Identifique problemas** de performance
4. **Verifique segurança** e vulnerabilidades
5. **Sugira melhorias** e refatorações
6. **Valide testes** e documentação

## Aspectos analisados

### Qualidade de Código
- Estrutura e organização
- Nomenclatura e convenções
- Complexidade ciclomática
- Duplicação de código
- Comentários e documentação

### Performance
- Otimizações de renderização
- Gerenciamento de estado
- Lazy loading e code splitting
- Otimizações de banco de dados
- Cache e memoização

### Segurança
- Validação de inputs
- Sanitização de dados
- Autenticação e autorização
- Vulnerabilidades conhecidas
- Exposição de dados sensíveis

### Testes
- Cobertura de testes
- Qualidade dos testes
- Cenários de teste
- Testes de integração
- Testes E2E

### Arquitetura
- Padrões arquiteturais
- Separação de responsabilidades
- Acoplamento e coesão
- Reutilização de código
- Escalabilidade

## Exemplo de uso

```
/review-code src/components/
```

## Saída esperada

- Relatório detalhado de qualidade
- Lista de problemas identificados
- Sugestões de melhorias
- Priorização de refatorações
- Recomendações de testes
- Plano de ação para correções
