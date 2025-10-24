# ✅ Checklist Antes do Commit

## 🔐 1. Configurar Secrets no GitHub (PRIMEIRO!)

**⚠️ FAÇA ISSO ANTES DE FAZER PUSH!**

Vá para: **GitHub → Seu Repositório → Settings → Secrets and variables → Actions**

Adicione 3 secrets clicando em **"New repository secret"**:

### Secret 1: SONAR_TOKEN
```
Name: SONAR_TOKEN
Value: [SEU_TOKEN_SONARCLOUD_AQUI]
```

### Secret 2: DOCKERHUB_USERNAME
```
Name: DOCKERHUB_USERNAME
Value: [SEU_USERNAME_DOCKERHUB_AQUI]
```

### Secret 3: DOCKERHUB_TOKEN
```
Name: DOCKERHUB_TOKEN
Value: [SEU_TOKEN_DOCKERHUB_AQUI]
```

**✅ Validar**: Você deve ver os 3 secrets listados

---

## 📦 2. Arquivos Prontos para Commit

Verifique que você tem estes arquivos:

### Workflows (Obrigatórios)
- [ ] `.github/workflows/java-reusable.yml` ✅
- [ ] `.github/workflows/main.yml` ✅

### Templates (Obrigatórios)
- [ ] `Dockerfile.template` ✅
- [ ] `sonar-project.properties.template` ✅

### Documentação
- [ ] `README.md` ✅
- [ ] `QUICKSTART.md` ✅
- [ ] `docs/ci-cd-configuration.md` ✅
- [ ] `docs/workflows-README.md` ✅

### Configuração
- [ ] `.gitignore` (atualizado) ✅

### BMAD Outputs
- [ ] `PRPs/bmad-output/briefs/` ✅
- [ ] `PRPs/bmad-output/prds/` ✅
- [ ] `PRPs/bmad-output/architecture/` ✅
- [ ] `PRPs/bmad-output/stories/` ✅
- [ ] `PRPs/bmad-output/WORKFLOW-SUMMARY.md` ✅

---

## 🚀 3. Fazer Commit e Push

```bash
# Navegue até o diretório do projeto
cd "/home/alexfelix/Área de trabalho/Projeto-prp-live"

# Ver status dos arquivos
git status

# Adicionar todos os arquivos novos/modificados
git add .github/
git add Dockerfile.template
git add sonar-project.properties.template
git add docs/
git add PRPs/
git add README.md
git add QUICKSTART.md
git add .gitignore

# NÃO adicionar arquivo de secrets!
# SECRETS-SETUP.md já está no .gitignore

# Ver o que será commitado
git status

# Commit com mensagem descritiva
git commit -m "ci: add complete CI/CD system with SonarCloud and DockerHub

- Add java-reusable workflow with Java 21 support
- Add main pipeline with 6 stages (build, sonar, security, docker)
- Add SonarCloud integration with quality gates
- Add DockerHub integration with multi-stage build
- Add comprehensive documentation (QUICKSTART, guides)
- Add BMAD methodology outputs (Brief, PRD, Architecture, Stories)
- Update .gitignore for Java projects

Features:
✅ Automated build & test
✅ Code quality analysis (SonarCloud)
✅ Security scanning (Trivy)
✅ Docker image optimization (multi-stage)
✅ Automatic deployment to DockerHub
✅ Complete documentation

This CI/CD system reduces setup time from 4 hours to 10 minutes.
"

# Push para GitHub
git push origin main
```

---

## 👀 4. Acompanhar Pipeline

Após o push:

1. **Abra GitHub** → Seu repositório
2. Vá em **Actions** (topo da página)
3. Você verá **"Main CI/CD Pipeline"** rodando
4. Clique nele para ver logs em tempo real

### O que esperar:

**Stages**:
1. 🏗️ **Build & Test** (3-5 min)
   - Compila código
   - Roda testes
   - Gera coverage

2. 📊 **SonarCloud Analysis** (1-2 min)
   - Analisa qualidade
   - Verifica quality gate
   - Gera métricas

3. 🔒 **Security Scan** (1 min)
   - Escaneia vulnerabilidades
   - Reporta issues críticos

4. 🐳 **Docker Build** (2-3 min)
   - Build multi-stage
   - Otimiza imagem
   - Cache de layers

5. 🚀 **Docker Push** (1 min)
   - Push para DockerHub
   - Tags: latest, main-{sha}

6. 📋 **Summary**
   - Relatório completo
   - Links úteis

**Duração total**: ~8-12 minutos (primeira vez)

---

## ✅ 5. Validar Resultados

Após pipeline completar com sucesso:

### GitHub Actions ✅
- [ ] Pipeline passou (check verde)
- [ ] Summary gerado
- [ ] Artifacts disponíveis

### SonarCloud ✅
- [ ] Acesse: https://sonarcloud.io
- [ ] Veja seu projeto
- [ ] Quality Gate status

### DockerHub ✅
- [ ] Acesse: https://hub.docker.com/u/alexcaje
- [ ] Veja imagem publicada
- [ ] Verifique tags: `latest`, `main-{sha}`

---

## 🧪 6. Testar Imagem Docker

```bash
# Pull da imagem publicada
docker pull alexcaje/projeto-prp-live:latest

# Rodar container (ajuste porta conforme sua app)
docker run -p 8080:8080 alexcaje/projeto-prp-live:latest

# Verificar que está rodando
docker ps
```

---

## 📊 7. Adicionar Badges ao README

Após primeira execução, adicione badges ao seu README.md:

```markdown
![CI/CD Pipeline](https://github.com/SEU_USERNAME/Projeto-prp-live/actions/workflows/main.yml/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=SEU_ORG_projeto-prp-live&metric=alert_status)](https://sonarcloud.io/dashboard?id=SEU_ORG_projeto-prp-live)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=SEU_ORG_projeto-prp-live&metric=coverage)](https://sonarcloud.io/dashboard?id=SEU_ORG_projeto-prp-live)
```

---

## 🎉 8. Pronto!

Seu CI/CD está completo e funcionando! 🚀

### O que você tem agora:

✅ Pipeline automático em cada push  
✅ Qualidade de código garantida  
✅ Segurança verificada  
✅ Deploy automático  
✅ Documentação completa  

### Próximos passos:

1. **Testar com PR**: Crie uma branch e pull request
2. **Ver análise**: Acesse SonarCloud dashboard
3. **Usar imagem**: Deploy sua aplicação com Docker
4. **Customizar**: Ajuste workflows conforme necessidade

---

## 🛠️ Troubleshooting Rápido

### Pipeline falhou?

**Build failed**:
```bash
mvn clean install
# Corrigir erros localmente primeiro
```

**SonarCloud failed**:
- Verificar SONAR_TOKEN configurado
- Ver logs no job sonar-analysis

**Docker push failed**:
- Verificar DOCKERHUB_USERNAME e DOCKERHUB_TOKEN
- Verificar repositório existe no DockerHub

**Documentação completa**: Ver `docs/ci-cd-configuration.md`

---

## 📞 Precisa de Ajuda?

- 📖 [QUICKSTART.md](QUICKSTART.md) - Guia de 10 minutos
- 📖 [docs/ci-cd-configuration.md](docs/ci-cd-configuration.md) - Guia completo
- 📖 [SECRETS-SETUP.md](SECRETS-SETUP.md) - Configuração de secrets
- 🐛 GitHub Issues - Reportar problemas
- 💬 GitHub Discussions - Perguntas e dúvidas

---

## ⚠️ IMPORTANTE

### Segurança:
- ✅ Secrets configurados no GitHub (seguros)
- ❌ Nunca commite `SECRETS-SETUP.md`
- ❌ Nunca commite tokens/passwords no código

### Arquivos que NÃO devem ser commitados:
- `SECRETS-SETUP.md` (já no .gitignore)
- Qualquer arquivo com extensão `.secret` ou `.token`

---

<div align="center">

# 🎉 Tudo Pronto para o Push! 🎉

**Siga os passos acima e seu CI/CD estará rodando em minutos!**

**⏱️ Tempo total**: ~15 minutos  
**💰 Investimento**: Zero (tudo gratuito)  
**📈 Benefício**: Para sempre

</div>

