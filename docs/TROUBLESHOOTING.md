# 🔧 Solução de Problemas - Anti-Ransomware Shield

## 🎯 Visão Geral

Este guia apresenta soluções para os problemas mais comuns encontrados ao usar o Anti-Ransomware Shield.

## 🚨 Problemas Críticos

### **Programa não inicia**

#### **Sintomas**
- Erro ao executar o programa
- Janela fecha imediatamente
- Mensagem de erro no terminal

#### **Soluções**

**1. Python não encontrado**
```bash
# Erro: 'python' não é reconhecido como comando interno
# Solução:
# 1. Instale Python 3.8+ do site oficial
# 2. Durante a instalação, marque "Add Python to PATH"
# 3. Reinicie o terminal
# 4. Verifique: python --version
```

**2. Dependências não instaladas**
```bash
# Erro: ModuleNotFoundError: No module named 'psutil'
# Solução:
pip install -r requirements.txt
```

**3. Erro de permissão**
```bash
# Erro: PermissionError: [WinError 5] Acesso negado
# Solução:
# 1. Execute como administrador
# 2. Clique direito > "Executar como administrador"
```

### **Interface não abre**

#### **Sintomas**
- Programa inicia mas interface não aparece
- Erro de tkinter
- Janela não responde

#### **Soluções**

**1. Erro de tkinter**
```bash
# Erro: ModuleNotFoundError: No module named 'tkinter'
# Solução:
# 1. Reinstale Python com tkinter
# 2. Ou instale: pip install tk
```

**2. Interface travada**
```bash
# Solução:
# 1. Feche o programa
# 2. Execute: python src/main.py --console
# 3. Verifique os logs
```

## ⚠️ Problemas de Funcionamento

### **Monitoramento não funciona**

#### **Sintomas**
- Arquivos não são monitorados
- Processos não aparecem na lista
- Logs vazios

#### **Soluções**

**1. Diretórios não existem**
```bash
# Verifique se os diretórios existem:
# C:\Users\[Usuário]\Documents
# C:\Users\[Usuário]\Desktop
# C:\Users\[Usuário]\Pictures
```

**2. Permissões insuficientes**
```bash
# Solução:
# 1. Execute como administrador
# 2. Verifique permissões dos diretórios
# 3. Configure exclusões se necessário
```

**3. Configuração incorreta**
```json
# Verifique config.json:
{
    "monitoring": {
        "enabled": true,
        "directories": [
            "C:\\Users\\%USERNAME%\\Documents"
        ]
    }
}
```

### **Detecção falsa**

#### **Sintomas**
- Alertas desnecessários
- Processos normais marcados como suspeitos
- Sistema lento

#### **Soluções**

**1. Ajustar sensibilidade**
```json
# config.json
{
    "detection": {
        "sensitivity": "low",  // ou "medium", "high"
        "thresholds": {
            "mass_file_activity": 50,  // aumentar limite
            "high_cpu_usage": 90,      // aumentar limite
            "high_memory_usage": 200   // aumentar limite
        }
    }
}
```

**2. Configurar exclusões**
```json
# config.json
{
    "monitoring": {
        "exclusions": [
            "C:\\Program Files\\",
            "C:\\Windows\\",
            "C:\\ProgramData\\",
            "C:\\Temp\\"
        ]
    }
}
```

**3. Ajustar análise comportamental**
```json
# config.json
{
    "detection": {
        "behavioral_analysis": false,  // desativar se necessário
        "signature_detection": true,
        "honeypots": true
    }
}
```

## 🐛 Problemas de Performance

### **Sistema lento**

#### **Sintomas**
- CPU alta
- Memória alta
- Interface travada
- Sistema lento

#### **Soluções**

**1. Ajustar intervalo de verificação**
```json
# config.json
{
    "monitoring": {
        "scan_interval": 5  // aumentar para 5 segundos
    }
}
```

**2. Reduzir diretórios monitorados**
```json
# config.json
{
    "monitoring": {
        "directories": [
            "C:\\Users\\%USERNAME%\\Documents"  // apenas documentos
        ]
    }
}
```

**3. Configurar exclusões**
```json
# config.json
{
    "monitoring": {
        "exclusions": [
            "C:\\Program Files\\",
            "C:\\Windows\\",
            "C:\\ProgramData\\",
            "C:\\Temp\\",
            "C:\\Users\\%USERNAME%\\AppData\\"
        ]
    }
}
```

### **Alto uso de recursos**

#### **Sintomas**
- CPU > 50%
- Memória > 500MB
- Sistema travado

#### **Soluções**

**1. Otimizar configurações**
```json
# config.json
{
    "monitoring": {
        "scan_interval": 10,  // verificar a cada 10 segundos
        "directories": [
            "C:\\Users\\%USERNAME%\\Documents"  // apenas documentos
        ]
    },
    "detection": {
        "behavioral_analysis": false,  // desativar análise comportamental
        "honeypots": false             // desativar honeypots
    }
}
```

**2. Limitar processos monitorados**
```python
# No código, limite o número de processos
# Máximo 20 processos para performance
```

**3. Usar modo console**
```bash
# Execute em modo console para menor uso de recursos
python src/main.py --console
```

## 🔒 Problemas de Segurança

### **Antivírus bloqueando**

#### **Sintomas**
- Antivírus detecta como malware
- Programa não executa
- Arquivos deletados

#### **Soluções**

**1. Adicionar exceção**
```
# No antivírus:
# 1. Adicione exceção para a pasta do projeto
# 2. Adicione exceção para python.exe
# 3. Adicione exceção para o executável
```

**2. Desativar temporariamente**
```
# Para teste:
# 1. Desative o antivírus temporariamente
# 2. Execute o programa
# 3. Reative o antivírus
# 4. Adicione exceções
```

**3. Verificar assinatura**
```
# Se possível:
# 1. Assine o executável
# 2. Use certificado digital
# 3. Submeta para análise do antivírus
```

### **Firewall bloqueando**

#### **Sintomas**
- Conexões bloqueadas
- Funcionalidades de rede não funcionam
- Erro de permissão de rede

#### **Soluções**

**1. Configurar firewall**
```bash
# Adicione regra no firewall:
netsh advfirewall firewall add rule name="Anti-Ransomware Shield" dir=in action=allow program="C:\AntiRansomware\AntiRansomwareShield.exe" enable=yes
```

**2. Permitir na interface**
```
# No Windows Defender:
# 1. Abra Windows Defender
# 2. Firewall e proteção de rede
# 3. Permitir um aplicativo pelo firewall
# 4. Adicione o programa
```

## 📊 Problemas de Logs

### **Logs não são gerados**

#### **Sintomas**
- Pasta logs vazia
- Arquivo de log não existe
- Erro ao escrever logs

#### **Soluções**

**1. Verificar permissões**
```bash
# Verifique se a pasta logs existe e tem permissão de escrita
mkdir logs
chmod 755 logs
```

**2. Verificar configuração**
```json
# config.json
{
    "logging": {
        "level": "INFO",
        "max_file_size": "10MB",
        "max_files": 5,
        "console_output": true
    }
}
```

**3. Verificar espaço em disco**
```bash
# Verifique se há espaço suficiente
dir C:\
```

### **Logs muito grandes**

#### **Sintomas**
- Arquivo de log muito grande
- Sistema lento
- Disco cheio

#### **Soluções**

**1. Configurar rotação**
```json
# config.json
{
    "logging": {
        "max_file_size": "5MB",  # reduzir tamanho
        "max_files": 3           # reduzir número de arquivos
    }
}
```

**2. Limpar logs antigos**
```bash
# Remover logs antigos
del logs\*.log
```

**3. Ajustar nível de log**
```json
# config.json
{
    "logging": {
        "level": "WARNING"  # apenas avisos e erros
    }
}
```

## 🎯 Problemas Específicos

### **Instalador Wizard não funciona**

#### **Sintomas**
- Instalador não abre
- Erro ao executar
- Interface não aparece

#### **Soluções**

**1. Verificar Python**
```bash
python --version
# Deve ser 3.8+
```

**2. Instalar dependências**
```bash
pip install tkinter psutil watchdog pillow
```

**3. Executar diretamente**
```bash
python installer/wizard_installer.py
```

### **Executável não funciona**

#### **Sintomas**
- Executável não abre
- Erro ao executar
- Dependências não encontradas

#### **Soluções**

**1. Usar versão portável**
```bash
cd dist/portable
run.bat
```

**2. Instalar dependências**
```bash
pip install -r requirements.txt
```

**3. Executar código fonte**
```bash
python src/main.py
```

## 🔍 Diagnóstico Avançado

### **Verificação de Sistema**

```bash
# Verificar Python
python --version

# Verificar dependências
pip list

# Verificar permissões
whoami

# Verificar espaço em disco
dir C:\
```

### **Logs de Diagnóstico**

```bash
# Verificar logs
type logs\antiransomware.log

# Filtrar erros
findstr "ERROR" logs\antiransomware.log

# Filtrar avisos
findstr "WARNING" logs\antiransomware.log
```

### **Teste de Funcionalidades**

```bash
# Teste básico
python test_simple.py

# Teste de detecção
python test_ransomware_detection.py

# Teste de ambiente
python test_safe_environment.py
```

## 📞 Suporte Adicional

### **Recursos de Ajuda**

- 📖 [Guia de Instalação](INSTALLATION.md)
- 👤 [Manual do Usuário](USER_GUIDE.md)
- 🧙‍♂️ [Instalador Wizard](WIZARD_INSTALLER_GUIDE.md)

### **Reportar Problemas**

Para reportar problemas:

1. **Colete informações**:
   - Versão do Python
   - Sistema operacional
   - Logs de erro
   - Configuração atual

2. **Crie um issue** no GitHub:
   - Título descritivo
   - Descrição detalhada
   - Logs de erro
   - Passos para reproduzir

3. **Inclua arquivos**:
   - `config.json`
   - `logs/antiransomware.log`
   - Screenshots se aplicável

### **Contato**

- **GitHub Issues**: [Reportar Problemas](https://github.com/[SEU_USUARIO]/Challenge-Fiap/issues)
- **Documentação**: Consulte os guias
- **Logs**: Envie logs de erro
- **Configuração**: Compartilhe configurações

---

**🔧 Use este guia para resolver problemas comuns!**

**💡 Se o problema persistir, reporte com logs detalhados!**
