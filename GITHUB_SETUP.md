# Comandos para configurar repositório GitHub

# 1. Inicializar repositório local
git init
git add .
git commit -m "feat: initial commit - Anti-Ransomware Shield"

# 2. Criar repositório no GitHub
# Vá para https://github.com/new
# Nome: Challenge-Fiap
# Descrição: Anti-Ransomware Shield - Ferramenta de proteção contra ransomware
# Público/Privado: Escolha conforme necessário

# 3. Conectar repositório local ao GitHub
git remote add origin https://github.com/[SEU_USUARIO]/Challenge-Fiap.git
git branch -M main
git push -u origin main

# 4. Configurar branch de desenvolvimento
git checkout -b develop
git push -u origin develop

# 5. Criar tags para releases
git tag -a v1.0.0 -m "Release v1.0.0 - Anti-Ransomware Shield"
git push origin v1.0.0

# 6. Configurar GitHub Pages (opcional)
# Vá para Settings > Pages
# Source: Deploy from a branch
# Branch: main
# Folder: / (root)

# 7. Configurar proteção de branches
# Vá para Settings > Branches
# Adicione regra para branch main
# Require pull request reviews before merging
# Require status checks to pass before merging

# 8. Configurar secrets para CI/CD (se necessário)
# Vá para Settings > Secrets and variables > Actions
# Adicione secrets necessários
