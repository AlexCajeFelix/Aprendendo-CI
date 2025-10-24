# 🚀 Configuração CI/CD - Guia Completo

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Pré-requisitos](#pré-requisitos)
3. [Quick Start (< 10 minutos)](#quick-start)
4. [Configuração Detalhada](#configuração-detalhada)
5. [Estrutura dos Workflows](#estrutura-dos-workflows)
6. [Troubleshooting](#troubleshooting)
7. [Exemplos Avançados](#exemplos-avançados)
8. [FAQ](#faq)

---

## 🎯 Visão Geral

Este repositório fornece um sistema CI/CD completo e reutilizável para projetos **Java/Spring Boot** com:

✅ **Build e testes automatizados** (Maven)  
✅ **Análise de qualidade de código** (SonarCloud)  
✅ **Scan de segurança** (Trivy)  
✅ **Build de imagens Docker** otimizadas  
✅ **Deploy automático** para DockerHub  

### Arquitetura

```
Push/PR → Build & Test → SonarCloud → Security Scan → Docker Build → Docker Push
              ↓              ↓              ↓              ↓              ↓
           ✅ JAR        ✅ Quality     ✅ No Vulns    ✅ Image      ✅ DockerHub
```

---

## 📦 Pré-requisitos

### Obrigatórios

- ✅ Projeto Java Maven (Spring Boot recomendado)
- ✅ Conta GitHub com repositório
- ✅ GitHub Actions habilitado no repositório
- ✅ Java 11, 17 ou 21

### Opcionais (mas recomendados)

- 🔹 Conta SonarCloud (para análise de qualidade)
- 🔹 Conta DockerHub (para deploy de imagens)

---

## ⚡ Quick Start

### Passo 1: Copiar Workflows (2 min)

```bash
# No seu projeto Java/Spring Boot

# 1. Criar estrutura de pastas
mkdir -p .github/workflows

# 2. Copiar workflows
cp /path/to/this/repo/.github/workflows/java-reusable.yml .github/workflows/
cp /path/to/this/repo/.github/workflows/main.yml .github/workflows/

# 3. Copiar templates
cp /path/to/this/repo/Dockerfile.template Dockerfile
cp /path/to/this/repo/sonar-project.properties.template sonar-project.properties
```

### Passo 2: Configurar sonar-project.properties (2 min)

Edite `sonar-project.properties` e substitua os placeholders:

```properties
# Antes
sonar.projectKey={{GITHUB_ORG}}_{{REPO_NAME}}

# Depois (exemplo)
sonar.projectKey=mycompany_my-spring-app
sonar.organization=mycompany
sonar.projectName=My Spring App
```

**Como descobrir valores:**
- `GITHUB_ORG`: Seu username/organização GitHub (ex: `octocat`)
- `REPO_NAME`: Nome do repositório (ex: `my-app`)
- `PROJECT_NAME`: Nome legível do projeto

### Passo 3: Configurar Secrets no GitHub (3 min)

1. Vá para: **Repository → Settings → Secrets and variables → Actions**

2. Clique em **"New repository secret"** e adicione:

#### SONAR_TOKEN (Obrigatório para SonarCloud)

```
Nome: SONAR_TOKEN
Valor: <seu token do SonarCloud>
```

**Como obter:**
1. Acesse [SonarCloud](https://sonarcloud.io)
2. Login com GitHub
3. Vá em: **My Account → Security → Generate Token**
4. Nome: `GitHub Actions`
5. Type: `User Token` ou `Project Analysis Token`
6. Copie o token gerado

#### DOCKERHUB_USERNAME (Obrigatório para DockerHub)

```
Nome: DOCKERHUB_USERNAME
Valor: seu_username_dockerhub
```

#### DOCKERHUB_TOKEN (Obrigatório para DockerHub)

```
Nome: DOCKERHUB_TOKEN
Valor: <seu access token do DockerHub>
```

**Como obter:**
1. Acesse [DockerHub](https://hub.docker.com)
2. Login
3. Vá em: **Account Settings → Security → New Access Token**
4. Description: `GitHub Actions`
5. Access permissions: `Read & Write`
6. Copie o token gerado

### Passo 4: Ajustar Dockerfile (1 min)

Edite `Dockerfile` e customize se necessário:

```dockerfile
# Ajuste o health check endpoint se sua app não usar Spring Actuator
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8080/actuator/health || exit 1

# Se sua app não tem health endpoint, remova a linha HEALTHCHECK
```

### Passo 5: Commit e Push (1 min)

```bash
git add .github/ Dockerfile sonar-project.properties
git commit -m "ci: add CI/CD workflows"
git push origin main
```

🎉 **Pronto!** Vá para **Actions** no GitHub e veja o pipeline rodando!

---

## 🔧 Configuração Detalhada

### Estrutura dos Workflows

```
.github/workflows/
├── java-reusable.yml    # Workflow reutilizável (build + test)
└── main.yml             # Pipeline completo (orquestrador)
```

### java-reusable.yml

**Propósito**: Template reutilizável para build e teste Java/Maven

**Inputs**:

| Input | Tipo | Default | Descrição |
|-------|------|---------|-----------|
| `java-version` | string | `'17'` | Versão do Java (11, 17, 21) |
| `maven-args` | string | `'clean install'` | Argumentos do Maven |
| `skip-tests` | boolean | `false` | Pular execução de testes |
| `upload-artifacts` | boolean | `true` | Upload de artifacts (JAR) |

**Outputs**:

| Output | Descrição |
|--------|-----------|
| `artifact-name` | Nome do artifact uploadado |
| `build-status` | Status do build (success/failure) |
| `jar-version` | Versão extraída do pom.xml |

**Exemplo de uso customizado**:

```yaml
jobs:
  my-build:
    uses: ./.github/workflows/java-reusable.yml
    with:
      java-version: '21'
      maven-args: 'clean package -Pproduction'
      skip-tests: false
```

### main.yml

**Propósito**: Pipeline completo com múltiplos stages

**Triggers**:
- ✅ Push em `main` ou `master`
- ✅ Pull Requests
- ✅ Manual (workflow_dispatch)

**Inputs manuais**:

| Input | Tipo | Default | Descrição |
|-------|------|---------|-----------|
| `skip-tests` | boolean | `false` | Pular testes |
| `skip-docker` | boolean | `false` | Pular Docker build |

**Jobs**:

1. **build-and-test**: Chama `java-reusable.yml`
2. **sonar-analysis**: Análise SonarCloud
3. **security-scan**: Trivy vulnerability scan
4. **docker-build**: Build imagem Docker
5. **docker-push**: Push para DockerHub (só em main)
6. **summary**: Resumo do pipeline

### Variáveis de Ambiente

**Definidas no workflow**:

```yaml
env:
  JAVA_VERSION: '17'
  MAVEN_OPTS: '-Xmx3072m'
```

**Customizar localmente** (para debugging):

```bash
export JAVA_VERSION=21
export MAVEN_OPTS="-Xmx4096m"
```

---

## 🔒 Gerenciamento de Secrets

### Secrets Necessários

| Secret | Obrigatório? | Usado em | Descrição |
|--------|--------------|----------|-----------|
| `SONAR_TOKEN` | ❌ Opcional* | sonar-analysis | Token do SonarCloud |
| `DOCKERHUB_USERNAME` | ❌ Opcional* | docker-push | Username DockerHub |
| `DOCKERHUB_TOKEN` | ❌ Opcional* | docker-push | Access token DockerHub |
| `GITHUB_TOKEN` | ✅ Automático | Todos | Token do GitHub (auto-gerado) |

\* *Opcional: Se não configurado, o step correspondente será pulado com warning*

### Best Practices de Segurança

✅ **FAZER**:
- Usar tokens com escopo mínimo necessário
- Rotacionar tokens a cada 90 dias
- Usar diferentes tokens para dev/prod
- Nunca commitar secrets no código

❌ **NÃO FAZER**:
- Logar secrets no console
- Usar tokens pessoais em produção
- Compartilhar tokens via Slack/Email
- Hardcodar tokens em workflows

### Validar Secrets Configurados

```bash
# Script para validar (não expõe valores)
gh secret list
```

Output esperado:
```
DOCKERHUB_TOKEN    Updated 2024-10-24
DOCKERHUB_USERNAME Updated 2024-10-24
SONAR_TOKEN        Updated 2024-10-24
```

---

## 🐳 Configuração Docker

### Dockerfile Multi-Stage

O template fornecido usa **multi-stage build** para otimizar:

**Stage 1: Builder**
- Base: `maven:3.9-eclipse-temurin-17`
- Propósito: Compilar aplicação
- Tamanho: ~700MB (descartado)

**Stage 2: Runtime**
- Base: `eclipse-temurin:17-jre-alpine`
- Propósito: Executar aplicação
- Tamanho: ~150-200MB ✅

### Customizações Comuns

#### Mudar versão do Java

```dockerfile
# De:
FROM maven:3.9-eclipse-temurin-17 AS builder
FROM eclipse-temurin:17-jre-alpine

# Para:
FROM maven:3.9-eclipse-temurin-21 AS builder
FROM eclipse-temurin:21-jre-alpine
```

#### Adicionar dependências do sistema

```dockerfile
# Stage runtime
FROM eclipse-temurin:17-jre-alpine

# Adicionar ferramentas
RUN apk add --no-cache curl bash
```

#### Customizar health check

```dockerfile
# Para API REST sem Actuator
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8080/health || exit 1

# Para apps sem health endpoint
# Remover linha HEALTHCHECK completamente
```

### Testar Imagem Localmente

```bash
# 1. Build local
docker build -t my-app:test .

# 2. Ver tamanho
docker images my-app:test

# 3. Rodar container
docker run -p 8080:8080 my-app:test

# 4. Testar health check
docker ps  # Deve mostrar "healthy" após 40s
```

---

## 📊 Configuração SonarCloud

### Setup Inicial

1. **Criar Projeto no SonarCloud**:
   - Acesse: https://sonarcloud.io
   - Clique: **"Analyze new project"**
   - Selecione repositório GitHub
   - Escolha: **"With GitHub Actions"**

2. **Configurar Quality Gate**:
   - Vá em: **Administration → Quality Gates**
   - Use: **"Sonar way"** (padrão) ou customize

### Métricas Coletadas

| Métrica | Threshold Padrão | Descrição |
|---------|------------------|-----------|
| **Coverage** | > 80% | Cobertura de testes |
| **Duplications** | < 3% | Código duplicado |
| **Maintainability** | A | Code smells |
| **Reliability** | A | Bugs |
| **Security** | A | Vulnerabilidades |

### Quality Gate: Quando Bloqueia?

O workflow **falha** se:
- ❌ Quality Gate = FAILED
- ❌ Vulnerabilidades = A ou B (critical/high)
- ❌ Bugs = A (critical)

O workflow **passa com warning** se:
- ⚠️ Coverage < 80%
- ⚠️ Code smells > threshold
- ⚠️ Duplicação > 3%

### Ver Resultados

Após o pipeline rodar:
1. Vá em: **Actions → Pipeline run → Summary**
2. Clique no link: **"SonarCloud Dashboard"**
3. Ou acesse direto: `https://sonarcloud.io/dashboard?id=ORG_REPO`

---

## 🛠️ Troubleshooting

### Problema 1: "SONAR_TOKEN not configured"

**Sintoma**:
```
⚠️ SONAR_TOKEN not configured. Skipping SonarCloud analysis.
```

**Solução**:
1. Configure secret conforme [Passo 3](#passo-3-configurar-secrets-no-github-3-min)
2. Se não quer SonarCloud, ignore o warning (não é erro fatal)

### Problema 2: "Could not find artifact"

**Sintoma**:
```
Error: Could not find artifact application-jar-abc123
```

**Solução**:
```yaml
# Em main.yml, certifique-se de usar o output correto:
- uses: actions/download-artifact@v4
  with:
    name: ${{ needs.build-and-test.outputs.artifact-name }}  # ✅
    # NÃO: name: application-jar  # ❌
```

### Problema 3: Docker push falha com "authentication required"

**Sintoma**:
```
Error: failed to solve: failed to push: authentication required
```

**Causas e Soluções**:

1. **Secrets não configurados**:
   ```bash
   # Verificar
   gh secret list | grep DOCKERHUB
   
   # Se vazio, configure conforme Passo 3
   ```

2. **Username ou token incorretos**:
   - Re-gere token no DockerHub
   - Atualiza secret no GitHub

3. **Token expirado**:
   - Tokens podem expirar (90 dias default)
   - Gere novo token

### Problema 4: Pipeline muito lento

**Sintoma**: Build levando > 15 minutos

**Soluções**:

1. **Verificar cache do Maven**:
   ```yaml
   # Em java-reusable.yml
   - uses: actions/setup-java@v4
     with:
       cache: 'maven'  # ← Certificar que está presente
   ```

2. **Verificar cache do Docker**:
   ```yaml
   # Em main.yml
   - uses: docker/build-push-action@v5
     with:
       cache-from: type=gha  # ← Deve estar presente
       cache-to: type=gha,mode=max
   ```

3. **Pular testes em rebuilds**:
   ```bash
   # Trigger manual com skip-tests
   gh workflow run main.yml -f skip-tests=true
   ```

### Problema 5: Quality Gate sempre falhando

**Sintoma**: SonarCloud sempre retorna FAILED

**Soluções**:

1. **Verificar threshold do Quality Gate**:
   - SonarCloud → Quality Gates
   - Ajustar se necessário (ex: coverage 70% em vez de 80%)

2. **Ignorar arquivos gerados**:
   ```properties
   # sonar-project.properties
   sonar.exclusions=**/generated/**,**/dto/**
   ```

3. **Corrigir código**:
   - Ver relatório detalhado no SonarCloud
   - Corrigir bugs/vulnerabilidades críticas

### Problema 6: "No tests were found"

**Sintoma**:
```
[ERROR] No tests were found
```

**Soluções**:

1. **Projeto sem testes ainda**:
   ```yaml
   # Use skip-tests temporariamente
   uses: ./.github/workflows/java-reusable.yml
   with:
     skip-tests: true
   ```

2. **Testes em diretório não padrão**:
   ```xml
   <!-- pom.xml -->
   <testSourceDirectory>src/test/java</testSourceDirectory>
   ```

### Debugging Avançado

#### Testar workflow localmente com act

```bash
# Instalar act
brew install act  # macOS
# ou
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Testar workflow
act -j build-and-test

# Com secrets
act -j sonar-analysis --secret-file .secrets

# Ver apenas o que seria executado
act -j build-and-test --dryrun
```

#### Ver logs detalhados

```bash
# Via GitHub CLI
gh run view --log

# Ou no navegador:
# Actions → <run> → <job> → <step>
```

---

## 🚀 Exemplos Avançados

### Exemplo 1: Workflow para Feature Branches

Criar `.github/workflows/feature.yml`:

```yaml
name: Feature Branch CI

on:
  push:
    branches-ignore:
      - main
      - master

jobs:
  quick-check:
    uses: ./.github/workflows/java-reusable.yml
    with:
      java-version: '17'
      skip-tests: false
      upload-artifacts: false  # Não precisa em feature branches
```

### Exemplo 2: Matrix Build (múltiplas versões Java)

```yaml
jobs:
  build-matrix:
    strategy:
      matrix:
        java: [11, 17, 21]
    uses: ./.github/workflows/java-reusable.yml
    with:
      java-version: ${{ matrix.java }}
```

### Exemplo 3: Deploy Condicional

```yaml
docker-push:
  if: |
    github.ref == 'refs/heads/main' &&
    contains(github.event.head_commit.message, '[deploy]')
  # ...resto do job
```

### Exemplo 4: Notificações Slack

```yaml
- name: Notify Slack
  if: failure()
  uses: slackapi/slack-github-action@v1
  with:
    webhook-url: ${{ secrets.SLACK_WEBHOOK }}
    payload: |
      {
        "text": "❌ Build failed: ${{ github.repository }}"
      }
```

---

## ❓ FAQ

### P: Posso usar Gradle em vez de Maven?

**R**: Atualmente não. O workflow é otimizado para Maven. Gradle será suportado na Fase 4.

**Workaround**:
```yaml
# Customize java-reusable.yml:
- name: Build with Gradle
  run: ./gradlew build
```

### P: Como fazer deploy em Kubernetes?

**R**: O workflow atual só faz push para DockerHub. Para K8s:

```yaml
# Adicionar job de deploy
deploy-k8s:
  needs: [docker-push]
  runs-on: ubuntu-latest
  steps:
    - name: Deploy to K8s
      run: |
        kubectl set image deployment/my-app \
          my-app=${{ secrets.DOCKERHUB_USERNAME }}/my-app:${{ github.sha }}
```

### P: Posso rodar pipeline em self-hosted runner?

**R**: Sim!

```yaml
jobs:
  build:
    runs-on: self-hosted  # Em vez de ubuntu-latest
```

### P: Como fazer rollback?

**R**:
```bash
# Listar tags disponíveis
gh api repos/{owner}/{repo}/actions/artifacts

# Re-rodar workflow de commit anterior
gh run rerun <run-id>

# Ou fazer deploy manual de tag antiga
docker pull myuser/myapp:abc123
docker tag myuser/myapp:abc123 myuser/myapp:latest
docker push myuser/myapp:latest
```

### P: SonarCloud é obrigatório?

**R**: Não! Se `SONAR_TOKEN` não estiver configurado, o step é pulado automaticamente.

### P: Quanto custa?

**R**:
- GitHub Actions: **Grátis** até 2000 min/mês (public repos ilimitado)
- SonarCloud: **Grátis** para projetos open source
- DockerHub: **Grátis** 1 repo privado, pulls ilimitados com login

---

## 📚 Recursos Adicionais

### Documentação Oficial

- [GitHub Actions](https://docs.github.com/en/actions)
- [SonarCloud](https://docs.sonarcloud.io/)
- [Docker Build Push Action](https://github.com/docker/build-push-action)
- [Trivy](https://aquasecurity.github.io/trivy/)

### Exemplos de Projetos

- [Spring PetClinic com CI/CD](https://github.com/spring-projects/spring-petclinic)
- [Reusable Workflows Best Practices](https://docs.github.com/en/actions/using-workflows/reusing-workflows)

### Suporte

- 🐛 Issues: [GitHub Issues](../../issues)
- 💬 Discussões: [GitHub Discussions](../../discussions)
- 📧 Email: devops@exemplo.com

---

## ✅ Checklist de Implementação

Use este checklist para garantir setup completo:

### Setup Inicial
- [ ] Workflows copiados para `.github/workflows/`
- [ ] `Dockerfile` criado na raiz
- [ ] `sonar-project.properties` criado e configurado
- [ ] Secrets configurados no GitHub

### Configuração SonarCloud
- [ ] Projeto criado no SonarCloud
- [ ] Quality Gate configurado
- [ ] `SONAR_TOKEN` adicionado aos secrets

### Configuração DockerHub
- [ ] Repositório criado no DockerHub
- [ ] `DOCKERHUB_USERNAME` adicionado aos secrets
- [ ] `DOCKERHUB_TOKEN` adicionado aos secrets

### Validação
- [ ] Push feito e pipeline executou
- [ ] Build passou com sucesso
- [ ] SonarCloud analisou (se configurado)
- [ ] Docker image foi criada
- [ ] Docker push funcionou (se em main)

### Documentação
- [ ] README atualizado com badges
- [ ] Time informado sobre novo CI/CD
- [ ] Troubleshooting guide revisado

---

**Versão**: 1.0.0  
**Última atualização**: 24/10/2025  
**Maintainers**: DevOps Team  

🎉 **Configuração completa! Seu CI/CD está pronto para uso!**

