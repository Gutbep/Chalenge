# 📦 Guia de Instalação - Anti-Ransomware Shield

## 🎯 Visão Geral

Este guia apresenta **múltiplas opções de instalação** para o Anti-Ransomware Shield, desde instalação manual até o **Instalador Wizard profissional**.

## 🧙‍♂️ Instalador Wizard (Recomendado)

### **Por que o Instalador Wizard?**

O instalador wizard oferece uma experiência de instalação **profissional e moderna**:

- ✅ **Interface Gráfica**: Design moderno e intuitivo
- ✅ **Verificação Automática**: Checa requisitos do sistema
- ✅ **Configuração Flexível**: Opções personalizáveis
- ✅ **Instalação Automática**: Dependências e configurações
- ✅ **Logs Detalhados**: Acompanhe cada etapa

### **🚀 Como Usar o Instalador Wizard**

#### **Opção 1: Executar Diretamente**
```bash
# Clone o repositório
git clone https://github.com/[SEU_USUARIO]/Challenge-Fiap.git
cd Challenge-Fiap

# Execute o instalador wizard
python installer/wizard_installer.py
```

#### **Opção 2: Criar Executável do Instalador**
```bash
# Cria instalador .exe
python create_wizard_installer.py

# Ou use o script batch
create_wizard.bat
```

#### **Opção 3: Usar o Executável**
```bash
# Após criar o executável
dist/AntiRansomwareShield_Installer.exe
```

### **📋 Etapas do Instalador Wizard**

#### **Etapa 1: Boas-vindas**
- Apresentação do programa
- Informações do sistema
- Verificação de requisitos

#### **Etapa 2: Licença**
- Termos de licença MIT
- Checkbox de aceite obrigatório
- Área de texto com scroll

#### **Etapa 3: Opções de Instalação**
- **Diretório de instalação** (padrão: C:\AntiRansomware)
- **Atalho na área de trabalho** ✅
- **Menu iniciar** ✅
- **Inicialização automática** ✅
- **Regra do firewall** ✅

#### **Etapa 4: Instalação**
- Progresso visual em tempo real
- Logs detalhados de cada ação
- Instalação de dependências
- Cópia de arquivos
- Configuração de atalhos
- Configuração do firewall

#### **Etapa 5: Conclusão**
- Confirmação de sucesso
- Instruções de uso
- Opção de executar o programa

## 📦 Instalação Manual

### **Pré-requisitos**

- **Python 3.8+**: [Download](https://www.python.org/downloads/)
- **Windows 10/11**: Sistema operacional
- **Privilégios de Administrador**: Recomendado

### **Passo a Passo**

#### **1. Clone o Repositório**
```bash
git clone https://github.com/[SEU_USUARIO]/Challenge-Fiap.git
cd Challenge-Fiap
```

#### **2. Crie Ambiente Virtual**
```bash
python -m venv venv
venv\Scripts\activate
```

#### **3. Instale Dependências**
```bash
pip install -r requirements.txt
```

#### **4. Execute o Programa**
```bash
# Modo GUI (padrão)
python src/main.py

# Modo Console
python src/main.py --console
```

## 🚀 Executáveis Prontos

### **Executável Simples (Recomendado)**

```bash
# Navegue até a pasta
cd dist/executavel_simples

# Execute o arquivo
AntiRansomwareShield.bat
```

**Características:**
- ✅ Verifica Python automaticamente
- ✅ Instala dependências automaticamente
- ✅ Interface gráfica completa
- ✅ Todas as funcionalidades incluídas

### **Versão Portável**

```bash
# Navegue até a pasta
cd dist/portable

# Execute o arquivo
run.bat

# Ou para instalação completa
install.bat
```

**Características:**
- ✅ Inclui todas as dependências
- ✅ Não precisa de instalação
- ✅ Pode ser executado de qualquer lugar
- ✅ Fácil de distribuir

### **Arquivo ZIP**

```bash
# Extraia o arquivo
dist/AntiRansomwareShield_Portavel.zip

# Execute
run.bat
```

## 🔧 Configuração Avançada

### **Arquivo de Configuração**

Edite `config.json` para personalizar:

```json
{
    "monitoring": {
        "enabled": true,
        "scan_interval": 1,
        "directories": [
            "C:\\Users\\%USERNAME%\\Documents",
            "C:\\Users\\%USERNAME%\\Desktop",
            "C:\\Users\\%USERNAME%\\Pictures"
        ],
        "exclusions": [
            "C:\\Program Files\\",
            "C:\\Windows\\",
            "C:\\ProgramData\\"
        ]
    },
    "detection": {
        "sensitivity": "medium",
        "behavioral_analysis": true,
        "signature_detection": true,
        "honeypots": true,
        "thresholds": {
            "mass_file_activity": 20,
            "high_cpu_usage": 80,
            "high_memory_usage": 100
        }
    },
    "protection": {
        "auto_quarantine": true,
        "emergency_mode_threshold": 80,
        "block_suspicious_network": true,
        "protect_critical_files": true,
        "terminate_suspicious_processes": true
    }
}
```

### **Diretórios Monitorados**

Por padrão, o sistema monitora:

- **Documentos**: `C:\Users\[Usuário]\Documents`
- **Desktop**: `C:\Users\[Usuário]\Desktop`
- **Imagens**: `C:\Users\[Usuário]\Pictures`
- **Público**: `C:\Users\Public`

### **Exclusões**

Diretórios excluídos do monitoramento:

- **Sistema**: `C:\Windows\`
- **Programas**: `C:\Program Files\`
- **Dados**: `C:\ProgramData\`

## 🛠️ Solução de Problemas

### **Python não encontrado**

**Problema**: `'python' não é reconhecido como comando interno`

**Solução**:
1. Instale Python 3.8+ do [site oficial](https://www.python.org/downloads/)
2. Durante a instalação, marque "Add Python to PATH"
3. Reinicie o terminal
4. Verifique: `python --version`

### **Erro de dependências**

**Problema**: `ModuleNotFoundError: No module named 'psutil'`

**Solução**:
```bash
pip install -r requirements.txt
```

### **Erro de permissão**

**Problema**: `PermissionError: [WinError 5] Acesso negado`

**Solução**:
1. Execute como administrador
2. Clique direito > "Executar como administrador"

### **Antivírus bloqueando**

**Problema**: Antivírus detecta como falso positivo

**Solução**:
1. Adicione exceção no antivírus
2. Adicione pasta do projeto às exceções
3. Desative temporariamente para teste

## 📊 Verificação da Instalação

### **Teste Básico**

```bash
# Execute o programa
python src/main.py

# Verifique se a interface abre
# Verifique se o monitoramento está ativo
# Verifique se os logs são gerados
```

### **Teste de Funcionalidades**

```bash
# Teste de detecção
python test_ransomware_detection.py

# Teste de ambiente seguro
python test_safe_environment.py
```

### **Verificação de Logs**

```bash
# Verifique os logs
type logs\antiransomware.log

# Verifique se há erros
findstr "ERROR" logs\antiransomware.log
```

## 🎯 Próximos Passos

Após a instalação:

1. **Configure o programa** através da interface
2. **Teste as funcionalidades** com arquivos de teste
3. **Configure exclusões** se necessário
4. **Monitore os logs** para verificar funcionamento
5. **Configure inicialização automática** se desejado

## 📞 Suporte

Para suporte adicional:

- 📖 [Manual do Usuário](USER_GUIDE.md)
- 🔧 [Solução de Problemas](TROUBLESHOOTING.md)
- 🧙‍♂️ [Guia do Instalador Wizard](WIZARD_INSTALLER_GUIDE.md)
- 🐛 [Reportar Problemas](https://github.com/[SEU_USUARIO]/Challenge-Fiap/issues)

---

**🛡️ Proteja seu sistema com o Anti-Ransomware Shield!**

**🧙‍♂️ Use o Instalador Wizard para uma experiência de instalação profissional!**