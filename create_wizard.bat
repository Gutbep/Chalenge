@echo off
echo ========================================
echo Anti-Ransomware Shield - Criador de Instalador Wizard
echo ========================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo ERRO: Python nao encontrado!
    echo Instale Python 3.8+ e tente novamente.
    pause
    exit /b 1
)

echo Python encontrado!
echo.

REM Instala dependências
echo Instalando dependencias...
pip install -r requirements.txt
if %errorLevel% neq 0 (
    echo ERRO: Falha ao instalar dependencias!
    pause
    exit /b 1
)

echo.
echo Dependencias instaladas com sucesso!
echo.

REM Cria instalador wizard
echo Criando instalador wizard...
python create_wizard_installer.py
if %errorLevel% neq 0 (
    echo ERRO: Falha ao criar instalador wizard!
    pause
    exit /b 1
)

echo.
echo ========================================
echo INSTALADOR WIZARD CRIADO COM SUCESSO!
echo ========================================
echo.
echo Arquivos criados:
echo - dist/AntiRansomwareShield_Installer.exe
echo - dist/installer_wizard/ (pacote completo)
echo.
echo Para distribuir:
echo 1. Copie a pasta dist/installer_wizard/ para o computador de destino
echo 2. Execute AntiRansomwareShield_Installer.exe
echo 3. Siga as instrucoes do wizard
echo.
pause
