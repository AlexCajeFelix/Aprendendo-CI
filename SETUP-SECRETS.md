# 🔐 Configuração de Secrets do GitHub

## ⚠️ **PROBLEMAS IDENTIFICADOS**

### 1. **DockerHub Authentication Error (401 Unauthorized)**
```
ERROR: failed to push ***/aprendendo-ci:latest: failed to authorize: 
failed to fetch oauth token: unexpected status from GET request to 
https://auth.docker.io/token?scope=repository%3A***%2Faprendendo-ci%3Apull%2Cpush&service=registry.docker.io: 
401 Unauthorized: access token has insufficient scopes
```

### 2. **SONAR_TOKEN não configurado**
```
Context access might be invalid: SONAR_TOKEN
```

## 🔧 **SOLUÇÕES NECESSÁRIAS**

### **Passo 1: Configurar DockerHub Secrets**

1. **Acesse o DockerHub:**
   - Vá para [hub.docker.com](https://hub.docker.com)
   - Faça login na sua conta

2. **Criar Access Token:**
   - Vá para **Account Settings** → **Security** → **New Access Token**
   - Nome: `github-actions-aprendendo-ci`
   - Permissões: **Read, Write, Delete**
   - Copie o token gerado

3. **Configurar no GitHub:**
   - Vá para o repositório: `AlexCajeFelix/Aprendendo-CI`
   - **Settings** → **Secrets and variables** → **Actions**
   - Adicione os seguintes secrets:

   ```
   DOCKERHUB_USERNAME = seu_usuario_dockerhub
   DOCKERHUB_TOKEN = token_gerado_no_passo_anterior
   ```

### **Passo 2: Configurar SonarCloud Token**

1. **Acesse o SonarCloud:**
   - Vá para [sonarcloud.io](https://sonarcloud.io)
   - Faça login com sua conta GitHub

2. **Criar Token:**
   - Vá para **My Account** → **Security** → **Generate Tokens**
   - Nome: `github-actions-aprendendo-ci`
   - Tipo: **Global Analysis Token**
   - Copie o token gerado

3. **Configurar no GitHub:**
   - No mesmo local dos secrets anteriores
   - Adicione:

   ```
   SONAR_TOKEN = token_gerado_no_sonarcloud
   ```

### **Passo 3: Verificar Configuração do Projeto SonarCloud**

1. **Criar projeto no SonarCloud:**
   - Vá para [sonarcloud.io](https://sonarcloud.io)
   - **+** → **Analyze new project**
   - **Import an organization from GitHub**
   - Selecione `AlexCajeFelix/Aprendendo-CI`

2. **Configurar sonar-project.properties:**
   - O arquivo já existe no projeto
   - Verificar se o `sonar.projectKey` está correto

## 📋 **CHECKLIST DE CONFIGURAÇÃO**

- [ ] DockerHub username configurado
- [ ] DockerHub token configurado (com permissões Read/Write/Delete)
- [ ] SonarCloud token configurado
- [ ] Projeto criado no SonarCloud
- [ ] Secrets adicionados no GitHub

## 🚀 **APÓS CONFIGURAR**

1. **Fazer commit das alterações:**
   ```bash
   git add .
   git commit -m "📝 Add setup instructions for GitHub secrets"
   git push origin main
   ```

2. **Executar o pipeline:**
   - Vá para **Actions** no GitHub
   - Execute o workflow manualmente ou faça um novo push

## 🔍 **VERIFICAÇÃO**

Após configurar os secrets, o pipeline deve:
- ✅ Build e testes passarem
- ✅ SonarCloud analysis funcionar
- ✅ Security scan executar
- ✅ Docker build e push funcionar
- ✅ Deploy ser bem-sucedido

## 📞 **SUPORTE**

Se ainda houver problemas:
1. Verifique os logs do GitHub Actions
2. Confirme se todos os secrets estão configurados
3. Verifique as permissões dos tokens
4. Consulte a documentação do SonarCloud e DockerHub
