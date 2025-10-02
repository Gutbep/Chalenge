"""
Instalador simplificado para Anti-Ransomware Shield
Funciona sem PyInstaller - apenas copia arquivos e configura
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def install_dependencies():
    """Instala dependências necessárias"""
    print("📦 Instalando dependências...")
    
    try:
        # Instala dependências do requirements.txt
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, capture_output=True)
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def create_installation_directory():
    """Cria diretório de instalação"""
    install_dir = "C:\\AntiRansomware"
    
    try:
        os.makedirs(install_dir, exist_ok=True)
        os.makedirs(f"{install_dir}\\logs", exist_ok=True)
        os.makedirs(f"{install_dir}\\Quarantine", exist_ok=True)
        os.makedirs(f"{install_dir}\\assets", exist_ok=True)
        print(f"✅ Diretório criado: {install_dir}")
        return install_dir
    except Exception as e:
        print(f"❌ Erro ao criar diretório: {e}")
        return None

def copy_files(install_dir):
    """Copia arquivos para diretório de instalação"""
    try:
        # Copia código fonte
        src_dir = "src"
        if os.path.exists(src_dir):
            shutil.copytree(src_dir, f"{install_dir}\\src", dirs_exist_ok=True)
            print("✅ Código fonte copiado")
        
        # Copia arquivo de configuração
        if os.path.exists("config.json"):
            shutil.copy("config.json", f"{install_dir}\\config.json")
            print("✅ Configuração copiada")
        
        # Copia requirements.txt
        if os.path.exists("requirements.txt"):
            shutil.copy("requirements.txt", f"{install_dir}\\requirements.txt")
            print("✅ Requirements copiado")
        
        return True
    except Exception as e:
        print(f"❌ Erro ao copiar arquivos: {e}")
        return False

def create_launcher_script(install_dir):
    """Cria script de inicialização"""
    launcher_script = f'''@echo off
echo ========================================
echo Anti-Ransomware Shield
echo ========================================
echo.

REM Muda para diretório de instalação
cd /d "{install_dir}"

REM Verifica se Python está disponível
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
call venv\\Scripts\\activate.bat

echo Instalando dependencias...
pip install -r requirements.txt

echo.
echo Iniciando Anti-Ransomware Shield...
echo.

REM Executa o programa
python src/main.py

pause
'''
    
    try:
        with open(f"{install_dir}\\run.bat", "w", encoding="utf-8") as f:
            f.write(launcher_script)
        print("✅ Script de inicialização criado")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar script: {e}")
        return False

def create_desktop_shortcut(install_dir):
    """Cria atalho na área de trabalho"""
    try:
        # Cria atalho usando PowerShell
        shortcut_script = f'''
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$env:USERPROFILE\\Desktop\\Anti-Ransomware Shield.lnk")
$Shortcut.TargetPath = "{install_dir}\\run.bat"
$Shortcut.WorkingDirectory = "{install_dir}"
$Shortcut.Description = "Anti-Ransomware Shield - Proteção contra ransomware"
$Shortcut.Save()
'''
        
        with open("create_shortcut.ps1", "w", encoding="utf-8") as f:
            f.write(shortcut_script)
        
        # Executa PowerShell
        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "create_shortcut.ps1"], 
                      capture_output=True)
        
        # Remove script temporário
        os.remove("create_shortcut.ps1")
        
        print("✅ Atalho na área de trabalho criado")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar atalho: {e}")
        return False

def create_start_menu_entry(install_dir):
    """Cria entrada no menu iniciar"""
    try:
        start_menu_script = f'''
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$env:APPDATA\\Microsoft\\Windows\\Start Menu\\Programs\\Anti-Ransomware Shield.lnk")
$Shortcut.TargetPath = "{install_dir}\\run.bat"
$Shortcut.WorkingDirectory = "{install_dir}"
$Shortcut.Description = "Anti-Ransomware Shield - Proteção contra ransomware"
$Shortcut.Save()
'''
        
        with open("create_start_menu.ps1", "w", encoding="utf-8") as f:
            f.write(start_menu_script)
        
        # Executa PowerShell
        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "create_start_menu.ps1"], 
                      capture_output=True)
        
        # Remove script temporário
        os.remove("create_start_menu.ps1")
        
        print("✅ Entrada no menu iniciar criada")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar entrada no menu: {e}")
        return False

def configure_auto_start(install_dir):
    """Configura inicialização automática"""
    try:
        # Adiciona ao registro para inicialização automática
        reg_script = f'''
reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "AntiRansomwareShield" /t REG_SZ /d "{install_dir}\\run.bat" /f
'''
        
        with open("configure_autostart.bat", "w", encoding="utf-8") as f:
            f.write(reg_script)
        
        # Executa script
        subprocess.run(["configure_autostart.bat"], capture_output=True)
        
        # Remove script temporário
        os.remove("configure_autostart.bat")
        
        print("✅ Inicialização automática configurada")
        return True
    except Exception as e:
        print(f"❌ Erro ao configurar auto-start: {e}")
        return False

def create_uninstaller(install_dir):
    """Cria script de desinstalação"""
    uninstaller_script = f'''@echo off
echo ========================================
echo Anti-Ransomware Shield - Desinstalador
echo ========================================
echo.

REM Verifica se está executando como administrador
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Executando como administrador...
) else (
    echo ERRO: Execute como administrador!
    pause
    exit /b 1
)

echo Parando processos...
taskkill /f /im python.exe 2>nul

echo Removendo inicializacao automatica...
reg delete "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "AntiRansomwareShield" /f 2>nul

echo Removendo atalhos...
del "%USERPROFILE%\\Desktop\\Anti-Ransomware Shield.lnk" 2>nul
del "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Anti-Ransomware Shield.lnk" 2>nul

echo Removendo arquivos...
rmdir /s /q "{install_dir}" 2>nul

echo.
echo ========================================
echo Desinstalacao concluida!
echo ========================================
echo.
pause
'''
    
    try:
        with open(f"{install_dir}\\uninstall.bat", "w", encoding="utf-8") as f:
            f.write(uninstaller_script)
        print("✅ Script de desinstalação criado")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar desinstalador: {e}")
        return False

def main():
    """Função principal do instalador"""
    print("=" * 50)
    print("🛡️  Anti-Ransomware Shield - Instalador Simples")
    print("=" * 50)
    print()
    
    # Verifica se está executando como administrador
    try:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        if not is_admin:
            print("⚠️  AVISO: Execute como administrador para instalação completa")
            print("   Algumas funcionalidades podem não estar disponíveis")
            print()
    except:
        print("⚠️  Não foi possível verificar privilégios de administrador")
        print()
    
    # Passo 1: Instala dependências
    if not install_dependencies():
        print("❌ Falha na instalação de dependências")
        return False
    
    # Passo 2: Cria diretório de instalação
    install_dir = create_installation_directory()
    if not install_dir:
        print("❌ Falha ao criar diretório de instalação")
        return False
    
    # Passo 3: Copia arquivos
    if not copy_files(install_dir):
        print("❌ Falha ao copiar arquivos")
        return False
    
    # Passo 4: Cria script de inicialização
    if not create_launcher_script(install_dir):
        print("❌ Falha ao criar script de inicialização")
        return False
    
    # Passo 5: Cria atalhos
    create_desktop_shortcut(install_dir)
    create_start_menu_entry(install_dir)
    
    # Passo 6: Configura inicialização automática
    configure_auto_start(install_dir)
    
    # Passo 7: Cria desinstalador
    create_uninstaller(install_dir)
    
    print()
    print("=" * 50)
    print("🎉 INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
    print("=" * 50)
    print()
    print(f"📁 Instalado em: {install_dir}")
    print("🖥️  Atalho criado na área de trabalho")
    print("📋 Entrada criada no menu iniciar")
    print("🔄 Inicialização automática configurada")
    print()
    print("Para executar:")
    print(f"1. Clique no atalho da área de trabalho")
    print(f"2. Ou execute: {install_dir}\\run.bat")
    print()
    print("Para desinstalar:")
    print(f"Execute: {install_dir}\\uninstall.bat")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    input("\nPressione Enter para continuar...")
    sys.exit(0 if success else 1)
