"""
Criador de Instalador Wizard Executável
Gera um instalador .exe profissional
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def create_wizard_executable():
    """Cria executável do instalador wizard"""
    print("🔧 Criando instalador wizard executável...")
    
    try:
        # Verifica se PyInstaller está instalado
        try:
            import PyInstaller
            print("✅ PyInstaller encontrado")
        except ImportError:
            print("📦 Instalando PyInstaller...")
            subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
        
        # Comando PyInstaller para criar instalador
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--onefile",
            "--windowed",
            "--name=AntiRansomwareShield_Installer",
            "--icon=assets/icon.ico",
            "--add-data=src;src",
            "--add-data=config.json;.",
            "--add-data=requirements.txt;.",
            "--hidden-import=tkinter",
            "--hidden-import=tkinter.ttk",
            "--hidden-import=tkinter.messagebox",
            "--hidden-import=tkinter.filedialog",
            "installer/wizard_installer.py"
        ]
        
        print("⚙️ Executando PyInstaller...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Instalador wizard criado com sucesso!")
            print("📁 Arquivo: dist/AntiRansomwareShield_Installer.exe")
            return True
        else:
            print(f"❌ Erro ao criar instalador: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def create_installer_package():
    """Cria pacote completo do instalador"""
    print("📦 Criando pacote do instalador...")
    
    try:
        # Cria diretório de distribuição
        dist_dir = "dist/installer_wizard"
        os.makedirs(dist_dir, exist_ok=True)
        
        # Copia executável
        if os.path.exists("dist/AntiRansomwareShield_Installer.exe"):
            shutil.copy("dist/AntiRansomwareShield_Installer.exe", dist_dir)
            print("✅ Executável copiado")
        else:
            print("❌ Executável não encontrado")
            return False
        
        # Copia arquivos necessários
        files_to_copy = [
            "src",
            "config.json", 
            "requirements.txt",
            "README.md"
        ]
        
        for item in files_to_copy:
            if os.path.exists(item):
                if os.path.isdir(item):
                    shutil.copytree(item, f"{dist_dir}/{item}", dirs_exist_ok=True)
                else:
                    shutil.copy(item, dist_dir)
                print(f"✅ {item} copiado")
        
        # Cria README do instalador
        readme_content = """
# 🛡️ Anti-Ransomware Shield - Instalador Wizard

## 🚀 Instalação

1. **Execute o instalador**:
   - Clique duas vezes em `AntiRansomwareShield_Installer.exe`
   - Siga as instruções do wizard

2. **Requisitos**:
   - Windows 10/11
   - Python 3.8+ (será verificado automaticamente)
   - 50 MB de espaço em disco
   - Privilégios de administrador (recomendado)

## ✨ Características do Instalador

- **Interface Wizard**: Instalação guiada passo a passo
- **Verificação Automática**: Checa requisitos do sistema
- **Configuração Flexível**: Escolha opções de instalação
- **Progresso Visual**: Acompanhe o progresso em tempo real
- **Logs Detalhados**: Veja o que está sendo instalado
- **Configuração Automática**: Atalhos, firewall, inicialização

## 🎯 Funcionalidades

- ✅ Instalação automática de dependências
- ✅ Criação de atalhos (área de trabalho e menu iniciar)
- ✅ Configuração de inicialização automática
- ✅ Configuração de regras do firewall
- ✅ Verificação de privilégios de administrador
- ✅ Interface moderna e intuitiva

## 📞 Suporte

Para suporte técnico, consulte:
- README.md - Documentação principal
- TROUBLESHOOTING.md - Solução de problemas
- GitHub Issues - Reportar problemas

---

**🛡️ Proteja seu sistema contra ransomware com o Anti-Ransomware Shield!**
"""
        
        with open(f"{dist_dir}/README_Instalador.txt", "w", encoding="utf-8") as f:
            f.write(readme_content)
        
        print("✅ README do instalador criado")
        print(f"📁 Pacote criado em: {dist_dir}/")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar pacote: {e}")
        return False

def main():
    """Função principal"""
    print("=" * 60)
    print("🛡️  Anti-Ransomware Shield - Criador de Instalador Wizard")
    print("=" * 60)
    print()
    
    # Passo 1: Cria executável
    if not create_wizard_executable():
        print("❌ Falha ao criar executável. Abortando...")
        return False
    
    print()
    
    # Passo 2: Cria pacote
    if not create_installer_package():
        print("❌ Falha ao criar pacote. Abortando...")
        return False
    
    print()
    print("🎉 INSTALADOR WIZARD CRIADO COM SUCESSO!")
    print("=" * 60)
    print()
    print("📁 Arquivos criados:")
    print("   • dist/AntiRansomwareShield_Installer.exe")
    print("   • dist/installer_wizard/ (pacote completo)")
    print()
    print("🚀 Para distribuir:")
    print("   1. Copie a pasta dist/installer_wizard/ para o computador de destino")
    print("   2. Execute AntiRansomwareShield_Installer.exe")
    print("   3. Siga as instruções do wizard")
    print()
    print("✨ Características do instalador:")
    print("   • Interface wizard moderna")
    print("   • Instalação guiada passo a passo")
    print("   • Verificação automática de requisitos")
    print("   • Configuração flexível")
    print("   • Progresso visual em tempo real")
    print("   • Logs detalhados da instalação")
    print("   • Configuração automática de atalhos e firewall")
    
    return True

if __name__ == "__main__":
    success = main()
    input("\nPressione Enter para continuar...")
    sys.exit(0 if success else 1)
