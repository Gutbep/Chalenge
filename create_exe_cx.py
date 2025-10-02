"""
Criador de Executável com cx_Freeze - Anti-Ransomware Shield
Alternativa mais confiável ao PyInstaller
"""

import os
import sys
import subprocess
import shutil

def install_cx_freeze():
    """Instala cx_Freeze"""
    print("📦 Instalando cx_Freeze...")
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "cx_Freeze"], check=True)
        print("✅ cx_Freeze instalado com sucesso")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar cx_Freeze: {e}")
        return False

def create_setup_script():
    """Cria script setup.py para cx_Freeze"""
    setup_content = '''
import sys
from cx_Freeze import setup, Executable

# Dependências
build_exe_options = {
    "packages": [
        "tkinter", "psutil", "watchdog", "PIL", 
        "threading", "subprocess", "json", "time",
        "datetime", "pathlib", "collections", "hashlib",
        "re", "signal", "os", "sys"
    ],
    "include_files": [
        ("config.json", "config.json"),
        ("src/", "src/")
    ],
    "excludes": ["test", "unittest", "pdb", "doctest"],
    "optimize": 2
}

# Configuração do executável
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Anti-Ransomware Shield",
    version="1.0.0",
    description="Ferramenta anti-ransomware para Windows",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "src/main.py",
            base=base,
            target_name="AntiRansomwareShield.exe",
            icon="assets/icon.ico" if os.path.exists("assets/icon.ico") else None
        )
    ]
)
'''
    
    with open("setup_cx.py", "w", encoding="utf-8") as f:
        f.write(setup_content)
    
    print("✅ Script setup.py criado")
    return True

def create_executable_cx():
    """Cria executável usando cx_Freeze"""
    print("🔧 Criando executável com cx_Freeze...")
    
    try:
        # Comando cx_Freeze
        cmd = [sys.executable, "setup_cx.py", "build"]
        
        print("⚙️ Executando cx_Freeze...")
        print("   Isso pode levar alguns minutos...")
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Executável criado com sucesso!")
            
            # Verifica se o arquivo foi criado
            exe_path = "build/exe.win-amd64-3.11/AntiRansomwareShield.exe"
            if os.path.exists(exe_path):
                size_mb = os.path.getsize(exe_path) / (1024 * 1024)
                print(f"📁 Arquivo: {exe_path}")
                print(f"📊 Tamanho: {size_mb:.1f} MB")
                
                # Copia para dist
                os.makedirs("dist", exist_ok=True)
                shutil.copy(exe_path, "dist/AntiRansomwareShield.exe")
                print("✅ Executável copiado para dist/")
                
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

def create_simple_executable():
    """Cria executável simples sem dependências externas"""
    print("🔧 Criando executável simples...")
    
    try:
        # Cria script que executa o programa
        exe_script = '''@echo off
title Anti-Ransomware Shield
echo ========================================
echo Anti-Ransomware Shield v1.0.0
echo ========================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo ERRO: Python nao encontrado!
    echo.
    echo Para usar este programa, voce precisa ter Python 3.8+ instalado.
    echo Download: https://www.python.org/downloads/
    echo.
    echo Apos instalar Python, execute este arquivo novamente.
    pause
    exit /b 1
)

echo Python encontrado!
echo.

REM Instala dependencias se necessario
echo Verificando dependencias...
pip install psutil watchdog pillow pywin32 cryptography requests >nul 2>&1

echo.
echo Iniciando Anti-Ransomware Shield...
echo.

REM Executa o programa
python src/main.py

echo.
echo Programa finalizado.
pause
'''
        
        # Cria diretório de distribuição
        dist_dir = "dist/executavel_simples"
        os.makedirs(dist_dir, exist_ok=True)
        
        # Copia código fonte
        if os.path.exists("src"):
            shutil.copytree("src", f"{dist_dir}/src", dirs_exist_ok=True)
        
        # Copia arquivos de configuração
        files_to_copy = ["config.json", "README.md"]
        for file in files_to_copy:
            if os.path.exists(file):
                shutil.copy(file, dist_dir)
        
        # Cria script executável
        with open(f"{dist_dir}/AntiRansomwareShield.bat", "w", encoding="utf-8") as f:
            f.write(exe_script)
        
        print("✅ Executável simples criado")
        print(f"📁 Localização: {dist_dir}/AntiRansomwareShield.bat")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar executável simples: {e}")
        return False

def main():
    """Função principal"""
    print("=" * 60)
    print("🛡️  Anti-Ransomware Shield - Criador de Executável")
    print("=" * 60)
    print()
    
    print("Escolha uma opção:")
    print("1. Executável com cx_Freeze (recomendado)")
    print("2. Executável simples (batch)")
    print("3. Usar versão portável existente")
    
    choice = input("\nDigite sua escolha (1-3): ").strip()
    
    if choice == "1":
        # Opção 1: cx_Freeze
        if not install_cx_freeze():
            return False
        
        if not create_setup_script():
            return False
        
        if not create_executable_cx():
            return False
        
        print("\n🎉 EXECUTÁVEL CRIADO COM CX_FREEZE!")
        
    elif choice == "2":
        # Opção 2: Executável simples
        if not create_simple_executable():
            return False
        
        print("\n🎉 EXECUTÁVEL SIMPLES CRIADO!")
        
    elif choice == "3":
        # Opção 3: Usar versão portável
        print("\n✅ VERSÃO PORTÁVEL DISPONÍVEL!")
        print("📁 Localização: dist/portable/")
        print("🚀 Para usar: Execute dist/portable/run.bat")
        
    else:
        print("❌ Opção inválida!")
        return False
    
    print("\n" + "=" * 60)
    print("📁 ARQUIVOS DISPONÍVEIS:")
    print("=" * 60)
    
    # Lista arquivos disponíveis
    if os.path.exists("dist/AntiRansomwareShield.exe"):
        print("✅ dist/AntiRansomwareShield.exe (executável real)")
    
    if os.path.exists("dist/executavel_simples"):
        print("✅ dist/executavel_simples/ (executável batch)")
    
    if os.path.exists("dist/portable"):
        print("✅ dist/portable/ (versão portável)")
    
    if os.path.exists("dist/AntiRansomwareShield_Portavel.zip"):
        print("✅ dist/AntiRansomwareShield_Portavel.zip (versão portável)")
    
    print("\n🚀 Para distribuir:")
    print("• Use o arquivo .exe se disponível")
    print("• Use a versão portável como alternativa")
    print("• Use o executável batch para simplicidade")
    
    return True

if __name__ == "__main__":
    success = main()
    input("\nPressione Enter para continuar...")
    sys.exit(0 if success else 1)
