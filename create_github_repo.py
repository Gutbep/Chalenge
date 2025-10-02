"""
Script para criar repositório GitHub automaticamente
Usa GitHub API para criar repositório e fazer push
"""

import requests
import json
import subprocess
import os
import sys

def get_github_token():
    """Obtém token do GitHub (se configurado)"""
    try:
        # Tenta obter token do git config
        result = subprocess.run(['git', 'config', '--global', 'github.token'], 
                              capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except:
        pass
    
    # Se não encontrar, pede para o usuário
    print("🔑 Para criar repositório automaticamente, você precisa de um token do GitHub:")
    print("1. Vá para https://github.com/settings/tokens")
    print("2. Clique em 'Generate new token'")
    print("3. Selecione 'repo' para permissões")
    print("4. Copie o token gerado")
    print()
    
    token = input("Digite seu token do GitHub (ou pressione Enter para pular): ").strip()
    return token if token else None

def create_github_repo(token, repo_name, description, is_private=False):
    """Cria repositório no GitHub usando API"""
    if not token:
        print("❌ Token não fornecido. Pulando criação automática.")
        return None
    
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    data = {
        "name": repo_name,
        "description": description,
        "private": is_private,
        "auto_init": False,
        "gitignore_template": "Python"
    }
    
    try:
        print(f"🚀 Criando repositório '{repo_name}' no GitHub...")
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 201:
            repo_data = response.json()
            print(f"✅ Repositório criado com sucesso!")
            print(f"📁 URL: {repo_data['html_url']")
            print(f"🔗 Clone URL: {repo_data['clone_url']}")
            return repo_data['clone_url']
        else:
            print(f"❌ Erro ao criar repositório: {response.status_code}")
            print(f"📝 Resposta: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
        return None

def setup_git_remote(repo_url):
    """Configura remote do Git"""
    if not repo_url:
        print("❌ URL do repositório não disponível")
        return False
    
    try:
        print(f"🔗 Configurando remote origin...")
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

def main():
    """Função principal"""
    print("🚀 Criando Repositório GitHub - Challenge FIAP")
    print("="*60)
    print()
    
    # Configurações do repositório
    repo_name = "Challenge-Fiap"
    description = "Anti-Ransomware Shield - Ferramenta de proteção contra ransomware"
    
    print(f"📁 Nome do repositório: {repo_name}")
    print(f"📝 Descrição: {description}")
    print()
    
    # Tenta obter token do GitHub
    token = get_github_token()
    
    if token:
        # Cria repositório automaticamente
        repo_url = create_github_repo(token, repo_name, description, is_private=False)
        
        if repo_url:
            # Configura remote
            if setup_git_remote(repo_url):
                # Faz push
                if push_to_github():
                    print("\n🎉 REPOSITÓRIO GITHUB CRIADO COM SUCESSO!")
                    print("="*60)
                    print(f"🌐 URL: https://github.com/[SEU_USUARIO]/{repo_name}")
                    print("📁 Repositório configurado e sincronizado!")
                    return True
    
    # Se não conseguiu criar automaticamente, mostra instruções manuais
    create_github_repo_manual()
    
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
