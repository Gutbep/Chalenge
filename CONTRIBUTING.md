# 🤝 Guia de Contribuição - Challenge FIAP

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
venv\Scripts\activate

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
