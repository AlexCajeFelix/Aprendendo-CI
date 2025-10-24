# [Nome do Projeto/Feature]

**Tipo:** [Tipo do PRP - ex: Aplicação Web, API, Componente, etc.]
**Complexidade:** [Baixa/Média/Alta]
**Tempo Estimado:** [Estimativa em horas]
**Versão:** 1.0

## 🎯 Objetivo

[Descrição clara e concisa do que será desenvolvido]

### Por que este projeto/feature é necessário?
- [Motivo 1]
- [Motivo 2]
- [Motivo 3]

### Critérios de Sucesso
- [ ] [Critério 1]
- [ ] [Critério 2]
- [ ] [Critério 3]

## 📋 O que será construído

[Descrição detalhada do que será implementado]

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

## 🧠 Todo Contexto Necessário

### Documentação & Referências

- **url:** https://exemplo.com/documentacao
  **por que:** [Por que esta documentação é importante]

- **arquivo:** src/exemplo/existing_code.py
  **por que:** [Padrão atual a ser seguido ou substituído]

- **doc:** https://framework.com/docs/feature
  **seção:** [Seção específica relevante]

### Armadilhas Conhecidas

# CRÍTICO: [Armadilha importante a evitar]
# IMPORTANTE: [Consideração importante]
# NOTA: [Observação adicional]

### Padrões do Projeto

```typescript
// Exemplo de padrão existente no projeto
interface User {
  id: string;
  name: string;
  email: string;
}
```

### Convenções de Código

- **Linguagem:** [Linguagem principal]
- **Framework:** [Framework utilizado]
- **Convenções:** [Convenções de código a seguir]
- **Testes:** [Estratégia de testes]

## 🏗️ Blueprint de Implementação

### Etapa 1: [Nome da Etapa]
```pseudocode
// Pseudocódigo da implementação
1. Criar estrutura básica
2. Implementar funcionalidade principal
3. Adicionar validações
4. Criar testes
```

### Etapa 2: [Nome da Etapa]
```pseudocode
// Pseudocódigo da implementação
1. Implementar funcionalidade secundária
2. Adicionar tratamento de erros
3. Otimizar performance
4. Documentar código
```

### Estrutura de Arquivos Esperada

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

## 🔄 Loop de Validação

### Nível 1: Sintaxe & Estilo
```bash
# Comandos que a IA pode executar para validar
npm run lint
npm run type-check
```

### Nível 2: Testes Unitários
```bash
# Comandos de teste
npm test
npm run test:coverage
```

### Nível 3: Teste de Integração
```bash
# Teste manual ou automatizado
curl -X POST http://localhost:3000/api/test \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'
```

### Nível 4: Validação Funcional
- [ ] [Funcionalidade 1 funciona conforme esperado]
- [ ] [Funcionalidade 2 funciona conforme esperado]
- [ ] [Interface está responsiva]
- [ ] [Performance está aceitável]

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

## 📚 Exemplos e Referências

### Exemplos de Uso
```typescript
// Exemplo de como usar o componente/funcionalidade
import { MinhaFuncionalidade } from './components/MinhaFuncionalidade';

const App = () => {
  return (
    <MinhaFuncionalidade 
      prop1="valor1" 
      prop2="valor2" 
    />
  );
};
```

### Referências
- [Link para documentação relevante]
- [Exemplo similar em outro projeto]
- [Padrões de design utilizados]

## 🔧 Configuração de Desenvolvimento

### Pré-requisitos
- Node.js >= 18.0.0
- npm >= 8.0.0
- [Outras dependências]

### Comandos de Desenvolvimento
```bash
# Instalar dependências
npm install

# Executar em desenvolvimento
npm run dev

# Executar testes
npm test

# Build para produção
npm run build
```

### Variáveis de Ambiente
```env
# Configurações necessárias
API_URL=http://localhost:3000
DATABASE_URL=postgresql://...
SECRET_KEY=your-secret-key
```

## 📝 Notas Adicionais

[Qualquer informação adicional que seja relevante para a implementação]

---

**Instruções para IA:**
1. Leia todo o contexto fornecido
2. Implemente seguindo exatamente o blueprint
3. Execute os comandos de validação
4. Corrija qualquer erro encontrado
5. Valide se todos os critérios de sucesso foram atendidos
6. Documente o código conforme necessário
