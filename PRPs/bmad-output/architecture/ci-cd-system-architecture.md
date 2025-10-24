# Arquitetura: Sistema CI/CD Reutilizável

## 📋 Informações do Documento

| Campo | Valor |
|-------|-------|
| **Sistema** | CI/CD Reutilizável |
| **Versão** | 1.0.0 |
| **Architect** | Architect Agent |
| **Data** | 24/10/2025 |
| **Status** | Em Revisão Colaborativa |

## 🎯 Visão Arquitetural

### Princípios de Design

1. **Reusabilidade**: Workflows são building blocks composáveis
2. **Separação de Responsabilidades**: Cada workflow tem um propósito único
3. **Fail-Fast**: Erros são detectados o mais cedo possível no pipeline
4. **Security by Default**: Secrets management e scanning automatizados
5. **Observable**: Logs, métricas e notificações em cada etapa

### Decisões Arquiteturais (ADRs)

#### ADR-001: GitHub Actions como Plataforma CI/CD
**Contexto**: Precisamos de plataforma CI/CD integrada com GitHub
**Decisão**: Usar GitHub Actions
**Justificativa**:
- ✅ Integração nativa com GitHub
- ✅ Workflows como código (YAML)
- ✅ Reusable workflows support
- ✅ Marketplace de actions prontas
- ✅ Free tier generoso (2000 min/mês)

**Alternativas Consideradas**:
- Jenkins: Requer infra própria, setup complexo
- GitLab CI: Projeto está no GitHub
- CircleCI: Custo adicional, menos integrado

#### ADR-002: Reusable Workflows vs Composite Actions
**Contexto**: Precisamos reutilizar lógica entre pipelines
**Decisão**: Usar Reusable Workflows
**Justificativa**:
- ✅ Suporta múltiplos jobs
- ✅ Pode receber secrets
- ✅ Mais poderoso que Composite Actions
- ✅ Versionável e testável independentemente

#### ADR-003: Maven como Build Tool (Fase 1)
**Contexto**: Projetos Java usam Maven ou Gradle
**Decisão**: Suportar apenas Maven na fase 1
**Justificativa**:
- ✅ Mais comum em projetos enterprise
- ✅ Convenções mais rígidas (menos variação)
- ✅ Gradle será adicionado na fase 4

#### ADR-004: Docker Multi-Stage Build
**Contexto**: Imagens Docker devem ser leves e seguras
**Decisão**: Usar multi-stage builds
**Justificativa**:
- ✅ Imagem final não contém build tools
- ✅ Menor surface de ataque
- ✅ Imagens 60% menores
- ✅ Build cache mais eficiente

#### ADR-005: SonarCloud Quality Gate como Bloqueador
**Contexto**: Definir quando falha de qualidade deve bloquear merge
**Decisão**: Quality Gate FAILED bloqueia, Coverage baixo só avisa
**Justificativa**:
- ✅ Bugs e vulnerabilities críticas bloqueiam
- ✅ Coverage é métrica de tendência, não absoluta
- ✅ Code smells podem ser ignorados se justificados
- ✅ Permite pragmatismo sem sacrificar segurança

## 🏗️ Arquitetura de Workflows

### Diagrama de Componentes

```
┌─────────────────────────────────────────────────────────────┐
│                     GitHub Repository                        │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              .github/workflows/                       │  │
│  │                                                        │  │
│  │  ┌────────────────────────────────────────────────┐  │  │
│  │  │         java-reusable.yml                      │  │  │
│  │  │  [REUSABLE WORKFLOW]                          │  │  │
│  │  │                                                │  │  │
│  │  │  • Setup Java + Maven                         │  │  │
│  │  │  • Dependency caching                         │  │  │
│  │  │  • Build + Test                               │  │  │
│  │  │  • Coverage report                            │  │  │
│  │  │  • Artifact upload                            │  │  │
│  │  └────────────────────────────────────────────────┘  │  │
│  │           ▲                            ▲              │  │
│  │           │                            │              │  │
│  │  ┌────────┴────────────┐    ┌─────────┴──────────┐  │  │
│  │  │   main.yml          │    │   feature.yml      │  │  │
│  │  │  [MAIN PIPELINE]    │    │  [FEATURE BRANCH]  │  │  │
│  │  │                     │    │                    │  │  │
│  │  │  1. Build & Test ───┼────┤  1. Build & Test  │  │  │
│  │  │     (calls reusable)│    │     (calls reusab) │  │  │
│  │  │  2. SonarCloud      │    │  2. SonarCloud PR  │  │  │
│  │  │  3. Security Scan   │    │  3. Security Scan  │  │  │
│  │  │  4. Docker Build    │    │  4. Docker Build   │  │  │
│  │  │  5. Docker Push ─┐  │    │     (no push)      │  │  │
│  │  └──────────────────┼──┘    └────────────────────┘  │  │
│  └───────────────────────────────────────────────────────┘  │
│                        │                                     │
└────────────────────────┼─────────────────────────────────────┘
                         │
                         ▼
        ┌────────────────────────────────────┐
        │      External Integrations         │
        │                                    │
        │  ┌──────────┐  ┌──────────────┐  │
        │  │SonarCloud│  │  DockerHub   │  │
        │  │          │  │              │  │
        │  │ Quality  │  │ Image        │  │
        │  │ Gate     │  │ Registry     │  │
        │  └──────────┘  └──────────────┘  │
        └────────────────────────────────────┘
```

### Fluxo de Dados: Pipeline Main

```
┌─────────────────────────────────────────────────────────────────┐
│                         TRIGGER EVENT                            │
│        (push to main / PR / manual workflow_dispatch)            │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  JOB 1: build-and-test                                          │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Calls: ./.github/workflows/java-reusable.yml          │   │
│  │  Inputs:                                                 │   │
│  │    - java-version: '17'                                 │   │
│  │    - maven-args: 'clean install'                        │   │
│  │  Outputs:                                                │   │
│  │    - artifact-path: target/*.jar                        │   │
│  │    - coverage-report: target/site/jacoco/jacoco.xml     │   │
│  └─────────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────────┘
                         │ [SUCCESS]
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  JOB 2: sonar-analysis                                          │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  needs: [build-and-test]                                │   │
│  │  Steps:                                                  │   │
│  │    1. Checkout code                                     │   │
│  │    2. Download coverage report (artifact)               │   │
│  │    3. SonarCloud scan                                   │   │
│  │       - Uses: SonarSource/sonarcloud-github-action      │   │
│  │       - Secrets: SONAR_TOKEN                            │   │
│  │    4. Check Quality Gate                                │   │
│  │       - If FAILED → Exit 1 (bloqueia pipeline)         │   │
│  └─────────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────────┘
                         │ [QUALITY GATE PASSED]
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  JOB 3: security-scan                                           │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  needs: [sonar-analysis]                                │   │
│  │  Steps:                                                  │   │
│  │    1. Checkout code                                     │   │
│  │    2. Run Trivy scan                                    │   │
│  │       - Scan filesystem for vulnerabilities             │   │
│  │       - Severity: HIGH,CRITICAL                         │   │
│  │    3. Upload results to GitHub Security                 │   │
│  └─────────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────────┘
                         │ [NO CRITICAL VULNERABILITIES]
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  JOB 4: docker-build                                            │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  needs: [security-scan]                                 │   │
│  │  Steps:                                                  │   │
│  │    1. Checkout code                                     │   │
│  │    2. Setup Docker Buildx                               │   │
│  │    3. Download JAR artifact                             │   │
│  │    4. Build image                                       │   │
│  │       - Multi-stage build                               │   │
│  │       - Cache from/to registry                          │   │
│  │       - Tag: temp-${{ github.sha }}                     │   │
│  │    5. Test image (smoke test)                           │   │
│  └─────────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────────┘
                         │ [IMAGE BUILT SUCCESSFULLY]
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  JOB 5: docker-push                                             │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  needs: [docker-build]                                  │   │
│  │  if: github.ref == 'refs/heads/main'                    │   │
│  │  Steps:                                                  │   │
│  │    1. Login to DockerHub                                │   │
│  │       - Username: ${{ secrets.DOCKERHUB_USERNAME }}     │   │
│  │       - Token: ${{ secrets.DOCKERHUB_TOKEN }}           │   │
│  │    2. Push with multiple tags                           │   │
│  │       - latest                                          │   │
│  │       - v{version} (from pom.xml)                       │   │
│  │       - {sha}                                           │   │
│  │    3. Update README on DockerHub (optional)             │   │
│  │    4. Logout                                            │   │
│  └─────────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────────┘
                         │ [DEPLOYMENT COMPLETED]
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  JOB 6: notify                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  if: always()                                           │   │
│  │  Steps:                                                  │   │
│  │    1. Generate summary                                  │   │
│  │    2. Post to GitHub Actions summary                    │   │
│  │    3. (Optional) Notify Slack/Discord                   │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

## 🔧 Especificações Técnicas Detalhadas

### Workflow 1: java-reusable.yml

```yaml
name: Java CI Reusable Workflow

on:
  workflow_call:
    inputs:
      java-version:
        description: 'Java version to use'
        required: false
        type: string
        default: '17'
      maven-args:
        description: 'Maven arguments'
        required: false
        type: string
        default: 'clean install'
      run-tests:
        description: 'Run tests'
        required: false
        type: boolean
        default: true
      upload-artifacts:
        description: 'Upload build artifacts'
        required: false
        type: boolean
        default: true
    outputs:
      artifact-path:
        description: 'Path to built artifact'
        value: ${{ jobs.build.outputs.artifact-path }}
      build-status:
        description: 'Build status (success/failure)'
        value: ${{ jobs.build.outputs.build-status }}
      test-results:
        description: 'Test results summary'
        value: ${{ jobs.build.outputs.test-results }}

jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      artifact-path: ${{ steps.build.outputs.artifact-path }}
      build-status: ${{ steps.build.outputs.status }}
      test-results: ${{ steps.test.outputs.summary }}
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up JDK ${{ inputs.java-version }}
        uses: actions/setup-java@v4
        with:
          java-version: ${{ inputs.java-version }}
          distribution: 'temurin'
          cache: 'maven'
      
      - name: Build with Maven
        id: build
        run: |
          mvn ${{ inputs.maven-args }} -B -V
          echo "artifact-path=target/*.jar" >> $GITHUB_OUTPUT
          echo "status=success" >> $GITHUB_OUTPUT
      
      - name: Run Tests
        id: test
        if: inputs.run-tests
        run: |
          mvn test -B
          # Generate summary
          TOTAL=$(grep -oP 'Tests run: \K\d+' target/surefire-reports/*.xml | awk '{s+=$1} END {print s}')
          FAILED=$(grep -oP 'Failures: \K\d+' target/surefire-reports/*.xml | awk '{s+=$1} END {print s}')
          echo "summary=Total: $TOTAL, Failed: $FAILED" >> $GITHUB_OUTPUT
      
      - name: Generate Coverage Report
        if: inputs.run-tests
        run: mvn jacoco:report
      
      - name: Upload JAR
        if: inputs.upload-artifacts
        uses: actions/upload-artifact@v4
        with:
          name: application-jar
          path: target/*.jar
          retention-days: 30
      
      - name: Upload Test Reports
        if: inputs.run-tests && inputs.upload-artifacts
        uses: actions/upload-artifact@v4
        with:
          name: test-reports
          path: |
            target/surefire-reports/
            target/site/jacoco/
          retention-days: 30
```

### Workflow 2: main.yml

**Triggers**:
```yaml
on:
  push:
    branches: [main, master]
    paths:
      - 'src/**'
      - 'pom.xml'
      - 'Dockerfile'
      - '.github/workflows/**'
  pull_request:
    branches: [main, master]
  workflow_dispatch:
    inputs:
      skip-tests:
        description: 'Skip tests'
        required: false
        type: boolean
        default: false
```

**Secrets Required**:
- `SONAR_TOKEN`: SonarCloud authentication
- `DOCKERHUB_USERNAME`: DockerHub username
- `DOCKERHUB_TOKEN`: DockerHub access token

**Environment Variables**:
```yaml
env:
  JAVA_VERSION: '17'
  MAVEN_OPTS: '-Xmx3072m'
  DOCKER_IMAGE: ${{ secrets.DOCKERHUB_USERNAME }}/${{ github.event.repository.name }}
```

### Dockerfile Multi-Stage

```dockerfile
# Stage 1: Build
FROM maven:3.9-eclipse-temurin-17 AS builder

WORKDIR /app

# Copy dependency files first (cache layer)
COPY pom.xml .
RUN mvn dependency:go-offline -B

# Copy source and build
COPY src ./src
RUN mvn clean package -DskipTests -B

# Stage 2: Runtime
FROM eclipse-temurin:17-jre-alpine

# Add non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

# Copy only the JAR from builder
COPY --from=builder /app/target/*.jar app.jar

# Set ownership
RUN chown -R appuser:appgroup /app

USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8080/actuator/health || exit 1

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
```

### SonarCloud Configuration

**sonar-project.properties** (na raiz do projeto):
```properties
sonar.projectKey=GITHUB_ORG_REPO_NAME
sonar.organization=GITHUB_ORG
sonar.projectName=Repository Name
sonar.projectVersion=1.0

# Source paths
sonar.sources=src/main/java
sonar.tests=src/test/java

# Java version
sonar.java.source=17
sonar.java.target=17

# Coverage
sonar.coverage.jacoco.xmlReportPaths=target/site/jacoco/jacoco.xml
sonar.junit.reportPaths=target/surefire-reports

# Exclusions
sonar.exclusions=**/config/**,**/dto/**,**/entity/**
sonar.test.exclusions=**/test/**

# Quality Gate
sonar.qualitygate.wait=true
sonar.qualitygate.timeout=300
```

## 🔒 Segurança

### Secrets Management

**Configuração de Secrets** (GitHub Repository Settings → Secrets and variables → Actions):

1. **SONAR_TOKEN**:
   - Obtido em: SonarCloud → My Account → Security → Generate Token
   - Scope: Analyze projects
   - Expiration: No expiration (ou 90 dias para maior segurança)

2. **DOCKERHUB_USERNAME**:
   - Seu username do DockerHub
   - Exemplo: `mycompany`

3. **DOCKERHUB_TOKEN**:
   - Obtido em: DockerHub → Account Settings → Security → New Access Token
   - Permissions: Read & Write
   - Never expires (ou configure expiração)

### Security Best Practices

```yaml
# ✅ BOM: Usar secrets corretamente
- name: Login to DockerHub
  uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKERHUB_USERNAME }}
    password: ${{ secrets.DOCKERHUB_TOKEN }}

# ❌ RUIM: Nunca imprimir secrets
- name: Debug (NÃO FAZER)
  run: echo ${{ secrets.DOCKERHUB_TOKEN }}

# ✅ BOM: Mascarar valores sensíveis
- name: Safe debug
  run: |
    echo "Username configured: ✓"
    echo "Token configured: ✓"
```

### Dependency Scanning

```yaml
- name: OWASP Dependency Check
  uses: dependency-check/Dependency-Check_Action@main
  with:
    path: '.'
    format: 'HTML'
    args: >
      --enableExperimental
      --failOnCVSS 7

- name: Upload Dependency Check results
  uses: actions/upload-artifact@v4
  with:
    name: dependency-check-report
    path: reports/
```

## 📊 Monitoramento & Observabilidade

### Métricas Coletadas

1. **Build Metrics**:
   - Tempo de build (total e por step)
   - Success rate (%)
   - Frequência de builds

2. **Quality Metrics**:
   - Code coverage (%)
   - Quality Gate status
   - Bugs/Vulnerabilities/Code Smells

3. **Deployment Metrics**:
   - Deployment frequency
   - Lead time (commit → deploy)
   - Change failure rate

### GitHub Actions Summary

```yaml
- name: Generate Summary
  if: always()
  run: |
    cat >> $GITHUB_STEP_SUMMARY <<EOF
    ## 🚀 Pipeline Summary
    
    ### Build & Test
    - **Status**: ${{ steps.build.outcome }}
    - **Duration**: ${{ steps.build.duration }}
    - **Tests**: ${{ steps.test.outputs.summary }}
    
    ### Quality Analysis
    - **SonarCloud**: ${{ steps.sonar.outcome }}
    - **Quality Gate**: ${{ steps.sonar.outputs.quality-gate }}
    - **Coverage**: ${{ steps.sonar.outputs.coverage }}%
    
    ### Security Scan
    - **Vulnerabilities**: ${{ steps.trivy.outputs.vulnerabilities }}
    
    ### Docker
    - **Image**: \`${{ env.DOCKER_IMAGE }}:${{ github.sha }}\`
    - **Size**: ${{ steps.docker.outputs.image-size }}
    
    ---
    📊 [View full report on SonarCloud](${{ steps.sonar.outputs.dashboard-url }})
    EOF
```

## 🧪 Estratégia de Testes

### Testes de Workflow

**act** - Run GitHub Actions locally:
```bash
# Instalar act
brew install act  # macOS
# ou
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Testar workflow localmente
act -j build-and-test
act -j sonar-analysis --secret-file .secrets
act push --workflows .github/workflows/main.yml
```

### Validação de YAML

```bash
# Instalar actionlint
brew install actionlint

# Validar workflows
actionlint .github/workflows/*.yml
```

### Projeto de Teste

Criar repositório de teste `java-ci-template-test` com:
- Aplicação Spring Boot mínima
- Testes unitários
- Dockerfile
- Workflows configurados
- SonarCloud e DockerHub configurados

## 📈 Performance & Otimização

### Cache Strategy

**Maven Dependencies**:
```yaml
- uses: actions/setup-java@v4
  with:
    java-version: '17'
    distribution: 'temurin'
    cache: 'maven'  # Automático
```

**Docker Layer Caching**:
```yaml
- uses: docker/build-push-action@v5
  with:
    cache-from: type=registry,ref=${{ env.DOCKER_IMAGE }}:cache
    cache-to: type=registry,ref=${{ env.DOCKER_IMAGE }}:cache,mode=max
```

### Build Time Optimization

| Otimização | Tempo Economizado | Implementação |
|------------|-------------------|---------------|
| Maven dependency cache | ~2-3 min | setup-java cache |
| Docker layer cache | ~1-2 min | build-push-action cache |
| Parallel tests | ~30s | maven-surefire parallel |
| Skip tests em retrigger | ~1 min | workflow_dispatch input |

**Target**: Build completo < 10 min, com cache < 5 min

## 🔄 Rollback & Recovery

### Rollback de Imagem Docker

```bash
# Listar tags disponíveis
curl -s https://hub.docker.com/v2/repositories/USERNAME/REPO/tags/ | jq

# Deploy de versão anterior
docker pull USERNAME/REPO:v1.2.0
docker tag USERNAME/REPO:v1.2.0 USERNAME/REPO:latest
docker push USERNAME/REPO:latest
```

### Reverter Workflow

```yaml
# Trigger manual com escolha de versão
workflow_dispatch:
  inputs:
    version:
      description: 'Version to deploy'
      required: true
      default: 'latest'
```

## 📚 Documentação de Configuração

### Documento: ci-cd-configuration.md

**Estrutura**:
1. **Pré-requisitos**
   - Conta GitHub
   - Conta SonarCloud
   - Conta DockerHub
   - Projeto Maven válido

2. **Quick Start** (< 10 minutos)
   - Passo 1: Copiar workflows
   - Passo 2: Configurar secrets
   - Passo 3: Criar sonar-project.properties
   - Passo 4: Criar Dockerfile
   - Passo 5: Push e validar

3. **Referência Completa**
   - Inputs de workflows
   - Outputs disponíveis
   - Variáveis de ambiente
   - Customização avançada

4. **Troubleshooting**
   - Top 10 erros
   - Como debugar
   - Logs úteis
   - Contatos de suporte

## ✅ Checklist de Implementação

### Para Desenvolvedores
- [ ] Copiar workflows para `.github/workflows/`
- [ ] Criar `sonar-project.properties` na raiz
- [ ] Criar `Dockerfile` na raiz
- [ ] Configurar secrets no GitHub
- [ ] Fazer push e validar primeiro build
- [ ] Adicionar badges no README

### Para DevOps
- [ ] Validar YAML com actionlint
- [ ] Testar workflows localmente com act
- [ ] Configurar projeto no SonarCloud
- [ ] Criar repositório no DockerHub
- [ ] Documentar processo de troubleshooting
- [ ] Configurar notificações (opcional)

## 🎯 Métricas de Sucesso Arquitetural

- ✅ **Reusabilidade**: Workflows funcionam em 100% dos projetos Maven padrão
- ✅ **Performance**: Build < 10 min (fresh), < 5 min (cached)
- ✅ **Confiabilidade**: Success rate > 95%
- ✅ **Manutenibilidade**: Mudanças em < 30 min
- ✅ **Segurança**: 0 secrets expostos, 0 vulnerabilities críticas

---

**Status**: Aguardando Revisão Colaborativa
**Próximos Passos**: Scrum Master quebra em stories implementáveis
**Aprovação**: Architect Agent
**Data**: 24/10/2025

