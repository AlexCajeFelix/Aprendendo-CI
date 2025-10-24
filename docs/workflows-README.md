# 🚀 CI/CD Workflows - Guia Rápido

[![CI/CD Pipeline](https://github.com/USERNAME/REPO/actions/workflows/main.yml/badge.svg)](https://github.com/USERNAME/REPO/actions/workflows/main.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ORG_REPO&metric=alert_status)](https://sonarcloud.io/dashboard?id=ORG_REPO)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=ORG_REPO&metric=coverage)](https://sonarcloud.io/dashboard?id=ORG_REPO)

## 📋 O que é isso?

Sistema de **CI/CD reutilizável** para projetos Java/Spring Boot que automatiza:

✅ Build e testes com Maven  
✅ Análise de qualidade (SonarCloud)  
✅ Scan de segurança (Trivy)  
✅ Build de imagens Docker otimizadas  
✅ Deploy automático para DockerHub  

## ⚡ Quick Start

### 1️⃣ Para usar em um projeto novo

```bash
# Copiar workflows
cp -r .github/workflows/* SEU_PROJETO/.github/workflows/

# Copiar templates
cp Dockerfile.template SEU_PROJETO/Dockerfile
cp sonar-project.properties.template SEU_PROJETO/sonar-project.properties

# Configurar secrets no GitHub:
# - SONAR_TOKEN
# - DOCKERHUB_USERNAME
# - DOCKERHUB_TOKEN
```

### 2️⃣ Customizar sonar-project.properties

```properties
sonar.projectKey=GITHUB_ORG_REPO_NAME
sonar.organization=GITHUB_ORG
sonar.projectName=Meu Projeto
```

### 3️⃣ Commit e Push

```bash
git add .github/ Dockerfile sonar-project.properties
git commit -m "ci: add CI/CD workflows"
git push origin main
```

🎉 **Pronto!** Pipeline rodando automaticamente.

## 📂 Estrutura

```
.github/workflows/
├── java-reusable.yml    # Workflow reutilizável (build + test)
└── main.yml             # Pipeline completo (orquestrador)

Dockerfile.template                      # Dockerfile multi-stage otimizado
sonar-project.properties.template        # Config SonarCloud
docs/ci-cd-configuration.md             # Documentação completa
```

## 🔧 Workflows Disponíveis

### java-reusable.yml

**Workflow reutilizável** para build e teste Java.

**Uso**:
```yaml
jobs:
  build:
    uses: ./.github/workflows/java-reusable.yml
    with:
      java-version: '17'
      maven-args: 'clean install'
      skip-tests: false
```

**Inputs**:
- `java-version`: `'11'`, `'17'`, `'21'` (default: `'17'`)
- `maven-args`: Argumentos Maven (default: `'clean install'`)
- `skip-tests`: Pular testes (default: `false`)
- `upload-artifacts`: Upload JAR (default: `true`)

**Outputs**:
- `artifact-name`: Nome do artifact
- `build-status`: Status do build
- `jar-version`: Versão do pom.xml

### main.yml

**Pipeline completo** com 6 stages:

1. 🏗️ **Build & Test** - Compila e testa aplicação
2. 📊 **SonarCloud** - Análise de qualidade
3. 🔒 **Security Scan** - Vulnerabilidades (Trivy)
4. 🐳 **Docker Build** - Cria imagem
5. 🚀 **Docker Push** - Publica no DockerHub (só em main)
6. 📋 **Summary** - Resumo do pipeline

**Triggers**:
- Push em `main`/`master`
- Pull Requests
- Manual (workflow_dispatch)

**Inputs manuais**:
- `skip-tests`: Pular testes
- `skip-docker`: Pular Docker build

## 🔒 Secrets Necessários

Configure em: **Repository → Settings → Secrets → Actions**

| Secret | Descrição | Como obter |
|--------|-----------|------------|
| `SONAR_TOKEN` | Token do SonarCloud | [sonarcloud.io](https://sonarcloud.io) → My Account → Security |
| `DOCKERHUB_USERNAME` | Username DockerHub | Seu username |
| `DOCKERHUB_TOKEN` | Access token DockerHub | [hub.docker.com](https://hub.docker.com) → Settings → Security |

## 📊 Badges para README

Adicione ao README.md do seu projeto:

```markdown
![CI/CD](https://github.com/USERNAME/REPO/actions/workflows/main.yml/badge.svg)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=ORG_REPO&metric=alert_status)](https://sonarcloud.io/dashboard?id=ORG_REPO)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=ORG_REPO&metric=coverage)](https://sonarcloud.io/dashboard?id=ORG_REPO)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ORG_REPO&metric=security_rating)](https://sonarcloud.io/dashboard?id=ORG_REPO)
```

Substitua:
- `USERNAME` → Seu username GitHub
- `REPO` → Nome do repositório
- `ORG_REPO` → `ORG_REPO` do SonarCloud

## 🐳 Docker

### Build local

```bash
docker build -t my-app:test .
docker run -p 8080:8080 my-app:test
```

### Pull da imagem

```bash
docker pull USERNAME/REPO:latest
docker run -p 8080:8080 USERNAME/REPO:latest
```

### Tags disponíveis

- `latest` - Última versão em main
- `v1.0.0` - Versão do pom.xml
- `main-abc123` - Commit SHA

## 📚 Documentação Completa

Para informações detalhadas, veja:

📖 **[docs/ci-cd-configuration.md](./ci-cd-configuration.md)**

Inclui:
- Configuração passo a passo
- Troubleshooting
- Exemplos avançados
- FAQ

## 🛠️ Troubleshooting Rápido

### Pipeline falhou?

1. **Build falhou**: Veja logs em Actions → Run → build-and-test
2. **SonarCloud**: Verifique `SONAR_TOKEN` configurado
3. **Docker push**: Verifique `DOCKERHUB_USERNAME` e `DOCKERHUB_TOKEN`
4. **Tests failed**: Rode localmente: `mvn test`

### Testar localmente

```bash
# Instalar act (GitHub Actions local)
brew install act

# Rodar workflow
act -j build-and-test

# Com secrets
act -j sonar-analysis --secret-file .secrets
```

## 📞 Suporte

- 📖 Documentação: [docs/ci-cd-configuration.md](./ci-cd-configuration.md)
- 🐛 Issues: [GitHub Issues](../../issues)
- 💬 Discussões: [GitHub Discussions](../../discussions)

---

## 🏆 Features

- ✅ **Zero configuração**: Copie e use
- ✅ **Reutilizável**: Um workflow, N projetos
- ✅ **Seguro**: Secrets management, vulnerability scanning
- ✅ **Rápido**: Build < 10 min com cache
- ✅ **Completo**: Build → Test → Quality → Security → Deploy

## 📈 Métricas

Pipeline típico:
- ⏱️ Build + Test: ~3-5 min
- 📊 SonarCloud: ~1-2 min
- 🔒 Security: ~1 min
- 🐳 Docker: ~2-3 min
- **Total**: ~8-12 min

Com cache:
- ⏱️ Build: ~1-2 min
- **Total**: ~4-6 min ⚡

## 🎯 Casos de Uso

### Para novos projetos

```bash
# Setup completo em 10 minutos
1. Copiar workflows ✅
2. Configurar secrets ✅
3. Push ✅
4. Pipeline rodando ✅
```

### Para projetos existentes

```bash
# Migração gradual
1. Adicionar java-reusable.yml
2. Testar build
3. Adicionar main.yml
4. Configurar SonarCloud
5. Configurar DockerHub
```

### Para múltiplos projetos

```bash
# Centralizar workflows
1. Fork este repo
2. Customize workflows
3. Use como template em todos projetos
4. Update uma vez, todos projetos se beneficiam
```

## 🔄 Atualizações

### Como atualizar workflows em projeto existente

```bash
# Backup atual
cp .github/workflows/main.yml .github/workflows/main.yml.bak

# Copiar nova versão
cp PATH/TO/TEMPLATE/.github/workflows/main.yml .github/workflows/

# Verificar diff
git diff .github/workflows/main.yml

# Commit
git add .github/workflows/
git commit -m "ci: update workflows to v1.1"
```

## 🤝 Contribuindo

Melhorias são bem-vindas!

1. Fork o repo
2. Crie branch: `git checkout -b feature/melhoria`
3. Commit: `git commit -m 'feat: adiciona feature X'`
4. Push: `git push origin feature/melhoria`
5. Abra Pull Request

---

**Versão**: 1.0.0  
**Última atualização**: 24/10/2025  
**Licença**: MIT  

🚀 **Happy Deploying!**

