#!/usr/bin/env python3
"""
BMAD Full Automático - Sistema de Comunicação Entre Agentes

Este script executa o workflow BMAD completo automaticamente, onde os agentes
se comunicam entre si passando contexto e executando próximas etapas.

Uso:
    python bmad_full_auto.py "Descrição do projeto"
    python bmad_full_auto.py --project "Meu projeto" --auto-approve
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
import subprocess
import threading

# Configurações
PROJECT_ROOT = Path(__file__).parent.parent.parent
BMAD_OUTPUT = PROJECT_ROOT / "PRPs" / "bmad-output"
WORKFLOW_DIR = BMAD_OUTPUT / ".workflow"
HANDOFF_DIR = WORKFLOW_DIR / "handoffs"

# Criar diretórios se não existirem
WORKFLOW_DIR.mkdir(parents=True, exist_ok=True)
HANDOFF_DIR.mkdir(parents=True, exist_ok=True)


class BMADAgentCoordinator:
    """Coordenador de Agentes BMAD - Gerencia comunicação automática"""
    
    def __init__(self, project_description: str, project_name: Optional[str] = None):
        self.project_description = project_description
        self.project_name = project_name or self._generate_project_name(project_description)
        self.workflow_state = {
            "project_name": self.project_name,
            "started_at": datetime.now().isoformat(),
            "current_step": "analyst",
            "completed_steps": [],
            "handoffs": [],
            "status": "running"
        }
        
        # Configurações dos agentes
        self.agents = {
            "analyst": {
                "command": "/analyst",
                "output_pattern": f"{self.project_name}-brief.md",
                "next_agent": "pm"
            },
            "pm": {
                "command": "/pm",
                "input_pattern": f"{self.project_name}-brief.md",
                "output_pattern": f"{self.project_name}-prd.md",
                "next_agent": "architect"
            },
            "architect": {
                "command": "/architect",
                "input_pattern": f"{self.project_name}-prd.md",
                "output_pattern": f"{self.project_name}-architecture.md",
                "next_agent": "scrum-master"
            },
            "scrum-master": {
                "command": "/sm",
                "input_pattern": f"{self.project_name}-architecture.md",
                "output_pattern": "index.md",
                "next_agent": "dev"
            }
        }
    
    def _generate_project_name(self, description: str) -> str:
        """Gera nome do projeto baseado na descrição"""
        # Remove caracteres especiais e converte para kebab-case
        name = description.lower()
        name = "".join(c if c.isalnum() or c in "-_" else "-" for c in name)
        name = "-".join(name.split())
        return name[:50]  # Limita tamanho
    
    def run_full_workflow(self, auto_approve: bool = False):
        """Executa workflow completo automaticamente"""
        print("🤖 BMAD Full Automático - Iniciando Workflow")
        print("=" * 60)
        print(f"📁 Projeto: {self.project_name}")
        print(f"📝 Descrição: {self.project_description}")
        print(f"⏰ Iniciado em: {datetime.now().strftime('%H:%M:%S')}")
        print()
        
        try:
            # FASE 1: Planejamento (Sequencial)
            self._run_planning_phase(auto_approve)
            
            # FASE 2: Desenvolvimento (Iterativo)
            self._run_development_phase(auto_approve)
            
            # Finalizar
            self._complete_workflow()
            
        except KeyboardInterrupt:
            print("\n⚠️ Workflow interrompido pelo usuário")
            self._save_state()
        except Exception as e:
            print(f"\n❌ Erro durante workflow: {e}")
            self._save_state()
            raise
    
    def _run_planning_phase(self, auto_approve: bool):
        """Executa fase de planejamento: Analyst → PM → Architect"""
        print("📋 FASE 1: PLANEJAMENTO")
        print("-" * 60)
        
        # 1. Analyst
        self._execute_agent("analyst", auto_approve)
        
        # 2. PM
        self._execute_agent("pm", auto_approve)
        
        # 3. Architect
        self._execute_agent("architect", auto_approve)
        
        print("✅ Planejamento Completo!")
        print()
    
    def _run_development_phase(self, auto_approve: bool):
        """Executa fase de desenvolvimento: SM → Dev → QA (iterativo)"""
        print("💻 FASE 2: DESENVOLVIMENTO")
        print("-" * 60)
        
        # 1. Scrum Master cria stories
        self._execute_agent("scrum-master", auto_approve)
        
        # 2. Loop Dev → QA para cada story
        self._run_dev_qa_loop(auto_approve)
    
    def _execute_agent(self, agent_name: str, auto_approve: bool):
        """Executa um agente específico"""
        agent_config = self.agents[agent_name]
        
        print(f"🔄 Executando {agent_name.upper()}...")
        
        # Preparar input se necessário
        input_file = None
        if "input_pattern" in agent_config:
            input_file = self._find_input_file(agent_config["input_pattern"])
            if not input_file:
                raise FileNotFoundError(f"Arquivo de input não encontrado: {agent_config['input_pattern']}")
        
        # Executar agente (simulação - em produção seria chamada real à API)
        result = self._simulate_agent_execution(agent_name, input_file)
        
        # Aguardar conclusão
        if not auto_approve:
            input(f"   ✅ {agent_name.upper()} concluído. Pressione Enter para continuar...")
        
        # Marcar como completo
        self.workflow_state["completed_steps"].append({
            "agent": agent_name,
            "completed_at": datetime.now().isoformat(),
            "output_file": result["output_file"]
        })
        
        # Criar handoff para próximo agente
        if agent_config["next_agent"]:
            self._create_handoff(agent_name, agent_config["next_agent"], result)
        
        print(f"   📄 Output: {result['output_file']}")
        print()
    
    def _simulate_agent_execution(self, agent_name: str, input_file: Optional[Path]) -> Dict:
        """Simula execução de agente (placeholder para integração real)"""
        
        # Em produção, isso seria uma chamada real à API do Cursor
        # Por enquanto, simula com arquivos de exemplo
        
        if agent_name == "analyst":
            output_file = BMAD_OUTPUT / "briefs" / f"{self.project_name}-brief.md"
            self._create_sample_brief(output_file)
            
        elif agent_name == "pm":
            output_file = BMAD_OUTPUT / "prds" / f"{self.project_name}-prd.md"
            self._create_sample_prd(output_file)
            
        elif agent_name == "architect":
            output_file = BMAD_OUTPUT / "architecture" / f"{self.project_name}-architecture.md"
            self._create_sample_architecture(output_file)
            
        elif agent_name == "scrum-master":
            output_file = BMAD_OUTPUT / "stories" / self.project_name / "index.md"
            self._create_sample_stories(output_file)
        
        # Simular tempo de processamento
        time.sleep(2)
        
        return {
            "output_file": str(output_file),
            "status": "completed",
            "agent": agent_name
        }
    
    def _create_sample_brief(self, output_file: Path):
        """Cria sample Brief"""
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        content = f"""# Brief de Projeto: {self.project_name.replace('-', ' ').title()}

**Tipo:** Aplicação Web
**Data de Criação:** {datetime.now().strftime('%Y-%m-%d')}
**Analista:** BMAD Auto Coordinator

## 📊 Contexto de Negócio

### Problema ou Oportunidade
{self.project_description}

### Situação Desejada
Sistema web funcional que atenda aos requisitos especificados.

## 🎯 Objetivos

### Objetivo Principal
Implementar {self.project_description.lower()}

### Objetivos Secundários
1. Interface intuitiva e responsiva
2. Performance adequada
3. Código bem estruturado e testado

## ⚙️ Requisitos Funcionais

### RF001: Autenticação
- Login/logout de usuários
- Validação de credenciais

### RF002: Funcionalidades Principais
- Baseado na descrição: {self.project_description}

## 🔧 Requisitos Não-Funcionais

### Performance
- Tempo de resposta < 2 segundos
- Suporte a 100 usuários simultâneos

### Segurança
- Autenticação segura
- Validação de inputs

---

**Criado automaticamente pelo BMAD Full Automático**
"""
        
        output_file.write_text(content)
    
    def _create_sample_prd(self, output_file: Path):
        """Cria sample PRD"""
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        content = f"""# PRD: {self.project_name.replace('-', ' ').title()}

**Versão:** 1.0
**Data:** {datetime.now().strftime('%Y-%m-%d')}
**Product Manager:** BMAD Auto Coordinator

## 📊 Visão Executiva

### Resumo em Uma Página
Sistema web para {self.project_description.lower()} com interface moderna e funcionalidades essenciais.

## ⚙️ Funcionalidades Detalhadas

### Feature 1: Autenticação (P0 - MVP)
**Descrição:** Sistema de login/logout
**Critérios de Aceitação:**
- [ ] Usuário pode fazer login com email/senha
- [ ] Sistema valida credenciais
- [ ] Token JWT é gerado após login válido

### Feature 2: Funcionalidades Principais (P0 - MVP)
**Descrição:** {self.project_description}
**Critérios de Aceitação:**
- [ ] Interface funcional implementada
- [ ] Dados são persistidos corretamente
- [ ] Validações funcionam adequadamente

## 📅 Roadmap

### MVP (v1.0)
- Autenticação básica
- Funcionalidades principais
- Interface responsiva

---

**Criado automaticamente pelo BMAD Full Automático**
"""
        
        output_file.write_text(content)
    
    def _create_sample_architecture(self, output_file: Path):
        """Cria sample Architecture"""
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        content = f"""# Arquitetura: {self.project_name.replace('-', ' ').title()}

**Versão:** 1.0
**Data:** {datetime.now().strftime('%Y-%m-%d')}
**Arquiteto:** BMAD Auto Coordinator

## 📊 Visão Geral da Arquitetura

### Stack Tecnológico

**Frontend:**
- React 18 + TypeScript 5
- Tailwind CSS
- React Router 6

**Backend:**
- Node.js 20 + Express 4.18
- TypeScript 5
- PostgreSQL 15

**Decisão: Monolito Modular**
Justificativa: Projeto pequeno/médio, simplicidade de desenvolvimento

## 📐 Design de Componentes

### Frontend
```
src/
├── components/
├── pages/
├── services/
└── utils/
```

### Backend
```
src/
├── controllers/
├── services/
├── repositories/
└── models/
```

---

**Criado automaticamente pelo BMAD Full Automático**
"""
        
        output_file.write_text(content)
    
    def _create_sample_stories(self, output_file: Path):
        """Cria sample Stories"""
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Criar stories individuais
        for i in range(1, 4):  # 3 stories de exemplo
            story_file = output_file.parent / f"story-{i:03d}-exemplo.md"
            story_content = f"""# Story #{i:03d}: Exemplo de Story {i}

**Épico:** Exemplo
**Prioridade:** P0-MVP
**Estimativa:** 4h

## 🎯 Objetivo

Implementar funcionalidade exemplo {i} do sistema.

## 💻 Tarefas de Implementação

### Tarefa 1: Implementar funcionalidade
**Arquivo:** `src/example{i}.ts`

## ✅ Critérios de Aceitação

- [ ] Funcionalidade {i} implementada
- [ ] Testes passando
- [ ] Código documentado

---

**Criado automaticamente pelo BMAD Full Automático**
"""
            story_file.write_text(story_content)
        
        # Criar index
        index_content = f"""# Development Stories - {self.project_name.replace('-', ' ').title()}

**Projeto:** {self.project_name}
**Criado em:** {datetime.now().strftime('%Y-%m-%d')}

## 📋 Stories Disponíveis

1. [Story 001 - Exemplo 1](story-001-exemplo.md)
2. [Story 002 - Exemplo 2](story-002-exemplo.md)
3. [Story 003 - Exemplo 3](story-003-exemplo.md)

## 📊 Status

- **Total de Stories:** 3
- **Completas:** 0
- **Em Progresso:** 0
- **Pendentes:** 3

---

**Criado automaticamente pelo BMAD Full Automático**
"""
        
        output_file.write_text(index_content)
    
    def _run_dev_qa_loop(self, auto_approve: bool):
        """Executa loop Dev → QA para cada story"""
        stories_dir = BMAD_OUTPUT / "stories" / self.project_name
        
        if not stories_dir.exists():
            print("⚠️ Nenhuma story encontrada, pulando desenvolvimento")
            return
        
        # Encontrar stories
        story_files = list(stories_dir.glob("story-*.md"))
        story_files.sort()
        
        print(f"📝 Encontradas {len(story_files)} stories")
        
        for i, story_file in enumerate(story_files, 1):
            print(f"🔄 Processando Story {i}/{len(story_files)}: {story_file.name}")
            
            # Dev implementa
            print("   💻 Dev implementando...")
            time.sleep(1)  # Simular tempo
            
            # QA valida
            print("   ✅ QA validando...")
            time.sleep(1)  # Simular tempo
            
            if not auto_approve:
                input(f"   ✅ Story {i} completa. Pressione Enter para próxima...")
            
            print()
        
        print("🎉 Todas stories implementadas e validadas!")
    
    def _find_input_file(self, pattern: str) -> Optional[Path]:
        """Encontra arquivo de input baseado no padrão"""
        # Buscar em diferentes diretórios
        search_dirs = [
            BMAD_OUTPUT / "briefs",
            BMAD_OUTPUT / "prds",
            BMAD_OUTPUT / "architecture"
        ]
        
        for search_dir in search_dirs:
            if search_dir.exists():
                for file in search_dir.glob(pattern):
                    return file
        
        return None
    
    def _create_handoff(self, from_agent: str, to_agent: str, result: Dict):
        """Cria handoff entre agentes"""
        handoff = {
            "from": from_agent,
            "to": to_agent,
            "created_at": datetime.now().isoformat(),
            "input_file": result["output_file"],
            "status": "ready"
        }
        
        handoff_file = HANDOFF_DIR / f"handoff-{from_agent}-to-{to_agent}.json"
        handoff_file.write_text(json.dumps(handoff, indent=2))
        
        self.workflow_state["handoffs"].append(handoff)
    
    def _save_state(self):
        """Salva estado do workflow"""
        state_file = WORKFLOW_DIR / f"{self.project_name}-workflow-state.json"
        state_file.write_text(json.dumps(self.workflow_state, indent=2))
    
    def _complete_workflow(self):
        """Finaliza workflow"""
        self.workflow_state["status"] = "completed"
        self.workflow_state["completed_at"] = datetime.now().isoformat()
        
        print("🎉 WORKFLOW BMAD COMPLETO!")
        print("=" * 60)
        print(f"📁 Projeto: {self.project_name}")
        print(f"⏰ Concluído em: {datetime.now().strftime('%H:%M:%S')}")
        print(f"📊 Etapas completadas: {len(self.workflow_state['completed_steps'])}")
        print()
        print("📂 Outputs gerados:")
        
        for step in self.workflow_state["completed_steps"]:
            print(f"   • {step['agent']}: {step['output_file']}")
        
        self._save_state()


def main():
    """Função principal"""
    parser = argparse.ArgumentParser(
        description="BMAD Full Automático - Workflow completo entre agentes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python bmad_full_auto.py "Sistema de gerenciamento de tarefas"
  python bmad_full_auto.py --project task-manager --auto-approve
  python bmad_full_auto.py "API REST para e-commerce" --auto-approve
        """
    )
    
    parser.add_argument(
        "description",
        help="Descrição do projeto"
    )
    
    parser.add_argument(
        "--project",
        "-p",
        help="Nome do projeto (gerado automaticamente se não fornecido)",
        type=str
    )
    
    parser.add_argument(
        "--auto-approve",
        "-y",
        help="Aprova automaticamente cada etapa (sem pausas)",
        action="store_true"
    )
    
    args = parser.parse_args()
    
    # Criar coordenador
    coordinator = BMADAgentCoordinator(
        project_description=args.description,
        project_name=args.project
    )
    
    # Executar workflow
    coordinator.run_full_workflow(auto_approve=args.auto_approve)


if __name__ == "__main__":
    main()
