# 🧙‍♂️ Guia do Instalador Wizard - Anti-Ransomware Shield

## 🎯 Visão Geral

O **Instalador Wizard** é a forma mais profissional e moderna de instalar o Anti-Ransomware Shield. Ele oferece uma experiência de instalação que rivaliza com produtos comerciais.

## ✨ Por que o Instalador Wizard?

### **🎨 Interface Profissional**
- Design moderno e intuitivo
- Navegação com botões Anterior/Próximo
- Barras de progresso em tempo real
- Logs detalhados de instalação

### **🔧 Funcionalidades Avançadas**
- Verificação automática de requisitos
- Configuração flexível de opções
- Instalação automática de dependências
- Configuração completa do sistema

### **📋 Experiência Completa**
- 5 etapas guiadas
- Validação em cada etapa
- Configuração personalizada
- Instalação automática

## 🚀 Como Usar o Instalador Wizard

### **Opção 1: Executar Diretamente**

```bash
# Clone o repositório
git clone https://github.com/[SEU_USUARIO]/Challenge-Fiap.git
cd Challenge-Fiap

# Execute o instalador wizard
python installer/wizard_installer.py
```

### **Opção 2: Criar Executável do Instalador**

```bash
# Cria instalador .exe
python create_wizard_installer.py

# Ou use o script batch
create_wizard.bat
```

### **Opção 3: Usar o Executável**

```bash
# Após criar o executável
dist/AntiRansomwareShield_Installer.exe
```

## 📋 Etapas do Instalador Wizard

### **Etapa 1: Boas-vindas**

#### **O que acontece:**
- Apresentação do programa
- Informações do sistema
- Verificação de requisitos

#### **Informações exibidas:**
```
🛡️ Anti-Ransomware Shield
   Instalador Wizard Profissional

Bem-vindo ao Anti-Ransomware Shield

Este assistente irá guiá-lo através da instalação...

Informações do Sistema:
• Python: 3.11.0
• Espaço livre em C:: 150 GB
• Privilégios: Administrador
```

#### **Verificações automáticas:**
- ✅ Python 3.8+ instalado
- ✅ Espaço em disco suficiente
- ✅ Privilégios de administrador
- ✅ Antivírus não bloqueando

### **Etapa 2: Licença**

#### **O que acontece:**
- Exibição dos termos de licença
- Checkbox de aceite obrigatório
- Área de texto com scroll

#### **Termos de licença:**
```
MIT License

Copyright (c) 2024 Anti-Ransomware Shield

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[Termos completos da licença MIT]
```

#### **Validação:**
- ✅ Checkbox de aceite obrigatório
- ✅ Botão "Próximo" habilitado apenas após aceite
- ✅ Validação automática

### **Etapa 3: Opções de Instalação**

#### **O que acontece:**
- Configuração do diretório de instalação
- Opções adicionais de instalação
- Verificação de requisitos

#### **Configurações disponíveis:**

**Diretório de Instalação:**
- **Padrão**: `C:\AntiRansomware`
- **Personalizável**: Botão "Procurar..."
- **Validação**: Verifica permissões de escrita

**Opções Adicionais:**
- ☑ **Criar atalho na área de trabalho**
- ☑ **Adicionar ao menu iniciar**
- ☑ **Iniciar automaticamente com o Windows**
- ☑ **Configurar regra do firewall**

**Requisitos:**
- **Espaço necessário**: ~50 MB
- **Python 3.8+**: Já instalado
- **Privilégios**: Administrador (recomendado)

### **Etapa 4: Instalação**

#### **O que acontece:**
- Progresso visual em tempo real
- Logs detalhados de cada ação
- Instalação automática de dependências
- Configuração completa do sistema

#### **Progresso da instalação:**
```
Instalando Anti-Ransomware Shield

[████████████████████████████████████] 75%

Log de Instalação:
[14:30:15] Iniciando instalação...
[14:30:16] Criando diretório de instalação...
[14:30:17] Instalando dependências...
[14:30:20] Copiando arquivos do programa...
[14:30:22] Criando atalho na área de trabalho...
[14:30:23] Configurando inicialização automática...
[14:30:24] Configurando regra do firewall...
[14:30:25] Instalação concluída com sucesso!
```

#### **Ações executadas:**
1. **Criação de diretório** de instalação
2. **Instalação de dependências** (psutil, watchdog, etc.)
3. **Cópia de arquivos** do programa
4. **Criação de atalhos** na área de trabalho
5. **Configuração de inicialização** automática
6. **Configuração do firewall** (regras de segurança)
7. **Configuração do registro** (inicialização)

### **Etapa 5: Conclusão**

#### **O que acontece:**
- Confirmação de sucesso
- Instruções de uso
- Opção de executar o programa

#### **Tela de conclusão:**
```
Instalação Concluída com Sucesso!

✅ Anti-Ransomware Shield foi instalado com sucesso!

Localização: C:\AntiRansomware\

Para executar:
1. Clique no atalho da área de trabalho
2. Ou execute: C:\AntiRansomware\AntiRansomwareShield.exe

O programa iniciará automaticamente no próximo boot.

[Executar Agora] [Finalizar]
```

## 🔧 Configurações Avançadas

### **Personalização do Instalador**

#### **Modificar diretório padrão:**
```python
# installer/wizard_installer.py
self.install_path = tk.StringVar(value="C:\\AntiRansomware")
```

#### **Modificar opções padrão:**
```python
# installer/wizard_installer.py
self.create_desktop_shortcut = tk.BooleanVar(value=True)
self.create_start_menu = tk.BooleanVar(value=True)
self.auto_start = tk.BooleanVar(value=True)
self.create_firewall_rule = tk.BooleanVar(value=True)
```

#### **Adicionar novas etapas:**
```python
def show_step(self, step):
    if step == 5:  # Nova etapa
        self.show_custom_step()
    
def show_custom_step(self):
    # Implementar nova etapa
    pass
```

### **Configurações de Instalação**

#### **Diretórios de instalação:**
```python
# Diretórios padrão
install_dirs = [
    "C:\\AntiRansomware",
    "C:\\Program Files\\AntiRansomware",
    "C:\\Users\\%USERNAME%\\AntiRansomware"
]
```

#### **Dependências automáticas:**
```python
# Dependências instaladas automaticamente
dependencies = [
    "psutil",
    "watchdog", 
    "pillow",
    "pywin32",
    "cryptography",
    "requests"
]
```

## 📦 Distribuição

### **Criar Pacote de Distribuição**

#### **Usando PyInstaller:**
```bash
# Cria instalador .exe
python create_wizard_installer.py
```

#### **Usando script batch:**
```bash
# Executa criação automática
create_wizard.bat
```

### **Pacote Completo**

Após executar `create_wizard_installer.py`, você terá:

```
dist/installer_wizard/
├── AntiRansomwareShield_Installer.exe  # Instalador principal
├── src/                                # Código fonte
├── config.json                         # Configuração
├── requirements.txt                    # Dependências
├── README.md                           # Documentação
└── README_Instalador.txt              # Guia do instalador
```

### **Para Distribuir**

1. **Copie a pasta** `dist/installer_wizard/` para o computador de destino
2. **Execute** `AntiRansomwareShield_Installer.exe`
3. **Siga as instruções** do wizard

## 🛡️ Segurança

### **Verificações de Segurança**

#### **Privilégios de administrador:**
- ✅ Verificação automática
- ✅ Aviso se não for administrador
- ✅ Recomendação de execução como admin

#### **Antivírus:**
- ✅ Detecção se está bloqueando
- ✅ Aviso sobre falsos positivos
- ✅ Instruções para exceções

#### **Espaço em disco:**
- ✅ Verificação de espaço disponível
- ✅ Cálculo de espaço necessário
- ✅ Aviso se insuficiente

### **Validações**

#### **Diretório de instalação:**
- ✅ Verifica permissões de escrita
- ✅ Valida caminho válido
- ✅ Cria diretório se necessário

#### **Dependências:**
- ✅ Instala automaticamente se necessário
- ✅ Verifica versões compatíveis
- ✅ Trata erros de instalação

#### **Firewall:**
- ✅ Configura regras de segurança
- ✅ Verifica permissões
- ✅ Testa conectividade

## 🎯 Vantagens sobre Instalação Manual

| Característica | Instalação Manual | Instalador Wizard |
|----------------|-------------------|-------------------|
| **Interface** | Linha de comando | Interface gráfica moderna |
| **Navegação** | Linear | Botões Anterior/Próximo |
| **Progresso** | Básico | Barras de progresso visuais |
| **Logs** | Limitados | Logs detalhados em tempo real |
| **Validação** | Manual | Validação automática |
| **Configuração** | Fixa | Opções flexíveis |
| **Experiência** | Básica | **Profissional** |

## 🚀 Próximos Passos

### **Melhorias Futuras**

#### **Temas:**
- Múltiplos temas visuais
- Personalização de cores
- Ícones personalizados

#### **Idiomas:**
- Suporte a múltiplos idiomas
- Localização completa
- Tradução automática

#### **Atualizações:**
- Sistema de atualização automática
- Verificação de versões
- Download de atualizações

### **Personalização**

#### **Logo personalizado:**
- Substitua o ícone padrão
- Use logo da empresa
- Personalize cores

#### **Textos:**
- Modifique textos e mensagens
- Personalize instruções
- Adicione informações da empresa

#### **Etapas:**
- Adicione ou remova etapas
- Personalize validações
- Configure opções específicas

## 🎉 Conclusão

O **Instalador Wizard** oferece uma experiência de instalação **profissional e moderna**, rivalizando com produtos comerciais:

✅ **Interface gráfica moderna**
✅ **Navegação intuitiva**
✅ **Progresso visual em tempo real**
✅ **Logs detalhados**
✅ **Configuração flexível**
✅ **Validação automática**
✅ **Experiência profissional**

**🎯 Resultado**: Um instalador que rivaliza com produtos comerciais, oferecendo uma experiência de instalação profissional e confiável!

---

**💡 Dica**: Para máxima compatibilidade, execute o instalador como administrador e mantenha o Python atualizado.

**🧙‍♂️ Experimente o Instalador Wizard para uma experiência de instalação profissional!**