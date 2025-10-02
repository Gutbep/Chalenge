"""
Criador Simples de Executável - Anti-Ransomware Shield
Versão simplificada para criar executável rapidamente
"""

import os
import sys
import subprocess
import shutil

def create_simple_executable():
    """Cria executável simples do programa principal"""
    print("🔧 Criando executável do Anti-Ransomware Shield...")
    
    try:
        # Verifica se PyInstaller está instalado
        try:
            import PyInstaller
            print("✅ PyInstaller encontrado")
        except ImportError:
            print("📦 Instalando PyInstaller...")
            subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
        
        # Comando PyInstaller simplificado
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--onefile",
            "--windowed",
            "--name=AntiRansomwareShield",
            "--add-data=src;src",
            "--hidden-import=psutil",
            "--hidden-import=watchdog",
            "--hidden-import=tkinter",
            "--hidden-import=PIL",
            "src/main.py"
        ]
        
        print("⚙️ Executando PyInstaller...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Executável criado com sucesso!")
            return True
        else:
            print(f"❌ Erro ao criar executável: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def create_installer_package():
    """Cria pacote de instalação"""
    print("📦 Criando pacote de instalação...")
    
    try:
        # Cria diretório de distribuição
        dist_dir = "dist/installer"
        os.makedirs(dist_dir, exist_ok=True)
        
        # Copia executável
        if os.path.exists("dist/AntiRansomwareShield.exe"):
            shutil.copy("dist/AntiRansomwareShield.exe", dist_dir)
            print("✅ Executável copiado")
        else:
            print("❌ Executável não encontrado")
            return False
        
        # Copia arquivos necessários
        files_to_copy = [
            "config.json",
            "requirements.txt",
            "README.md"
        ]
        
        for item in files_to_copy:
            if os.path.exists(item):
                shutil.copy(item, dist_dir)
                print(f"✅ {item} copiado")
        
        # Cria script de instalação
        install_script = f'''@echo off
echo ========================================
echo Anti-Ransomware Shield - Instalador
echo ========================================
echo.

REM Cria diretorio de instalacao
echo Criando diretorio de instalacao...
mkdir "C:\\AntiRansomware" 2>nul
mkdir "C:\\AntiRansomware\\logs" 2>nul
mkdir "C:\\AntiRansomware\\Quarantine" 2>nul

REM Copia executavel
echo Copiando executavel...
copy "AntiRansomwareShield.exe" "C:\\AntiRansomware\\" /Y

REM Copia arquivos de configuracao
echo Copiando arquivos de configuracao...
copy "config.json" "C:\\AntiRansomware\\" /Y
copy "requirements.txt" "C:\\AntiRansomware\\" /Y

REM Cria atalho na area de trabalho
echo Criando atalho na area de trabalho...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\\Desktop\\Anti-Ransomware Shield.lnk'); $Shortcut.TargetPath = 'C:\\AntiRansomware\\AntiRansomwareShield.exe'; $Shortcut.Save()" 2>nul

REM Cria entrada no menu iniciar
echo Criando entrada no menu iniciar...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Anti-Ransomware Shield.lnk'); $Shortcut.TargetPath = 'C:\\AntiRansomware\\AntiRansomwareShield.exe'; $Shortcut.Save()" 2>nul

REM Configura inicializacao automatica
echo Configurando inicializacao automatica...
reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "AntiRansomwareShield" /t REG_SZ /d "C:\\AntiRansomware\\AntiRansomwareShield.exe" /f >nul

REM Configura firewall
echo Configurando firewall...
netsh advfirewall firewall add rule name="Anti-Ransomware Shield" dir=in action=allow program="C:\\AntiRansomware\\AntiRansomwareShield.exe" enable=yes >nul

echo.
echo ========================================
echo INSTALACAO CONCLUIDA COM SUCESSO!
echo ========================================
echo.
echo O Anti-Ransomware Shield foi instalado em:
echo C:\\AntiRansomware\\
echo.
echo Para executar:
echo 1. Clique no atalho da area de trabalho
echo 2. Ou execute: C:\\AntiRansomware\\AntiRansomwareShield.exe
echo.
echo O programa iniciara automaticamente no proximo boot.
echo.
pause
'''
        
        with open(f"{dist_dir}/install.bat", "w", encoding="utf-8") as f:
            f.write(install_script)
        
        print("✅ Script de instalação criado")
        print(f"📁 Pacote criado em: {dist_dir}/")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar pacote: {e}")
        return False

def main():
    """Função principal"""
    print("=" * 60)
    print("🛡️  Anti-Ransomware Shield - Criador de Executável")
    print("=" * 60)
    print()
    
    # Passo 1: Cria executável
    if not create_simple_executable():
        print("❌ Falha ao criar executável. Abortando...")
        return False
    
    print()
    
    # Passo 2: Cria pacote
    if not create_installer_package():
        print("❌ Falha ao criar pacote. Abortando...")
        return False
    
    print()
    print("🎉 EXECUTÁVEL CRIADO COM SUCESSO!")
    print("=" * 60)
    print()
    print("📁 Arquivos criados:")
    print("   • dist/AntiRansomwareShield.exe")
    print("   • dist/installer/ (pacote completo)")
    print()
    print("🚀 Para distribuir:")
    print("   1. Copie a pasta dist/installer/ para o computador de destino")
    print("   2. Execute install.bat como administrador")
    print("   3. O programa será instalado em C:\\AntiRansomware\\")
    print()
    print("✨ Características:")
    print("   • Executável standalone (não precisa de Python)")
    print("   • Interface gráfica completa")
    print("   • Todas as funcionalidades incluídas")
    print("   • Instalação automática")
    
    return True

if __name__ == "__main__":
    success = main()
    input("\nPressione Enter para continuar...")
    sys.exit(0 if success else 1)
