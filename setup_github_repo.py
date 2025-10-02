"""
Script para configurar repositório GitHub - Challenge FIAP
Cria estrutura completa do repositório com documentação
"""

import os
import subprocess
import shutil
from pathlib import Path

def create_github_structure():
    """Cria estrutura completa do repositório GitHub"""
    print("🔧 Configurando repositório GitHub - Challenge FIAP")
    print("=" * 60)
    
    # Cria diretórios necessários
    directories = [
        "docs",
        "assets",
        "screenshots",
        "examples",
        "tests"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Diretório criado: {directory}/")
    
    # Cria arquivos de documentação
    create_documentation_files()
    
    # Cria arquivos de configuração
    create_config_files()
    
    # Cria exemplos
    create_examples()
    
    # Cria testes
    create_tests()
    
    print("\n🎉 Estrutura do repositório criada com sucesso!")
    print("=" * 60)

def create_documentation_files():
    """Cria arquivos de documentação"""
    print("\n📚 Criando documentação...")
    
    # CONTRIBUTING.md
    contributing_content = """# 🤝 Guia de Contribuição - Challenge FIAP

## 🎯 Como Contribuir

### **1. Fork do Repositório**
```bash
# Faça fork do repositório
# Clone seu fork
git clone https://github.com/[SEU_USUARIO]/Challenge-Fiap.git
cd Challenge-Fiap
```

### **2. Configurar Ambiente**
```bash
# Crie branch para sua feature
git checkout -b feature/nova-funcionalidade

# Configure ambiente virtual
python -m venv venv
venv\\Scripts\\activate

# Instale dependências
pip install -r requirements.txt
```

### **3. Desenvolvimento**
```bash
# Faça suas alterações
# Teste o código
python test_simple.py

# Execute o programa
python src/main.py
```

### **4. Commit e Push**
```bash
# Adicione suas alterações
git add .

# Faça commit
git commit -m "feat: adiciona nova funcionalidade"

# Push para seu fork
git push origin feature/nova-funcionalidade
```

### **5. Pull Request**
- Abra Pull Request no repositório original
- Descreva suas alterações
- Inclua testes se aplicável
- Aguarde revisão

## 📋 Padrões de Código

### **Python**
- Use PEP 8
- Documente funções e classes
- Adicione type hints
- Escreva testes

### **Commits**
- Use conventional commits
- Exemplos: `feat:`, `fix:`, `docs:`, `test:`
- Seja descritivo

### **Pull Requests**
- Título claro
- Descrição detalhada
- Screenshots se aplicável
- Testes incluídos

## 🧪 Testes

### **Executar Testes**
```bash
# Teste básico
python test_simple.py

# Teste de detecção
python test_ransomware_detection.py

# Teste de ambiente
python test_safe_environment.py
```

### **Criar Novos Testes**
```python
# tests/test_nova_funcionalidade.py
import unittest
from src.core.detector import RansomwareDetector

class TestNovaFuncionalidade(unittest.TestCase):
    def test_exemplo(self):
        detector = RansomwareDetector()
        # Seu teste aqui
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
```

## 📝 Documentação

### **Atualizar Documentação**
- Mantenha README.md atualizado
- Documente novas funcionalidades
- Atualize guias de instalação
- Adicione screenshots

### **Estrutura de Documentação**
```
docs/
├── INSTALLATION.md      # Guia de instalação
├── USER_GUIDE.md        # Manual do usuário
├── TROUBLESHOOTING.md   # Solução de problemas
└── API.md              # Documentação da API
```

## 🐛 Reportar Problemas

### **Como Reportar**
1. **Verifique se já existe** issue similar
2. **Use template** de bug report
3. **Inclua informações**:
   - Sistema operacional
   - Versão do Python
   - Logs de erro
   - Passos para reproduzir

### **Template de Bug Report**
```markdown
## 🐛 Descrição do Bug
[Descrição clara do problema]

## 🔄 Passos para Reproduzir
1. Vá para '...'
2. Clique em '...'
3. Veja erro

## 🎯 Comportamento Esperado
[O que deveria acontecer]

## 📊 Informações do Sistema
- OS: Windows 10/11
- Python: 3.8+
- Versão: 1.0.0

## 📝 Logs
[Logs de erro se aplicável]
```

## ✨ Sugerir Funcionalidades

### **Como Sugerir**
1. **Verifique se já existe** feature request
2. **Use template** de feature request
3. **Descreva detalhadamente**:
   - Problema que resolve
   - Solução proposta
   - Alternativas consideradas

### **Template de Feature Request**
```markdown
## ✨ Descrição da Funcionalidade
[Descrição clara da funcionalidade]

## 🎯 Problema que Resolve
[Problema específico]

## 💡 Solução Proposta
[Solução detalhada]

## 🔄 Alternativas Consideradas
[Outras opções consideradas]

## 📊 Informações Adicionais
[Contexto adicional]
```

## 📞 Suporte

### **Canais de Suporte**
- **GitHub Issues**: Para bugs e features
- **Discussions**: Para discussões gerais
- **Wiki**: Para documentação colaborativa
- **Email**: Para suporte direto

### **Respondendo Issues**
- Seja respeitoso e construtivo
- Forneça soluções quando possível
- Peça mais informações se necessário
- Marque como resolvido quando apropriado

## 🏆 Reconhecimento

### **Contribuidores**
- Lista de contribuidores no README
- Menção em releases
- Badges de contribuição

### **Tipos de Contribuição**
- 🐛 **Bug Reports**: Reportar problemas
- ✨ **Features**: Novas funcionalidades
- 📚 **Documentação**: Melhorar docs
- 🧪 **Testes**: Adicionar testes
- 🔧 **Manutenção**: Melhorias gerais

---

**🤝 Obrigado por contribuir com o Challenge FIAP!**

**💡 Sua contribuição ajuda a tornar o Anti-Ransomware Shield ainda melhor!**
"""
    
    with open("CONTRIBUTING.md", "w", encoding="utf-8") as f:
        f.write(contributing_content)
    print("✅ CONTRIBUTING.md criado")
    
    # CHANGELOG.md
    changelog_content = """# 📝 Changelog - Anti-Ransomware Shield

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.0.0] - 2024-01-XX

### ✨ Adicionado
- Sistema de monitoramento em tempo real
- Detecção inteligente de ransomware
- Proteção automática contra ameaças
- Interface gráfica moderna
- Instalador wizard profissional
- Sistema de honeypots
- Análise comportamental
- Detecção por assinatura
- Proteção de arquivos críticos
- Modo de emergência
- Logs detalhados
- Configurações avançadas
- Suporte a múltiplas famílias de ransomware
- Executáveis portáveis
- Documentação completa

### 🔧 Funcionalidades
- **Monitoramento**: Arquivos, processos, recursos
- **Detecção**: Comportamental, assinatura, honeypots
- **Proteção**: Terminação automática, quarentena, isolamento
- **Interface**: GUI moderna e intuitiva
- **Instalador**: Wizard profissional
- **Logs**: Histórico completo de atividades

### 🛡️ Proteção Contra Ransomware
- **WannaCry**: Detecção por assinatura e comportamento
- **Petya/NotPetya**: Análise de boot e criptografia
- **Locky**: Detecção de extensões e processos
- **Ryuk**: Monitoramento de atividade em massa
- **Sodinokibi (REvil)**: Análise comportamental
- **Maze**: Detecção de honeypots
- **Conti**: Monitoramento de rede
- **DarkSide**: Análise de comandos

### 📚 Documentação
- README.md completo
- Guia de instalação
- Manual do usuário
- Solução de problemas
- Guia do instalador wizard
- Documentação da API
- Exemplos de uso
- Testes automatizados

### 🧪 Testes
- Teste básico de funcionalidade
- Teste de detecção de ransomware
- Teste de ambiente seguro
- Validação de executáveis
- Teste de performance

### 🚀 Executáveis
- Executável simples
- Versão portável
- Instalador wizard
- Arquivo ZIP
- Scripts de instalação

## [0.9.0] - 2024-01-XX (Beta)

### ✨ Adicionado
- Versão beta do sistema
- Funcionalidades básicas
- Interface inicial
- Testes preliminares

### 🔧 Melhorias
- Otimização de performance
- Correção de bugs
- Melhoria da interface
- Documentação inicial

## [0.8.0] - 2024-01-XX (Alpha)

### ✨ Adicionado
- Versão alpha do sistema
- Conceito inicial
- Protótipos básicos
- Estrutura do projeto

### 🔧 Desenvolvimento
- Arquitetura do sistema
- Componentes principais
- Interface básica
- Testes iniciais

---

**📝 Formato do Changelog**

- **✨ Adicionado**: Para novas funcionalidades
- **🔧 Melhorias**: Para mudanças em funcionalidades existentes
- **🐛 Corrigido**: Para correções de bugs
- **🗑️ Removido**: Para funcionalidades removidas
- **🔒 Segurança**: Para correções de segurança
- **📚 Documentação**: Para mudanças na documentação
- **🧪 Testes**: Para mudanças nos testes
- **🚀 Executáveis**: Para mudanças nos executáveis

**💡 Para mais informações sobre versionamento, consulte [SemVer](https://semver.org/lang/pt-BR/)**
"""
    
    with open("CHANGELOG.md", "w", encoding="utf-8") as f:
        f.write(changelog_content)
    print("✅ CHANGELOG.md criado")

def create_config_files():
    """Cria arquivos de configuração"""
    print("\n⚙️ Criando arquivos de configuração...")
    
    # .github/workflows/ci.yml
    os.makedirs(".github/workflows", exist_ok=True)
    
    ci_content = """name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: windows-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.8'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        python test_simple.py
        python test_ransomware_detection.py
    
    - name: Build executable
      run: |
        python create_simple_exe_direct.py
    
    - name: Upload artifacts
      uses: actions/upload-artifact@v3
      with:
        name: executables
        path: dist/
"""
    
    with open(".github/workflows/ci.yml", "w", encoding="utf-8") as f:
        f.write(ci_content)
    print("✅ .github/workflows/ci.yml criado")
    
    # .github/ISSUE_TEMPLATE/bug_report.md
    os.makedirs(".github/ISSUE_TEMPLATE", exist_ok=True)
    
    bug_template = """---
name: 🐛 Bug Report
about: Reportar um problema
title: '[BUG] '
labels: bug
assignees: ''
---

## 🐛 Descrição do Bug
[Descrição clara e concisa do problema]

## 🔄 Passos para Reproduzir
1. Vá para '...'
2. Clique em '...'
3. Veja o erro

## 🎯 Comportamento Esperado
[Descrição clara do que deveria acontecer]

## 📊 Informações do Sistema
- **OS**: [ex: Windows 10, Windows 11]
- **Python**: [ex: 3.8.0, 3.9.0]
- **Versão**: [ex: 1.0.0]
- **Antivírus**: [ex: Windows Defender, Avast]

## 📝 Logs de Erro
```
[Cole aqui os logs de erro]
```

## 📸 Screenshots
[Se aplicável, adicione screenshots]

## 📋 Contexto Adicional
[Qualquer outra informação relevante]
"""
    
    with open(".github/ISSUE_TEMPLATE/bug_report.md", "w", encoding="utf-8") as f:
        f.write(bug_template)
    print("✅ .github/ISSUE_TEMPLATE/bug_report.md criado")
    
    # .github/ISSUE_TEMPLATE/feature_request.md
    feature_template = """---
name: ✨ Feature Request
about: Sugerir uma nova funcionalidade
title: '[FEATURE] '
labels: enhancement
assignees: ''
---

## ✨ Descrição da Funcionalidade
[Descrição clara e concisa da funcionalidade desejada]

## 🎯 Problema que Resolve
[Descrição do problema que esta funcionalidade resolveria]

## 💡 Solução Proposta
[Descrição clara da solução que você gostaria de ver]

## 🔄 Alternativas Consideradas
[Descrição de soluções alternativas que você considerou]

## 📊 Informações Adicionais
[Qualquer contexto adicional sobre a funcionalidade]
"""
    
    with open(".github/ISSUE_TEMPLATE/feature_request.md", "w", encoding="utf-8") as f:
        f.write(feature_template)
    print("✅ .github/ISSUE_TEMPLATE/feature_request.md criado")

def create_examples():
    """Cria exemplos de uso"""
    print("\n📚 Criando exemplos...")
    
    # examples/basic_usage.py
    basic_usage = """#!/usr/bin/env python3
\"\"\"
Exemplo básico de uso do Anti-Ransomware Shield
Demonstra como usar a API do sistema
\"\"\"

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.monitor import AntiRansomwareMonitor
from src.core.detector import RansomwareDetector
from src.core.protector import AntiRansomwareProtector

def main():
    \"\"\"Exemplo básico de uso\"\"\"
    print("🛡️ Anti-Ransomware Shield - Exemplo Básico")
    print("=" * 50)
    
    # Cria instâncias dos componentes
    monitor = AntiRansomwareMonitor()
    detector = RansomwareDetector()
    protector = AntiRansomwareProtector()
    
    # Configura callbacks
    def on_threat_detected(event):
        print(f"🚨 Ameaça detectada: {event}")
        protector.handle_threat(event)
    
    monitor.add_callback(on_threat_detected)
    detector.add_callback(on_threat_detected)
    
    # Inicia monitoramento
    print("🔍 Iniciando monitoramento...")
    monitor.start_monitoring()
    
    # Simula detecção
    print("🧪 Simulando detecção...")
    detector.analyze_event({
        'type': 'suspicious_process',
        'process_name': 'crypto.exe',
        'pid': 1234
    })
    
    print("✅ Exemplo concluído!")
    print("💡 Para uso completo, execute: python src/main.py")

if __name__ == "__main__":
    main()
"""
    
    with open("examples/basic_usage.py", "w", encoding="utf-8") as f:
        f.write(basic_usage)
    print("✅ examples/basic_usage.py criado")
    
    # examples/advanced_config.py
    advanced_config = """#!/usr/bin/env python3
\"\"\"
Exemplo de configuração avançada do Anti-Ransomware Shield
Demonstra como personalizar o sistema
\"\"\"

import json
import os

def create_advanced_config():
    \"\"\"Cria configuração avançada\"\"\"
    config = {
        "monitoring": {
            "enabled": True,
            "scan_interval": 2,
            "directories": [
                "C:\\\\Users\\\\%USERNAME%\\\\Documents",
                "C:\\\\Users\\\\%USERNAME%\\\\Desktop",
                "C:\\\\Users\\\\%USERNAME%\\\\Pictures",
                "C:\\\\Users\\\\%USERNAME%\\\\Videos"
            ],
            "exclusions": [
                "C:\\\\Program Files\\\\",
                "C:\\\\Windows\\\\",
                "C:\\\\ProgramData\\\\",
                "C:\\\\Temp\\\\",
                "C:\\\\Users\\\\%USERNAME%\\\\AppData\\\\"
            ]
        },
        "detection": {
            "sensitivity": "high",
            "behavioral_analysis": True,
            "signature_detection": True,
            "honeypots": True,
            "thresholds": {
                "mass_file_activity": 15,
                "high_cpu_usage": 70,
                "high_memory_usage": 80
            }
        },
        "protection": {
            "auto_quarantine": True,
            "emergency_mode_threshold": 70,
            "block_suspicious_network": True,
            "protect_critical_files": True,
            "terminate_suspicious_processes": True
        },
        "logging": {
            "level": "DEBUG",
            "max_file_size": "5MB",
            "max_files": 3,
            "console_output": True
        },
        "gui": {
            "theme": "dark",
            "language": "pt_BR",
            "auto_start": True,
            "minimize_to_tray": True
        }
    }
    
    # Salva configuração
    with open("config_advanced.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    
    print("✅ Configuração avançada criada: config_advanced.json")
    print("📋 Características:")
    print("   • Sensibilidade alta")
    print("   • Monitoramento expandido")
    print("   • Proteção reforçada")
    print("   • Logs detalhados")
    print("   • Interface escura")

if __name__ == "__main__":
    create_advanced_config()
"""
    
    with open("examples/advanced_config.py", "w", encoding="utf-8") as f:
        f.write(advanced_config)
    print("✅ examples/advanced_config.py criado")

def create_tests():
    """Cria testes adicionais"""
    print("\n🧪 Criando testes...")
    
    # tests/test_integration.py
    integration_test = """#!/usr/bin/env python3
\"\"\"
Teste de integração do Anti-Ransomware Shield
Verifica se todos os componentes funcionam juntos
\"\"\"

import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.monitor import AntiRansomwareMonitor
from src.core.detector import RansomwareDetector
from src.core.protector import AntiRansomwareProtector

class TestIntegration(unittest.TestCase):
    \"\"\"Teste de integração\"\"\"
    
    def setUp(self):
        \"\"\"Configuração inicial\"\"\"
        self.monitor = AntiRansomwareMonitor()
        self.detector = RansomwareDetector()
        self.protector = AntiRansomwareProtector()
        
        self.detected_threats = []
        
        def threat_callback(event):
            self.detected_threats.append(event)
        
        self.monitor.add_callback(threat_callback)
        self.detector.add_callback(threat_callback)
    
    def test_monitor_initialization(self):
        \"\"\"Testa inicialização do monitor\"\"\"
        self.assertIsNotNone(self.monitor)
        self.assertFalse(self.monitor.running)
    
    def test_detector_initialization(self):
        \"\"\"Testa inicialização do detector\"\"\"
        self.assertIsNotNone(self.detector)
    
    def test_protector_initialization(self):
        \"\"\"Testa inicialização do protetor\"\"\"
        self.assertIsNotNone(self.protector)
    
    def test_threat_detection(self):
        \"\"\"Testa detecção de ameaças\"\"\"
        # Simula evento suspeito
        event = {
            'type': 'suspicious_process',
            'process_name': 'crypto.exe',
            'pid': 1234
        }
        
        result = self.detector.analyze_event(event)
        self.assertIsNotNone(result)
    
    def test_callback_system(self):
        \"\"\"Testa sistema de callbacks\"\"\"
        # Simula evento
        event = {'type': 'test_event'}
        self.monitor._handle_event(event)
        
        # Verifica se callback foi chamado
        self.assertEqual(len(self.detected_threats), 1)
        self.assertEqual(self.detected_threats[0], event)

if __name__ == '__main__':
    unittest.main()
"""
    
    with open("tests/test_integration.py", "w", encoding="utf-8") as f:
        f.write(integration_test)
    print("✅ tests/test_integration.py criado")

def create_github_commands():
    """Cria comandos para configurar GitHub"""
    print("\n🚀 Criando comandos para GitHub...")
    
    commands = """# Comandos para configurar repositório GitHub

# 1. Inicializar repositório local
git init
git add .
git commit -m "feat: initial commit - Anti-Ransomware Shield"

# 2. Criar repositório no GitHub
# Vá para https://github.com/new
# Nome: Challenge-Fiap
# Descrição: Anti-Ransomware Shield - Ferramenta de proteção contra ransomware
# Público/Privado: Escolha conforme necessário

# 3. Conectar repositório local ao GitHub
git remote add origin https://github.com/[SEU_USUARIO]/Challenge-Fiap.git
git branch -M main
git push -u origin main

# 4. Configurar branch de desenvolvimento
git checkout -b develop
git push -u origin develop

# 5. Criar tags para releases
git tag -a v1.0.0 -m "Release v1.0.0 - Anti-Ransomware Shield"
git push origin v1.0.0

# 6. Configurar GitHub Pages (opcional)
# Vá para Settings > Pages
# Source: Deploy from a branch
# Branch: main
# Folder: / (root)

# 7. Configurar proteção de branches
# Vá para Settings > Branches
# Adicione regra para branch main
# Require pull request reviews before merging
# Require status checks to pass before merging

# 8. Configurar secrets para CI/CD (se necessário)
# Vá para Settings > Secrets and variables > Actions
# Adicione secrets necessários
"""
    
    with open("GITHUB_SETUP.md", "w", encoding="utf-8") as f:
        f.write(commands)
    print("✅ GITHUB_SETUP.md criado")

def main():
    """Função principal"""
    print("🔧 Configurando repositório GitHub - Challenge FIAP")
    print("=" * 60)
    
    # Cria estrutura completa
    create_github_structure()
    
    # Cria comandos para GitHub
    create_github_commands()
    
    print("\n🎉 REPOSITÓRIO GITHUB CONFIGURADO!")
    print("=" * 60)
    print()
    print("📁 Estrutura criada:")
    print("   • docs/ - Documentação completa")
    print("   • examples/ - Exemplos de uso")
    print("   • tests/ - Testes adicionais")
    print("   • .github/ - Configurações do GitHub")
    print("   • Arquivos de configuração")
    print()
    print("🚀 Próximos passos:")
    print("   1. Execute: git init")
    print("   2. Adicione arquivos: git add .")
    print("   3. Commit inicial: git commit -m 'feat: initial commit'")
    print("   4. Crie repositório no GitHub")
    print("   5. Conecte: git remote add origin [URL]")
    print("   6. Push: git push -u origin main")
    print()
    print("📚 Documentação incluída:")
    print("   • README.md - Visão geral completa")
    print("   • docs/INSTALLATION.md - Guia de instalação")
    print("   • docs/USER_GUIDE.md - Manual do usuário")
    print("   • docs/TROUBLESHOOTING.md - Solução de problemas")
    print("   • WIZARD_INSTALLER_GUIDE.md - Guia do instalador wizard")
    print()
    print("🧙‍♂️ Destaque para o Instalador Wizard:")
    print("   • Interface gráfica moderna")
    print("   • 5 etapas guiadas")
    print("   • Validação automática")
    print("   • Configuração flexível")
    print("   • Experiência profissional")
    print()
    print("💡 Consulte GITHUB_SETUP.md para comandos detalhados!")

if __name__ == "__main__":
    main()
