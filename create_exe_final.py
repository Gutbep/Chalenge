"""
Criador Final de Executável - Anti-Ransomware Shield
Cria executável real usando PyInstaller com configurações otimizadas
"""

import os
import sys
import subprocess
import shutil

def create_executable_final():
    """Cria executável final do Anti-Ransomware Shield"""
    print("🔧 Criando executável final...")
    
    try:
        # Verifica se PyInstaller está instalado
        try:
            import PyInstaller
            print("✅ PyInstaller encontrado")
        except ImportError:
            print("📦 Instalando PyInstaller...")
            subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
        
        # Limpa builds anteriores
        if os.path.exists("build"):
            shutil.rmtree("build")
        if os.path.exists("dist"):
            # Remove apenas arquivos antigos, mantém portable
            for item in os.listdir("dist"):
                if item != "portable":
                    item_path = os.path.join("dist", item)
                    if os.path.isfile(item_path):
                        os.remove(item_path)
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)
        
        # Comando PyInstaller otimizado
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--onefile",
            "--windowed",
            "--name=AntiRansomwareShield",
            "--distpath=dist",
            "--workpath=build",
            "--specpath=.",
            "--add-data=src;src",
            "--add-data=config.json;.",
            "--hidden-import=psutil",
            "--hidden-import=watchdog",
            "--hidden-import=tkinter",
            "--hidden-import=tkinter.ttk",
            "--hidden-import=tkinter.messagebox",
            "--hidden-import=tkinter.scrolledtext",
            "--hidden-import=tkinter.filedialog",
            "--hidden-import=PIL",
            "--hidden-import=PIL.Image",
            "--hidden-import=PIL.ImageTk",
            "--hidden-import=threading",
            "--hidden-import=subprocess",
            "--hidden-import=json",
            "--hidden-import=time",
            "--hidden-import=datetime",
            "--hidden-import=pathlib",
            "--hidden-import=collections",
            "--hidden-import=hashlib",
            "--hidden-import=re",
            "--hidden-import=signal",
            "--clean",
            "src/main.py"
        ]
        
        print("⚙️ Executando PyInstaller...")
        print("   Isso pode levar alguns minutos...")
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Executável criado com sucesso!")
            
            # Verifica se o arquivo foi criado
            exe_path = "dist/AntiRansomwareShield.exe"
            if os.path.exists(exe_path):
                size_mb = os.path.getsize(exe_path) / (1024 * 1024)
                print(f"📁 Arquivo: {exe_path}")
                print(f"📊 Tamanho: {size_mb:.1f} MB")
                return True
            else:
                print("❌ Executável não encontrado após criação")
                return False
        else:
            print(f"❌ Erro ao criar executável:")
            print(f"STDOUT: {result.stdout}")
            print(f"STDERR: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def create_installer_package_final():
    """Cria pacote final de instalação"""
    print("📦 Criando pacote final de instalação...")
    
    try:
        # Cria diretório de distribuição
        dist_dir = "dist/installer_final"
        os.makedirs(dist_dir, exist_ok=True)
        
        # Copia executável
        exe_path = "dist/AntiRansomwareShield.exe"
        if os.path.exists(exe_path):
            shutil.copy(exe_path, dist_dir)
            print("✅ Executável copiado")
        else:
            print("❌ Executável não encontrado")
            return False
        
        # Copia arquivos de configuração
        files_to_copy = [
            "config.json",
            "README.md"
        ]
        
        for item in files_to_copy:
            if os.path.exists(item):
                shutil.copy(item, dist_dir)
                print(f"✅ {item} copiado")
        
        # Cria script de instalação
        install_script = '''@echo off
echo ========================================
echo Anti-Ransomware Shield - Instalador Final
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
echo CARACTERISTICAS DO EXECUTAVEL:
echo - Nao precisa de Python instalado
echo - Interface grafica completa
echo - Todas as funcionalidades incluidas
echo - Protecao contra ransomware
echo.
pause
'''
        
        with open(f"{dist_dir}/install.bat", "w", encoding="utf-8") as f:
            f.write(install_script)
        
        print("✅ Script de instalação criado")
        
        # Cria README do executável
        readme_content = """
# 🛡️ Anti-Ransomware Shield - Executável Final

## 🚀 Instalação

### Método 1: Instalação Automática
1. Execute `install.bat` como administrador
2. Siga as instruções na tela
3. O programa será instalado em `C:\\AntiRansomware\\`

### Método 2: Execução Direta
1. Execute `AntiRansomwareShield.exe` diretamente
2. O programa funcionará sem instalação

## ✨ Características do Executável

- ✅ **Standalone**: Não precisa de Python instalado
- ✅ **Interface Gráfica**: Interface moderna e intuitiva
- ✅ **Proteção Completa**: Monitoramento, detecção e proteção
- ✅ **Todas as Funcionalidades**: Incluídas no executável
- ✅ **Portável**: Pode ser executado de qualquer lugar

## 🛡️ Funcionalidades

- **Monitoramento em Tempo Real**: Observa sistema 24/7
- **Detecção Inteligente**: Múltiplos algoritmos de detecção
- **Proteção Automática**: Ação imediata contra ameaças
- **Modo de Emergência**: Ativação automática em situações críticas
- **Interface Profissional**: GUI moderna e intuitiva
- **Logs Detalhados**: Histórico completo de atividades

## 📞 Suporte

Para suporte técnico:
- README.md - Documentação principal
- TROUBLESHOOTING.md - Solução de problemas
- GitHub Issues - Reportar problemas

---

**🛡️ Proteja seu sistema contra ransomware!**
"""
        
        with open(f"{dist_dir}/README_Executavel.txt", "w", encoding="utf-8") as f:
            f.write(readme_content)
        
        print("✅ README do executável criado")
        print(f"📁 Pacote final criado em: {dist_dir}/")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar pacote final: {e}")
        return False

def main():
    """Função principal"""
    print("=" * 60)
    print("🛡️  Anti-Ransomware Shield - Criador de Executável Final")
    print("=" * 60)
    print()
    
    # Passo 1: Cria executável
    if not create_executable_final():
        print("❌ Falha ao criar executável. Abortando...")
        return False
    
    print()
    
    # Passo 2: Cria pacote final
    if not create_installer_package_final():
        print("❌ Falha ao criar pacote final. Abortando...")
        return False
    
    print()
    print("🎉 EXECUTÁVEL FINAL CRIADO COM SUCESSO!")
    print("=" * 60)
    print()
    print("📁 Arquivos criados:")
    print("   • dist/AntiRansomwareShield.exe (executável principal)")
    print("   • dist/installer_final/ (pacote de instalação)")
    print("   • dist/portable/ (versão portável)")
    print("   • dist/AntiRansomwareShield_Portavel.zip")
    print()
    print("🚀 Para distribuir:")
    print("   1. EXECUTÁVEL: Use dist/AntiRansomwareShield.exe")
    print("   2. INSTALAÇÃO: Use dist/installer_final/install.bat")
    print("   3. PORTÁVEL: Use dist/portable/run.bat")
    print()
    print("✨ Características do executável:")
    print("   • Standalone (não precisa de Python)")
    print("   • Interface gráfica completa")
    print("   • Todas as funcionalidades incluídas")
    print("   • Proteção contra ransomware")
    print("   • Tamanho otimizado")
    
    return True

if __name__ == "__main__":
    success = main()
    input("\nPressione Enter para continuar...")
    sys.exit(0 if success else 1)
