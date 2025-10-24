#!/usr/bin/env python3
"""
Template Generator - Gerador de templates de PRP
Baseado no sistema PRPs-agentic-eng adaptado para Cursor
"""

import argparse
import json
import os
from pathlib import Path
from typing import Dict, Any, List
import yaml
from datetime import datetime

class TemplateGenerator:
    def __init__(self, config_path: str = None):
        self.config_path = Path(config_path) if config_path else Path("config/templates.json")
        self.templates_dir = Path("PRPs/templates")
        self.project_root = Path.cwd()
        
    def load_config(self) -> Dict[str, Any]:
        """Carrega configuração de templates"""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Arquivo de configuração não encontrado: {self.config_path}")
            
        with open(self.config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def analyze_project_tech_stack(self) -> Dict[str, Any]:
        """Analisa stack tecnológico do projeto"""
        tech_stack = {
            'frontend': [],
            'backend': [],
            'database': [],
            'tools': [],
            'languages': []
        }
        
        # Detectar package.json
        package_json = self.project_root / 'package.json'
        if package_json.exists():
            with open(package_json, 'r', encoding='utf-8') as f:
                package_data = json.load(f)
                
            dependencies = package_data.get('dependencies', {})
            dev_dependencies = package_data.get('devDependencies', {})
            all_deps = {**dependencies, **dev_dependencies}
            
            # Detectar frameworks frontend
            frontend_frameworks = ['react', 'vue', 'angular', 'next', 'nuxt', 'svelte']
            for dep in all_deps:
                if any(fw in dep.lower() for fw in frontend_frameworks):
                    tech_stack['frontend'].append(dep)
            
            # Detectar frameworks backend
            backend_frameworks = ['express', 'fastify', 'koa', 'hapi', 'nest']
            for dep in all_deps:
                if any(fw in dep.lower() for fw in backend_frameworks):
                    tech_stack['backend'].append(dep)
            
            # Detectar banco de dados
            db_clients = ['mongoose', 'sequelize', 'typeorm', 'prisma', 'pg', 'mysql2']
            for dep in all_deps:
                if any(db in dep.lower() for db in db_clients):
                    tech_stack['database'].append(dep)
            
            # Detectar ferramentas
            tools = ['typescript', 'jest', 'cypress', 'eslint', 'prettier', 'webpack', 'vite']
            for dep in all_deps:
                if any(tool in dep.lower() for tool in tools):
                    tech_stack['tools'].append(dep)
        
        # Detectar Python
        py_files = ['pyproject.toml', 'requirements.txt', 'setup.py']
        if any((self.project_root / f).exists() for f in py_files):
            tech_stack['backend'].append('python')
            tech_stack['languages'].append('python')
        
        # Detectar arquivos TypeScript/JavaScript
        ts_files = list(self.project_root.rglob('*.ts'))
        js_files = list(self.project_root.rglob('*.js'))
        if ts_files:
            tech_stack['languages'].append('typescript')
        elif js_files:
            tech_stack['languages'].append('javascript')
        
        return tech_stack
    
    def generate_custom_template(self, template_type: str, project_context: Dict[str, Any]) -> str:
        """Gera template customizado baseado no contexto do projeto"""
        
        base_template = self._get_base_template(template_type)
        tech_stack = project_context.get('tech_stack', {})
        
        # Personalizar template baseado na stack tecnológica
        customized_template = base_template
        
        # Substituir placeholders com tecnologias detectadas
        if tech_stack.get('frontend'):
            frontend_tech = ', '.join(tech_stack['frontend'][:3])  # Top 3
            customized_template = customized_template.replace(
                '[React/Vue/Angular/Next.js/Nuxt.js]', 
                frontend_tech
            )
        
        if tech_stack.get('backend'):
            backend_tech = ', '.join(tech_stack['backend'][:3])  # Top 3
            customized_template = customized_template.replace(
                '[Node.js/Express/FastAPI/Django]', 
                backend_tech
            )
        
        if tech_stack.get('database'):
            db_tech = ', '.join(tech_stack['database'][:3])  # Top 3
            customized_template = customized_template.replace(
                '[PostgreSQL/MySQL/MongoDB]', 
                db_tech
            )
        
        # Adicionar seção de contexto específico do projeto
        project_section = self._generate_project_context_section(project_context)
        customized_template = customized_template.replace(
            '## 🧠 Todo Contexto Necessário',
            f'## 🧠 Todo Contexto Necessário\n\n{project_section}'
        )
        
        return customized_template
    
    def _get_base_template(self, template_type: str) -> str:
        """Retorna template base baseado no tipo"""
        template_map = {
            'web-application': 'PRPs/templates/web-application.md',
            'api-service': 'PRPs/templates/api-service.md',
            'frontend-component': 'PRPs/templates/frontend-component.md',
            'database-schema': 'PRPs/templates/database-schema.md',
            'microservice': 'PRPs/templates/microservice.md'
        }
        
        template_file = template_map.get(template_type, 'PRPs/templates/prp_base.md')
        template_path = self.project_root / template_file
        
        if not template_path.exists():
            raise FileNotFoundError(f"Template não encontrado: {template_path}")
        
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def _generate_project_context_section(self, project_context: Dict[str, Any]) -> str:
        """Gera seção de contexto específico do projeto"""
        tech_stack = project_context.get('tech_stack', {})
        structure = project_context.get('structure', {})
        
        context_section = "### Contexto Específico do Projeto\n\n"
        
        # Stack tecnológico detectado
        if tech_stack.get('frontend') or tech_stack.get('backend'):
            context_section += "**Stack Tecnológico Detectado:**\n"
            if tech_stack.get('frontend'):
                context_section += f"- Frontend: {', '.join(tech_stack['frontend'])}\n"
            if tech_stack.get('backend'):
                context_section += f"- Backend: {', '.join(tech_stack['backend'])}\n"
            if tech_stack.get('database'):
                context_section += f"- Banco de Dados: {', '.join(tech_stack['database'])}\n"
            context_section += "\n"
        
        # Estrutura do projeto
        if structure:
            context_section += "**Estrutura do Projeto:**\n"
            context_section += "```\n"
            for path, info in list(structure.items())[:10]:  # Top 10
                context_section += f"{path}\n"
            context_section += "```\n\n"
        
        # Comandos específicos do projeto
        context_section += "**Comandos Específicos do Projeto:**\n"
        context_section += "```bash\n"
        
        # Detectar scripts do package.json
        package_json = self.project_root / 'package.json'
        if package_json.exists():
            with open(package_json, 'r', encoding='utf-8') as f:
                package_data = json.load(f)
            
            scripts = package_data.get('scripts', {})
            for script_name, script_command in scripts.items():
                if any(keyword in script_name.lower() for keyword in ['test', 'lint', 'build', 'dev']):
                    context_section += f"npm run {script_name}  # {script_command}\n"
        
        context_section += "```\n"
        
        return context_section
    
    def create_prp_from_template(self, template_type: str, output_path: str, 
                                feature_name: str = None) -> str:
        """Cria PRP baseado em template específico"""
        
        # Carregar configuração
        config = self.load_config()
        
        if template_type not in config.get('templates', {}):
            raise ValueError(f"Tipo de template não encontrado: {template_type}")
        
        template_config = config['templates'][template_type]
        
        # Analisar contexto do projeto
        project_context = {
            'tech_stack': self.analyze_project_tech_stack(),
            'structure': self._analyze_project_structure(),
            'config': config
        }
        
        # Gerar template customizado
        customized_template = self.generate_custom_template(template_type, project_context)
        
        # Personalizar com nome da feature
        if feature_name:
            customized_template = customized_template.replace(
                '[Nome do Projeto/Feature]', 
                feature_name
            )
            customized_template = customized_template.replace(
                '[Nome da Especificação]', 
                feature_name
            )
            customized_template = customized_template.replace(
                '[Nome do Componente Frontend]', 
                feature_name
            )
        
        # Salvar arquivo
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(customized_template)
        
        return str(output_file)
    
    def _analyze_project_structure(self) -> Dict[str, Any]:
        """Analisa estrutura do projeto"""
        structure = {}
        
        for item in self.project_root.rglob('*'):
            if item.is_file() and len(item.relative_to(self.project_root).parts) <= 3:
                relative_path = str(item.relative_to(self.project_root))
                structure[relative_path] = {
                    'type': 'file',
                    'size': item.stat().st_size
                }
        
        return structure
    
    def list_available_templates(self) -> List[Dict[str, Any]]:
        """Lista templates disponíveis"""
        config = self.load_config()
        templates = []
        
        for template_id, template_config in config.get('templates', {}).items():
            templates.append({
                'id': template_id,
                'name': template_config.get('name', ''),
                'description': template_config.get('description', ''),
                'complexity': template_config.get('complexity', []),
                'estimated_time': template_config.get('estimatedTime', ''),
                'technologies': template_config.get('technologies', [])
            })
        
        return templates
    
    def generate_template_from_description(self, description: str, output_path: str) -> str:
        """Gera template baseado em descrição de feature"""
        
        # Analisar contexto do projeto
        project_context = {
            'tech_stack': self.analyze_project_tech_stack(),
            'structure': self._analyze_project_structure()
        }
        
        # Determinar tipo de template baseado na descrição
        template_type = self._determine_template_type(description)
        
        # Gerar template customizado
        customized_template = self.generate_custom_template(template_type, project_context)
        
        # Personalizar com descrição
        customized_template = customized_template.replace(
            '[Nome do Projeto/Feature]', 
            description
        )
        
        # Adicionar seção específica baseada na descrição
        description_section = self._generate_description_section(description)
        customized_template = customized_template.replace(
            '## 🎯 Objetivo',
            f'## 🎯 Objetivo\n\n{description_section}'
        )
        
        # Salvar arquivo
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(customized_template)
        
        return str(output_file)
    
    def _determine_template_type(self, description: str) -> str:
        """Determina tipo de template baseado na descrição"""
        description_lower = description.lower()
        
        if any(keyword in description_lower for keyword in ['componente', 'component', 'ui', 'interface']):
            return 'frontend-component'
        elif any(keyword in description_lower for keyword in ['api', 'serviço', 'service', 'endpoint']):
            return 'api-service'
        elif any(keyword in description_lower for keyword in ['aplicação', 'app', 'web', 'site']):
            return 'web-application'
        elif any(keyword in description_lower for keyword in ['banco', 'database', 'schema', 'tabela']):
            return 'database-schema'
        elif any(keyword in description_lower for keyword in ['microserviço', 'microservice', 'serviço distribuído']):
            return 'microservice'
        else:
            return 'prp_base'
    
    def _generate_description_section(self, description: str) -> str:
        """Gera seção baseada na descrição"""
        return f"""
### Descrição Detalhada
{description}

### Objetivos Específicos
- Implementar funcionalidade conforme especificado
- Manter qualidade e padrões do projeto
- Garantir testabilidade e manutenibilidade
- Documentar adequadamente

### Justificativa
Esta funcionalidade é necessária para [explicar por que é importante].
"""

def main():
    parser = argparse.ArgumentParser(description='Template Generator para PRPs')
    parser.add_argument('--type', help='Tipo de template a gerar')
    parser.add_argument('--output', help='Caminho de saída do arquivo')
    parser.add_argument('--feature', help='Nome da feature')
    parser.add_argument('--description', help='Descrição da feature')
    parser.add_argument('--list', action='store_true', help='Listar templates disponíveis')
    parser.add_argument('--config', help='Caminho para arquivo de configuração')
    
    args = parser.parse_args()
    
    try:
        generator = TemplateGenerator(args.config)
        
        if args.list:
            templates = generator.list_available_templates()
            print("📋 Templates Disponíveis:")
            for template in templates:
                print(f"\n🔹 {template['id']}")
                print(f"   Nome: {template['name']}")
                print(f"   Descrição: {template['description']}")
                print(f"   Complexidade: {', '.join(template['complexity'])}")
                print(f"   Tempo Estimado: {template['estimated_time']}")
        else:
            if args.description:
                output_file = generator.generate_template_from_description(
                    args.description, 
                    args.output or f"PRPs/{args.description.lower().replace(' ', '-')}.md"
                )
            else:
                output_file = generator.create_prp_from_template(
                    args.type or 'prp_base',
                    args.output or f"PRPs/{args.feature or 'novo-prp'}.md",
                    args.feature
                )
            
            print(f"✅ Template gerado: {output_file}")
            
    except Exception as e:
        print(f"❌ Erro: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    import sys
    main()
