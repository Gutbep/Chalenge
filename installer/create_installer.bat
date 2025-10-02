@echo off
echo ========================================
echo Anti-Ransomware Shield - Criador de Instalador
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

echo Instalando dependencias...
pip install -r requirements.txt

echo.
echo Criando executavel...
python installer/setup.py

echo.
echo ========================================
echo Instalador criado com sucesso!
echo ========================================
echo.
echo Arquivos criados:
echo - dist/installer/AntiRansomwareShield.exe
echo - dist/installer/install.bat
echo - dist/installer/uninstall.bat
echo - dist/installer/README.txt
echo.
echo Para distribuir:
echo 1. Copie a pasta dist/installer/ para o computador de destino
echo 2. Execute install.bat como administrador
echo.
pause
