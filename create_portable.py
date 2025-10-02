"""
Criador de Versão Portável - Anti-Ransomware Shield
Cria uma versão portável que funciona sem instalação
"""

import os
import sys
import shutil
import zipfile
from pathlib import Path

def create_portable_version():
    """Cria versão portável do Anti-Ransomware Shield"""
    print("📦 Criando versão portável...")
    
    try:
        # Cria diretório portável
        portable_dir = "dist/portable"
        os.makedirs(portable_dir, exist_ok=True)
        
        # Copia código fonte
        if os.path.exists("src"):
            shutil.copytree("src", f"{portable_dir}/src", dirs_exist_ok=True)
            print("✅ Código fonte copiado")
        
        # Copia arquivos de configuração
        files_to_copy = [
            "config.json",
            "requirements.txt",
            "README.md"
        ]
        
        for file in files_to_copy:
            if os.path.exists(file):
                shutil.copy(file, portable_dir)
                print(f"✅ {file} copiado")
        
        # Cria script de execução
        run_script = '''@echo off
echo ========================================
echo Anti-Ransomware Shield - Versao Portavel
echo ========================================
echo.

REM Verifica se Python esta instalado
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

REM Instala dependencias se necessario
echo Instalando dependencias...
pip install -r requirements.txt
if %errorLevel% neq 0 (
    echo ERRO: Falha ao instalar dependencias!
    echo Execute: pip install -r requirements.txt
    pause
    exit /b 1
)

echo.
echo Dependencias instaladas com sucesso!
echo.

REM Executa o programa
echo Iniciando Anti-Ransomware Shield...
echo.
python src/main.py

pause
'''
        
        with open(f"{portable_dir}/run.bat", "w", encoding="utf-8") as f:
            f.write(run_script)
        
        print("✅ Script de execução criado")
        
        # Cria README da versão portável
        readme_content = """
# 🛡️ Anti-Ransomware Shield - Versão Portável

## 🚀 Como Usar

### Pré-requisitos
- Python 3.8+ instalado
- Conexão com internet (para instalar dependências)

### Execução
1. **Execute o programa**:
   ```
   run.bat
   ```

2. **Ou execute manualmente**:
   ```
   pip install -r requirements.txt
   python src/main.py
   ```

## ✨ Características

- ✅ **Portável**: Não precisa de instalação
- ✅ **Completo**: Todas as funcionalidades incluídas
- ✅ **Interface Gráfica**: Interface moderna e intuitiva
- ✅ **Proteção Completa**: Monitoramento, detecção e proteção
- ✅ **Configurável**: Opções avançadas disponíveis

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
        
        with open(f"{portable_dir}/README_Portavel.txt", "w", encoding="utf-8") as f:
            f.write(readme_content)
        
        print("✅ README da versão portável criado")
        
        # Cria arquivo ZIP
        zip_path = "dist/AntiRansomwareShield_Portavel.zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(portable_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arc_path = os.path.relpath(file_path, portable_dir)
                    zipf.write(file_path, arc_path)
        
        print(f"✅ Arquivo ZIP criado: {zip_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar versão portável: {e}")
        return False

def create_installer_script():
    """Cria script de instalação para a versão portável"""
    print("🔧 Criando script de instalação...")
    
    try:
        installer_script = '''@echo off
echo ========================================
echo Anti-Ransomware Shield - Instalador
echo ========================================
echo.

REM Verifica se Python esta instalado
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

REM Cria diretorio de instalacao
echo Criando diretorio de instalacao...
mkdir "C:\\AntiRansomware" 2>nul
mkdir "C:\\AntiRansomware\\logs" 2>nul
mkdir "C:\\AntiRansomware\\Quarantine" 2>nul

REM Copia arquivos
echo Copiando arquivos...
xcopy "src" "C:\\AntiRansomware\\src\\" /E /I /Y >nul
copy "config.json" "C:\\AntiRansomware\\" /Y >nul
copy "requirements.txt" "C:\\AntiRansomware\\" /Y >nul

REM Cria script de execucao
echo Criando script de execucao...
(
echo @echo off
echo echo ========================================
echo echo Anti-Ransomware Shield
echo echo ========================================
echo echo.
echo.
echo cd /d "C:\\AntiRansomware"
echo.
echo python src\\main.py
echo.
echo pause
) > "C:\\AntiRansomware\\run.bat"

REM Cria atalho na area de trabalho
echo Criando atalho na area de trabalho...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\\Desktop\\Anti-Ransomware Shield.lnk'); $Shortcut.TargetPath = 'C:\\AntiRansomware\\run.bat'; $Shortcut.Save()" 2>nul

REM Cria entrada no menu iniciar
echo Criando entrada no menu iniciar...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Anti-Ransomware Shield.lnk'); $Shortcut.TargetPath = 'C:\\AntiRansomware\\run.bat'; $Shortcut.Save()" 2>nul

REM Configura inicializacao automatica
echo Configurando inicializacao automatica...
reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "AntiRansomwareShield" /t REG_SZ /d "C:\\AntiRansomware\\run.bat" /f >nul

REM Instala dependencias
echo Instalando dependencias...
cd /d "C:\\AntiRansomware"
pip install -r requirements.txt

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
echo 2. Ou execute: C:\\AntiRansomware\\run.bat
echo.
echo O programa iniciara automaticamente no proximo boot.
echo.
pause
'''
        
        with open("dist/portable/install.bat", "w", encoding="utf-8") as f:
            f.write(installer_script)
        
        print("✅ Script de instalação criado")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar script de instalação: {e}")
        return False

def main():
    """Função principal"""
    print("=" * 60)
    print("🛡️  Anti-Ransomware Shield - Criador de Versão Portável")
    print("=" * 60)
    print()
    
    # Passo 1: Cria versão portável
    if not create_portable_version():
        print("❌ Falha ao criar versão portável. Abortando...")
        return False
    
    print()
    
    # Passo 2: Cria script de instalação
    if not create_installer_script():
        print("❌ Falha ao criar script de instalação. Abortando...")
        return False
    
    print()
    print("🎉 VERSÃO PORTÁVEL CRIADA COM SUCESSO!")
    print("=" * 60)
    print()
    print("📁 Arquivos criados:")
    print("   • dist/portable/ (versão portável)")
    print("   • dist/AntiRansomwareShield_Portavel.zip")
    print()
    print("🚀 Para usar:")
    print("   1. Extraia o arquivo ZIP")
    print("   2. Execute run.bat")
    print("   3. Ou execute install.bat para instalação completa")
    print()
    print("✨ Características:")
    print("   • Portável (não precisa de instalação)")
    print("   • Funciona em qualquer computador com Python")
    print("   • Todas as funcionalidades incluídas")
    print("   • Interface gráfica completa")
    
    return True

if __name__ == "__main__":
    success = main()
    input("\nPressione Enter para continuar...")
    sys.exit(0 if success else 1)
