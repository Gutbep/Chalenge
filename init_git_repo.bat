@echo off
echo ========================================
echo Inicializando Repositorio Git - Challenge FIAP
echo ========================================
echo.

REM Inicializa repositório Git
echo Inicializando repositorio Git...
git init
if %errorLevel% neq 0 (
    echo ERRO: Git nao encontrado!
    echo Instale Git e tente novamente.
    echo Download: https://git-scm.com/downloads
    pause
    exit /b 1
)

echo.
echo Git inicializado com sucesso!
echo.

REM Adiciona todos os arquivos
echo Adicionando arquivos ao repositorio...
git add .
if %errorLevel% neq 0 (
    echo ERRO: Falha ao adicionar arquivos!
    pause
    exit /b 1
)

echo.
echo Arquivos adicionados com sucesso!
echo.

REM Commit inicial
echo Criando commit inicial...
git commit -m "feat: initial commit - Anti-Ransomware Shield

- Sistema completo de proteção contra ransomware
- Interface gráfica moderna e intuitiva
- Instalador wizard profissional
- Monitoramento em tempo real
- Detecção inteligente de ameaças
- Proteção automática contra ransomware
- Suporte a múltiplas famílias de ransomware
- Documentação completa
- Executáveis portáveis
- Testes automatizados

Funcionalidades:
- Monitoramento de arquivos, processos e recursos
- Detecção comportamental e por assinatura
- Sistema de honeypots para detecção precoce
- Proteção automática com quarentena
- Modo de emergência para situações críticas
- Interface gráfica profissional
- Instalador wizard com 5 etapas
- Configurações avançadas personalizáveis
- Logs detalhados de atividades
- Suporte a WannaCry, Petya, Locky, Ryuk, Sodinokibi, Maze, Conti, DarkSide

Desenvolvido para o Challenge FIAP"
if %errorLevel% neq 0 (
    echo ERRO: Falha ao criar commit!
    pause
    exit /b 1
)

echo.
echo Commit inicial criado com sucesso!
echo.

REM Configura branch main
echo Configurando branch main...
git branch -M main
if %errorLevel% neq 0 (
    echo ERRO: Falha ao configurar branch!
    pause
    exit /b 1
)

echo.
echo Branch main configurada!
echo.

REM Cria branch develop
echo Criando branch develop...
git checkout -b develop
if %errorLevel% neq 0 (
    echo ERRO: Falha ao criar branch develop!
    pause
    exit /b 1
)

echo.
echo Branch develop criada!
echo.

REM Volta para main
git checkout main

echo.
echo ========================================
echo REPOSITORIO GIT INICIALIZADO COM SUCESSO!
echo ========================================
echo.
echo 📁 Estrutura do repositorio:
echo    • README.md - Visao geral completa
echo    • docs/ - Documentacao detalhada
echo    • examples/ - Exemplos de uso
echo    • tests/ - Testes automatizados
echo    • src/ - Codigo fonte
echo    • dist/ - Executaveis
echo    • installer/ - Instaladores
echo.
echo 🚀 Proximos passos:
echo    1. Crie repositorio no GitHub: https://github.com/new
echo    2. Nome: Challenge-Fiap
echo    3. Descricao: Anti-Ransomware Shield - Ferramenta de protecao contra ransomware
echo    4. Conecte: git remote add origin [URL_DO_SEU_REPOSITORIO]
echo    5. Push: git push -u origin main
echo.
echo 🧙‍♂️ Destaque para o Instalador Wizard:
echo    • Interface grafica moderna
echo    • 5 etapas guiadas
echo    • Validacao automatica
echo    • Configuracao flexivel
echo    • Experiencia profissional
echo.
echo 📚 Documentacao incluida:
echo    • Guia de instalacao
echo    • Manual do usuario
echo    • Solucao de problemas
echo    • Guia do instalador wizard
echo    • Exemplos de uso
echo    • Testes automatizados
echo.
echo 💡 Consulte GITHUB_SETUP.md para comandos detalhados!
echo.
pause
