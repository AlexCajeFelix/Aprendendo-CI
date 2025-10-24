# Criar Documento de Planejamento

Cria documentos de planejamento detalhados com diagramas e fluxos de trabalho para projetos complexos.

## Argumentos: $ARGUMENTS

Forneça uma descrição do projeto/feature que precisa ser planejado. Exemplo:
- "sistema de e-commerce completo"
- "arquitetura de microserviços"
- "dashboard de analytics"

## Como usar

1. **Analise os requisitos** do projeto
2. **Crie diagramas de arquitetura** usando Mermaid
3. **Defina fluxos de trabalho** detalhados
4. **Estruture fases de implementação**
5. **Identifique dependências** e riscos
6. **Documente decisões técnicas**

## Tipos de planejamento

### Planejamento Arquitetural
- Diagramas de sistema
- Fluxos de dados
- Interfaces entre componentes
- Padrões de comunicação

### Planejamento de Desenvolvimento
- Fases de implementação
- Cronograma de entregas
- Dependências técnicas
- Recursos necessários

### Planejamento de Qualidade
- Estratégia de testes
- Critérios de aceitação
- Métricas de qualidade
- Processos de review

## Template usado

O comando usa o template `PRPs/templates/prp_planning_base.md` como base.

## Exemplo de uso

```
/planning-create sistema de pagamentos com múltiplos gateways
```

## Saída esperada

- Documento de planejamento completo
- Diagramas de arquitetura em Mermaid
- Fluxos de trabalho detalhados
- Cronograma de implementação
- Análise de riscos e mitigações
- Estratégia de testes
- Pronto para execução com `/spec-execute`
