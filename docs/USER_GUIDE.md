# 👤 Manual do Usuário - Anti-Ransomware Shield

## 🎯 Introdução

Bem-vindo ao **Anti-Ransomware Shield**! Este manual o guiará através de todas as funcionalidades da ferramenta de proteção contra ransomware.

## 🚀 Primeiros Passos

### **Executando o Programa**

#### **Opção 1: Executável Simples**
```bash
cd dist/executavel_simples
AntiRansomwareShield.bat
```

#### **Opção 2: Versão Portável**
```bash
cd dist/portable
run.bat
```

#### **Opção 3: Código Fonte**
```bash
python src/main.py
```

### **Primeira Execução**

1. **Aceite os termos de licença**
2. **Configure as opções básicas**
3. **Inicie o monitoramento**
4. **Verifique o status do sistema**

## 🎨 Interface Gráfica

### **Dashboard Principal**

A interface principal exibe:

- **🛡️ Status de Proteção**: Indicador visual do estado do sistema
- **📊 Estatísticas**: CPU, memória e processos ativos
- **📋 Lista de Processos**: Processos monitorados com status
- **📝 Logs**: Histórico de atividades e alertas

### **Navegação**

- **Início**: Dashboard principal
- **Monitoramento**: Estatísticas em tempo real
- **Configurações**: Opções avançadas
- **Logs**: Histórico detalhado
- **Sobre**: Informações do programa

## 🛡️ Sistema de Proteção

### **Monitoramento Automático**

O sistema monitora automaticamente:

#### **Arquivos**
- **Documentos**: `.docx`, `.pdf`, `.txt`
- **Imagens**: `.jpg`, `.png`, `.gif`
- **Planilhas**: `.xlsx`, `.csv`
- **Apresentações**: `.pptx`

#### **Processos**
- **Todos os processos** do sistema
- **Análise de recursos** (CPU/memória)
- **Comandos executados**
- **Comportamento suspeito**

#### **Diretórios**
- **Documentos**: `C:\Users\[Usuário]\Documents`
- **Desktop**: `C:\Users\[Usuário]\Desktop`
- **Imagens**: `C:\Users\[Usuário]\Pictures`
- **Público**: `C:\Users\Public`

### **Sistema de Detecção**

#### **Análise Comportamental**
- ✅ **Atividade em Massa**: Múltiplos arquivos modificados
- ✅ **Uso Excessivo**: CPU/memória alta
- ✅ **Padrões Suspeitos**: Criptografia em massa
- ✅ **Comportamento Anômalo**: Atividade fora do normal

#### **Detecção por Assinatura**
- ✅ **Nomes Suspeitos**: `crypto`, `encrypt`, `lock`, `ransom`
- ✅ **Extensões Maliciosas**: `.locked`, `.encrypted`, `.crypto`
- ✅ **Comandos Conhecidos**: Comandos de ransomware
- ✅ **Processos Maliciosos**: Executáveis suspeitos

#### **Sistema de Honeypots**
- ✅ **Arquivos Isca**: Arquivos estratégicos
- ✅ **Detecção de Modificação**: Alerta imediato
- ✅ **Verificação de Integridade**: Hash dos arquivos
- ✅ **Localização Estratégica**: Diretórios importantes

### **Proteção Automática**

#### **Resposta Imediata**
- 🚨 **Terminação de Processos**: Para processos maliciosos
- 🚨 **Quarentena de Arquivos**: Isola arquivos suspeitos
- 🚨 **Proteção de Arquivos**: Protege documentos críticos
- 🚨 **Modo de Emergência**: Ativação automática

#### **Isolamento de Rede**
- 🔒 **Bloqueio de IPs**: Bloqueia conexões suspeitas
- 🔒 **Firewall**: Configura regras automáticas
- 🔒 **Isolamento**: Desconecta da rede se necessário
- 🔒 **Proteção**: Mantém sistema seguro

## ⚙️ Configurações

### **Configurações Básicas**

#### **Monitoramento**
- **Ativar/Desativar**: Controle principal
- **Intervalo de Verificação**: Frequência de análise
- **Diretórios**: Pastas monitoradas
- **Exclusões**: Pastas ignoradas

#### **Detecção**
- **Sensibilidade**: Nível de detecção
- **Análise Comportamental**: Ativar/desativar
- **Detecção por Assinatura**: Ativar/desativar
- **Honeypots**: Ativar/desativar

#### **Proteção**
- **Quarentena Automática**: Isolamento automático
- **Terminação de Processos**: Parar processos suspeitos
- **Modo de Emergência**: Ativação automática
- **Proteção de Arquivos**: Proteger arquivos críticos

### **Configurações Avançadas**

#### **Limites e Thresholds**
- **Atividade em Massa**: Número de arquivos
- **CPU Alta**: Percentual de uso
- **Memória Alta**: Uso de memória
- **Tempo de Resposta**: Latência máxima

#### **Logs e Relatórios**
- **Nível de Log**: Detalhamento
- **Tamanho Máximo**: Limite de arquivo
- **Rotação**: Número de arquivos
- **Console**: Saída no terminal

## 📊 Monitoramento em Tempo Real

### **Dashboard de Status**

#### **Indicadores Visuais**
- 🟢 **Verde**: Sistema seguro
- 🟡 **Amarelo**: Atenção necessária
- 🔴 **Vermelho**: Ameaça detectada
- ⚫ **Preto**: Modo de emergência

#### **Estatísticas do Sistema**
- **CPU**: Percentual de uso
- **Memória**: Uso de RAM
- **Disco**: Espaço disponível
- **Rede**: Atividade de rede

### **Lista de Processos**

#### **Informações Exibidas**
- **PID**: Identificador do processo
- **Nome**: Nome do executável
- **CPU**: Uso de processador
- **Memória**: Uso de RAM
- **Status**: Estado do processo

#### **Status dos Processos**
- 🟢 **Normal**: Processo seguro
- 🚨 **Suspeito**: Nome suspeito
- ⚠️ **Alto CPU**: Uso excessivo de CPU
- ⚠️ **Alta Memória**: Uso excessivo de RAM

### **Logs Detalhados**

#### **Tipos de Log**
- **INFO**: Informações gerais
- **WARNING**: Avisos importantes
- **ERROR**: Erros do sistema
- **CRITICAL**: Situações críticas

#### **Filtros de Log**
- **Por Tipo**: Filtrar por nível
- **Por Tempo**: Filtrar por período
- **Por Processo**: Filtrar por processo
- **Por Arquivo**: Filtrar por arquivo

## 🚨 Alertas e Notificações

### **Tipos de Alertas**

#### **Alertas de Detecção**
- 🚨 **Processo Suspeito**: Processo malicioso detectado
- 🚨 **Atividade em Massa**: Múltiplos arquivos modificados
- 🚨 **Honeypot Comprometido**: Arquivo isca modificado
- 🚨 **Comando Malicioso**: Comando suspeito executado

#### **Alertas de Sistema**
- ⚠️ **CPU Alta**: Uso excessivo de processador
- ⚠️ **Memória Alta**: Uso excessivo de RAM
- ⚠️ **Disco Cheio**: Espaço insuficiente
- ⚠️ **Rede Suspeita**: Atividade de rede anômala

### **Notificações**

#### **Notificações Visuais**
- **Popup**: Janela de alerta
- **Tray**: Ícone na bandeja do sistema
- **Interface**: Indicadores na GUI
- **Logs**: Entradas no histórico

#### **Configuração de Notificações**
- **Som**: Ativar/desativar
- **Visual**: Tipo de notificação
- **Frequência**: Intervalo de alertas
- **Filtros**: Tipos de alerta

## 🔧 Solução de Problemas

### **Problemas Comuns**

#### **Programa não inicia**
1. Verifique se Python está instalado
2. Execute como administrador
3. Verifique as dependências
4. Consulte os logs de erro

#### **Detecção falsa**
1. Adicione exceções nas configurações
2. Ajuste a sensibilidade
3. Configure exclusões
4. Verifique os logs

#### **Performance lenta**
1. Ajuste o intervalo de verificação
2. Configure exclusões
3. Reduza o número de processos monitorados
4. Verifique recursos do sistema

### **Logs de Diagnóstico**

#### **Localização dos Logs**
- **Arquivo**: `logs/antiransomware.log`
- **Console**: Saída do terminal
- **Interface**: Área de logs na GUI

#### **Informações dos Logs**
- **Timestamp**: Data e hora
- **Nível**: Tipo de mensagem
- **Módulo**: Componente responsável
- **Mensagem**: Detalhes do evento

## 📈 Relatórios e Estatísticas

### **Relatórios de Segurança**

#### **Relatório Diário**
- **Processos Monitorados**: Número total
- **Arquivos Analisados**: Quantidade
- **Ameaças Detectadas**: Número de detecções
- **Ações Tomadas**: Respostas automáticas

#### **Relatório Semanal**
- **Tendências**: Padrões de atividade
- **Estatísticas**: Métricas de performance
- **Alertas**: Resumo de notificações
- **Recomendações**: Sugestões de melhoria

### **Estatísticas de Performance**

#### **Métricas do Sistema**
- **CPU**: Uso médio e pico
- **Memória**: Consumo de RAM
- **Disco**: I/O e espaço
- **Rede**: Tráfego e conexões

#### **Métricas de Detecção**
- **Precisão**: Taxa de detecção correta
- **Latência**: Tempo de resposta
- **Cobertura**: Área monitorada
- **Eficácia**: Taxa de sucesso

## 🎯 Dicas de Uso

### **Melhores Práticas**

#### **Configuração Inicial**
1. **Execute como administrador** para máxima proteção
2. **Configure exclusões** para pastas do sistema
3. **Ajuste a sensibilidade** conforme necessário
4. **Teste as funcionalidades** antes do uso em produção

#### **Uso Diário**
1. **Monitore os logs** regularmente
2. **Verifique os alertas** imediatamente
3. **Mantenha o programa atualizado**
4. **Faça backup** das configurações

#### **Manutenção**
1. **Limpe os logs** periodicamente
2. **Verifique as exclusões** regularmente
3. **Atualize as assinaturas** se disponível
4. **Teste a proteção** ocasionalmente

### **Otimização de Performance**

#### **Configurações Recomendadas**
- **Intervalo**: 1-5 segundos
- **Processos**: Máximo 50
- **Arquivos**: Diretórios essenciais
- **Logs**: Nível INFO

#### **Recursos do Sistema**
- **RAM**: Mínimo 4GB
- **CPU**: Processador moderno
- **Disco**: SSD recomendado
- **Rede**: Conexão estável

## 📞 Suporte

### **Recursos de Ajuda**

- 📖 [Guia de Instalação](INSTALLATION.md)
- 🔧 [Solução de Problemas](TROUBLESHOOTING.md)
- 🧙‍♂️ [Instalador Wizard](WIZARD_INSTALLER_GUIDE.md)
- 🐛 [Reportar Problemas](https://github.com/[SEU_USUARIO]/Challenge-Fiap/issues)

### **Contato**

Para suporte técnico:
- **GitHub Issues**: Reporte problemas
- **Documentação**: Consulte os guias
- **Logs**: Envie logs de erro
- **Configuração**: Compartilhe configurações

---

**🛡️ Proteja seu sistema com o Anti-Ransomware Shield!**

**💡 Use este manual para aproveitar ao máximo todas as funcionalidades!**