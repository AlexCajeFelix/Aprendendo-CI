#!/usr/bin/env python3
"""
BMAD Demo Automático - Demonstração do Sistema de Comunicação Entre Agentes

Este script demonstra como usar o sistema BMAD Full Automático para executar
workflows completos onde os agentes se comunicam automaticamente.
"""

import os
import sys
import time
from pathlib import Path

# Adicionar diretório pai ao path
sys.path.append(str(Path(__file__).parent.parent.parent))

def demo_bmad_auto():
    """Demonstra o uso do BMAD Full Automático"""
    
    print("🎭 DEMONSTRAÇÃO: BMAD Full Automático")
    print("=" * 60)
    print()
    
    # Exemplo 1: Sistema de Tarefas
    print("📝 EXEMPLO 1: Sistema de Gerenciamento de Tarefas")
    print("-" * 60)
    
    project_description = "Sistema web para gerenciar tarefas pessoais com autenticação, CRUD de tarefas e dashboard"
    
    print(f"Descrição: {project_description}")
    print()
    
    # Simular execução (em produção seria chamada real)
    print("🚀 Executando workflow automático...")
    print()
    
    print("🤖 FASE 1: PLANEJAMENTO")
    print("   🔄 Analyst analisando requisitos...")
    time.sleep(1)
    print("   ✅ Brief criado: task-manager-brief.md")
    print()
    
    print("   🔄 PM criando PRD...")
    time.sleep(1)
    print("   ✅ PRD criado: task-manager-prd.md")
    print()
    
    print("   🔄 Architect definindo arquitetura...")
    time.sleep(1)
    print("   ✅ Arquitetura definida: task-manager-architecture.md")
    print()
    
    print("💻 FASE 2: DESENVOLVIMENTO")
    print("   🔄 Scrum Master criando stories...")
    time.sleep(1)
    print("   ✅ Stories criadas: 4 stories implementáveis")
    print()
    
    print("   🔄 Loop Dev → QA automático:")
    for i in range(1, 5):
        print(f"      📝 Story {i}: Dev implementando...")
        time.sleep(0.5)
        print(f"      ✅ Story {i}: QA aprovou")
    
    print()
    print("🎉 WORKFLOW COMPLETO!")
    print("   📊 4 stories implementadas e validadas")
    print("   📁 Outputs em: PRPs/bmad-output/")
    print("   🚀 Projeto pronto para deploy!")
    print()
    
    # Exemplo 2: API REST
    print("📝 EXEMPLO 2: API REST para E-commerce")
    print("-" * 60)
    
    api_description = "API REST para e-commerce com autenticação JWT, CRUD de produtos, carrinho e checkout"
    
    print(f"Descrição: {api_description}")
    print()
    print("🤖 Workflow automático executaria:")
    print("   1. Analyst → Brief com requisitos de API")
    print("   2. PM → PRD com endpoints e especificações")
    print("   3. Architect → Arquitetura com Node.js + PostgreSQL")
    print("   4. Scrum Master → Stories para cada endpoint")
    print("   5. Dev → Implementação de cada story")
    print("   6. QA → Validação de cada implementação")
    print()
    
    # Comandos práticos
    print("💻 COMANDOS PRÁTICOS")
    print("-" * 60)
    print()
    
    print("1. Via Cursor (Recomendado):")
    print("   /bmad-auto \"Sistema de gerenciamento de tarefas\"")
    print()
    
    print("2. Via Script Direto:")
    print("   python PRPs/scripts/bmad_full_auto.py \"API REST para e-commerce\"")
    print()
    
    print("3. Via Orchestrator:")
    print("   python PRPs/scripts/bmad_orchestrator.py --auto \"Dashboard de métricas\"")
    print()
    
    print("4. Com Nome de Projeto Específico:")
    print("   python PRPs/scripts/bmad_full_auto.py \"Sistema de vendas\" --project sales-system")
    print()
    
    # Vantagens
    print("✨ VANTAGENS DO SISTEMA AUTOMÁTICO")
    print("-" * 60)
    print()
    
    advantages = [
        "🔄 Comunicação automática entre agentes",
        "📋 Workflow completo sem intervenção manual",
        "📁 Outputs organizados automaticamente",
        "🔗 Contexto passado entre agentes",
        "⏱️ Execução mais rápida",
        "📊 Logs e monitoramento completos",
        "🎯 Foco no resultado final",
        "🚀 Deploy mais rápido"
    ]
    
    for advantage in advantages:
        print(f"   {advantage}")
        time.sleep(0.2)
    
    print()
    
    # Comparação
    print("📊 COMPARAÇÃO: Manual vs Automático")
    print("-" * 60)
    print()
    
    print("MANUAL (Comandos individuais):")
    print("   ✅ Controle total sobre cada etapa")
    print("   ✅ Fácil debugging")
    print("   ✅ Flexibilidade máxima")
    print("   ❌ Mais lento")
    print("   ❌ Intervenção manual necessária")
    print()
    
    print("AUTOMÁTICO (BMAD Full Auto):")
    print("   ✅ Execução rápida e contínua")
    print("   ✅ Comunicação automática")
    print("   ✅ Workflow completo")
    print("   ✅ Logs detalhados")
    print("   ❌ Menos controle granular")
    print("   ❌ Debugging via logs")
    print()
    
    # Próximos passos
    print("🚀 PRÓXIMOS PASSOS")
    print("-" * 60)
    print()
    
    print("1. Teste o sistema:")
    print("   /bmad-auto \"Seu projeto aqui\"")
    print()
    
    print("2. Monitore o progresso:")
    print("   python PRPs/scripts/bmad_orchestrator.py")
    print()
    
    print("3. Verifique os outputs:")
    print("   ls -la PRPs/bmad-output/")
    print()
    
    print("4. Para projetos futuros:")
    print("   Use /bmad-auto para projetos completos")
    print("   Use comandos individuais para features específicas")
    print()
    
    print("=" * 60)
    print("🎭 Demonstração concluída!")
    print("🤖 BMAD Full Automático está pronto para uso!")
    print("=" * 60)


def demo_agent_communication():
    """Demonstra como os agentes se comunicam"""
    
    print()
    print("🤖 DEMONSTRAÇÃO: Comunicação Entre Agentes")
    print("=" * 60)
    print()
    
    print("📨 FLUXO DE HANDOFFS AUTOMÁTICOS:")
    print("-" * 60)
    print()
    
    handoffs = [
        ("System", "Analyst", "Descrição do projeto", "Brief detalhado"),
        ("Analyst", "PM", "Brief de requisitos", "PRD completo"),
        ("PM", "Architect", "PRD e Brief", "Documento de Arquitetura"),
        ("Architect", "Scrum Master", "PRD + Brief + Arquitetura", "Development Stories"),
        ("Scrum Master", "Dev", "Story específica", "Código implementado"),
        ("Dev", "QA", "Código + Dev Notes", "QA Report"),
        ("QA", "Dev", "QA Report (se reprovado)", "Código corrigido"),
        ("QA", "Scrum Master", "QA Report (se aprovado)", "Próxima Story")
    ]
    
    for i, (from_agent, to_agent, input_desc, output_desc) in enumerate(handoffs, 1):
        print(f"{i:2d}. {from_agent:15} → {to_agent:15}")
        print(f"    Input:  {input_desc}")
        print(f"    Output: {output_desc}")
        print()
        time.sleep(0.3)
    
    print("🔄 O sistema coordena automaticamente:")
    print("   • Criação de handoffs entre agentes")
    print("   • Passagem de contexto")
    print("   • Execução sequencial e iterativa")
    print("   • Monitoramento de progresso")
    print("   • Logs detalhados")
    print()


if __name__ == "__main__":
    demo_bmad_auto()
    demo_agent_communication()
