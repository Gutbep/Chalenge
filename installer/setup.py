"""
Instalador para Anti-Ransomware Shield
Cria executável e instala no sistema Windows
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def create_executable():
    """Cria executável usando PyInstaller"""
    try:
        print("Criando executável...")
        
        # Verifica se PyInstaller está instalado
        try:
            import PyInstaller
            print("✅ PyInstaller encontrado")
        except ImportError:
            print("📦 Instalando PyInstaller...")
            subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
        
        # Comando PyInstaller
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--onefile",
            "--windowed",
            "--name=AntiRansomwareShield",
            "--add-data=src;src",
            "--hidden-import=psutil",
            "--hidden-import=watchdog",
            "--hidden-import=PIL",
            "--hidden-import=tkinter",
            "--hidden-import=tkinter.ttk",
            "--hidden-import=tkinter.messagebox",
            "--hidden-import=tkinter.scrolledtext",
            "--hidden-import=tkinter.filedialog",
            "src/main.py"
        ]
        
        # Executa PyInstaller
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Executável criado com sucesso!")
            return True
        else:
            print(f"❌ Erro ao criar executável: {result.stderr}")
            print(f"Output: {result.stdout}")
            return False
            
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def create_installer_script():
    """Cria script de instalação"""
    installer_script = """
@echo off
echo ========================================
echo Anti-Ransomware Shield - Instalador
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

echo Criando diretorios...
mkdir "C:\\AntiRansomware" 2>nul
mkdir "C:\\AntiRansomware\\logs" 2>nul
mkdir "C:\\AntiRansomware\\Quarantine" 2>nul

echo Copiando arquivos...
copy "AntiRansomwareShield.exe" "C:\\AntiRansomware\\" /Y
copy "assets\\*" "C:\\AntiRansomware\\assets\\" /Y

echo Criando atalho na area de trabalho...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\\Desktop\\Anti-Ransomware Shield.lnk'); $Shortcut.TargetPath = 'C:\\AntiRansomware\\AntiRansomwareShield.exe'; $Shortcut.Save()"

echo Criando entrada no menu iniciar...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Anti-Ransomware Shield.lnk'); $Shortcut.TargetPath = 'C:\\AntiRansomware\\AntiRansomwareShield.exe'; $Shortcut.Save()"

echo Configurando inicializacao automatica...
reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "AntiRansomwareShield" /t REG_SZ /d "C:\\AntiRansomware\\AntiRansomwareShield.exe" /f

echo Configurando firewall...
netsh advfirewall firewall add rule name="Anti-Ransomware Shield" dir=in action=allow program="C:\\AntiRansomware\\AntiRansomwareShield.exe" enable=yes

echo.
echo ========================================
echo Instalacao concluida com sucesso!
echo ========================================
echo.
echo O Anti-Ransomware Shield foi instalado em:
echo C:\\AntiRansomware\\
echo.
echo O programa iniciara automaticamente no proximo boot.
echo.
pause
"""
    
    with open("install.bat", "w", encoding="utf-8") as f:
        f.write(installer_script)
    
    print("✅ Script de instalação criado!")

def create_uninstaller_script():
    """Cria script de desinstalação"""
    uninstaller_script = """
@echo off
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

echo Parando servico...
taskkill /f /im AntiRansomwareShield.exe 2>nul

echo Removendo inicializacao automatica...
reg delete "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "AntiRansomwareShield" /f 2>nul

echo Removendo regra do firewall...
netsh advfirewall firewall delete rule name="Anti-Ransomware Shield" 2>nul

echo Removendo atalhos...
del "%USERPROFILE%\\Desktop\\Anti-Ransomware Shield.lnk" 2>nul
del "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Anti-Ransomware Shield.lnk" 2>nul

echo Removendo arquivos...
rmdir /s /q "C:\\AntiRansomware" 2>nul

echo.
echo ========================================
echo Desinstalacao concluida!
echo ========================================
echo.
pause
"""
    
    with open("uninstall.bat", "w", encoding="utf-8") as f:
        f.write(uninstaller_script)
    
    print("✅ Script de desinstalação criado!")

def create_assets():
    """Cria diretório de assets"""
    os.makedirs("assets", exist_ok=True)
    
    # Cria ícone simples (seria melhor ter um ícone real)
    icon_content = """
# Placeholder para ícone
# Em produção, substitua por um ícone real (.ico)
"""
    
    with open("assets/icon.ico", "w") as f:
        f.write(icon_content)
    
    print("✅ Assets criados!")

def create_installer_package():
    """Cria pacote de instalação completo"""
    try:
        print("Criando pacote de instalação...")
        
        # Cria diretório de distribuição
        dist_dir = "dist/installer"
        os.makedirs(dist_dir, exist_ok=True)
        
        # Copia executável
        if os.path.exists("dist/AntiRansomwareShield.exe"):
            shutil.copy("dist/AntiRansomwareShield.exe", dist_dir)
            print("✅ Executável copiado")
        else:
            print("❌ Executável não encontrado. Execute create_executable() primeiro.")
            return False
        
        # Copia scripts
        shutil.copy("install.bat", dist_dir)
        shutil.copy("uninstall.bat", dist_dir)
        
        # Copia assets
        if os.path.exists("assets"):
            shutil.copytree("assets", f"{dist_dir}/assets", dirs_exist_ok=True)
        
        # Cria README
        readme_content = """
# Anti-Ransomware Shield v1.0

## Instalação

1. Execute `install.bat` como administrador
2. O programa será instalado em C:\\AntiRansomware\\
3. Será criado um atalho na área de trabalho
4. O programa iniciará automaticamente no boot

## Desinstalação

Execute `uninstall.bat` como administrador

## Requisitos

- Windows 10/11
- Privilégios de administrador para instalação
- 50 MB de espaço em disco

## Uso

1. Execute o programa
2. Clique em "Iniciar Proteção"
3. O sistema começará a monitorar automaticamente
4. Em caso de detecção, o programa agirá automaticamente

## Suporte

Para suporte técnico, consulte os logs em:
C:\\AntiRansomware\\logs\\
"""
        
        with open(f"{dist_dir}/README.txt", "w", encoding="utf-8") as f:
            f.write(readme_content)
        
        print("✅ Pacote de instalação criado em dist/installer/")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar pacote: {e}")
        return False

def main():
    """Função principal do instalador"""
    print("=== Anti-Ransomware Shield - Instalador ===")
    print()
    
    # Cria assets
    create_assets()
    
    # Cria executável
    if not create_executable():
        print("Falha ao criar executável. Abortando...")
        return
    
    # Cria scripts
    create_installer_script()
    create_uninstaller_script()
    
    # Cria pacote
    if create_installer_package():
        print()
        print("🎉 Instalador criado com sucesso!")
        print("📁 Pacote disponível em: dist/installer/")
        print()
        print("Para instalar:")
        print("1. Copie a pasta dist/installer/ para o computador de destino")
        print("2. Execute install.bat como administrador")
        print()
    else:
        print("❌ Falha ao criar pacote de instalação")

if __name__ == "__main__":
    main()
