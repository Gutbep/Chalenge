@echo off
echo ========================================
echo Configuracao Final do Repositorio GitHub
echo ========================================
echo.

echo 📋 INSTRUCOES PARA CRIAR REPOSITORIO NO GITHUB:
echo.
echo 1. Vá para https://github.com/new
echo 2. Preencha os dados:
echo    • Repository name: Challenge-Fiap
echo    • Description: Anti-Ransomware Shield - Ferramenta de protecao contra ransomware
echo    • Visibility: Public (ou Private se preferir)
echo    • NÃO marque 'Add a README file' (ja temos)
echo    • NÃO marque 'Add .gitignore' (ja temos)
echo    • NÃO marque 'Choose a license' (ja temos)
echo 3. Clique em 'Create repository'
echo 4. Copie a URL do repositorio criado
echo.

set /p REPO_URL="Digite a URL do seu repositorio GitHub: "

if "%REPO_URL%"=="" (
    echo ❌ URL nao fornecida. Abortando...
    pause
    exit /b 1
)

echo.
echo 🔗 Configurando remote origin...
git remote add origin %REPO_URL%
if %errorLevel% neq 0 (
    echo ❌ Erro ao configurar remote!
    pause
    exit /b 1
)

echo ✅ Remote configurado!
echo.

echo 📤 Fazendo push para o GitHub...
git push -u origin main
if %errorLevel% neq 0 (
    echo ❌ Erro no push da branch main!
    pause
    exit /b 1
)

echo ✅ Push da branch main realizado!
echo.

echo 🌿 Criando branch develop...
git checkout -b develop
if %errorLevel% neq 0 (
    echo ❌ Erro ao criar branch develop!
    pause
    exit /b 1
)

git push -u origin develop
if %errorLevel% neq 0 (
    echo ❌ Erro no push da branch develop!
    pause
    exit /b 1
)

echo ✅ Branch develop criada e enviada!
echo.

echo 🔄 Voltando para branch main...
git checkout main
if %errorLevel% neq 0 (
    echo ❌ Erro ao voltar para main!
    pause
    exit /b 1
)

echo ✅ Voltou para branch main
echo.

echo ========================================
echo 🎉 REPOSITORIO GITHUB CONFIGURADO COM SUCESSO!
echo ========================================
echo.
echo 📁 Repositorio: %REPO_URL%
echo 🌿 Branches: main, develop
echo 📤 Push realizado com sucesso!
echo.
echo 🧙‍♂️ Destaque para o Instalador Wizard:
echo    • Interface grafica moderna
echo    • 5 etapas guiadas
echo    • Validacao automatica
echo    • Configuracao flexivel
echo    • Experiencia profissional
echo.
echo 📚 Documentacao incluida:
echo    • README.md - Visao geral completa
echo    • docs/INSTALLATION.md - Guia de instalacao
echo    • docs/USER_GUIDE.md - Manual do usuario
echo    • docs/TROUBLESHOOTING.md - Solucao de problemas
echo    • WIZARD_INSTALLER_GUIDE.md - Guia do instalador wizard
echo.
echo 🛡️ Funcionalidades do Anti-Ransomware Shield:
echo    • Monitoramento em tempo real
echo    • Deteccao inteligente de ameacas
echo    • Protecao automatica contra ransomware
echo    • Interface grafica profissional
echo    • Instalador wizard destacado
echo    • Suporte a multiplas familias de ransomware
echo.
pause
