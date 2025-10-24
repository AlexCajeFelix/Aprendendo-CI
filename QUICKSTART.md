# ⚡ Quick Start - CI/CD Reutilizável

> Configure CI/CD completo em seu projeto Java em **menos de 10 minutos**!

## 🎯 O que você vai ter

Após seguir este guia, seu projeto terá:

✅ **Build e testes automáticos** a cada push  
✅ **Análise de qualidade** com SonarCloud  
✅ **Scan de segurança** com Trivy  
✅ **Docker build automático**  
✅ **Deploy para DockerHub** em cada merge para main  

---

## 📋 Pré-requisitos (5 min)

### 1. Projeto Java/Maven

Seu projeto precisa ter:
- `pom.xml` na raiz
- Estrutura padrão Maven (`src/main/java`, `src/test/java`)
- Java 11, 17 ou 21

### 2. Contas (Gratuitas)

- ✅ **GitHub** (você já tem)
- 🔹 **SonarCloud** → [sonarcloud.io](https://sonarcloud.io) (login com GitHub)
- 🔹 **DockerHub** → [hub.docker.com](https://hub.docker.com) (criar conta)

---

## 🚀 Passo a Passo

### Passo 1: Copiar Workflows (1 min)

```bash
# Entre no diretório do seu projeto
cd /path/to/seu-projeto

# Crie pasta de workflows
mkdir -p .github/workflows

# Copie os workflows deste repositório
cp /path/to/Projeto-prp-live/.github/workflows/java-reusable.yml .github/workflows/
cp /path/to/Projeto-prp-live/.github/workflows/main.yml .github/workflows/

# Copie templates
cp /path/to/Projeto-prp-live/Dockerfile.template Dockerfile
cp /path/to/Projeto-prp-live/sonar-project.properties.template sonar-project.properties
```

### Passo 2: Configurar SonarCloud (2 min)

#### 2.1. Criar projeto no SonarCloud

1. Acesse [sonarcloud.io](https://sonarcloud.io)
2. Login com GitHub
3. Clique **"+"** → **"Analyze new project"**
4. Selecione seu repositório
5. Escolha **"With GitHub Actions"**

#### 2.2. Obter token

1. Vá em: **My Account** → **Security** → **Generate Token**
2. Nome: `GitHub Actions`
3. Type: `User Token`
4. **Copie o token** (você vai usar no Passo 3)

#### 2.3. Editar sonar-project.properties

```bash
# Abra o arquivo
nano sonar-project.properties
```

Substitua os valores:

```properties
# Antes
sonar.projectKey={{GITHUB_ORG}}_{{REPO_NAME}}
sonar.organization={{GITHUB_ORG}}
sonar.projectName={{PROJECT_NAME}}

# Depois (exemplo)
sonar.projectKey=meuuser_meu-app
sonar.organization=meuuser
sonar.projectName=Meu App Spring Boot
```

**Como descobrir valores:**
- `GITHUB_ORG`: Seu username GitHub (ex: `octocat`)
- `REPO_NAME`: Nome do repositório (ex: `my-spring-app`)
- `PROJECT_NAME`: Nome legível (ex: `My Spring App`)

### Passo 3: Configurar DockerHub (2 min)

#### 3.1. Criar repositório

1. Login em [hub.docker.com](https://hub.docker.com)
2. Clique **"Create Repository"**
3. Nome: mesmo nome do seu projeto (ex: `my-spring-app`)
4. Visibilidade: Public ou Private
5. Criar

#### 3.2. Gerar Access Token

1. DockerHub → **Account Settings** → **Security**
2. Clique **"New Access Token"**
3. Description: `GitHub Actions`
4. Permissions: **Read & Write**
5. **Copie o token** (aparece uma vez só!)

### Passo 4: Configurar Secrets no GitHub (2 min)

1. Vá para seu repositório no GitHub
2. Clique **Settings** → **Secrets and variables** → **Actions**
3. Clique **"New repository secret"** 3 vezes:

#### Secret 1: SONAR_TOKEN
```
Name: SONAR_TOKEN
Secret: [cole o token do SonarCloud do Passo 2.2]
```

#### Secret 2: DOCKERHUB_USERNAME
```
Name: DOCKERHUB_USERNAME
Secret: [seu username do DockerHub]
```

#### Secret 3: DOCKERHUB_TOKEN
```
Name: DOCKERHUB_TOKEN
Secret: [cole o token do DockerHub do Passo 3.2]
```

### Passo 5: Customizar Dockerfile (1 min)

Abra `Dockerfile` e ajuste se necessário:

```dockerfile
# Se seu app não usa Spring Actuator, ajuste health check:
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8080/api/health || exit 1

# Ou remova a linha HEALTHCHECK completamente se não tiver endpoint de health
```

### Passo 6: Commit e Push (1 min)

```bash
# Adicionar arquivos
git add .github/workflows/ Dockerfile sonar-project.properties

# Commit
git commit -m "ci: add CI/CD workflows with SonarCloud and DockerHub"

# Push
git push origin main
```

### Passo 7: Verificar Pipeline (1 min) 🎉

1. Vá para **Actions** no GitHub
2. Você verá o workflow **"Main CI/CD Pipeline"** rodando
3. Clique nele para ver os logs

**Pipeline vai executar:**
- 🏗️ Build & Test (~3-5 min)
- 📊 SonarCloud Analysis (~1-2 min)
- 🔒 Security Scan (~1 min)
- 🐳 Docker Build (~2-3 min)
- 🚀 Docker Push (~1 min, só em main)

**Total**: ~8-12 minutos na primeira vez, ~4-6 min depois (com cache) ⚡

---

## ✅ Checklist de Validação

Após o pipeline rodar, verifique:

- [ ] ✅ Build passou (check verde em Actions)
- [ ] 📊 SonarCloud tem análise do projeto
- [ ] 🐳 Imagem Docker aparece no DockerHub
- [ ] 🏷️ Tags criadas: `latest`, `main-{sha}`

---

## 🎨 Adicionar Badges ao README (Opcional)

Adicione ao `README.md` do seu projeto:

```markdown
![CI/CD](https://github.com/USERNAME/REPO/actions/workflows/main.yml/badge.svg)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=ORG_REPO&metric=alert_status)](https://sonarcloud.io/dashboard?id=ORG_REPO)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=ORG_REPO&metric=coverage)](https://sonarcloud.io/dashboard?id=ORG_REPO)
```

**Substitua**:
- `USERNAME` → Seu username GitHub
- `REPO` → Nome do repositório
- `ORG_REPO` → `organization_reponame` do SonarCloud

---

## 🧪 Testar Localmente (Opcional)

### Testar Build

```bash
# Build local
mvn clean install

# Rodar testes
mvn test
```

### Testar Docker

```bash
# Build imagem
docker build -t my-app:test .

# Rodar container
docker run -p 8080:8080 my-app:test

# Testar
curl http://localhost:8080/actuator/health
```

### Testar Workflow com act

```bash
# Instalar act
brew install act  # macOS
# ou
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Rodar workflow localmente
act -j build-and-test
```

---

## 🛠️ Troubleshooting

### ❌ "SONAR_TOKEN not configured"

**Problema**: Secret não configurado ou nome errado

**Solução**:
1. Verifique: Settings → Secrets → SONAR_TOKEN existe?
2. Nome deve ser exatamente `SONAR_TOKEN` (maiúsculas)
3. Refaça Passo 4

### ❌ "Authentication required" (DockerHub)

**Problema**: Credentials inválidas

**Solução**:
1. Verifique DOCKERHUB_USERNAME (lowercase, sem espaços)
2. Re-gere token no DockerHub
3. Atualiza secret DOCKERHUB_TOKEN

### ❌ "Build failed"

**Problema**: Código não compila

**Solução**:
```bash
# Testar localmente
mvn clean install

# Ver erros detalhados
mvn clean install -X
```

### ❌ "Quality Gate failed"

**Problema**: Código não atinge padrões SonarCloud

**Solução**:
1. Ver relatório: SonarCloud → Dashboard
2. Corrigir bugs/vulnerabilidades críticas
3. Melhorar coverage (> 80%)

---

## 📚 Próximos Passos

### Documentação Completa

Para informações detalhadas:
- 📖 [Guia Completo de Configuração](docs/ci-cd-configuration.md) (40+ páginas)
- 📖 [Guia de Workflows](docs/workflows-README.md)
- 📖 [Arquitetura](PRPs/bmad-output/architecture/ci-cd-system-architecture.md)

### Customizações

- 🔧 [Mudar versão do Java](docs/ci-cd-configuration.md#customizações-comuns)
- 🔧 [Adicionar Gradle](docs/ci-cd-configuration.md#exemplo-gradle)
- 🔧 [Notificações Slack](docs/ci-cd-configuration.md#exemplo-4-notificações-slack)
- 🔧 [Matrix builds](docs/ci-cd-configuration.md#exemplo-2-matrix-build)

### Suporte

- 🐛 Issues: [GitHub Issues](../../issues)
- 💬 Discussões: [GitHub Discussions](../../discussions)
- 📧 Email: devops@exemplo.com

---

## 🎉 Pronto!

Seu projeto agora tem **CI/CD completo e profissional**! 🚀

A cada push:
- ✅ Build automático
- ✅ Testes executados
- ✅ Qualidade analisada
- ✅ Segurança verificada
- ✅ Docker image criada
- ✅ Deploy automático (em main)

---

## 📊 O que fazer agora?

### 1. Fazer uma mudança de teste

```bash
# Edite qualquer arquivo
echo "// test" >> src/main/java/Main.java

# Commit e push
git add .
git commit -m "test: trigger CI/CD"
git push origin main

# Veja pipeline rodar em Actions
```

### 2. Criar uma Pull Request

```bash
# Criar branch
git checkout -b feature/minha-feature

# Fazer mudanças
# ...

# Push
git push origin feature/minha-feature

# Abrir PR no GitHub
# Pipeline vai rodar automaticamente!
```

### 3. Ver análise de qualidade

1. Acesse SonarCloud dashboard
2. Ver métricas: coverage, bugs, vulnerabilities
3. Ver tendências ao longo do tempo

### 4. Usar imagem Docker

```bash
# Pull da imagem
docker pull SEU_USERNAME/SEU_REPO:latest

# Rodar
docker run -p 8080:8080 SEU_USERNAME/SEU_REPO:latest
```

---

<div align="center">

# 🎉 Parabéns! 🎉

**Seu CI/CD está pronto e rodando!**

**Tempo total de setup**: ~10 minutos ⚡  
**ROI**: Positivo em < 1 mês 📈  
**Benefício**: Pipelines automáticos para sempre ♾️  

---

**⭐ Se este guia ajudou, considere dar uma estrela no repositório! ⭐**

**🤝 Desenvolvido com metodologia BMAD**

</div>

