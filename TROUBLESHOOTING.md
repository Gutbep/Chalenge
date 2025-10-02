# 🔧 Solução de Problemas - Anti-Ransomware Shield

## ❌ Problemas Comuns e Soluções

### 1. "Python não encontrado"
**Erro**: `'python' não é reconhecido como comando interno ou externo`

**Solução**:
```bash
# 1. Instale Python 3.8+ do site oficial
# https://www.python.org/downloads/

# 2. Durante a instalação, marque "Add Python to PATH"

# 3. Reinicie o terminal e teste:
python --version
```

### 2. "Módulo não encontrado"
**Erro**: `ModuleNotFoundError: No module named 'psutil'`

**Solução**:
```bash
# Instale as dependências
pip install -r requirements.txt

# Ou instale manualmente
pip install psutil watchdog pillow pywin32 cryptography requests
```

### 3. "Erro de permissão"
**Erro**: `PermissionError: [WinError 5] Acesso negado`

**Solução**:
```bash
# Execute como administrador
# Clique direito no terminal > "Executar como administrador"

# Ou use o instalador
install.bat
```

### 4. "Interface não abre"
**Erro**: Interface gráfica não carrega

**Solução**:
```bash
# Teste se tkinter funciona
python -c "import tkinter; print('OK')"

# Se não funcionar, reinstale Python com tkinter
# Ou execute em modo console:
python src/main.py --console
```

### 5. "Alto uso de CPU"
**Problema**: Programa consome muita CPU

**Solução**:
1. **Ajuste configurações**:
   ```json
   {
     "monitoring": {
       "scan_interval": 5  // Aumente o intervalo
     }
   }
   ```

2. **Exclua diretórios desnecessários**:
   ```json
   {
     "monitoring": {
       "exclusions": [
         "C:\\Program Files\\",
         "C:\\Windows\\",
         "C:\\temp\\"
       ]
     }
   }
   ```

### 6. "Falsos positivos"
**Problema**: Programa detecta programas legítimos como suspeitos

**Solução**:
1. **Reduza sensibilidade**:
   ```json
   {
     "detection": {
       "sensitivity": "low"
     }
   }
   ```

2. **Adicione exceções**:
   - Vá em Configurações > Exclusões
   - Adicione programas legítimos

### 7. "Antivírus bloqueando"
**Problema**: Antivírus detecta como falso positivo

**Solução**:
1. **Adicione exceção no antivírus**:
   - Windows Defender: Configurações > Exclusões
   - Adicione: `C:\AntiRansomware\`
   - Adicione: `python.exe`

2. **Desative temporariamente** o antivírus para instalação

### 8. "Firewall bloqueando"
**Problema**: Firewall impede funcionamento

**Solução**:
```bash
# Adicione exceção manualmente
netsh advfirewall firewall add rule name="Anti-Ransomware Shield" dir=in action=allow program="C:\AntiRansomware\run.bat" enable=yes
```

### 9. "Erro de importação"
**Erro**: `ImportError: No module named 'core'`

**Solução**:
```bash
# Execute do diretório correto
cd C:\Users\bosta\Desktop\Chalenge
python src/main.py

# Ou use o script de execução
run.bat
```

### 10. "Logs não aparecem"
**Problema**: Logs não são exibidos na interface

**Solução**:
1. **Verifique permissões** de escrita em `C:\AntiRansomware\logs\`
2. **Execute como administrador**
3. **Verifique configuração**:
   ```json
   {
     "logging": {
       "level": "INFO",
       "console_output": true
     }
   }
   ```

## 🔍 Diagnóstico Avançado

### Verificar Status do Sistema
```bash
# Execute o teste completo
python test_simple.py

# Verifique logs
type C:\AntiRansomware\logs\antiransomware.log
```

### Verificar Dependências
```bash
# Lista módulos instalados
pip list

# Verifica versões específicas
python -c "import psutil; print(psutil.__version__)"
python -c "import watchdog; print(watchdog.__version__)"
```

### Verificar Permissões
```bash
# Testa criação de arquivo
echo test > C:\AntiRansomware\test.txt
del C:\AntiRansomware\test.txt
```

### Verificar Recursos do Sistema
```bash
# Verifica uso de CPU e memória
python -c "import psutil; print(f'CPU: {psutil.cpu_percent()}%, RAM: {psutil.virtual_memory().percent}%')"
```

## 🚨 Problemas Críticos

### 1. "Sistema travado"
**Solução**:
1. **Pare o programa**: `Ctrl+C` no terminal
2. **Termine processos**: `taskkill /f /im python.exe`
3. **Reinicie o computador**

### 2. "Modo de emergência ativado"
**Solução**:
1. **Reinicie o computador**
2. **Execute verificação completa**
3. **Verifique se não há arquivos criptografados**

### 3. "Alto uso de memória"
**Solução**:
1. **Pare o programa**
2. **Limpe logs antigos**:
   ```bash
   del C:\AntiRansomware\logs\*.log
   ```
3. **Reinicie o programa**

## 📞 Suporte Técnico

### Informações para Suporte
Ao solicitar ajuda, inclua:

1. **Versão do Windows**:
   ```bash
   winver
   ```

2. **Versão do Python**:
   ```bash
   python --version
   ```

3. **Logs de erro**:
   ```bash
   type C:\AntiRansomware\logs\antiransomware.log
   ```

4. **Configuração atual**:
   ```bash
   type C:\AntiRansomware\config.json
   ```

### Canais de Suporte
- **GitHub Issues**: [Abrir issue](../../issues)
- **Email**: suporte@antiransomware.com
- **Documentação**: [Wiki](../../wiki)

## 🔄 Reset Completo

### Desinstalação Completa
```bash
# 1. Execute o desinstalador
C:\AntiRansomware\uninstall.bat

# 2. Remova manualmente se necessário
rmdir /s /q C:\AntiRansomware

# 3. Limpe registro
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "AntiRansomwareShield" /f
```

### Reinstalação Limpa
```bash
# 1. Desinstale completamente
# 2. Reinicie o computador
# 3. Execute install.bat novamente
```

## 💡 Dicas de Performance

### Otimização para Sistemas Lentos
```json
{
  "monitoring": {
    "scan_interval": 10,
    "directories": [
      "C:\\Users\\%USERNAME%\\Documents"
    ]
  },
  "detection": {
    "sensitivity": "low"
  }
}
```

### Otimização para Sistemas Rápidos
```json
{
  "monitoring": {
    "scan_interval": 1,
    "directories": [
      "C:\\Users\\%USERNAME%\\Documents",
      "C:\\Users\\%USERNAME%\\Desktop",
      "C:\\Users\\%USERNAME%\\Pictures"
    ]
  },
  "detection": {
    "sensitivity": "high"
  }
}
```

---

**💡 Lembre-se**: Se o problema persistir, execute `python test_simple.py` para diagnóstico completo!
