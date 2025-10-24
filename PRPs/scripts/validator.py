#!/usr/bin/env python3
"""
PRP Validator - Validador de Product Requirement Prompts
Baseado no sistema PRPs-agentic-eng adaptado para Cursor
"""

import argparse
import json
import os
from pathlib import Path
from typing import Dict, Any, List, Tuple
import re
from datetime import datetime

class PRPValidator:
    def __init__(self, config_path: str = None):
        self.config_path = Path(config_path) if config_path else Path("config/templates.json")
        self.validation_rules = self._load_validation_rules()
        
    def _load_validation_rules(self) -> Dict[str, Any]:
        """Carrega regras de validação"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            return config.get('validation', {})
        except FileNotFoundError:
            # Regras padrão se arquivo não existir
            return {
                'requiredSections': [
                    'Objetivo',
                    'Requisitos Funcionais',
                    'Requisitos Técnicos',
                    'Entregáveis Esperados'
                ],
                'optionalSections': [
                    'Critérios de Qualidade',
                    'Exemplos e Referências',
                    'Considerações Adicionais'
                ],
                'minContentLength': 1000,
                'requiredMetadata': ['Tipo', 'Complexidade', 'Tempo Estimado']
            }
    
    def validate_prp(self, prp_path: str) -> Dict[str, Any]:
        """Valida um arquivo PRP"""
        prp_file = Path(prp_path)
        
        if not prp_file.exists():
            return {
                'valid': False,
                'errors': [f'Arquivo não encontrado: {prp_path}'],
                'warnings': [],
                'score': 0
            }
        
        with open(prp_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        validation_result = {
            'file': str(prp_file),
            'timestamp': datetime.now().isoformat(),
            'valid': True,
            'errors': [],
            'warnings': [],
            'score': 0,
            'details': {}
        }
        
        # Validar estrutura básica
        structure_validation = self._validate_structure(content)
        validation_result['details']['structure'] = structure_validation
        
        # Validar metadados
        metadata_validation = self._validate_metadata(content)
        validation_result['details']['metadata'] = metadata_validation
        
        # Validar conteúdo
        content_validation = self._validate_content(content)
        validation_result['details']['content'] = content_validation
        
        # Validar seções obrigatórias
        sections_validation = self._validate_sections(content)
        validation_result['details']['sections'] = sections_validation
        
        # Validar comandos de validação
        commands_validation = self._validate_validation_commands(content)
        validation_result['details']['commands'] = commands_validation
        
        # Calcular score final
        validation_result['score'] = self._calculate_score(validation_result['details'])
        
        # Determinar se é válido
        all_errors = (
            structure_validation['errors'] +
            metadata_validation['errors'] +
            content_validation['errors'] +
            sections_validation['errors'] +
            commands_validation['errors']
        )
        
        all_warnings = (
            structure_validation['warnings'] +
            metadata_validation['warnings'] +
            content_validation['warnings'] +
            sections_validation['warnings'] +
            commands_validation['warnings']
        )
        
        validation_result['errors'] = all_errors
        validation_result['warnings'] = all_warnings
        validation_result['valid'] = len(all_errors) == 0
        
        return validation_result
    
    def _validate_structure(self, content: str) -> Dict[str, Any]:
        """Valida estrutura básica do PRP"""
        result = {'errors': [], 'warnings': [], 'checks': {}}
        
        # Verificar se tem cabeçalho
        has_header = content.startswith('# ')
        result['checks']['has_header'] = has_header
        if not has_header:
            result['errors'].append('PRP deve começar com um cabeçalho (# Título)')
        
        # Verificar se tem metadados
        has_metadata = '**Tipo:**' in content
        result['checks']['has_metadata'] = has_metadata
        if not has_metadata:
            result['errors'].append('PRP deve ter seção de metadados (**Tipo:**, **Complexidade:**, etc.)')
        
        # Verificar se tem seções principais
        has_sections = content.count('## ') >= 3
        result['checks']['has_sections'] = has_sections
        if not has_sections:
            result['warnings'].append('PRP deve ter pelo menos 3 seções principais')
        
        return result
    
    def _validate_metadata(self, content: str) -> Dict[str, Any]:
        """Valida metadados do PRP"""
        result = {'errors': [], 'warnings': [], 'checks': {}}
        
        required_metadata = self.validation_rules.get('requiredMetadata', [])
        
        for metadata in required_metadata:
            pattern = f'\\*\\*{metadata}:\\*\\*'
            has_metadata = bool(re.search(pattern, content))
            result['checks'][f'has_{metadata.lower().replace(" ", "_")}'] = has_metadata
            
            if not has_metadata:
                result['errors'].append(f'Metadado obrigatório não encontrado: **{metadata}:**')
        
        # Validar valores dos metadados
        complexity_match = re.search(r'\*\*Complexidade:\*\*\s*(\w+)', content)
        if complexity_match:
            complexity = complexity_match.group(1)
            valid_complexities = ['Baixa', 'Média', 'Alta']
            if complexity not in valid_complexities:
                result['warnings'].append(f'Complexidade deve ser uma de: {", ".join(valid_complexities)}')
        
        return result
    
    def _validate_content(self, content: str) -> Dict[str, Any]:
        """Valida conteúdo do PRP"""
        result = {'errors': [], 'warnings': [], 'checks': {}}
        
        # Verificar tamanho mínimo
        min_length = self.validation_rules.get('minContentLength', 1000)
        content_length = len(content)
        result['checks']['min_length'] = content_length >= min_length
        
        if content_length < min_length:
            result['warnings'].append(f'Conteúdo muito curto ({content_length} chars). Mínimo recomendado: {min_length}')
        
        # Verificar se tem exemplos de código
        has_code_examples = '```' in content
        result['checks']['has_code_examples'] = has_code_examples
        if not has_code_examples:
            result['warnings'].append('PRP deveria incluir exemplos de código')
        
        # Verificar se tem comandos de validação
        has_validation_commands = '```bash' in content
        result['checks']['has_validation_commands'] = has_validation_commands
        if not has_validation_commands:
            result['warnings'].append('PRP deveria incluir comandos de validação executáveis')
        
        # Verificar se tem entregáveis
        has_deliverables = '- [ ]' in content
        result['checks']['has_deliverables'] = has_deliverables
        if not has_deliverables:
            result['warnings'].append('PRP deveria incluir lista de entregáveis')
        
        return result
    
    def _validate_sections(self, content: str) -> Dict[str, Any]:
        """Valida seções obrigatórias"""
        result = {'errors': [], 'warnings': [], 'checks': {}}
        
        required_sections = self.validation_rules.get('requiredSections', [])
        optional_sections = self.validation_rules.get('optionalSections', [])
        
        # Verificar seções obrigatórias
        for section in required_sections:
            pattern = f'## .*{re.escape(section)}'
            has_section = bool(re.search(pattern, content, re.IGNORECASE))
            result['checks'][f'has_section_{section.lower().replace(" ", "_")}'] = has_section
            
            if not has_section:
                result['errors'].append(f'Seção obrigatória não encontrada: {section}')
        
        # Verificar seções opcionais
        for section in optional_sections:
            pattern = f'## .*{re.escape(section)}'
            has_section = bool(re.search(pattern, content, re.IGNORECASE))
            result['checks'][f'has_section_{section.lower().replace(" ", "_")}'] = has_section
        
        # Contar total de seções
        section_count = len(re.findall(r'^## ', content, re.MULTILINE))
        result['checks']['section_count'] = section_count
        
        if section_count < len(required_sections):
            result['warnings'].append(f'PRP tem apenas {section_count} seções. Recomendado: {len(required_sections)}+')
        
        return result
    
    def _validate_validation_commands(self, content: str) -> Dict[str, Any]:
        """Valida comandos de validação"""
        result = {'errors': [], 'warnings': [], 'checks': {}}
        
        # Extrair comandos bash
        bash_blocks = re.findall(r'```bash\n(.*?)\n```', content, re.DOTALL)
        
        result['checks']['has_bash_commands'] = len(bash_blocks) > 0
        
        if len(bash_blocks) == 0:
            result['warnings'].append('PRP deveria incluir comandos bash para validação')
        
        # Verificar tipos de comandos
        all_commands = []
        for block in bash_blocks:
            commands = [cmd.strip() for cmd in block.split('\n') if cmd.strip()]
            all_commands.extend(commands)
        
        command_types = {
            'lint': any('lint' in cmd.lower() for cmd in all_commands),
            'test': any('test' in cmd.lower() for cmd in all_commands),
            'build': any('build' in cmd.lower() for cmd in all_commands),
            'format': any('format' in cmd.lower() for cmd in all_commands)
        }
        
        result['checks'].update(command_types)
        
        # Verificar se tem pelo menos um comando de cada tipo importante
        if not command_types['lint']:
            result['warnings'].append('Deveria incluir comandos de linting')
        
        if not command_types['test']:
            result['warnings'].append('Deveria incluir comandos de teste')
        
        return result
    
    def _calculate_score(self, details: Dict[str, Any]) -> int:
        """Calcula score de qualidade do PRP"""
        score = 0
        max_score = 100
        
        # Estrutura (20 pontos)
        structure = details.get('structure', {})
        if structure.get('checks', {}).get('has_header'):
            score += 5
        if structure.get('checks', {}).get('has_metadata'):
            score += 5
        if structure.get('checks', {}).get('has_sections'):
            score += 10
        
        # Metadados (15 pontos)
        metadata = details.get('metadata', {})
        metadata_checks = metadata.get('checks', {})
        metadata_score = sum(1 for check in metadata_checks.values() if check)
        score += min(metadata_score * 3, 15)
        
        # Conteúdo (25 pontos)
        content = details.get('content', {})
        content_checks = content.get('checks', {})
        if content_checks.get('min_length'):
            score += 10
        if content_checks.get('has_code_examples'):
            score += 5
        if content_checks.get('has_deliverables'):
            score += 5
        if content_checks.get('has_validation_commands'):
            score += 5
        
        # Seções (25 pontos)
        sections = details.get('sections', {})
        section_count = sections.get('checks', {}).get('section_count', 0)
        required_sections = len(self.validation_rules.get('requiredSections', []))
        
        if section_count >= required_sections:
            score += 15
        if section_count >= required_sections + 2:
            score += 10
        
        # Comandos (15 pontos)
        commands = details.get('commands', {})
        command_checks = commands.get('checks', {})
        if command_checks.get('has_bash_commands'):
            score += 5
        if command_checks.get('lint'):
            score += 3
        if command_checks.get('test'):
            score += 4
        if command_checks.get('build'):
            score += 3
        
        return min(score, max_score)
    
    def validate_directory(self, directory: str) -> Dict[str, Any]:
        """Valida todos os PRPs em um diretório"""
        dir_path = Path(directory)
        
        if not dir_path.exists():
            return {
                'valid': False,
                'errors': [f'Diretório não encontrado: {directory}'],
                'results': {}
            }
        
        results = {}
        overall_valid = True
        
        # Encontrar arquivos PRP
        prp_files = list(dir_path.glob('*.md'))
        
        for prp_file in prp_files:
            result = self.validate_prp(str(prp_file))
            results[prp_file.name] = result
            
            if not result['valid']:
                overall_valid = False
        
        return {
            'valid': overall_valid,
            'directory': str(dir_path),
            'timestamp': datetime.now().isoformat(),
            'total_files': len(prp_files),
            'valid_files': sum(1 for r in results.values() if r['valid']),
            'results': results
        }
    
    def generate_report(self, validation_result: Dict[str, Any]) -> str:
        """Gera relatório de validação"""
        if 'results' in validation_result:  # Validação de diretório
            return self._generate_directory_report(validation_result)
        else:  # Validação de arquivo único
            return self._generate_file_report(validation_result)
    
    def _generate_file_report(self, result: Dict[str, Any]) -> str:
        """Gera relatório para arquivo único"""
        output = []
        output.append("🔍 PRP Validation Report")
        output.append("=" * 50)
        output.append(f"📁 Arquivo: {result['file']}")
        output.append(f"⏰ Timestamp: {result['timestamp']}")
        output.append(f"✅ Status: {'VÁLIDO' if result['valid'] else 'INVÁLIDO'}")
        output.append(f"📊 Score: {result['score']}/100")
        output.append("")
        
        # Erros
        if result['errors']:
            output.append("❌ Erros:")
            for error in result['errors']:
                output.append(f"  • {error}")
            output.append("")
        
        # Warnings
        if result['warnings']:
            output.append("⚠️ Avisos:")
            for warning in result['warnings']:
                output.append(f"  • {warning}")
            output.append("")
        
        # Detalhes
        output.append("📋 Detalhes:")
        for category, details in result['details'].items():
            output.append(f"\n🔹 {category.title()}:")
            checks = details.get('checks', {})
            for check, passed in checks.items():
                status = "✅" if passed else "❌"
                output.append(f"  {status} {check}")
        
        return '\n'.join(output)
    
    def _generate_directory_report(self, result: Dict[str, Any]) -> str:
        """Gera relatório para diretório"""
        output = []
        output.append("🔍 PRP Directory Validation Report")
        output.append("=" * 50)
        output.append(f"📁 Diretório: {result['directory']}")
        output.append(f"⏰ Timestamp: {result['timestamp']}")
        output.append(f"📊 Total de arquivos: {result['total_files']}")
        output.append(f"✅ Arquivos válidos: {result['valid_files']}")
        output.append(f"❌ Arquivos inválidos: {result['total_files'] - result['valid_files']}")
        output.append("")
        
        # Resumo por arquivo
        output.append("📋 Resumo por arquivo:")
        for filename, file_result in result['results'].items():
            status = "✅" if file_result['valid'] else "❌"
            output.append(f"  {status} {filename} (Score: {file_result['score']}/100)")
            
            if file_result['errors']:
                for error in file_result['errors'][:2]:  # Mostrar apenas 2 primeiros erros
                    output.append(f"    • {error}")
        
        return '\n'.join(output)

def main():
    parser = argparse.ArgumentParser(description='PRP Validator - Validador de Product Requirement Prompts')
    parser.add_argument('path', help='Caminho para arquivo ou diretório PRP')
    parser.add_argument('--config', help='Caminho para arquivo de configuração')
    parser.add_argument('--report', action='store_true', help='Gerar relatório detalhado')
    parser.add_argument('--output', help='Salvar relatório em arquivo')
    
    args = parser.parse_args()
    
    try:
        validator = PRPValidator(args.config)
        
        # Determinar se é arquivo ou diretório
        path = Path(args.path)
        
        if path.is_file():
            result = validator.validate_prp(str(path))
        elif path.is_dir():
            result = validator.validate_directory(str(path))
        else:
            print(f"❌ Caminho não encontrado: {path}")
            sys.exit(1)
        
        # Gerar e exibir relatório
        report = validator.generate_report(result)
        print(report)
        
        # Salvar relatório se solicitado
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"\n💾 Relatório salvo em: {args.output}")
        
        # Exit code baseado na validação
        if not result['valid']:
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ Erro: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    import sys
    main()
