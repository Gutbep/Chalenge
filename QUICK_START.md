# ⚡ Guia de Início Rápido - Anti-Ransomware Shield

## 🚀 Instalação em 3 Passos

### Passo 1: Verificar Pré-requisitos
```bash
# Verifica se Python está instalado
python --version

# Se não estiver instalado, baixe de:
# https://www.python.org/downloads/
```

### Passo 2: Instalar o Programa
```bash
# Opção A: Instalação automática (recomendada)
install.bat

# Opção B: Instalação manual
pip install -r requirements.txt
python src/main.py
```

### Passo 3: Executar
```bash
# Clique no atalho da área de trabalho
# OU execute:
C:\AntiRansomware\run.bat
```

## 🎯 Primeiro Uso

### 1. Abrir o Programa
- **Clique no atalho** "Anti-Ransomware Shield" na área de trabalho
- **Aguarde a inicialização** (pode levar alguns segundos)

### 2. Ativar Proteção
- **Clique em "▶️ Iniciar Proteção"**
- **Aguarde a confirmação** (status muda para "✅ Ativo")
- **O sistema começará a monitorar** automaticamente

### 3. Verificar Status
- **Status Verde**: Sistema seguro
- **Status Amarelo**: Atenção necessária  
- **Status Vermelho**: Ameaça detectada

## 🛡️ Funcionalidades Principais

### Monitoramento Automático
- ✅ **Arquivos**: Detecta modificações suspeitas
- ✅ **Processos**: Monitora programas em execução
- ✅ **Rede**: Bloqueia conexões suspeitas
- ✅ **Sistema**: Protege arquivos críticos

### Detecção Inteligente
- 🔍 **Comportamental**: Padrões suspeitos de ransomware
- 🔍 **Assinatura**: Nomes e extensões conhecidas
- 🔍 **Honeypots**: Arquivos isca para detecção
- 🔍 **Recursos**: Uso excessivo de CPU/memória

### Proteção Automática
- 🛡️ **Terminação**: Para processos maliciosos
- 🛡️ **Quarentena**: Isola arquivos suspeitos
- 🛡️ **Isolamento**: Bloqueia rede em emergência
- 🛡️ **Backup**: Protege arquivos importantes

## ⚙️ Configurações Básicas

### Acessar Configurações
1. **Clique em "⚙️ Configurações"**
2. **Navegue pelas abas**:
   - **Geral**: Configurações básicas
   - **Proteção**: Níveis de detecção
   - **Monitoramento**: Diretórios monitorados

### Configurações Recomendadas
```json
{
  "detection": {
    "sensitivity": "medium"  // low, medium, high
  },
  "monitoring": {
    "directories": [
      "C:\\Users\\%USERNAME%\\Documents",
      "C:\\Users\\%USERNAME%\\Desktop"
    ]
  }
}
```

## 🧪 Teste Rápido

### Verificar se Está Funcionando
```bash
# Execute o teste
python test_simple.py

# Deve mostrar: "🎉 Sistema pronto para uso!"
```

### Simular Detecção
1. **Crie um arquivo** com extensão suspeita:
   ```bash
   echo "teste" > documento.encrypted
   ```

2. **Observe o sistema** detectar e alertar

3. **Verifique os logs** na interface

## 🚨 Modo de Emergência

### Ativação Manual
- **Clique em "🚨 Modo Emergência"**
- **Confirme a ativação**
- **Sistema isolará** automaticamente

### Ativação Automática
- **Ocorre quando**:
  - Ransomware conhecido detectado
  - Atividade suspeita em massa
  - Honeypots comprometidos
  - Comandos maliciosos executados

## 📊 Interface Principal

### Painel de Status
- **🟢 Verde**: Sistema seguro
- **🟡 Amarelo**: Atenção
- **🔴 Vermelho**: Ameaça
- **⚫ Preto**: Desligado

### Métricas em Tempo Real
- **CPU**: Uso do processador
- **Memória**: Uso de RAM
- **Rede**: Status da conexão
- **Processos**: Lista de programas

### Logs de Atividade
- **INFO**: Informações gerais
- **WARNING**: Avisos importantes
- **ERROR**: Erros do sistema
- **THREAT**: Ameaças detectadas

## 🔧 Solução de Problemas Rápidos

### "Programa não inicia"
```bash
# Execute como administrador
# Ou use: python src/main.py
```

### "Muitos falsos positivos"
```bash
# Reduza sensibilidade nas configurações
# Adicione exceções para programas legítimos
```

### "Alto uso de CPU"
```bash
# Aumente intervalo de monitoramento
# Exclua diretórios desnecessários
```

### "Antivírus bloqueando"
```bash
# Adicione exceção no antivírus
# Caminho: C:\AntiRansomware\
```

## 📞 Suporte

### Problemas Comuns
- **Documentação**: [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **Guia Completo**: [USER_GUIDE.md](docs/USER_GUIDE.md)
- **Instalação**: [INSTALLATION.md](docs/INSTALLATION.md)

### Contato
- **GitHub Issues**: [Abrir issue](../../issues)
- **Email**: suporte@antiransomware.com

## 🎯 Próximos Passos

### 1. Configuração Avançada
- Ajuste sensibilidade de detecção
- Configure diretórios monitorados
- Defina exceções personalizadas

### 2. Monitoramento Contínuo
- Mantenha o programa sempre ativo
- Configure inicialização automática
- Monitore logs regularmente

### 3. Backup e Segurança
- Faça backups regulares
- Mantenha o programa atualizado
- Use senhas fortes

---

**🎉 Parabéns!** Seu sistema está protegido contra ransomware!

**💡 Dica**: Para máxima proteção, mantenha o programa sempre ativo e faça backups regulares dos seus dados importantes.
