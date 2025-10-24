#!/usr/bin/env python3
"""
BMAD Orchestrator - Gerenciador de Workflow BMAD

Este script ajuda a gerenciar o workflow dos agentes BMAD:
- Valida estado atual do projeto
- Sugere próximo passo baseado em documentos existentes
- Verifica se todos pré-requisitos estão prontos
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional

# Configurações
PROJECT_ROOT = Path(__file__).parent.parent.parent
BMAD_OUTPUT = PROJECT_ROOT / "PRPs" / "bmad-output"
BRIEFS_DIR = BMAD_OUTPUT / "briefs"
PRDS_DIR = BMAD_OUTPUT / "prds"
ARCH_DIR = BMAD_OUTPUT / "architecture"
STORIES_DIR = BMAD_OUTPUT / "stories"
IMPL_DIR = BMAD_OUTPUT / "implementations"
QA_DIR = BMAD_OUTPUT / "qa-reports"


class BMADOrchestrator:
    """Orquestrador do workflow BMAD"""
    
    def __init__(self, project_name: Optional[str] = None):
        self.project_name = project_name
        self.state = self.analyze_state()
    
    def analyze_state(self) -> Dict:
        """Analisa o estado atual do projeto"""
        state = {
            "phase": None,
            "has_brief": False,
            "has_prd": False,
            "has_architecture": False,
            "stories_created": False,
            "stories_count": 0,
            "stories_completed": 0,
            "next_step": None,
            "ready_for": []
        }
        
        # Verificar fase de planejamento
        if self._has_files(BRIEFS_DIR):
            state["has_brief"] = True
            state["phase"] = "planning"
            state["ready_for"].append("PM")
        
        if self._has_files(PRDS_DIR):
            state["has_prd"] = True
            state["ready_for"].append("Architect")
        
        if self._has_files(ARCH_DIR):
            state["has_architecture"] = True
            state["ready_for"].append("Scrum Master")
            if state["phase"] == "planning":
                state["phase"] = "planning-complete"
        
        # Verificar fase de desenvolvimento
        if self._has_files(STORIES_DIR):
            state["stories_created"] = True
            state["phase"] = "development"
            state["stories_count"] = self._count_stories()
            state["stories_completed"] = self._count_completed_stories()
            
            if state["stories_count"] > 0:
                next_story = state["stories_completed"] + 1
                if next_story <= state["stories_count"]:
                    state["ready_for"].append(f"Dev (story {next_story})")
        
        # Determinar próximo passo
        state["next_step"] = self._determine_next_step(state)
        
        return state
    
    def _has_files(self, directory: Path) -> bool:
        """Verifica se diretório tem arquivos .md"""
        if not directory.exists():
            return False
        return len(list(directory.glob("**/*.md"))) > 0
    
    def _count_stories(self) -> int:
        """Conta total de stories criadas"""
        if not STORIES_DIR.exists():
            return 0
        stories = list(STORIES_DIR.glob("**/story-*.md"))
        return len([s for s in stories if s.name != "index.md"])
    
    def _count_completed_stories(self) -> int:
        """Conta stories com QA report aprovado"""
        if not QA_DIR.exists():
            return 0
        
        approved = 0
        for qa_file in QA_DIR.glob("story-*-qa-report.md"):
            content = qa_file.read_text()
            if "✅ APROVADA" in content or "Status Final:** ✅" in content:
                approved += 1
        
        return approved
    
    def _determine_next_step(self, state: Dict) -> str:
        """Determina qual deve ser o próximo passo"""
        if not state["has_brief"]:
            return "Use `/analyst` para criar Brief de requisitos"
        
        if not state["has_prd"]:
            return "Use `/pm` para criar PRD baseado no Brief"
        
        if not state["has_architecture"]:
            return "Use `/architect` para definir arquitetura técnica"
        
        if not state["stories_created"]:
            return "Use `/scrum-master` ou `/sm` para criar Development Stories"
        
        if state["stories_count"] == 0:
            return "Aguardando Scrum Master criar stories"
        
        next_story_num = state["stories_completed"] + 1
        if next_story_num <= state["stories_count"]:
            return f"Use `/dev story-{next_story_num:03d}` para implementar próxima story"
        
        return "🎉 Todas stories completas! Projeto pronto para deploy."
    
    def print_status(self):
        """Imprime status atual do projeto"""
        print("=" * 60)
        print("🤖 BMAD Orchestrator - Status do Projeto")
        print("=" * 60)
        print()
        
        if self.project_name:
            print(f"📁 Projeto: {self.project_name}")
            print()
        
        # Fase de Planejamento
        print("📋 FASE DE PLANEJAMENTO")
        print("-" * 60)
        self._print_check("Brief criado (Analyst)", self.state["has_brief"])
        self._print_check("PRD criado (PM)", self.state["has_prd"])
        self._print_check("Arquitetura definida (Architect)", self.state["has_architecture"])
        print()
        
        # Fase de Desenvolvimento
        print("💻 FASE DE DESENVOLVIMENTO")
        print("-" * 60)
        self._print_check("Development Stories criadas (SM)", self.state["stories_created"])
        
        if self.state["stories_count"] > 0:
            progress = (self.state["stories_completed"] / self.state["stories_count"]) * 100
            print(f"   Stories: {self.state['stories_completed']}/{self.state['stories_count']} completas ({progress:.0f}%)")
        print()
        
        # Status Geral
        print("🎯 STATUS GERAL")
        print("-" * 60)
        print(f"   Fase Atual: {self.state['phase'] or 'Não iniciado'}")
        print()
        
        # Próximo Passo
        print("➡️  PRÓXIMO PASSO")
        print("-" * 60)
        print(f"   {self.state['next_step']}")
        print()
        
        # Opções Disponíveis
        if self.state["ready_for"]:
            print("✅ PRONTO PARA")
            print("-" * 60)
            for option in self.state["ready_for"]:
                print(f"   • {option}")
            print()
        
        print("=" * 60)
    
    def _print_check(self, label: str, status: bool):
        """Imprime linha com checkmark"""
        symbol = "✅" if status else "⭕"
        print(f"   {symbol} {label}")
    
    def suggest_workflow(self):
        """Sugere workflow completo baseado no estado"""
        print()
        print("📖 WORKFLOW SUGERIDO")
        print("-" * 60)
        
        if not self.state["has_architecture"]:
            print("FASE 1: Planejamento")
            print("  1. /analyst    → Cria Brief de requisitos")
            print("  2. /pm         → Cria PRD (Product Requirements)")
            print("  3. /architect  → Define arquitetura técnica")
            print()
        
        if self.state["has_architecture"]:
            print("FASE 2: Desenvolvimento (Iterativo)")
            print("  4. /sm         → Cria Development Stories")
            print("  5. /dev        → Implementa story")
            print("  6. /qa         → Valida story")
            print("  7. Repita 5-6 para cada story")
            print()
        
        print("🤖 WORKFLOW AUTOMÁTICO")
        print("-" * 60)
        print("  /bmad-auto \"Descrição do projeto\"  → Executa workflow completo automaticamente")
        print("  python bmad_full_auto.py \"Projeto\"  → Execução via script")
        print()
        
        print("Use: `python PRPs/scripts/bmad_orchestrator.py --help` para mais opções")
        print()
    
    def run_auto_workflow(self, project_description: str, project_name: Optional[str] = None):
        """Executa workflow automático usando BMAD Full Auto"""
        import subprocess
        import sys
        
        # Construir comando
        cmd = [
            sys.executable,
            "PRPs/scripts/bmad_full_auto.py",
            project_description
        ]
        
        if project_name:
            cmd.extend(["--project", project_name])
        
        cmd.append("--auto-approve")  # Execução automática
        
        print(f"🚀 Iniciando workflow automático...")
        print(f"📝 Descrição: {project_description}")
        if project_name:
            print(f"📁 Projeto: {project_name}")
        print()
        
        try:
            # Executar workflow automático
            result = subprocess.run(cmd, cwd=os.getcwd(), capture_output=False)
            
            if result.returncode == 0:
                print("✅ Workflow automático concluído com sucesso!")
            else:
                print(f"❌ Workflow automático falhou com código: {result.returncode}")
                
        except Exception as e:
            print(f"❌ Erro executando workflow automático: {e}")


def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="BMAD Orchestrator - Gerenciador de Workflow",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python bmad_orchestrator.py                    # Status do projeto
  python bmad_orchestrator.py --project meu-app  # Status de projeto específico
  python bmad_orchestrator.py --workflow         # Mostra workflow sugerido
  python bmad_orchestrator.py --auto "Projeto"   # Executa workflow automático
  python bmad_orchestrator.py --collaborative "Projeto"  # Workflow colaborativo
  python bmad_orchestrator.py --collab "API REST" --project-name api  # Colaborativo com nome
        """
    )
    
    parser.add_argument(
        "--project",
        "-p",
        help="Nome do projeto específico",
        type=str
    )
    
    parser.add_argument(
        "--workflow",
        "-w",
        help="Mostra workflow sugerido",
        action="store_true"
    )
    
    parser.add_argument(
        "--json",
        "-j",
        help="Output em formato JSON",
        action="store_true"
    )
    
    parser.add_argument(
        "--auto",
        help="Execute automatic workflow with project description",
        type=str
    )
    
    parser.add_argument(
        "--collaborative",
        "--collab",
        help="Execute collaborative workflow with agent reviews",
        type=str
    )
    
    parser.add_argument(
        "--project-name",
        help="Project name for automatic/collaborative workflow",
        type=str
    )
    
    args = parser.parse_args()
    
    # Verificar se é execução colaborativa
    if args.collaborative:
        # Executar workflow colaborativo
        cmd = [
            sys.executable,
            "PRPs/scripts/bmad_collaborative_workflow.py",
            args.collaborative
        ]
        
        if args.project_name:
            cmd.extend(["--project", args.project_name])
        
        print(f"🤝 Iniciando workflow colaborativo...")
        print(f"📝 Descrição: {args.collaborative}")
        if args.project_name:
            print(f"📁 Projeto: {args.project_name}")
        print()
        
        try:
            result = subprocess.run(cmd, cwd=os.getcwd(), capture_output=False)
            
            if result.returncode == 0:
                print("\n✅ Workflow colaborativo concluído com sucesso!")
            else:
                print(f"\n❌ Workflow colaborativo falhou com código: {result.returncode}")
                
        except Exception as e:
            print(f"\n❌ Erro executando workflow colaborativo: {e}")
    
    # Verificar se é execução automática
    elif args.auto:
        orchestrator = BMADOrchestrator()
        orchestrator.run_auto_workflow(args.auto, args.project_name)
    else:
        # Criar orquestrador
        orchestrator = BMADOrchestrator(project_name=args.project)
        
        # Output
        if args.json:
            print(json.dumps(orchestrator.state, indent=2))
        else:
            orchestrator.print_status()
            
            if args.workflow:
                orchestrator.suggest_workflow()


if __name__ == "__main__":
    main()

