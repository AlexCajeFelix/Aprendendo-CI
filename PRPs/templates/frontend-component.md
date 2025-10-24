# [Nome do Componente Frontend]

**Tipo:** Componente Frontend Reutilizável
**Complexidade:** [Baixa/Média/Alta]
**Tempo Estimado:** [1-8 horas]
**Versão:** 1.0

## 🎯 Objetivo

Desenvolver um componente frontend reutilizável e bem documentado para [descrição do componente].

### Por que este componente é necessário?
- [Motivo 1]
- [Motivo 2]
- [Motivo 3]

### Critérios de Sucesso
- [ ] Componente reutilizável e bem estruturado
- [ ] Props bem definidas e tipadas
- [ ] Testes unitários completos
- [ ] Documentação e exemplos
- [ ] Acessibilidade implementada

## 📋 O que será construído

### Interface do Componente
- Props bem definidas e tipadas
- Eventos customizados
- Estados internos gerenciados
- Validação de props
- Tratamento de erros

### Funcionalidades Principais
1. **[Funcionalidade 1]**
   - Descrição: [Detalhes da funcionalidade]
   - Props necessárias: [Lista de props]
   - Critérios de aceitação: [Como validar se está funcionando]

2. **[Funcionalidade 2]**
   - Descrição: [Detalhes da funcionalidade]
   - Props necessárias: [Lista de props]
   - Critérios de aceitação: [Como validar se está funcionando]

## 🧠 Todo Contexto Necessário

### Stack Tecnológico
- **Framework:** [React/Vue/Angular/Svelte]
- **Linguagem:** [TypeScript/JavaScript]
- **Styling:** [CSS Modules/Styled Components/Tailwind]
- **Testes:** [Jest/Vitest/Cypress]

### Documentação & Referências

- **url:** https://framework.com/docs/components
  **por que:** Documentação oficial de componentes

- **arquivo:** src/components/existing-component.tsx
  **por que:** Padrão de componentes existente no projeto

- **doc:** https://design-system.com/components
  **seção:** Padrões de design system

### Armadilhas Conhecidas

# CRÍTICO: Implementar acessibilidade (ARIA labels, keyboard navigation)
# IMPORTANTE: Validar props obrigatórias
# NOTA: Considerar performance com React.memo se necessário

### Padrões do Projeto

```typescript
// Exemplo de componente React
import React, { useState, useEffect } from 'react';

interface ComponentProps {
  title: string;
  onAction: (data: any) => void;
  disabled?: boolean;
  className?: string;
}

const Component: React.FC<ComponentProps> = ({
  title,
  onAction,
  disabled = false,
  className = ''
}) => {
  const [isLoading, setIsLoading] = useState(false);

  const handleAction = async () => {
    setIsLoading(true);
    try {
      await onAction({});
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={`component ${className}`}>
      <h2>{title}</h2>
      <button 
        onClick={handleAction}
        disabled={disabled || isLoading}
        aria-label={`Executar ação para ${title}`}
      >
        {isLoading ? 'Carregando...' : 'Ação'}
      </button>
    </div>
  );
};

export default Component;
```

## 🏗️ Blueprint de Implementação

### Etapa 1: Estrutura Base
```pseudocode
1. Criar arquivo do componente
2. Definir interface de props
3. Implementar estrutura básica
4. Configurar exportações
5. Adicionar tipos TypeScript
```

### Etapa 2: Funcionalidades
```pseudocode
1. Implementar lógica principal
2. Adicionar estados internos
3. Implementar eventos
4. Adicionar validações
5. Configurar tratamento de erros
```

### Etapa 3: Styling e UX
```pseudocode
1. Implementar estilos
2. Adicionar estados visuais
3. Configurar responsividade
4. Implementar animações
5. Otimizar acessibilidade
```

### Etapa 4: Testes
```pseudocode
1. Criar testes unitários
2. Testar props e eventos
3. Testar estados internos
4. Testar acessibilidade
5. Validar renderização
```

### Estrutura de Arquivos Esperada

```
components/
├── ComponentName/
│   ├── index.ts              # Exportações
│   ├── ComponentName.tsx     # Componente principal
│   ├── ComponentName.module.css # Estilos
│   ├── ComponentName.test.tsx   # Testes
│   ├── ComponentName.stories.tsx # Storybook
│   └── types.ts              # Tipos específicos
```

## 🔄 Loop de Validação

### Nível 1: Sintaxe & Estilo
```bash
# Verificar sintaxe e estilo
npm run lint
npm run type-check
npm run format

# Verificar componente específico
npm run lint src/components/ComponentName/
```

### Nível 2: Testes Unitários
```bash
# Executar testes do componente
npm test ComponentName

# Verificar cobertura
npm run test:coverage -- ComponentName
```

### Nível 3: Teste Visual
```bash
# Executar Storybook
npm run storybook

# Validar renderização
# - Props diferentes
# - Estados internos
# - Responsividade
# - Acessibilidade
```

### Nível 4: Teste de Integração
```bash
# Testar em aplicação real
npm run dev

# Validar uso do componente
# - Props funcionando
# - Eventos disparando
# - Estilos aplicados
# - Performance adequada
```

## 📦 Entregáveis Esperados

### Componente
- [ ] Arquivo principal implementado
- [ ] Props bem definidas e tipadas
- [ ] Estados internos gerenciados
- [ ] Eventos customizados
- [ ] Tratamento de erros

### Styling
- [ ] Estilos implementados
- [ ] Responsividade
- [ ] Estados visuais (hover, focus, disabled)
- [ ] Animações suaves
- [ ] Acessibilidade visual

### Testes
- [ ] Testes unitários completos
- [ ] Testes de props
- [ ] Testes de eventos
- [ ] Testes de acessibilidade
- [ ] Storybook stories

### Documentação
- [ ] README do componente
- [ ] Exemplos de uso
- [ ] Documentação de props
- [ ] Guia de acessibilidade
- [ ] Changelog

## ✅ Critérios de Qualidade

### Funcionalidade
- [ ] Props funcionando corretamente
- [ ] Eventos disparando adequadamente
- [ ] Estados internos gerenciados
- [ ] Validações implementadas
- [ ] Tratamento de erros

### Performance
- [ ] Renderização otimizada
- [ ] Sem memory leaks
- [ ] Lazy loading se necessário
- [ ] Bundle size otimizado

### Acessibilidade
- [ ] ARIA labels implementados
- [ ] Keyboard navigation
- [ ] Screen reader friendly
- [ ] Contraste adequado
- [ ] Focus management

### Reutilização
- [ ] Props bem definidas
- [ ] Interface clara
- [ ] Documentação completa
- [ ] Exemplos de uso
- [ ] Versão semântica

## 📚 Exemplos e Referências

### Exemplo de Uso
```typescript
import Component from './components/ComponentName';

// Uso básico
<Component
  title="Título do Componente"
  onAction={(data) => console.log('Ação executada:', data)}
/>

// Uso avançado
<Component
  title="Título Personalizado"
  onAction={handleComplexAction}
  disabled={isLoading}
  className="custom-styles"
/>
```

### Exemplo de Teste
```typescript
import { render, screen, fireEvent } from '@testing-library/react';
import Component from './ComponentName';

describe('ComponentName', () => {
  it('should render with correct title', () => {
    render(<Component title="Test Title" onAction={jest.fn()} />);
    expect(screen.getByText('Test Title')).toBeInTheDocument();
  });

  it('should call onAction when button is clicked', () => {
    const mockAction = jest.fn();
    render(<Component title="Test" onAction={mockAction} />);
    
    fireEvent.click(screen.getByRole('button'));
    expect(mockAction).toHaveBeenCalled();
  });
});
```

### Exemplo de Storybook
```typescript
import type { Meta, StoryObj } from '@storybook/react';
import Component from './ComponentName';

const meta: Meta<typeof Component> = {
  title: 'Components/ComponentName',
  component: Component,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
};

export default meta;
type Story = StoryObj<typeof meta>;

export const Default: Story = {
  args: {
    title: 'Título Padrão',
    onAction: () => console.log('Ação executada'),
  },
};

export const Disabled: Story = {
  args: {
    title: 'Componente Desabilitado',
    onAction: () => console.log('Ação executada'),
    disabled: true,
  },
};
```

## 🔧 Configuração de Desenvolvimento

### Pré-requisitos
- Node.js >= 18.0.0
- npm >= 8.0.0
- Framework escolhido configurado

### Comandos de Desenvolvimento
```bash
# Instalar dependências
npm install

# Executar em desenvolvimento
npm run dev

# Executar testes
npm test

# Executar Storybook
npm run storybook

# Build para produção
npm run build
```

### Estrutura de Props
```typescript
interface ComponentProps {
  // Props obrigatórias
  title: string;
  onAction: (data: any) => void;
  
  // Props opcionais
  disabled?: boolean;
  className?: string;
  size?: 'small' | 'medium' | 'large';
  variant?: 'primary' | 'secondary' | 'danger';
  
  // Props avançadas
  loading?: boolean;
  error?: string;
  onError?: (error: string) => void;
}
```

## 📝 Notas Adicionais

- Considerar implementação de React.memo para performance
- Implementar forwardRef se necessário
- Configurar PropTypes ou usar TypeScript
- Considerar implementação de hooks customizados
- Planejar versionamento semântico

---

**Instruções para IA:**
1. Analise o contexto do projeto e padrões existentes
2. Implemente o componente seguindo o blueprint
3. Execute todos os comandos de validação
4. Crie testes abrangentes
5. Documente o componente adequadamente
6. Configure Storybook stories
7. Valide acessibilidade e performance
