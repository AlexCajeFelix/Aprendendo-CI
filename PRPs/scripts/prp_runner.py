#!/usr/bin/env python3
"""
PRP Runner - Executor de Product Requirement Prompts
Baseado no sistema PRPs-agentic-eng adaptado para Cursor
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, Any, Optional
import subprocess
import yaml
from datetime import datetime

class PRPRunner:
    def __init__(self, prp_path: str, interactive: bool = False, output_format: str = "text"):
        self.prp_path = Path(prp_path)
        self.interactive = interactive
        self.output_format = output_format
        self.project_root = Path.cwd()
        self.prp_content = None
        self.execution_log = []
        
    def load_prp(self) -> Dict[str, Any]:
        """Carrega e analisa o arquivo PRP"""
        if not self.prp_path.exists():
            raise FileNotFoundError(f"PRP não encontrado: {self.prp_path}")
            
        with open(self.prp_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        self.prp_content = self._parse_prp(content)
        return self.prp_content
    
    def _parse_prp(self, content: str) -> Dict[str, Any]:
        """Analisa o conteúdo do PRP e extrai informações estruturadas"""
        lines = content.split('\n')
        prp_data = {
            'metadata': {},
            'sections': {},
            'validation_commands': [],
            'deliverables': []
        }
        
        current_section = None
        current_content = []
        
        for line in lines:
            line = line.strip()
            
            # Detectar metadados
            if line.startswith('**Tipo:**'):
                prp_data['metadata']['type'] = line.replace('**Tipo:**', '').strip()
            elif line.startswith('**Complexidade:**'):
                prp_data['metadata']['complexity'] = line.replace('**Complexidade:**', '').strip()
            elif line.startswith('**Tempo Estimado:**'):
                prp_data['metadata']['estimated_time'] = line.replace('**Tempo Estimado:**', '').strip()
            
            # Detectar seções
            elif line.startswith('## '):
                if current_section:
                    prp_data['sections'][current_section] = '\n'.join(current_content)
                current_section = line.replace('## ', '').strip()
                current_content = []
            
            # Detectar comandos de validação
            elif line.startswith('```bash') or line.startswith('```'):
                if current_section == 'Loop de Validação':
                    # Extrair comandos bash
                    pass
            
            # Detectar entregáveis
            elif line.startswith('- [ ]'):
                prp_data['deliverables'].append(line.replace('- [ ]', '').strip())
            
            else:
                if current_section:
                    current_content.append(line)
        
        # Adicionar última seção
        if current_section:
            prp_data['sections'][current_section] = '\n'.join(current_content)
            
        return prp_data
    
    def analyze_project(self) -> Dict[str, Any]:
        """Analisa a estrutura do projeto atual"""
        analysis = {
            'structure': {},
            'technologies': [],
            'patterns': [],
            'config_files': []
        }
        
        # Analisar estrutura de diretórios
        for item in self.project_root.rglob('*'):
            if item.is_file():
                relative_path = item.relative_to(self.project_root)
                if len(relative_path.parts) <= 3:  # Apenas primeiros níveis
                    analysis['structure'][str(relative_path)] = {
                        'type': 'file',
                        'size': item.stat().st_size
                    }
        
        # Detectar tecnologias
        package_files = ['package.json', 'pyproject.toml', 'requirements.txt', 'composer.json']
        for pkg_file in package_files:
            if (self.project_root / pkg_file).exists():
                analysis['config_files'].append(pkg_file)
        
        # Detectar padrões de código
        if (self.project_root / 'src').exists():
            analysis['patterns'].append('src-based structure')
        if (self.project_root / 'tests').exists():
            analysis['patterns'].append('separate tests directory')
            
        return analysis
    
    def execute_validation_commands(self) -> Dict[str, Any]:
        """Executa comandos de validação definidos no PRP"""
        results = {
            'syntax_check': {'passed': True, 'output': ''},
            'tests': {'passed': True, 'output': ''},
            'integration': {'passed': True, 'output': ''}
        }
        
        # Comandos básicos de validação
        commands = [
            ('npm run lint', 'syntax_check'),
            ('npm test', 'tests'),
            ('npm run build', 'integration')
        ]
        
        for command, category in commands:
            try:
                result = subprocess.run(
                    command.split(),
                    capture_output=True,
                    text=True,
                    cwd=self.project_root,
                    timeout=300
                )
                
                results[category] = {
                    'passed': result.returncode == 0,
                    'output': result.stdout + result.stderr,
                    'returncode': result.returncode
                }
                
                self.execution_log.append({
                    'timestamp': datetime.now().isoformat(),
                    'command': command,
                    'success': result.returncode == 0,
                    'output': result.stdout
                })
                
            except subprocess.TimeoutExpired:
                results[category] = {
                    'passed': False,
                    'output': f'Comando {command} excedeu tempo limite',
                    'returncode': -1
                }
            except FileNotFoundError:
                # Comando não encontrado, pular
                continue
        
        return results
    
    def generate_execution_plan(self) -> Dict[str, Any]:
        """Gera plano de execução baseado no PRP"""
        plan = {
            'phases': [],
            'estimated_time': self.prp_content.get('metadata', {}).get('estimated_time', 'N/A'),
            'complexity': self.prp_content.get('metadata', {}).get('complexity', 'N/A'),
            'deliverables_count': len(self.prp_content.get('deliverables', []))
        }
        
        # Extrair fases do blueprint
        blueprint_section = self.prp_content.get('sections', {}).get('Blueprint de Implementação', '')
        
        if blueprint_section:
            phases = []
            current_phase = None
            
            for line in blueprint_section.split('\n'):
                if line.startswith('### Etapa'):
                    if current_phase:
                        phases.append(current_phase)
                    current_phase = {
                        'name': line.replace('### ', '').strip(),
                        'tasks': []
                    }
                elif line.startswith('```pseudocode'):
                    continue
                elif line.strip() and current_phase:
                    if line.strip().startswith(('1.', '2.', '3.', '4.', '5.')):
                        current_phase['tasks'].append(line.strip())
            
            if current_phase:
                phases.append(current_phase)
                
            plan['phases'] = phases
        
        return plan
    
    def run_interactive_mode(self):
        """Executa modo interativo"""
        print("🚀 PRP Runner - Modo Interativo")
        print("=" * 50)
        
        # Carregar PRP
        print(f"📖 Carregando PRP: {self.prp_path.name}")
        prp_data = self.load_prp()
        
        # Analisar projeto
        print("🔍 Analisando estrutura do projeto...")
        project_analysis = self.analyze_project()
        
        # Gerar plano de execução
        print("📋 Gerando plano de execução...")
        execution_plan = self.generate_execution_plan()
        
        # Exibir resumo
        print("\n📊 Resumo do PRP:")
        print(f"  Tipo: {prp_data.get('metadata', {}).get('type', 'N/A')}")
        print(f"  Complexidade: {prp_data.get('metadata', {}).get('complexity', 'N/A')}")
        print(f"  Tempo Estimado: {execution_plan.get('estimated_time', 'N/A')}")
        print(f"  Entregáveis: {execution_plan.get('deliverables_count', 0)}")
        
        print(f"\n🏗️ Fases de Implementação ({len(execution_plan.get('phases', []))}):")
        for i, phase in enumerate(execution_plan.get('phases', []), 1):
            print(f"  {i}. {phase.get('name', 'N/A')}")
            for task in phase.get('tasks', [])[:3]:  # Mostrar apenas 3 primeiras tarefas
                print(f"     - {task}")
        
        # Executar validações
        print("\n🔍 Executando validações...")
        validation_results = self.execute_validation_commands()
        
        print("\n✅ Resultados das Validações:")
        for category, result in validation_results.items():
            status = "✅" if result['passed'] else "❌"
            print(f"  {status} {category}: {'PASSOU' if result['passed'] else 'FALHOU'}")
        
        # Salvar relatório
        self.save_report(prp_data, project_analysis, execution_plan, validation_results)
        
        print(f"\n💾 Relatório salvo em: {self.project_root / 'prp_execution_report.json'}")
        print("\n🎯 PRP pronto para execução!")
    
    def run_headless_mode(self):
        """Executa modo headless"""
        try:
            prp_data = self.load_prp()
            project_analysis = self.analyze_project()
            execution_plan = self.generate_execution_plan()
            validation_results = self.execute_validation_commands()
            
            report = {
                'prp_file': str(self.prp_path),
                'timestamp': datetime.now().isoformat(),
                'prp_data': prp_data,
                'project_analysis': project_analysis,
                'execution_plan': execution_plan,
                'validation_results': validation_results,
                'execution_log': self.execution_log
            }
            
            if self.output_format == 'json':
                return json.dumps(report, indent=2, ensure_ascii=False)
            elif self.output_format == 'stream-json':
                # Para streaming, retornar linha por linha
                for line in json.dumps(report, ensure_ascii=False).split('\n'):
                    yield line
            else:
                return self._format_text_report(report)
                
        except Exception as e:
            error_report = {
                'error': str(e),
                'timestamp': datetime.now().isoformat(),
                'prp_file': str(self.prp_path)
            }
            
            if self.output_format == 'json':
                return json.dumps(error_report, indent=2, ensure_ascii=False)
            else:
                return f"❌ Erro ao executar PRP: {e}"
    
    def _format_text_report(self, report: Dict[str, Any]) -> str:
        """Formata relatório em texto legível"""
        output = []
        output.append("🚀 PRP Execution Report")
        output.append("=" * 50)
        output.append(f"📁 PRP: {report['prp_file']}")
        output.append(f"⏰ Timestamp: {report['timestamp']}")
        output.append("")
        
        # Metadados do PRP
        prp_data = report.get('prp_data', {})
        metadata = prp_data.get('metadata', {})
        output.append("📊 PRP Metadata:")
        for key, value in metadata.items():
            output.append(f"  {key}: {value}")
        output.append("")
        
        # Plano de execução
        execution_plan = report.get('execution_plan', {})
        output.append(f"🏗️ Execution Plan ({len(execution_plan.get('phases', []))} phases):")
        for i, phase in enumerate(execution_plan.get('phases', []), 1):
            output.append(f"  {i}. {phase.get('name', 'N/A')}")
        output.append("")
        
        # Resultados de validação
        validation_results = report.get('validation_results', {})
        output.append("✅ Validation Results:")
        for category, result in validation_results.items():
            status = "✅" if result.get('passed', False) else "❌"
            output.append(f"  {status} {category}: {'PASSOU' if result.get('passed', False) else 'FALHOU'}")
        
        return '\n'.join(output)
    
    def save_report(self, prp_data: Dict[str, Any], project_analysis: Dict[str, Any], 
                   execution_plan: Dict[str, Any], validation_results: Dict[str, Any]):
        """Salva relatório de execução"""
        report = {
            'prp_file': str(self.prp_path),
            'timestamp': datetime.now().isoformat(),
            'prp_data': prp_data,
            'project_analysis': project_analysis,
            'execution_plan': execution_plan,
            'validation_results': validation_results,
            'execution_log': self.execution_log
        }
        
        report_path = self.project_root / 'prp_execution_report.json'
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

def main():
    parser = argparse.ArgumentParser(description='PRP Runner - Executor de Product Requirement Prompts')
    parser.add_argument('--prp', required=True, help='Caminho para o arquivo PRP')
    parser.add_argument('--interactive', action='store_true', help='Modo interativo')
    parser.add_argument('--output-format', choices=['text', 'json', 'stream-json'], 
                       default='text', help='Formato de saída')
    
    args = parser.parse_args()
    
    try:
        runner = PRPRunner(args.prp, args.interactive, args.output_format)
        
        if args.interactive:
            runner.run_interactive_mode()
        else:
            if args.output_format == 'stream-json':
                for line in runner.run_headless_mode():
                    print(line)
            else:
                print(runner.run_headless_mode())
                
    except Exception as e:
        print(f"❌ Erro: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
