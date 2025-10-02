"""
Criador Direto de Executável Simples
"""

import os
import shutil

def create_simple_executable():
    """Cria executável simples"""
    print("🔧 Criando executável simples...")
    
    try:
        # Cria diretório de distribuição
        dist_dir = "dist/executavel_simples"
        os.makedirs(dist_dir, exist_ok=True)
        
        # Copia código fonte
        if os.path.exists("src"):
            shutil.copytree("src", f"{dist_dir}/src", dirs_exist_ok=True)
            print("✅ Código fonte copiado")
        
        # Copia arquivos de configuração
        files_to_copy = ["config.json", "README.md"]
        for file in files_to_copy:
            if os.path.exists(file):
                shutil.copy(file, dist_dir)
                print(f"✅ {file} copiado")
        
        # Cria script executável
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
        
        with open(f"{dist_dir}/AntiRansomwareShield.bat", "w", encoding="utf-8") as f:
            f.write(exe_script)
        
        print("✅ Executável simples criado")
        print(f"📁 Localização: {dist_dir}/AntiRansomwareShield.bat")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    print("🛡️ Criando executável simples...")
    success = create_simple_executable()
    
    if success:
        print("\n🎉 EXECUTÁVEL SIMPLES CRIADO!")
        print("📁 Localização: dist/executavel_simples/AntiRansomwareShield.bat")
        print("\n🚀 Para usar:")
        print("1. Execute dist/executavel_simples/AntiRansomwareShield.bat")
        print("2. Ou use a versão portável: dist/portable/run.bat")
    else:
        print("❌ Falha ao criar executável")
    
    input("\nPressione Enter para continuar...")
