# PRD: Sistema CI/CD Reutilizável

## 📋 Informações do Documento

| Campo | Valor |
|-------|-------|
| **Produto** | Sistema CI/CD Reutilizável |
| **Versão** | 1.0.0 |
| **PM Responsável** | PM Agent |
| **Data** | 24/10/2025 |
| **Status** | Em Revisão Colaborativa |

## 🎯 Visão do Produto

### Problema
Atualmente, cada novo projeto Java requer configuração manual e repetitiva de pipelines CI/CD, resultando em:
- **70% do tempo** gasto em configuração vs desenvolvimento
- **Inconsistências** entre ambientes e projetos
- **Bugs em produção** por falta de testes automatizados
- **Falta de visibilidade** da qualidade do código

### Solução
Sistema de CI/CD modular e reutilizável que automatiza completamente o ciclo de build, teste, análise de qualidade e deployment para projetos Java/Spring Boot.

### Proposta de Valor
> "Configure uma vez, reutilize infinitas vezes. CI/CD enterprise-grade em minutos, não dias."

## 👥 Personas & Stakeholders

### Persona 1: Alex - Desenvolvedor Full Stack
**Perfil**:
- 3 anos de experiência
- Trabalha em múltiplos projetos simultaneamente
- Prefere focar em features, não em configuração

**Necessidades**:
- ✅ Setup de CI/CD em < 5 minutos
- ✅ Feedback rápido de builds (< 10 min)
- ✅ Visibilidade clara de quality gates

**Dores**:
- ❌ Configurar workflow do zero a cada projeto
- ❌ Debugar falhas de pipeline obscuras
- ❌ Não saber se código está produção-ready

### Persona 2: Maria - DevOps Engineer
**Perfil**:
- 5+ anos de experiência
- Responsável por infraestrutura de 15+ projetos
- Foco em padronização e segurança

**Necessidades**:
- ✅ Workflows padronizados e auditáveis
- ✅ Segurança e compliance garantidos
- ✅ Manutenção centralizada

**Dores**:
- ❌ Workflows inconsistentes entre projetos
- ❌ Secrets expostos acidentalmente
- ❌ Dificuldade de aplicar updates em massa

### Persona 3: João - Tech Lead
**Perfil**:
- 8+ anos de experiência
- Responsável por decisões arquiteturais
- Foco em qualidade e performance

**Necessidades**:
- ✅ Métricas de qualidade de código
- ✅ Gates de qualidade automatizados
- ✅ Rastreabilidade de deployments

**Dores**:
- ❌ Falta de visibilidade de qualidade
- ❌ Deploy de código com baixa cobertura
- ❌ Vulnerabilidades não detectadas

## 🎨 User Stories & Funcionalidades

### Epic 1: Workflow Reutilizável Java

#### Story 1.1: Configurar Java Version Flexível
```
COMO desenvolvedor
QUERO especificar a versão do Java do meu projeto
PARA garantir compatibilidade com minhas dependências

CRITÉRIOS DE ACEITAÇÃO:
✅ Suporta Java 11, 17, 21
✅ Default é Java 17
✅ Configurável via input do workflow
✅ Usa actions/setup-java@v4
```

#### Story 1.2: Build e Test com Cache
```
COMO desenvolvedor
QUERO que meu build seja rápido
PARA ter feedback ágil

CRITÉRIOS DE ACEITAÇÃO:
✅ Cache de dependências Maven (~/.m2/repository)
✅ Build incremental quando possível
✅ Executa mvn clean install
✅ Gera relatórios de teste em XML/HTML
✅ Build completo < 5 minutos
```

#### Story 1.3: Upload de Artifacts
```
COMO DevOps
QUERO que artifacts sejam salvos automaticamente
PARA poder fazer rollback se necessário

CRITÉRIOS DE ACEITAÇÃO:
✅ Upload de JAR compilado
✅ Upload de relatórios de teste
✅ Retenção de 30 dias
✅ Nomeação semântica (app-${version}-${sha}.jar)
```

### Epic 2: Workflow Main Orquestrador

#### Story 2.1: Trigger Automático em Push/PR
```
COMO desenvolvedor
QUERO que o pipeline execute automaticamente
PARA validar minhas mudanças imediatamente

CRITÉRIOS DE ACEITAÇÃO:
✅ Trigger em push para main/master
✅ Trigger em pull requests
✅ Workflow dispatch manual
✅ Filtros: paths src/**, pom.xml, Dockerfile
✅ Ignora: docs/**, *.md (exceto root README.md)
```

#### Story 2.2: Integração com Workflow Java
```
COMO desenvolvedor
QUERO que o workflow main chame o workflow Java
PARA reaproveitar configurações

CRITÉRIOS DE ACEITAÇÃO:
✅ Usa uses: ./.github/workflows/java-reusable.yml
✅ Passa inputs: java-version, maven-args
✅ Recebe outputs: build-status, artifact-path
✅ Herda secrets automaticamente
```

#### Story 2.3: Pipeline Multi-Estágio
```
COMO DevOps
QUERO um pipeline com múltiplos estágios
PARA separar responsabilidades

CRITÉRIOS DE ACEITAÇÃO:
✅ Stage 1: Build & Test (chama java-reusable)
✅ Stage 2: Quality Analysis (SonarCloud)
✅ Stage 3: Security Scan (Trivy)
✅ Stage 4: Docker Build
✅ Stage 5: Docker Push (só em main)
✅ Cada stage depende do sucesso do anterior
```

### Epic 3: Integração SonarCloud

#### Story 3.1: Análise de Qualidade Automática
```
COMO Tech Lead
QUERO análise de qualidade automática
PARA garantir padrões de código

CRITÉRIOS DE ACEITAÇÃO:
✅ Integração com SonarCloud
✅ Análise em cada PR
✅ Métricas: coverage, duplicação, code smells, bugs
✅ Comentários automáticos em PR com resultados
```

#### Story 3.2: Quality Gate Enforcement
```
COMO Tech Lead
QUERO bloquear merges de código de baixa qualidade
PARA manter saúde do codebase

CRITÉRIOS DE ACEITAÇÃO:
✅ Quality Gate FAILED → Workflow falha
✅ Coverage < 80% → Warning (não bloqueia)
✅ Bugs/Vulnerabilities A/B → Bloqueia
✅ Status visível no PR (check verde/vermelho)
```

#### Story 3.3: Dashboard de Métricas
```
COMO Tech Lead
QUERO visualizar métricas históricas
PARA acompanhar evolução da qualidade

CRITÉRIOS DE ACEITAÇÃO:
✅ Link para SonarCloud dashboard no README
✅ Badge de Quality Gate no README
✅ Histórico de coverage disponível
```

### Epic 4: Integração DockerHub

#### Story 4.1: Build de Imagem Docker
```
COMO DevOps
QUERO build automático de imagens Docker
PARA padronizar deployments

CRITÉRIOS DE ACEITAÇÃO:
✅ Dockerfile multi-stage (build + runtime)
✅ Base image: eclipse-temurin:17-jre-alpine
✅ Otimizado para cache de layers
✅ Build < 3 minutos
✅ Imagem final < 200MB
```

#### Story 4.2: Push com Tags Semânticas
```
COMO DevOps
QUERO tags semânticas nas imagens
PARA controlar versões facilmente

CRITÉRIOS DE ACEITAÇÃO:
✅ Tag latest (em main)
✅ Tag v${version} (de pom.xml)
✅ Tag ${branch}-${sha} (para todas branches)
✅ Tag ${pr-number} (para PRs)
```

#### Story 4.3: Autenticação Segura
```
COMO DevOps
QUERO autenticação segura com DockerHub
PARA proteger credenciais

CRITÉRIOS DE ACEITAÇÃO:
✅ Usa secrets: DOCKERHUB_USERNAME, DOCKERHUB_TOKEN
✅ Login apenas quando necessário (não em PRs externos)
✅ Logout após push
✅ Secrets nunca aparecem em logs
```

### Epic 5: Documentação de Configuração

#### Story 5.1: Guia de Quick Start
```
COMO desenvolvedor novo
QUERO começar rapidamente
PARA não perder tempo com configuração

CRITÉRIOS DE ACEITAÇÃO:
✅ Seção "Quick Start" com 5 passos
✅ Tempo para setup: < 10 minutos
✅ Exemplos de código prontos para copiar
✅ Screenshots de configuração de secrets
```

#### Story 5.2: Referência Completa
```
COMO DevOps
QUERO documentação técnica completa
PARA entender detalhes e customizar

CRITÉRIOS DE ACEITAÇÃO:
✅ Arquitetura dos workflows
✅ Inputs e outputs de cada workflow
✅ Variáveis de ambiente suportadas
✅ Hooks de customização
✅ Exemplos avançados
```

#### Story 5.3: Troubleshooting Guide
```
COMO desenvolvedor
QUERO resolver problemas rapidamente
PARA não bloquear meu trabalho

CRITÉRIOS DE ACEITAÇÃO:
✅ Top 10 erros comuns e soluções
✅ Como debugar workflow localmente (act)
✅ Como ver logs detalhados
✅ Contatos para suporte
```

## 🎯 Objetivos e Métricas (OKRs)

### Objective 1: Acelerar Time-to-Market
**Key Results**:
- KR1: ✅ Reduzir tempo de setup de novo projeto de 4h para < 30min (87% redução)
- KR2: ✅ Aumentar deployment frequency de 1x/semana para 5x/semana
- KR3: ✅ Reduzir tempo médio de build de 12min para < 5min (58% redução)

### Objective 2: Melhorar Qualidade de Código
**Key Results**:
- KR1: ✅ Atingir coverage médio de 80%+ em todos projetos
- KR2: ✅ Reduzir bugs em produção em 60%
- KR3: ✅ 0 vulnerabilidades críticas em produção

### Objective 3: Padronizar Processos
**Key Results**:
- KR1: ✅ 100% dos projetos usando workflows reutilizáveis
- KR2: ✅ Reduzir variação de configuração entre projetos para < 5%
- KR3: ✅ 90% dos desenvolvedores satisfeitos com CI/CD (NPS > 50)

## 🚀 Roadmap & Faseamento

### Fase 1: MVP (Semana 1-2)
**Objetivo**: CI/CD básico funcionando
**Entregas**:
- ✅ Workflow Java reutilizável (build + test)
- ✅ Workflow main básico
- ✅ Integração SonarCloud
- ✅ Documentação mínima

**Critério de Sucesso**: 1 projeto piloto usando workflows

### Fase 2: Production-Ready (Semana 3)
**Objetivo**: Adicionar features essenciais
**Entregas**:
- ✅ Integração DockerHub
- ✅ Quality gates enforcement
- ✅ Security scanning (Trivy)
- ✅ Documentação completa

**Critério de Sucesso**: 5 projetos migrados

### Fase 3: Otimização (Semana 4)
**Objetivo**: Performance e DX
**Entregas**:
- ✅ Cache otimizado (dependencies + Docker layers)
- ✅ Notificações (Slack/Discord)
- ✅ Matrix builds (múltiplas versões Java)
- ✅ Troubleshooting guide

**Critério de Sucesso**: Build < 5min, NPS > 50

### Fase 4: Escalabilidade (Futuro)
**Objetivo**: Enterprise features
**Entregas**:
- 🔮 Suporte a Gradle
- 🔮 Deploy em Kubernetes
- 🔮 Multi-cloud (AWS, GCP, Azure)
- 🔮 Advanced caching (remote cache)

## 🔧 Especificações Técnicas

### Arquitetura de Workflows

```yaml
# Estrutura de arquivos
.github/workflows/
├── java-reusable.yml      # [REUTILIZÁVEL] Build & Test Java
├── main.yml               # [MAIN] Pipeline completo para main/master
├── feature.yml            # [FEATURE] Pipeline para feature branches
└── docker-publish.yml     # [HELPER] Build e push Docker

docs/
└── ci-cd-configuration.md # Documentação completa
```

### Workflow java-reusable.yml

**Tipo**: Reusable Workflow
**Trigger**: workflow_call
**Inputs**:
- `java-version` (string, default: '17')
- `maven-args` (string, default: 'clean install')
- `run-tests` (boolean, default: true)
- `upload-artifacts` (boolean, default: true)

**Outputs**:
- `build-status` (success/failure)
- `artifact-path` (caminho do JAR)
- `test-results` (passed/failed/total)

**Jobs**:
1. **setup**: Checkout + Setup Java + Cache
2. **build**: Maven build
3. **test**: JUnit + Jacoco coverage
4. **artifact**: Upload JAR + reports

### Workflow main.yml

**Tipo**: Main Workflow
**Trigger**:
```yaml
on:
  push:
    branches: [main, master]
    paths:
      - 'src/**'
      - 'pom.xml'
      - 'Dockerfile'
  pull_request:
    branches: [main, master]
  workflow_dispatch:
```

**Jobs**:
1. **build-and-test**: Chama java-reusable.yml
2. **sonar-analysis**: SonarCloud scan
3. **security-scan**: Trivy vulnerability scan
4. **docker-build**: Build imagem Docker
5. **docker-push**: Push para DockerHub (só em main)

**Secrets Necessários**:
- `SONAR_TOKEN`
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

### Integrações Externas

#### SonarCloud
```yaml
- name: SonarCloud Scan
  uses: SonarSource/sonarcloud-github-action@master
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
  with:
    args: >
      -Dsonar.projectKey=${{ github.repository_owner }}_${{ github.event.repository.name }}
      -Dsonar.organization=${{ github.repository_owner }}
      -Dsonar.coverage.jacoco.xmlReportPaths=target/site/jacoco/jacoco.xml
```

#### DockerHub
```yaml
- name: Login to DockerHub
  uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKERHUB_USERNAME }}
    password: ${{ secrets.DOCKERHUB_TOKEN }}

- name: Build and Push
  uses: docker/build-push-action@v5
  with:
    context: .
    push: true
    tags: |
      ${{ secrets.DOCKERHUB_USERNAME }}/${{ github.event.repository.name }}:latest
      ${{ secrets.DOCKERHUB_USERNAME }}/${{ github.event.repository.name }}:${{ github.sha }}
    cache-from: type=registry,ref=${{ secrets.DOCKERHUB_USERNAME }}/${{ github.event.repository.name }}:cache
    cache-to: type=registry,ref=${{ secrets.DOCKERHUB_USERNAME }}/${{ github.event.repository.name }}:cache,mode=max
```

## ✅ Critérios de Aceitação do Produto

### Funcionalidade
- ✅ Build Java funciona em projetos Maven padrão
- ✅ Testes executam e geram relatórios
- ✅ SonarCloud analisa e reporta métricas
- ✅ Docker build e push funcionam
- ✅ Quality gates bloqueiam merges quando apropriado

### Performance
- ✅ Build completo < 10 minutos
- ✅ Cache reduz builds subsequentes em 50%+
- ✅ Imagem Docker < 200MB

### Usabilidade
- ✅ Setup em < 10 minutos seguindo docs
- ✅ Erros têm mensagens claras
- ✅ Logs são legíveis e úteis

### Confiabilidade
- ✅ Success rate > 95%
- ✅ Falhas transitórias têm retry
- ✅ Secrets nunca expostos

## 🚧 Restrições & Dependências

### Restrições Técnicas
- GitHub Actions runners (Ubuntu latest)
- Java 11+ obrigatório
- Maven como build tool (Gradle em fase futura)
- Dockerfile deve existir no root do projeto

### Dependências Externas
- Conta SonarCloud configurada
- Conta DockerHub configurada
- GitHub repository com Actions habilitado

### Riscos
| Risco | Impacto | Mitigação |
|-------|---------|-----------|
| GitHub Actions quota excedida | Alto | Monitorar uso, otimizar cache |
| SonarCloud indisponível | Médio | Tornar step opcional com warning |
| DockerHub rate limit | Médio | Usar Docker Hub Pro ou cache local |
| Secrets expostos acidentalmente | Crítico | Code review, dependabot alerts |

## 📚 Referências & Recursos

### Documentação Externa
- [GitHub Actions Reusable Workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)
- [SonarCloud for GitHub](https://docs.sonarcloud.io/advanced-setup/ci-based-analysis/github-actions/)
- [Docker Build Push Action](https://github.com/docker/build-push-action)

### Documentação Interna
- `docs/ci-cd-configuration.md` (a ser criado)
- `PRPs/templates/bmad/` (templates BMAD)

---

**Status**: Aguardando Revisão Colaborativa
**Próximos Passos**: Architect define arquitetura técnica detalhada
**Aprovação**: PM Agent
**Data**: 24/10/2025

