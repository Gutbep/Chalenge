@echo off
echo ========================================
echo Anti-Ransomware Shield - Executor
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

REM Instala dependências se necessário
if not exist "venv" (
    echo Criando ambiente virtual...
    python -m venv venv
)

echo Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo Instalando dependencias...
pip install -r requirements.txt

echo.
echo Iniciando Anti-Ransomware Shield...
echo.

REM Executa o programa
python src/main.py

pause
