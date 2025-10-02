@echo off
echo ========================================
echo Anti-Ransomware Shield - Instalador
echo ========================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo ERRO: Python nao encontrado!
    echo Instale Python 3.8+ e tente novamente.
    echo Download: https://www.python.org/downloads/
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

REM Cria diretório de instalação
echo Criando diretorio de instalacao...
mkdir "C:\AntiRansomware" 2>nul
mkdir "C:\AntiRansomware\logs" 2>nul
mkdir "C:\AntiRansomware\Quarantine" 2>nul

REM Copia arquivos
echo Copiando arquivos...
xcopy "src" "C:\AntiRansomware\src\" /E /I /Y >nul
copy "config.json" "C:\AntiRansomware\" /Y >nul
copy "requirements.txt" "C:\AntiRansomware\" /Y >nul

REM Cria script de execução
echo Criando script de execucao...
(
echo @echo off
echo echo ========================================
echo echo Anti-Ransomware Shield
echo echo ========================================
echo echo.
echo.
echo cd /d "C:\AntiRansomware"
echo.
echo python src\main.py
echo.
echo pause
) > "C:\AntiRansomware\run.bat"

REM Cria atalho na área de trabalho
echo Criando atalho na area de trabalho...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\Anti-Ransomware Shield.lnk'); $Shortcut.TargetPath = 'C:\AntiRansomware\run.bat'; $Shortcut.Save()" 2>nul

REM Cria entrada no menu iniciar
echo Criando entrada no menu iniciar...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%APPDATA%\Microsoft\Windows\Start Menu\Programs\Anti-Ransomware Shield.lnk'); $Shortcut.TargetPath = 'C:\AntiRansomware\run.bat'; $Shortcut.Save()" 2>nul

REM Configura inicialização automática
echo Configurando inicializacao automatica...
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "AntiRansomwareShield" /t REG_SZ /d "C:\AntiRansomware\run.bat" /f >nul

REM Cria desinstalador
echo Criando desinstalador...
(
echo @echo off
echo echo ========================================
echo echo Anti-Ransomware Shield - Desinstalador
echo echo ========================================
echo echo.
echo.
echo echo Parando processos...
echo taskkill /f /im python.exe 2^>nul
echo.
echo echo Removendo inicializacao automatica...
echo reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "AntiRansomwareShield" /f 2^>nul
echo.
echo echo Removendo atalhos...
echo del "%USERPROFILE%\Desktop\Anti-Ransomware Shield.lnk" 2^>nul
echo del "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Anti-Ransomware Shield.lnk" 2^>nul
echo.
echo echo Removendo arquivos...
echo rmdir /s /q "C:\AntiRansomware" 2^>nul
echo.
echo echo Desinstalacao concluida!
echo pause
) > "C:\AntiRansomware\uninstall.bat"

echo.
echo ========================================
echo INSTALACAO CONCLUIDA COM SUCESSO!
echo ========================================
echo.
echo O Anti-Ransomware Shield foi instalado em:
echo C:\AntiRansomware\
echo.
echo Para executar:
echo 1. Clique no atalho da area de trabalho
echo 2. Ou execute: C:\AntiRansomware\run.bat
echo.
echo Para desinstalar:
echo Execute: C:\AntiRansomware\uninstall.bat
echo.
echo O programa iniciara automaticamente no proximo boot.
echo.
pause
