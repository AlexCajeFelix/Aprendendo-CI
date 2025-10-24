# 🚀 Projeto PRP Live - Sistema CI/CD Reutilizável

[![CI/CD Pipeline](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Java](https://img.shields.io/badge/Java-17%2B-007396?logo=openjdk&logoColor=white)](https://openjdk.org/)
[![Maven](https://img.shields.io/badge/Maven-3.9%2B-C71A36?logo=apache-maven&logoColor=white)](https://maven.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-Multi--Stage-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![SonarCloud](https://img.shields.io/badge/SonarCloud-Quality-orange?logo=sonarcloud&logoColor=white)](https://sonarcloud.io/)

## 📋 Sobre o Projeto

Sistema de **CI/CD reutilizável e pronto para produção** para projetos Java/Spring Boot, desenvolvido usando a metodologia **BMAD (Brief, Milestones, Architecture, Development)**.

### 🎯 Objetivos

- ✅ **Reduzir tempo de setup** de 4 horas para < 10 minutos
- ✅ **Padronizar pipelines** em todos os projetos
- ✅ **Automatizar qualidade** com gates de qualidade
- ✅ **Acelerar deploys** com build otimizado
- ✅ **Garantir segurança** com vulnerability scanning

### 🏆 Features

| Feature | Status | Descrição |
|---------|--------|-----------|
| 🏗️ **Build & Test** | ✅ | Workflow reutilizável para Java/Maven |
| 📊 **SonarCloud** | ✅ | Análise de qualidade e coverage |
| 🔒 **Security Scan** | ✅ | Trivy vulnerability scanner |
| 🐳 **Docker Build** | ✅ | Multi-stage otimizado (< 200MB) |
| 🚀 **Auto Deploy** | ✅ | Push automático para DockerHub |
| 📚 **Documentação** | ✅ | Guia completo de configuração |

---

## 🚀 Quick Start

### Para usar este CI/CD em seu projeto

```bash
# 1. Clone este repositório
git clone https://github.com/SEU_USER/Projeto-prp-live.git
cd Projeto-prp-live

# 2. Copie os workflows para seu projeto
cp -r .github/workflows/* /path/to/seu-projeto/.github/workflows/
cp Dockerfile.template /path/to/seu-projeto/Dockerfile
cp sonar-project.properties.template /path/to/seu-projeto/sonar-project.properties

# 3. Configure secrets no GitHub (veja seção abaixo)

# 4. Customize sonar-project.properties
# Edite e substitua {{PLACEHOLDERS}}

# 5. Commit e push
cd /path/to/seu-projeto
git add .github/ Dockerfile sonar-project.properties
git commit -m "ci: add CI/CD workflows"
git push origin main
```

### Configurar Secrets

No seu repositório GitHub: **Settings → Secrets and variables → Actions**

| Secret | Valor | Como obter |
|--------|-------|------------|
| `SONAR_TOKEN` | Token SonarCloud | [sonarcloud.io](https://sonarcloud.io) → My Account → Security → Generate Token |
| `DOCKERHUB_USERNAME` | Username DockerHub | Seu username |
| `DOCKERHUB_TOKEN` | Access token DockerHub | [hub.docker.com](https://hub.docker.com) → Settings → Security → New Access Token |

---

## 📂 Estrutura do Projeto

```
Projeto-prp-live/
├── .github/
│   └── workflows/
│       ├── java-reusable.yml        # ⭐ Workflow reutilizável Java
│       └── main.yml                 # ⭐ Pipeline completo
│
├── config/
│   ├── agents.json                  # Configuração BMAD Agents
│   ├── mcp-config.json              # MCP configuration
│   └── templates.json               # Templates BMAD
│
├── docs/
│   ├── ci-cd-configuration.md       # 📖 Guia completo de setup
│   ├── workflows-README.md          # 📖 Guia rápido workflows
│   ├── bmad-auto-system.md          # BMAD Auto System
│   ├── bmad-collaborative-mode.md   # BMAD Colaborativo
│   ├── best-practices.md            # Best practices
│   └── setup.md                     # Setup inicial
│
├── PRPs/
│   ├── bmad-output/                 # 📦 Outputs BMAD
│   │   ├── briefs/
│   │   ├── prds/
│   │   ├── architecture/
│   │   └── stories/
│   ├── scripts/                     # 🤖 Scripts BMAD
│   ├── templates/                   # 📄 Templates
│   └── examples/                    # Exemplos
│
├── Dockerfile.template              # ⭐ Dockerfile multi-stage
├── sonar-project.properties.template # ⭐ Config SonarCloud
├── .gitignore                       # Git ignore (Java + Node)
└── README.md                        # Este arquivo
```

---

## 🔧 Workflows Disponíveis

### 1. java-reusable.yml

**Workflow reutilizável** para build e teste de projetos Java/Maven.

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

**Features**:
- ✅ Setup Java (11, 17, 21)
- ✅ Cache de dependências Maven
- ✅ Build otimizado
- ✅ Testes com JUnit
- ✅ Coverage com Jacoco
- ✅ Upload de artifacts

### 2. main.yml

**Pipeline completo** com 6 stages:

```
Push/PR → Build & Test → SonarCloud → Security → Docker Build → Docker Push
```

**Stages**:
1. 🏗️ **Build & Test** - Compila, testa, gera artifacts
2. 📊 **SonarCloud** - Análise de qualidade e coverage
3. 🔒 **Security Scan** - Trivy vulnerability scan
4. 🐳 **Docker Build** - Cria imagem otimizada
5. 🚀 **Docker Push** - Deploy para DockerHub (só em main)
6. 📋 **Summary** - Relatório completo

**Triggers**:
- Push em `main`/`master`
- Pull Requests
- Manual (workflow_dispatch)

---

## 📊 Integração SonarCloud

### Setup

1. Crie projeto em [sonarcloud.io](https://sonarcloud.io)
2. Escolha "With GitHub Actions"
3. Gere token em: My Account → Security
4. Configure secret `SONAR_TOKEN`

### Quality Gates

O pipeline **bloqueia merge** se:
- ❌ Quality Gate = FAILED
- ❌ Vulnerabilidades HIGH/CRITICAL
- ❌ Bugs críticos

O pipeline **avisa** mas não bloqueia se:
- ⚠️ Coverage < 80%
- ⚠️ Code smells acima do threshold

### Badges

Adicione ao README do seu projeto:

```markdown
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=ORG_REPO&metric=alert_status)](https://sonarcloud.io/dashboard?id=ORG_REPO)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=ORG_REPO&metric=coverage)](https://sonarcloud.io/dashboard?id=ORG_REPO)
```

---

## 🐳 Docker

### Dockerfile Multi-Stage

Otimizado para produção:

- **Stage 1 (Builder)**: Maven 3.9 + JDK 17 (~700MB)
- **Stage 2 (Runtime)**: JRE 17 Alpine (~150MB) ✅

**Benefícios**:
- ✅ Imagem final 60% menor
- ✅ Menos superfície de ataque
- ✅ Melhor cache de layers
- ✅ Health check integrado

### Build Local

```bash
# Build
docker build -t my-app:test .

# Run
docker run -p 8080:8080 my-app:test

# Verificar tamanho
docker images my-app:test
```

### Tags no DockerHub

Automaticamente criadas:
- `latest` - Última versão em main
- `v1.0.0` - Versão do pom.xml
- `main-abc123` - Commit SHA

---

## 📚 Documentação

| Documento | Descrição |
|-----------|-----------|
| [ci-cd-configuration.md](docs/ci-cd-configuration.md) | 📖 Guia completo de configuração (40+ páginas) |
| [workflows-README.md](docs/workflows-README.md) | 📖 Guia rápido de workflows |
| [bmad-auto-system.md](docs/bmad-auto-system.md) | 🤖 Sistema BMAD Automático |
| [bmad-collaborative-mode.md](docs/bmad-collaborative-mode.md) | 🤝 Modo Colaborativo BMAD |

---

## 🤖 Sistema BMAD

Este projeto foi desenvolvido usando **BMAD** (Brief, Milestones, Architecture, Development):

### Metodologia

1. **📋 Brief** - Análise de requisitos completa
2. **📊 PRD** - Product Requirements Document
3. **🏗️ Architecture** - Decisões arquiteturais (ADRs)
4. **📝 Stories** - User stories com critérios de aceitação
5. **💻 Development** - Implementação com código real
6. **🧪 QA** - Validação e testes

### Documentos BMAD Gerados

- [Brief](PRPs/bmad-output/briefs/ci-cd-system-brief.md)
- [PRD](PRPs/bmad-output/prds/ci-cd-system-prd.md)
- [Arquitetura](PRPs/bmad-output/architecture/ci-cd-system-architecture.md)
- [Stories](PRPs/bmad-output/stories/ci-cd-system/index.md)

---

## 🛠️ Troubleshooting

### Pipeline falhou?

1. **Build failed**: 
   ```bash
   mvn clean install
   ```

2. **SonarCloud failed**: 
   - Verificar `SONAR_TOKEN` configurado
   - Ver logs em Actions → Run → sonar-analysis

3. **Docker push failed**: 
   - Verificar `DOCKERHUB_USERNAME` e `DOCKERHUB_TOKEN`
   - Confirmar repositório existe no DockerHub

### Testar localmente

```bash
# Instalar act (GitHub Actions local)
brew install act  # macOS
# ou
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Rodar workflow
act -j build-and-test

# Com secrets
echo "SONAR_TOKEN=xxx" > .secrets
act -j sonar-analysis --secret-file .secrets
```

### Validar YAML

```bash
# Instalar actionlint
brew install actionlint

# Validar workflows
actionlint .github/workflows/*.yml
```

---

## 📈 Performance

### Benchmarks

| Métrica | Sem Cache | Com Cache |
|---------|-----------|-----------|
| Build & Test | 4-5 min | 1-2 min ⚡ |
| SonarCloud | 1-2 min | 1-2 min |
| Security Scan | 1 min | 1 min |
| Docker Build | 3-4 min | 1-2 min ⚡ |
| **Total** | **9-12 min** | **4-7 min** ⚡ |

### Otimizações Aplicadas

- ✅ Maven dependency cache
- ✅ Docker layer caching (GitHub Cache)
- ✅ Parallel jobs quando possível
- ✅ Conditional steps (skip quando não necessário)

---

## 🤝 Contribuindo

Contribuições são bem-vindas!

1. Fork o projeto
2. Crie uma branch: `git checkout -b feature/minha-feature`
3. Commit: `git commit -m 'feat: adiciona minha feature'`
4. Push: `git push origin feature/minha-feature`
5. Abra um Pull Request

### Padrão de Commits

Seguimos [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: nova feature
fix: correção de bug
docs: atualização de documentação
ci: mudanças em CI/CD
refactor: refatoração de código
test: adição de testes
```

---

## 📞 Suporte

- 📖 **Documentação**: [docs/](docs/)
- 🐛 **Issues**: [GitHub Issues](../../issues)
- 💬 **Discussões**: [GitHub Discussions](../../discussions)
- 📧 **Email**: devops@exemplo.com

---

## 📊 Status do Projeto

| Fase | Status | Conclusão |
|------|--------|-----------|
| 📋 Brief | ✅ Completo | 100% |
| 📊 PRD | ✅ Completo | 100% |
| 🏗️ Arquitetura | ✅ Completo | 100% |
| 📝 Stories | ✅ Completo | 100% |
| 💻 Implementação | ✅ Completo | 100% |
| 📚 Documentação | ✅ Completo | 100% |
| 🧪 Testes | ⏳ Em andamento | 80% |

---

## 📜 Licença

Este projeto está sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.

---

## 🎯 Roadmap

### ✅ Fase 1: MVP (Completo)
- Workflow Java reutilizável
- Pipeline completo
- SonarCloud integration
- DockerHub integration
- Documentação completa

### 🔄 Fase 2: Melhorias (Em planejamento)
- [ ] Suporte a Gradle
- [ ] Matrix builds (múltiplas versões Java)
- [ ] Notificações Slack/Discord
- [ ] Caching remoto avançado

### 🔮 Fase 3: Enterprise (Futuro)
- [ ] Deploy para Kubernetes
- [ ] Multi-cloud support
- [ ] Advanced security scanning
- [ ] Performance monitoring

---

## 🏆 Agradecimentos

Desenvolvido com a metodologia **BMAD** usando:
- ✅ GitHub Actions
- ✅ SonarCloud
- ✅ DockerHub
- ✅ Trivy Security Scanner
- ✅ Maven
- ✅ Spring Boot (exemplos)

---

## 📌 Links Úteis

- 📖 [GitHub Actions Docs](https://docs.github.com/en/actions)
- 📊 [SonarCloud Docs](https://docs.sonarcloud.io/)
- 🐳 [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- ☕ [Maven Docs](https://maven.apache.org/guides/)
- 🔒 [Trivy Security Scanner](https://aquasecurity.github.io/trivy/)

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela! ⭐**

**Feito com ❤️ usando metodologia BMAD**

**Versão**: 1.0.0 | **Última atualização**: 24/10/2025

</div>

