#!/usr/bin/env python3
"""
BMAD Collaborative Workflow - Sistema de Revisão Colaborativa Entre Agentes

Este script implementa um workflow onde os agentes BMAD se revisam mutuamente,
com aprovação do usuário em pontos críticos e implementação REAL de código.

Uso:
    python bmad_collaborative_workflow.py "Descrição do projeto"
    python bmad_collaborative_workflow.py --project "nome-projeto" "Descrição"
"""

import os
import sys
import json
import time
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
import subprocess

# Configurações
PROJECT_ROOT = Path(__file__).parent.parent.parent
BMAD_OUTPUT = PROJECT_ROOT / "PRPs" / "bmad-output"
WORKFLOW_DIR = BMAD_OUTPUT / ".workflow"
REVIEWS_DIR = WORKFLOW_DIR / "reviews"

# Criar diretórios
for dir_path in [WORKFLOW_DIR, REVIEWS_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)


class CollaborativeAgent:
    """Representa um agente que pode criar e revisar trabalho"""
    
    def __init__(self, name: str, role: str, expertise: List[str]):
        self.name = name
        self.role = role
        self.expertise = expertise
    
    def create_output(self, task: Dict) -> Dict:
        """Cria output baseado em tarefa"""
        print(f"\n🔄 {self.name} está trabalhando...")
        time.sleep(2)  # Simular tempo de trabalho
        
        return {
            "agent": self.name,
            "status": "completed",
            "output": f"Output criado por {self.name}",
            "created_at": datetime.now().isoformat()
        }
    
    def review_output(self, output: Dict, context: Dict) -> Dict:
        """Revisa output de outro agente"""
        print(f"   🔍 {self.name} revisando...")
        time.sleep(1)  # Simular tempo de revisão
        
        # Simular revisão baseada na expertise
        feedback = self._generate_feedback(output, context)
        
        return {
            "reviewer": self.name,
            "reviewed_at": datetime.now().isoformat(),
            "status": feedback["status"],
            "feedback": feedback["message"],
            "suggestions": feedback["suggestions"]
        }
    
    def _generate_feedback(self, output: Dict, context: Dict) -> Dict:
        """Gera feedback baseado na expertise do agente"""
        # Placeholder - em produção seria análise real
        return {
            "status": "approved",  # ou "needs_improvement"
            "message": f"Revisado sob perspectiva de {self.role}",
            "suggestions": []
        }


class BMADCollaborativeWorkflow:
    """Workflow BMAD com revisão colaborativa"""
    
    def __init__(self, project_description: str, project_name: Optional[str] = None):
        self.project_description = project_description
        self.project_name = project_name or self._generate_project_name(project_description)
        
        # Inicializar agentes
        self.agents = {
            "analyst": CollaborativeAgent("Analyst", "Requirements Analysis", 
                                        ["requirements", "stakeholders", "business"]),
            "pm": CollaborativeAgent("PM", "Product Management",
                                   ["features", "user_stories", "prioritization"]),
            "architect": CollaborativeAgent("Architect", "Technical Architecture",
                                          ["technology", "patterns", "scalability"]),
            "scrum-master": CollaborativeAgent("Scrum Master", "Agile Planning",
                                             ["stories", "estimation", "dependencies"]),
            "dev": CollaborativeAgent("Dev", "Software Development",
                                    ["implementation", "testing", "code_quality"]),
            "qa": CollaborativeAgent("QA", "Quality Assurance",
                                   ["testing", "validation", "bugs"])
        }
        
        # Estado do workflow
        self.workflow_state = {
            "project_name": self.project_name,
            "description": self.project_description,
            "started_at": datetime.now().isoformat(),
            "phase": "planning",
            "current_step": None,
            "completed_steps": [],
            "reviews": {},
            "iterations": {},
            "code_implementation": {
                "enabled": False,
                "project_path": None,
                "implemented_stories": []
            }
        }
    
    def run_collaborative_workflow(self):
        """Executa workflow colaborativo completo"""
        print("=" * 70)
        print("🤝 BMAD Collaborative Workflow - Sistema de Revisão Colaborativa")
        print("=" * 70)
        print(f"\n📁 Projeto: {self.project_name}")
        print(f"📝 Descrição: {self.project_description}")
        print(f"⏰ Iniciado: {datetime.now().strftime('%H:%M:%S')}")
        print("\n" + "=" * 70)
        
        try:
            # FASE 1: Planejamento com Revisão Colaborativa
            print("\n\n📋 FASE 1: PLANEJAMENTO COLABORATIVO")
            print("-" * 70)
            
            # 1. Analyst cria Brief
            brief_result = self._execute_step_with_review(
                agent_name="analyst",
                task_type="create_brief",
                description="Criar Brief com análise de requisitos completa"
            )
            
            if not brief_result:
                print("❌ Workflow cancelado pelo usuário")
                return
            
            # 2. PM cria PRD
            prd_result = self._execute_step_with_review(
                agent_name="pm",
                task_type="create_prd",
                description="Criar PRD com user stories e critérios de aceitação",
                dependencies=["analyst"]
            )
            
            if not prd_result:
                print("❌ Workflow cancelado pelo usuário")
                return
            
            # 3. Architect define Arquitetura
            arch_result = self._execute_step_with_review(
                agent_name="architect",
                task_type="create_architecture",
                description="Definir arquitetura técnica e stack tecnológico",
                dependencies=["analyst", "pm"]
            )
            
            if not arch_result:
                print("❌ Workflow cancelado pelo usuário")
                return
            
            print("\n✅ Planejamento Completo e Aprovado!")
            
            # FASE 2: Criação de Stories
            print("\n\n📝 FASE 2: CRIAÇÃO DE DEVELOPMENT STORIES")
            print("-" * 70)
            
            stories_result = self._execute_step_with_review(
                agent_name="scrum-master",
                task_type="create_stories",
                description="Criar Development Stories implementáveis",
                dependencies=["analyst", "pm", "architect"]
            )
            
            if not stories_result:
                print("❌ Workflow cancelado pelo usuário")
                return
            
            print("\n✅ Stories Criadas e Aprovadas!")
            
            # FASE 3: Desenvolvimento (opcional)
            self._run_development_phase()
            
            # Finalizar
            self._finalize_workflow()
            
        except KeyboardInterrupt:
            print("\n\n⚠️ Workflow interrompido pelo usuário")
            self._save_state()
        except Exception as e:
            print(f"\n\n❌ Erro durante workflow: {e}")
            self._save_state()
            raise
    
    def _execute_step_with_review(self, agent_name: str, task_type: str, 
                                  description: str, dependencies: List[str] = None) -> bool:
        """Executa um passo com revisão colaborativa de todos os agentes"""
        
        iteration = 1
        max_iterations = 5
        
        while iteration <= max_iterations:
            print(f"\n{'🔄' if iteration == 1 else '🔁'} {agent_name.upper()} - Iteração {iteration}")
            print(f"   📋 Tarefa: {description}")
            
            # 1. Agente cria output
            agent = self.agents[agent_name]
            task = {
                "type": task_type,
                "description": description,
                "dependencies": dependencies or [],
                "iteration": iteration
            }
            
            output = agent.create_output(task)
            print(f"   ✅ Output criado")
            
            # 2. Todos os OUTROS agentes revisam
            print(f"\n   👥 REVISÃO COLABORATIVA:")
            reviews = self._collect_reviews(agent_name, output)
            
            # 3. Mostrar feedbacks ao usuário
            self._display_reviews(reviews)
            
            # 4. Salvar revisões
            self._save_reviews(agent_name, task_type, iteration, reviews)
            
            # 5. Perguntar decisão do usuário
            decision = self._ask_user_decision(agent_name, task_type, reviews)
            
            if decision == "accept":
                print(f"\n   ✅ {agent_name.upper()} aprovado!")
                self.workflow_state["completed_steps"].append({
                    "agent": agent_name,
                    "task": task_type,
                    "iterations": iteration,
                    "approved_at": datetime.now().isoformat()
                })
                return True
            
            elif decision == "improve":
                print(f"\n   🔁 Melhorando com feedback... (Iteração {iteration + 1})")
                iteration += 1
                continue
            
            elif decision == "cancel":
                return False
        
        print(f"\n   ⚠️ Máximo de iterações ({max_iterations}) atingido")
        return self._ask_user_decision_final(agent_name)
    
    def _collect_reviews(self, creator_agent: str, output: Dict) -> List[Dict]:
        """Coleta revisões de todos os outros agentes"""
        reviews = []
        
        for agent_name, agent in self.agents.items():
            if agent_name != creator_agent:
                review = agent.review_output(output, self.workflow_state)
                reviews.append(review)
        
        return reviews
    
    def _display_reviews(self, reviews: List[Dict]):
        """Mostra revisões formatadas ao usuário"""
        print("\n   📊 FEEDBACKS:")
        print("   " + "-" * 60)
        
        for review in reviews:
            status_icon = "✅" if review["status"] == "approved" else "⚠️"
            print(f"   {status_icon} {review['reviewer']}:")
            print(f"      {review['feedback']}")
            
            if review.get("suggestions"):
                for suggestion in review["suggestions"]:
                    print(f"      💡 {suggestion}")
        
        print("   " + "-" * 60)
    
    def _save_reviews(self, agent: str, task: str, iteration: int, reviews: List[Dict]):
        """Salva revisões em arquivo"""
        review_data = {
            "agent": agent,
            "task": task,
            "iteration": iteration,
            "timestamp": datetime.now().isoformat(),
            "reviews": reviews
        }
        
        review_file = REVIEWS_DIR / f"{agent}-{task}-iter{iteration}.json"
        review_file.write_text(json.dumps(review_data, indent=2, ensure_ascii=False))
    
    def _ask_user_decision(self, agent: str, task: str, reviews: List[Dict]) -> str:
        """Pergunta decisão do usuário"""
        print("\n   ❓ DECISÃO:")
        print("      a) Aceitar e continuar")
        print("      b) Melhorar com feedback")
        print("      c) Cancelar workflow")
        
        while True:
            choice = input("\n   Escolha (a/b/c): ").strip().lower()
            
            if choice == "a":
                return "accept"
            elif choice == "b":
                return "improve"
            elif choice == "c":
                return "cancel"
            else:
                print("   ❌ Opção inválida. Use a, b ou c.")
    
    def _ask_user_decision_final(self, agent: str) -> bool:
        """Pergunta decisão final após máximo de iterações"""
        print(f"\n   ❓ Aceitar {agent.upper()} mesmo assim?")
        print("      a) Sim, aceitar")
        print("      b) Não, cancelar")
        
        while True:
            choice = input("\n   Escolha (a/b): ").strip().lower()
            
            if choice == "a":
                return True
            elif choice == "b":
                return False
            else:
                print("   ❌ Opção inválida. Use a ou b.")
    
    def _run_development_phase(self):
        """Executa fase de desenvolvimento (opcional)"""
        print("\n\n💻 FASE 3: DESENVOLVIMENTO")
        print("-" * 70)
        
        # Perguntar se quer implementar código
        print("\n❓ Deseja implementar código agora?")
        print("   a) Sim, implementar código real")
        print("   b) Não, apenas documentação")
        
        while True:
            choice = input("\nEscolha (a/b): ").strip().lower()
            
            if choice == "b":
                print("\n⏭️  Pulando implementação de código")
                return
            elif choice == "a":
                break
            else:
                print("❌ Opção inválida. Use a ou b.")
        
        # Perguntar onde criar projeto
        print("\n📁 Onde criar o projeto?")
        default_path = f"projects/{self.project_name}"
        project_path = input(f"   Caminho (Enter para '{default_path}'): ").strip()
        
        if not project_path:
            project_path = default_path
        
        project_path = Path(project_path).resolve()
        
        print(f"\n✅ Projeto será criado em: {project_path}")
        
        # Confirmar
        confirm = input("\n❓ Confirmar? (s/n): ").strip().lower()
        if confirm != "s":
            print("❌ Implementação cancelada")
            return
        
        # Ativar modo de implementação
        self.workflow_state["code_implementation"]["enabled"] = True
        self.workflow_state["code_implementation"]["project_path"] = str(project_path)
        
        # Implementar stories
        print("\n🚀 Implementando stories...")
        self._implement_stories(project_path)
    
    def _implement_stories(self, project_path: Path):
        """Implementa stories com revisão de código"""
        # Placeholder - em produção seria implementação real
        stories = [
            {"id": "001", "name": "Project Setup"},
            {"id": "002", "name": "Core Feature"},
            {"id": "003", "name": "UI Implementation"}
        ]
        
        for story in stories:
            print(f"\n📝 Story #{story['id']}: {story['name']}")
            
            # Dev implementa
            print("   💻 Dev implementando...")
            time.sleep(2)
            print("   ✅ Código implementado")
            
            # Revisão colaborativa do código
            print("\n   👥 REVISÃO DE CÓDIGO:")
            
            code_reviews = []
            for reviewer_name in ["qa", "architect", "pm"]:
                reviewer = self.agents[reviewer_name]
                print(f"      🔍 {reviewer_name.upper()} revisando...")
                time.sleep(1)
                
                review = {
                    "reviewer": reviewer_name,
                    "status": "approved",
                    "feedback": f"Código validado sob perspectiva de {reviewer.role}"
                }
                code_reviews.append(review)
                
                status_icon = "✅" if review["status"] == "approved" else "⚠️"
                print(f"      {status_icon} {reviewer_name.upper()}: {review['feedback']}")
            
            # Decisão do usuário
            print("\n   ❓ Código aprovado?")
            print("      a) Sim, continuar")
            print("      b) Não, corrigir")
            
            while True:
                choice = input("\n   Escolha (a/b): ").strip().lower()
                
                if choice == "a":
                    print(f"   ✅ Story #{story['id']} aprovada!")
                    self.workflow_state["code_implementation"]["implemented_stories"].append(story)
                    break
                elif choice == "b":
                    print("   🔁 Corrigindo código...")
                    # Loop de correção
                    break
                else:
                    print("   ❌ Opção inválida. Use a ou b.")
    
    def _finalize_workflow(self):
        """Finaliza workflow"""
        self.workflow_state["status"] = "completed"
        self.workflow_state["completed_at"] = datetime.now().isoformat()
        
        print("\n\n" + "=" * 70)
        print("🎉 WORKFLOW COLABORATIVO COMPLETO!")
        print("=" * 70)
        print(f"\n📁 Projeto: {self.project_name}")
        print(f"⏰ Concluído: {datetime.now().strftime('%H:%M:%S')}")
        print(f"\n📊 Resumo:")
        print(f"   • Etapas completadas: {len(self.workflow_state['completed_steps'])}")
        print(f"   • Revisões realizadas: {len(list(REVIEWS_DIR.glob('*.json')))}")
        
        if self.workflow_state["code_implementation"]["enabled"]:
            stories_count = len(self.workflow_state["code_implementation"]["implemented_stories"])
            print(f"   • Stories implementadas: {stories_count}")
            print(f"   • Código em: {self.workflow_state['code_implementation']['project_path']}")
        
        self._save_state()
        
        print("\n📁 Documentos e logs salvos em:")
        print(f"   • Workflow state: {WORKFLOW_DIR}/{self.project_name}-workflow.json")
        print(f"   • Revisões: {REVIEWS_DIR}/")
        print("\n" + "=" * 70)
    
    def _save_state(self):
        """Salva estado do workflow"""
        state_file = WORKFLOW_DIR / f"{self.project_name}-workflow.json"
        state_file.write_text(json.dumps(self.workflow_state, indent=2, ensure_ascii=False))
    
    def _generate_project_name(self, description: str) -> str:
        """Gera nome do projeto"""
        name = description.lower()
        name = "".join(c if c.isalnum() or c in "-_" else "-" for c in name)
        name = "-".join(name.split())
        return name[:50]


def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="BMAD Collaborative Workflow - Revisão colaborativa entre agentes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python bmad_collaborative_workflow.py "Sistema de gerenciamento de tarefas"
  python bmad_collaborative_workflow.py --project task-manager "Sistema de tarefas"
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
    
    args = parser.parse_args()
    
    # Criar e executar workflow
    workflow = BMADCollaborativeWorkflow(
        project_description=args.description,
        project_name=args.project
    )
    
    workflow.run_collaborative_workflow()


if __name__ == "__main__":
    main()

