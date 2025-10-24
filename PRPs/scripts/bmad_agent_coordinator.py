#!/usr/bin/env python3
"""
BMAD Agent Coordinator - Sistema Avançado de Comunicação Entre Agentes

Este script implementa um sistema real de comunicação entre agentes BMAD,
permitindo que eles se comuniquem via arquivos de handoff e coordenem
execução automática do workflow.
"""

import os
import sys
import json
import time
import asyncio
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
import subprocess
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configurações
PROJECT_ROOT = Path(__file__).parent.parent.parent
BMAD_OUTPUT = PROJECT_ROOT / "PRPs" / "bmad-output"
WORKFLOW_DIR = BMAD_OUTPUT / ".workflow"
HANDOFF_DIR = WORKFLOW_DIR / "handoffs"
STATUS_DIR = WORKFLOW_DIR / "status"

# Criar diretórios
for dir_path in [WORKFLOW_DIR, HANDOFF_DIR, STATUS_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)


class HandoffEvent(FileSystemEventHandler):
    """Monitor de eventos de handoff entre agentes"""
    
    def __init__(self, coordinator):
        self.coordinator = coordinator
    
    def on_created(self, event):
        if event.is_file and event.src_path.endswith('.json'):
            handoff_file = Path(event.src_path)
            if handoff_file.parent == HANDOFF_DIR:
                print(f"📨 Novo handoff detectado: {handoff_file.name}")
                self.coordinator.process_handoff(handoff_file)


class BMADAgentCoordinator:
    """Coordenador avançado de agentes BMAD"""
    
    def __init__(self):
        self.active_workflows = {}
        self.agent_queue = []
        self.running = False
        
        # Configurações dos agentes
        self.agent_configs = {
            "analyst": {
                "command": "/analyst",
                "input_type": "description",
                "output_type": "brief",
                "next_agents": ["pm"],
                "timeout": 300,  # 5 minutos
                "retries": 3
            },
            "pm": {
                "command": "/pm",
                "input_type": "brief",
                "output_type": "prd",
                "next_agents": ["architect"],
                "timeout": 300,
                "retries": 3
            },
            "architect": {
                "command": "/architect",
                "input_type": "prd",
                "output_type": "architecture",
                "next_agents": ["scrum-master"],
                "timeout": 300,
                "retries": 3
            },
            "scrum-master": {
                "command": "/sm",
                "input_type": "architecture",
                "output_type": "stories",
                "next_agents": ["dev"],
                "timeout": 300,
                "retries": 3
            },
            "dev": {
                "command": "/dev",
                "input_type": "story",
                "output_type": "code",
                "next_agents": ["qa"],
                "timeout": 600,  # 10 minutos
                "retries": 3
            },
            "qa": {
                "command": "/qa",
                "input_type": "code",
                "output_type": "report",
                "next_agents": [],  # QA é final na chain
                "timeout": 300,
                "retries": 3
            }
        }
    
    def start_coordination(self):
        """Inicia sistema de coordenação"""
        print("🤖 BMAD Agent Coordinator - Iniciando Sistema")
        print("=" * 60)
        
        self.running = True
        
        # Configurar monitor de arquivos
        self.observer = Observer()
        event_handler = HandoffEvent(self)
        self.observer.schedule(event_handler, str(HANDOFF_DIR), recursive=False)
        self.observer.start()
        
        print("✅ Sistema de coordenação ativo")
        print("📁 Monitorando:", HANDOFF_DIR)
        print("🔄 Aguardando handoffs...")
        print()
        
        try:
            # Manter sistema rodando
            while self.running:
                time.sleep(1)
                
                # Processar fila de agentes
                self._process_agent_queue()
                
        except KeyboardInterrupt:
            print("\n⚠️ Sistema interrompido pelo usuário")
            self.stop_coordination()
    
    def stop_coordination(self):
        """Para sistema de coordenação"""
        print("🛑 Parando sistema de coordenação...")
        self.running = False
        if hasattr(self, 'observer'):
            self.observer.stop()
            self.observer.join()
        print("✅ Sistema parado")
    
    def initiate_workflow(self, project_description: str, project_name: Optional[str] = None):
        """Inicia novo workflow automaticamente"""
        if not project_name:
            project_name = self._generate_project_name(project_description)
        
        workflow_id = f"{project_name}-{int(time.time())}"
        
        workflow = {
            "id": workflow_id,
            "project_name": project_name,
            "description": project_description,
            "status": "initiated",
            "created_at": datetime.now().isoformat(),
            "current_step": "analyst",
            "completed_steps": [],
            "pending_steps": ["analyst", "pm", "architect", "scrum-master"],
            "stories": [],
            "dev_queue": []
        }
        
        self.active_workflows[workflow_id] = workflow
        self._save_workflow_state(workflow)
        
        # Criar primeiro handoff para Analyst
        self._create_initial_handoff(workflow)
        
        print(f"🚀 Workflow iniciado: {workflow_id}")
        print(f"📝 Projeto: {project_name}")
        print(f"📋 Descrição: {project_description}")
        
        return workflow_id
    
    def _create_initial_handoff(self, workflow: Dict):
        """Cria handoff inicial para Analyst"""
        handoff = {
            "workflow_id": workflow["id"],
            "from": "system",
            "to": "analyst",
            "created_at": datetime.now().isoformat(),
            "data": {
                "description": workflow["description"],
                "project_name": workflow["project_name"]
            },
            "status": "ready",
            "priority": "high"
        }
        
        self._save_handoff(handoff)
        
        # Adicionar Analyst à fila
        self._queue_agent("analyst", workflow["id"], handoff)
    
    def process_handoff(self, handoff_file: Path):
        """Processa handoff recebido"""
        try:
            handoff_data = json.loads(handoff_file.read_text())
            
            print(f"📨 Processando handoff: {handoff_data['from']} → {handoff_data['to']}")
            
            # Determinar workflow
            workflow_id = handoff_data.get("workflow_id")
            if workflow_id and workflow_id in self.active_workflows:
                workflow = self.active_workflows[workflow_id]
                
                # Processar handoff baseado no tipo
                if handoff_data["to"] in ["analyst", "pm", "architect", "scrum-master"]:
                    self._process_planning_handoff(handoff_data, workflow)
                elif handoff_data["to"] in ["dev", "qa"]:
                    self._process_development_handoff(handoff_data, workflow)
                
                # Atualizar estado do workflow
                self._save_workflow_state(workflow)
                
        except Exception as e:
            print(f"❌ Erro processando handoff {handoff_file}: {e}")
    
    def _process_planning_handoff(self, handoff: Dict, workflow: Dict):
        """Processa handoff da fase de planejamento"""
        target_agent = handoff["to"]
        
        # Marcar step anterior como completo
        if handoff["from"] != "system":
            workflow["completed_steps"].append(handoff["from"])
        
        # Adicionar próximo agente à fila
        if target_agent in workflow["pending_steps"]:
            workflow["pending_steps"].remove(target_agent)
            self._queue_agent(target_agent, workflow["id"], handoff)
        
        # Verificar se planejamento está completo
        if not workflow["pending_steps"] and workflow["current_step"] == "scrum-master":
            print(f"✅ Planejamento completo para {workflow['project_name']}")
            self._initiate_development_phase(workflow)
    
    def _process_development_handoff(self, handoff: Dict, workflow: Dict):
        """Processa handoff da fase de desenvolvimento"""
        target_agent = handoff["to"]
        
        if target_agent == "dev":
            # Dev recebeu story para implementar
            story_info = handoff["data"].get("story_info", {})
            self._queue_agent("dev", workflow["id"], handoff, story_info)
            
        elif target_agent == "qa":
            # QA recebeu implementação para validar
            self._queue_agent("qa", workflow["id"], handoff)
    
    def _initiate_development_phase(self, workflow: Dict):
        """Inicia fase de desenvolvimento após planejamento completo"""
        print(f"💻 Iniciando fase de desenvolvimento para {workflow['project_name']}")
        
        # Simular criação de stories (em produção, seria baseado na arquitetura)
        stories = [
            {"id": "story-001", "title": "Setup do Projeto", "estimated_hours": 2},
            {"id": "story-002", "title": "Autenticação Básica", "estimated_hours": 4},
            {"id": "story-003", "title": "CRUD Principal", "estimated_hours": 6},
            {"id": "story-004", "title": "Interface Frontend", "estimated_hours": 4}
        ]
        
        workflow["stories"] = stories
        workflow["dev_queue"] = stories.copy()
        workflow["current_step"] = "development"
        
        # Criar primeiro handoff para Dev
        if stories:
            first_story = stories[0]
            handoff = {
                "workflow_id": workflow["id"],
                "from": "scrum-master",
                "to": "dev",
                "created_at": datetime.now().isoformat(),
                "data": {
                    "story_info": first_story,
                    "project_name": workflow["project_name"]
                },
                "status": "ready",
                "priority": "normal"
            }
            
            self._save_handoff(handoff)
            self._queue_agent("dev", workflow["id"], handoff, first_story)
    
    def _queue_agent(self, agent_name: str, workflow_id: str, handoff: Dict, extra_data: Optional[Dict] = None):
        """Adiciona agente à fila de execução"""
        agent_task = {
            "agent": agent_name,
            "workflow_id": workflow_id,
            "handoff": handoff,
            "extra_data": extra_data,
            "queued_at": datetime.now().isoformat(),
            "status": "queued"
        }
        
        self.agent_queue.append(agent_task)
        print(f"📋 {agent_name.upper()} adicionado à fila para {workflow_id}")
    
    def _process_agent_queue(self):
        """Processa fila de agentes"""
        if not self.agent_queue:
            return
        
        # Processar primeiro agente na fila
        agent_task = self.agent_queue.pop(0)
        
        print(f"🔄 Executando {agent_task['agent'].upper()} para {agent_task['workflow_id']}")
        
        try:
            # Executar agente (simulação)
            self._execute_agent(agent_task)
            
        except Exception as e:
            print(f"❌ Erro executando {agent_task['agent']}: {e}")
            # Implementar retry logic aqui
    
    def _execute_agent(self, agent_task: Dict):
        """Executa agente específico"""
        agent_name = agent_task["agent"]
        workflow_id = agent_task["workflow_id"]
        
        config = self.agent_configs[agent_name]
        
        # Simular execução do agente
        print(f"   ⚙️ {agent_name.upper()} processando...")
        time.sleep(2)  # Simular tempo de processamento
        
        # Criar output simulado
        output_data = self._create_agent_output(agent_name, agent_task)
        
        # Marcar como completo
        agent_task["status"] = "completed"
        agent_task["completed_at"] = datetime.now().isoformat()
        agent_task["output"] = output_data
        
        print(f"   ✅ {agent_name.upper()} concluído")
        
        # Criar próximo handoff se necessário
        self._create_next_handoff(agent_task)
    
    def _create_agent_output(self, agent_name: str, agent_task: Dict) -> Dict:
        """Cria output simulado para agente"""
        workflow_id = agent_task["workflow_id"]
        workflow = self.active_workflows[workflow_id]
        
        base_path = BMAD_OUTPUT
        
        if agent_name == "analyst":
            output_file = base_path / "briefs" / f"{workflow['project_name']}-brief.md"
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(f"# Brief: {workflow['project_name']}\n\n{workflow['description']}")
            
        elif agent_name == "pm":
            output_file = base_path / "prds" / f"{workflow['project_name']}-prd.md"
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(f"# PRD: {workflow['project_name']}\n\nProduct requirements document")
            
        elif agent_name == "architect":
            output_file = base_path / "architecture" / f"{workflow['project_name']}-architecture.md"
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(f"# Architecture: {workflow['project_name']}\n\nTechnical architecture document")
            
        elif agent_name == "scrum-master":
            output_file = base_path / "stories" / workflow['project_name'] / "index.md"
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(f"# Stories: {workflow['project_name']}\n\nDevelopment stories")
            
        elif agent_name == "dev":
            story_info = agent_task.get("extra_data", {})
            story_id = story_info.get("id", "unknown")
            output_file = base_path / "implementations" / f"{story_id}-dev-notes.md"
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(f"# Dev Notes: {story_id}\n\nImplementation completed")
            
        elif agent_name == "qa":
            story_info = agent_task.get("extra_data", {})
            story_id = story_info.get("id", "unknown")
            output_file = base_path / "qa-reports" / f"{story_id}-qa-report.md"
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(f"# QA Report: {story_id}\n\n✅ APPROVED")
        
        return {
            "output_file": str(output_file),
            "agent": agent_name,
            "completed_at": datetime.now().isoformat()
        }
    
    def _create_next_handoff(self, completed_task: Dict):
        """Cria próximo handoff baseado no agente que acabou de executar"""
        agent_name = completed_task["agent"]
        workflow_id = completed_task["workflow_id"]
        workflow = self.active_workflows[workflow_id]
        
        config = self.agent_configs[agent_name]
        next_agents = config.get("next_agents", [])
        
        for next_agent in next_agents:
            if next_agent == "dev" and workflow["dev_queue"]:
                # Próxima story para Dev
                next_story = workflow["dev_queue"].pop(0)
                handoff = {
                    "workflow_id": workflow_id,
                    "from": agent_name,
                    "to": "dev",
                    "created_at": datetime.now().isoformat(),
                    "data": {
                        "story_info": next_story,
                        "project_name": workflow["project_name"]
                    },
                    "status": "ready",
                    "priority": "normal"
                }
                
            elif next_agent == "qa":
                # QA valida implementação do Dev
                story_info = completed_task.get("extra_data", {})
                handoff = {
                    "workflow_id": workflow_id,
                    "from": agent_name,
                    "to": "qa",
                    "created_at": datetime.now().isoformat(),
                    "data": {
                        "story_info": story_info,
                        "project_name": workflow["project_name"]
                    },
                    "status": "ready",
                    "priority": "normal"
                }
                
            else:
                # Handoff normal para próximo agente
                handoff = {
                    "workflow_id": workflow_id,
                    "from": agent_name,
                    "to": next_agent,
                    "created_at": datetime.now().isoformat(),
                    "data": {
                        "project_name": workflow["project_name"]
                    },
                    "status": "ready",
                    "priority": "normal"
                }
            
            self._save_handoff(handoff)
            self._queue_agent(next_agent, workflow_id, handoff, completed_task.get("extra_data"))
    
    def _save_handoff(self, handoff: Dict):
        """Salva handoff em arquivo"""
        timestamp = int(time.time() * 1000)
        handoff_file = HANDOFF_DIR / f"handoff-{timestamp}-{handoff['from']}-to-{handoff['to']}.json"
        handoff_file.write_text(json.dumps(handoff, indent=2))
    
    def _save_workflow_state(self, workflow: Dict):
        """Salva estado do workflow"""
        state_file = STATUS_DIR / f"{workflow['id']}-state.json"
        state_file.write_text(json.dumps(workflow, indent=2))
    
    def _generate_project_name(self, description: str) -> str:
        """Gera nome do projeto"""
        name = description.lower()
        name = "".join(c if c.isalnum() or c in "-_" else "-" for c in name)
        name = "-".join(name.split())
        return name[:50]
    
    def get_workflow_status(self, workflow_id: str) -> Optional[Dict]:
        """Obtém status de workflow específico"""
        return self.active_workflows.get(workflow_id)
    
    def list_active_workflows(self) -> List[Dict]:
        """Lista workflows ativos"""
        return list(self.active_workflows.values())


def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="BMAD Agent Coordinator - Sistema de comunicação entre agentes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python bmad_agent_coordinator.py --start                    # Iniciar sistema
  python bmad_agent_coordinator.py --initiate "Meu projeto"   # Iniciar workflow
  python bmad_agent_coordinator.py --status workflow-id       # Ver status
        """
    )
    
    parser.add_argument(
        "--start",
        help="Iniciar sistema de coordenação",
        action="store_true"
    )
    
    parser.add_argument(
        "--initiate",
        help="Iniciar novo workflow",
        type=str
    )
    
    parser.add_argument(
        "--status",
        help="Ver status de workflow específico",
        type=str
    )
    
    parser.add_argument(
        "--list",
        help="Listar workflows ativos",
        action="store_true"
    )
    
    args = parser.parse_args()
    
    coordinator = BMADAgentCoordinator()
    
    if args.start:
        coordinator.start_coordination()
    elif args.initiate:
        workflow_id = coordinator.initiate_workflow(args.initiate)
        print(f"Workflow iniciado: {workflow_id}")
    elif args.status:
        status = coordinator.get_workflow_status(args.status)
        if status:
            print(json.dumps(status, indent=2))
        else:
            print(f"Workflow não encontrado: {args.status}")
    elif args.list:
        workflows = coordinator.list_active_workflows()
        for workflow in workflows:
            print(f"- {workflow['id']}: {workflow['project_name']} ({workflow['status']})")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
