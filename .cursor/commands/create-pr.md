# Criar Pull Request

Cria um Pull Request no GitHub com base nas mudanças locais, incluindo descrição detalhada e checklist.

## Argumentos: $ARGUMENTS

Forneça informações para o PR:
- Título do PR (opcional)
- Descrição das mudanças (opcional)
- ou deixe vazio para usar informações do Git

## Como usar

1. **Analise mudanças** no branch atual
2. **Gere título** descritivo baseado nos commits
3. **Crie descrição** detalhada das mudanças
4. **Inclua checklist** de validação
5. **Adicione labels** apropriados
6. **Configure reviewers** se necessário

## Informações incluídas

### Título do PR
- Baseado nos commits recentes
- Seguindo convenção de commits
- Descritivo e claro

### Descrição Detalhada
- Resumo das mudanças
- Funcionalidades implementadas
- Correções realizadas
- Melhorias de performance

### Checklist de Validação
- [ ] Código revisado
- [ ] Testes passando
- [ ] Documentação atualizada
- [ ] Performance validada
- [ ] Segurança verificada

### Informações Técnicas
- Arquivos modificados
- Linhas alteradas
- Dependências atualizadas
- Breaking changes

### Screenshots/Demo
- Capturas de tela (se aplicável)
- Links para demo
- Documentação visual

## Exemplo de uso

```
/create-pr "Implementa sistema de autenticação JWT"
```

## Requisitos

- Mudanças devem estar commitadas
- Branch deve estar sincronizado
- Repositório deve ter acesso ao GitHub
- Configuração de GitHub deve estar correta

## Saída esperada

- Pull Request criado no GitHub
- Título e descrição apropriados
- Checklist de validação incluído
- Labels e reviewers configurados
- Link para o PR criado
