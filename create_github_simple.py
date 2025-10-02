"""
Script simples para criar repositório GitHub
"""

import subprocess
import sys

def create_github_repo_manual():
    """Instruções para criação manual"""
    print("\n" + "="*60)
    print("📋 INSTRUÇÕES PARA CRIAÇÃO MANUAL DO REPOSITÓRIO")
    print("="*60)
    print()
    print("1. 🌐 Vá para https://github.com/new")
    print("2. 📝 Preencha os dados:")
    print("   • Repository name: Challenge-Fiap")
    print("   • Description: Anti-Ransomware Shield - Ferramenta de proteção contra ransomware")
    print("   • Visibility: Public (ou Private se preferir)")
    print("   • NÃO marque 'Add a README file' (já temos)")
    print("   • NÃO marque 'Add .gitignore' (já temos)")
    print("   • NÃO marque 'Choose a license' (já temos)")
    print("3. 🎯 Clique em 'Create repository'")
    print("4. 📋 Copie a URL do repositório criado")
    print("5. 🔗 Execute os comandos abaixo:")
    print()
    print("git remote add origin [URL_DO_SEU_REPOSITORIO]")
    print("git branch -M main")
    print("git push -u origin main")
    print("git checkout -b develop")
    print("git push -u origin develop")
    print()

def setup_git_remote():
    """Configura remote do Git"""
    print("🔗 Configurando remote origin...")
    print("Digite a URL do seu repositório GitHub:")
    print("Exemplo: https://github.com/[SEU_USUARIO]/Challenge-Fiap.git")
    
    repo_url = input("URL do repositório: ").strip()
    
    if not repo_url:
        print("❌ URL não fornecida")
        return False
    
    try:
        subprocess.run(['git', 'remote', 'add', 'origin', repo_url], check=True)
        print("✅ Remote configurado!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao configurar remote: {e}")
        return False

def push_to_github():
    """Faz push para o GitHub"""
    try:
        print("📤 Fazendo push para o GitHub...")
        
        # Push da branch main
        subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True)
        print("✅ Push da branch main realizado!")
        
        # Cria e push da branch develop
        subprocess.run(['git', 'checkout', '-b', 'develop'], check=True)
        subprocess.run(['git', 'push', '-u', 'origin', 'develop'], check=True)
        print("✅ Branch develop criada e enviada!")
        
        # Volta para main
        subprocess.run(['git', 'checkout', 'main'], check=True)
        print("✅ Voltou para branch main")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro no push: {e}")
        return False

def main():
    """Função principal"""
    print("🚀 Criando Repositório GitHub - Challenge FIAP")
    print("="*60)
    print()
    
    print("📁 Nome do repositório: Challenge-Fiap")
    print("📝 Descrição: Anti-Ransomware Shield - Ferramenta de proteção contra ransomware")
    print()
    
    # Mostra instruções
    create_github_repo_manual()
    
    # Pergunta se quer configurar remote
    config_remote = input("Deseja configurar o remote agora? (s/n): ").strip().lower()
    
    if config_remote in ['s', 'sim', 'y', 'yes']:
        if setup_git_remote():
            push_now = input("Deseja fazer push agora? (s/n): ").strip().lower()
            if push_now in ['s', 'sim', 'y', 'yes']:
                if push_to_github():
                    print("\n🎉 REPOSITÓRIO GITHUB CONFIGURADO COM SUCESSO!")
                    print("="*60)
                    print("📁 Repositório configurado e sincronizado!")
                    return True
    
    print("\n💡 Alternativa: Use GitHub CLI se disponível")
    print("   gh repo create Challenge-Fiap --public --description 'Anti-Ransomware Shield'")
    print("   git remote add origin https://github.com/[SEU_USUARIO]/Challenge-Fiap.git")
    print("   git push -u origin main")
    
    return False

if __name__ == "__main__":
    try:
        success = main()
        if success:
            print("\n✅ Repositório criado e configurado automaticamente!")
        else:
            print("\n📋 Siga as instruções manuais acima para criar o repositório.")
    except KeyboardInterrupt:
        print("\n❌ Operação cancelada pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
    
    input("\nPressione Enter para continuar...")
