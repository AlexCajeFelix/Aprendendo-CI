# Criar Especificação Avançada

Cria especificações técnicas detalhadas com requisitos funcionais e não funcionais, arquitetura e estratégia de testes.

## Argumentos: $ARGUMENTS

Forneça uma descrição do que precisa ser especificado. Exemplo:
- "API REST para gerenciamento de pedidos"
- "sistema de autenticação e autorização"
- "dashboard de métricas em tempo real"

## Como usar

1. **Analise os requisitos** funcionais e não funcionais
2. **Defina arquitetura** e componentes
3. **Especifique interfaces** e contratos
4. **Documente modelo de dados**
5. **Defina estratégia de testes**
6. **Crie plano de implementação**

## Seções incluídas

### Requisitos Funcionais
- Descrição detalhada de funcionalidades
- Critérios de aceitação claros
- Priorização de requisitos
- Casos de uso

### Requisitos Não Funcionais
- Performance e escalabilidade
- Segurança e privacidade
- Usabilidade e acessibilidade
- Compatibilidade

### Arquitetura Técnica
- Diagramas de componentes
- Fluxos de dados
- Interfaces e APIs
- Padrões arquiteturais

### Modelo de Dados
- Entidades e relacionamentos
- Regras de negócio
- Validações e constraints
- Estrutura de banco

### Estratégia de Testes
- Testes unitários
- Testes de integração
- Testes E2E
- Cenários de teste

## Template usado

O comando usa o template `PRPs/templates/prp_spec.md` como base.

## Exemplo de uso

```
/spec-create sistema de notificações push com múltiplos canais
```

## Saída esperada

- Especificação técnica completa
- Requisitos funcionais e não funcionais
- Arquitetura detalhada com diagramas
- Modelo de dados estruturado
- Estratégia de testes abrangente
- Plano de implementação
- Análise de riscos
- Pronto para execução com `/spec-execute`
