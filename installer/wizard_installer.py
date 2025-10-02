"""
Instalador Wizard Profissional - Anti-Ransomware Shield
Interface gráfica moderna com etapas guiadas
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import sys
import shutil
import subprocess
import threading
import time
from pathlib import Path
import json

class InstallerWizard:
    """Instalador wizard profissional"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_styles()
        
        # Variáveis do instalador
        self.install_path = tk.StringVar(value="C:\\AntiRansomware")
        self.create_desktop_shortcut = tk.BooleanVar(value=True)
        self.create_start_menu = tk.BooleanVar(value=True)
        self.auto_start = tk.BooleanVar(value=True)
        self.create_firewall_rule = tk.BooleanVar(value=True)
        
        # Estado do instalador
        self.current_step = 0
        self.total_steps = 5
        self.installation_success = False
        
        # Cria interface
        self.create_widgets()
        
    def setup_window(self):
        """Configura janela principal"""
        self.root.title("Anti-Ransomware Shield - Instalador")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        
        # Centraliza janela
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (700 // 2)
        y = (self.root.winfo_screenheight() // 2) - (500 // 2)
        self.root.geometry(f"700x500+{x}+{y}")
        
        # Ícone (se disponível)
        try:
            self.root.iconbitmap("assets/icon.ico")
        except:
            pass
    
    def setup_styles(self):
        """Configura estilos da interface"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Cores personalizadas
        self.colors = {
            'primary': '#2c3e50',
            'secondary': '#34495e',
            'success': '#27ae60',
            'warning': '#f39c12',
            'danger': '#e74c3c',
            'info': '#3498db'
        }
        
        # Configura estilos
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), foreground=self.colors['primary'])
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'), foreground=self.colors['secondary'])
        style.configure('Step.TLabel', font=('Arial', 10, 'bold'), foreground=self.colors['info'])
    
    def create_widgets(self):
        """Cria widgets da interface"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Cabeçalho
        self.create_header(main_frame)
        
        # Área de conteúdo
        self.content_frame = ttk.Frame(main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True, pady=(20, 0))
        
        # Barra de progresso
        self.create_progress_bar(main_frame)
        
        # Botões de navegação
        self.create_navigation_buttons(main_frame)
        
        # Mostra primeira etapa
        self.show_step(0)
    
    def create_header(self, parent):
        """Cria cabeçalho do instalador"""
        header_frame = ttk.Frame(parent)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Título
        title_label = ttk.Label(header_frame, text="🛡️ Anti-Ransomware Shield", style='Title.TLabel')
        title_label.pack()
        
        # Subtítulo
        subtitle_label = ttk.Label(header_frame, text="Instalador Wizard Profissional", style='Header.TLabel')
        subtitle_label.pack(pady=(5, 0))
    
    def create_progress_bar(self, parent):
        """Cria barra de progresso"""
        progress_frame = ttk.Frame(parent)
        progress_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Label da etapa atual
        self.step_label = ttk.Label(progress_frame, text="Etapa 1 de 5", style='Step.TLabel')
        self.step_label.pack()
        
        # Barra de progresso
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, 
                                          mode='determinate', length=400)
        self.progress_bar.pack(pady=(5, 0))
    
    def create_navigation_buttons(self, parent):
        """Cria botões de navegação"""
        button_frame = ttk.Frame(parent)
        button_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Botão Anterior
        self.prev_button = ttk.Button(button_frame, text="◀ Anterior", 
                                    command=self.previous_step, state='disabled')
        self.prev_button.pack(side=tk.LEFT)
        
        # Botão Próximo
        self.next_button = ttk.Button(button_frame, text="Próximo ▶", 
                                    command=self.next_step)
        self.next_button.pack(side=tk.RIGHT)
        
        # Botão Cancelar
        self.cancel_button = ttk.Button(button_frame, text="Cancelar", 
                                      command=self.cancel_installation)
        self.cancel_button.pack(side=tk.RIGHT, padx=(0, 10))
    
    def show_step(self, step):
        """Mostra etapa específica"""
        # Limpa conteúdo anterior
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Atualiza progresso
        self.current_step = step
        progress = ((step + 1) / self.total_steps) * 100
        self.progress_var.set(progress)
        self.step_label.config(text=f"Etapa {step + 1} de {self.total_steps}")
        
        # Mostra conteúdo da etapa
        if step == 0:
            self.show_welcome()
        elif step == 1:
            self.show_license()
        elif step == 2:
            self.show_installation_options()
        elif step == 3:
            self.show_installation_progress()
        elif step == 4:
            self.show_completion()
        
        # Atualiza botões
        self.update_navigation_buttons()
    
    def show_welcome(self):
        """Mostra tela de boas-vindas"""
        welcome_frame = ttk.Frame(self.content_frame)
        welcome_frame.pack(fill=tk.BOTH, expand=True)
        
        # Ícone/logo
        icon_label = ttk.Label(welcome_frame, text="🛡️", font=('Arial', 48))
        icon_label.pack(pady=(20, 20))
        
        # Título
        title_label = ttk.Label(welcome_frame, text="Bem-vindo ao Anti-Ransomware Shield", 
                               style='Header.TLabel')
        title_label.pack(pady=(0, 10))
        
        # Descrição
        desc_text = """Este assistente irá guiá-lo através da instalação do Anti-Ransomware Shield.

O Anti-Ransomware Shield é uma ferramenta avançada de proteção que:
• Monitora seu sistema em tempo real
• Detecta e bloqueia ransomwares automaticamente
• Protege seus arquivos importantes
• Oferece interface profissional e fácil de usar

Clique em 'Próximo' para continuar com a instalação."""
        
        desc_label = ttk.Label(welcome_frame, text=desc_text, justify=tk.LEFT, 
                              wraplength=600)
        desc_label.pack(pady=(0, 20))
        
        # Informações do sistema
        info_frame = ttk.LabelFrame(welcome_frame, text="Informações do Sistema", padding="10")
        info_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Verifica Python
        python_version = sys.version.split()[0]
        python_label = ttk.Label(info_frame, text=f"Python: {python_version}")
        python_label.pack(anchor=tk.W)
        
        # Verifica espaço em disco
        try:
            free_space = shutil.disk_usage("C:")[2] // (1024**3)  # GB
            space_label = ttk.Label(info_frame, text=f"Espaço livre em C:: {free_space} GB")
            space_label.pack(anchor=tk.W)
        except:
            space_label = ttk.Label(info_frame, text="Espaço livre: Verificando...")
            space_label.pack(anchor=tk.W)
    
    def show_license(self):
        """Mostra tela de licença"""
        license_frame = ttk.Frame(self.content_frame)
        license_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(license_frame, text="Termos de Licença", style='Header.TLabel')
        title_label.pack(pady=(0, 10))
        
        # Texto da licença
        license_text = """MIT License

Copyright (c) 2024 Anti-Ransomware Shield

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
        
        # Área de texto com scroll
        text_frame = ttk.Frame(license_frame)
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        text_widget = tk.Text(text_frame, height=15, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)
        
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        text_widget.insert(tk.END, license_text)
        text_widget.config(state=tk.DISABLED)
        
        # Checkbox de aceite
        self.accept_license = tk.BooleanVar()
        accept_check = ttk.Checkbutton(license_frame, text="Eu aceito os termos da licença", 
                                     variable=self.accept_license)
        accept_check.pack(pady=(10, 0))
    
    def show_installation_options(self):
        """Mostra opções de instalação"""
        options_frame = ttk.Frame(self.content_frame)
        options_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(options_frame, text="Opções de Instalação", style='Header.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Diretório de instalação
        dir_frame = ttk.LabelFrame(options_frame, text="Diretório de Instalação", padding="10")
        dir_frame.pack(fill=tk.X, pady=(0, 20))
        
        dir_input_frame = ttk.Frame(dir_frame)
        dir_input_frame.pack(fill=tk.X)
        
        ttk.Label(dir_input_frame, text="Instalar em:").pack(side=tk.LEFT)
        
        dir_entry = ttk.Entry(dir_input_frame, textvariable=self.install_path, width=50)
        dir_entry.pack(side=tk.LEFT, padx=(10, 10), fill=tk.X, expand=True)
        
        browse_button = ttk.Button(dir_input_frame, text="Procurar...", 
                                 command=self.browse_directory)
        browse_button.pack(side=tk.RIGHT)
        
        # Opções adicionais
        options_label_frame = ttk.LabelFrame(options_frame, text="Opções Adicionais", padding="10")
        options_label_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Checkboxes
        ttk.Checkbutton(options_label_frame, text="Criar atalho na área de trabalho", 
                       variable=self.create_desktop_shortcut).pack(anchor=tk.W)
        ttk.Checkbutton(options_label_frame, text="Adicionar ao menu iniciar", 
                       variable=self.create_start_menu).pack(anchor=tk.W)
        ttk.Checkbutton(options_label_frame, text="Iniciar automaticamente com o Windows", 
                       variable=self.auto_start).pack(anchor=tk.W)
        ttk.Checkbutton(options_label_frame, text="Configurar regra do firewall", 
                       variable=self.create_firewall_rule).pack(anchor=tk.W)
        
        # Informações de espaço
        info_frame = ttk.LabelFrame(options_frame, text="Requisitos", padding="10")
        info_frame.pack(fill=tk.X)
        
        ttk.Label(info_frame, text="• Espaço necessário: ~50 MB").pack(anchor=tk.W)
        ttk.Label(info_frame, text="• Python 3.8+ (já instalado)").pack(anchor=tk.W)
        ttk.Label(info_frame, text="• Privilégios de administrador (recomendado)").pack(anchor=tk.W)
    
    def show_installation_progress(self):
        """Mostra progresso da instalação"""
        progress_frame = ttk.Frame(self.content_frame)
        progress_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(progress_frame, text="Instalando Anti-Ransomware Shield", 
                               style='Header.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Barra de progresso da instalação
        self.install_progress_var = tk.DoubleVar()
        self.install_progress_bar = ttk.Progressbar(progress_frame, 
                                                   variable=self.install_progress_var,
                                                   mode='determinate', length=400)
        self.install_progress_bar.pack(pady=(0, 20))
        
        # Label de status
        self.status_label = ttk.Label(progress_frame, text="Preparando instalação...")
        self.status_label.pack()
        
        # Área de log
        log_frame = ttk.LabelFrame(progress_frame, text="Log de Instalação", padding="10")
        log_frame.pack(fill=tk.BOTH, expand=True, pady=(20, 0))
        
        self.log_text = tk.Text(log_frame, height=8, wrap=tk.WORD)
        log_scrollbar = ttk.Scrollbar(log_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=log_scrollbar.set)
        
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        log_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Inicia instalação em thread separada
        self.start_installation()
    
    def show_completion(self):
        """Mostra tela de conclusão"""
        completion_frame = ttk.Frame(self.content_frame)
        completion_frame.pack(fill=tk.BOTH, expand=True)
        
        # Ícone de sucesso
        if self.installation_success:
            icon_label = ttk.Label(completion_frame, text="✅", font=('Arial', 48))
            icon_label.pack(pady=(20, 20))
            
            title_label = ttk.Label(completion_frame, text="Instalação Concluída!", 
                                   style='Header.TLabel')
            title_label.pack(pady=(0, 10))
            
            desc_text = """O Anti-Ransomware Shield foi instalado com sucesso!

Para usar o programa:
• Clique no atalho da área de trabalho
• Ou execute: C:\\AntiRansomware\\run.bat
• Configure suas preferências na primeira execução

Obrigado por escolher o Anti-Ransomware Shield!"""
        else:
            icon_label = ttk.Label(completion_frame, text="❌", font=('Arial', 48))
            icon_label.pack(pady=(20, 20))
            
            title_label = ttk.Label(completion_frame, text="Instalação Falhou", 
                                   style='Header.TLabel')
            title_label.pack(pady=(0, 10))
            
            desc_text = """A instalação não foi concluída com sucesso.

Possíveis causas:
• Privilégios insuficientes
• Antivírus bloqueando
• Espaço em disco insuficiente

Tente executar como administrador ou verifique os logs."""
        
        desc_label = ttk.Label(completion_frame, text=desc_text, justify=tk.LEFT, 
                              wraplength=600)
        desc_label.pack(pady=(0, 20))
    
    def browse_directory(self):
        """Abre diálogo para escolher diretório"""
        directory = filedialog.askdirectory(initialdir="C:\\", 
                                          title="Escolher diretório de instalação")
        if directory:
            self.install_path.set(directory)
    
    def update_navigation_buttons(self):
        """Atualiza botões de navegação"""
        # Botão Anterior
        if self.current_step == 0:
            self.prev_button.config(state='disabled')
        else:
            self.prev_button.config(state='normal')
        
        # Botão Próximo
        if self.current_step == self.total_steps - 1:
            self.next_button.config(text="Concluir", command=self.finish_installation)
        else:
            self.next_button.config(text="Próximo ▶", command=self.next_step)
    
    def next_step(self):
        """Vai para próxima etapa"""
        if self.current_step < self.total_steps - 1:
            # Validações específicas por etapa
            if self.current_step == 1:  # Licença
                if not self.accept_license.get():
                    messagebox.showwarning("Atenção", "Você deve aceitar os termos da licença para continuar.")
                    return
            
            self.show_step(self.current_step + 1)
    
    def previous_step(self):
        """Volta para etapa anterior"""
        if self.current_step > 0:
            self.show_step(self.current_step - 1)
    
    def start_installation(self):
        """Inicia processo de instalação"""
        def install_thread():
            try:
                self.log_message("Iniciando instalação...")
                self.update_progress(10)
                
                # 1. Cria diretório de instalação
                self.log_message("Criando diretório de instalação...")
                install_dir = self.install_path.get()
                os.makedirs(install_dir, exist_ok=True)
                os.makedirs(f"{install_dir}\\logs", exist_ok=True)
                os.makedirs(f"{install_dir}\\Quarantine", exist_ok=True)
                self.update_progress(20)
                
                # 2. Instala dependências
                self.log_message("Instalando dependências...")
                self.install_dependencies()
                self.update_progress(40)
                
                # 3. Copia arquivos
                self.log_message("Copiando arquivos do programa...")
                self.copy_files(install_dir)
                self.update_progress(60)
                
                # 4. Cria atalhos
                if self.create_desktop_shortcut.get():
                    self.log_message("Criando atalho na área de trabalho...")
                    self.create_desktop_shortcut_func(install_dir)
                
                if self.create_start_menu.get():
                    self.log_message("Adicionando ao menu iniciar...")
                    self.create_start_menu_func(install_dir)
                
                self.update_progress(80)
                
                # 5. Configura inicialização automática
                if self.auto_start.get():
                    self.log_message("Configurando inicialização automática...")
                    self.setup_auto_start(install_dir)
                
                # 6. Configura firewall
                if self.create_firewall_rule.get():
                    self.log_message("Configurando regra do firewall...")
                    self.setup_firewall_rule(install_dir)
                
                self.update_progress(100)
                self.log_message("Instalação concluída com sucesso!")
                
                self.installation_success = True
                
            except Exception as e:
                self.log_message(f"Erro durante a instalação: {str(e)}")
                self.installation_success = False
        
        # Inicia thread de instalação
        threading.Thread(target=install_thread, daemon=True).start()
    
    def install_dependencies(self):
        """Instala dependências Python"""
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                          check=True, capture_output=True, text=True)
            self.log_message("Dependências instaladas com sucesso")
        except subprocess.CalledProcessError as e:
            self.log_message(f"Erro ao instalar dependências: {e}")
            raise
    
    def copy_files(self, install_dir):
        """Copia arquivos do programa"""
        try:
            # Copia código fonte
            if os.path.exists("src"):
                shutil.copytree("src", f"{install_dir}\\src", dirs_exist_ok=True)
                self.log_message("Código fonte copiado")
            
            # Copia arquivo de configuração
            if os.path.exists("config.json"):
                shutil.copy("config.json", f"{install_dir}\\config.json")
                self.log_message("Configuração copiada")
            
            # Copia requirements.txt
            if os.path.exists("requirements.txt"):
                shutil.copy("requirements.txt", f"{install_dir}\\requirements.txt")
                self.log_message("Requirements copiado")
            
            # Cria script de execução
            self.create_launcher_script(install_dir)
            
        except Exception as e:
            self.log_message(f"Erro ao copiar arquivos: {e}")
            raise
    
    def create_launcher_script(self, install_dir):
        """Cria script de inicialização"""
        launcher_script = f'''@echo off
echo ========================================
echo Anti-Ransomware Shield
echo ========================================
echo.

REM Muda para diretório de instalação
cd /d "{install_dir}"

REM Verifica se Python está disponível
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo ERRO: Python nao encontrado!
    echo Instale Python 3.8+ e tente novamente.
    pause
    exit /b 1
)

REM Instala dependências se necessário
if not exist "venv" (
    echo Criando ambiente virtual...
    python -m venv venv
)

echo Ativando ambiente virtual...
call venv\\Scripts\\activate.bat

echo Instalando dependencias...
pip install -r requirements.txt

echo.
echo Iniciando Anti-Ransomware Shield...
echo.

REM Executa o programa
python src/main.py

pause
'''
        
        with open(f"{install_dir}\\run.bat", "w", encoding="utf-8") as f:
            f.write(launcher_script)
        self.log_message("Script de inicialização criado")
    
    def create_desktop_shortcut_func(self, install_dir):
        """Cria atalho na área de trabalho"""
        try:
            shortcut_script = f'''
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$env:USERPROFILE\\Desktop\\Anti-Ransomware Shield.lnk")
$Shortcut.TargetPath = "{install_dir}\\run.bat"
$Shortcut.WorkingDirectory = "{install_dir}"
$Shortcut.Description = "Anti-Ransomware Shield - Proteção contra ransomware"
$Shortcut.Save()
'''
            
            with open("create_shortcut.ps1", "w", encoding="utf-8") as f:
                f.write(shortcut_script)
            
            subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "create_shortcut.ps1"], 
                          capture_output=True)
            
            os.remove("create_shortcut.ps1")
            self.log_message("Atalho na área de trabalho criado")
            
        except Exception as e:
            self.log_message(f"Erro ao criar atalho: {e}")
    
    def create_start_menu_func(self, install_dir):
        """Cria entrada no menu iniciar"""
        try:
            start_menu_script = f'''
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$env:APPDATA\\Microsoft\\Windows\\Start Menu\\Programs\\Anti-Ransomware Shield.lnk")
$Shortcut.TargetPath = "{install_dir}\\run.bat"
$Shortcut.WorkingDirectory = "{install_dir}"
$Shortcut.Description = "Anti-Ransomware Shield - Proteção contra ransomware"
$Shortcut.Save()
'''
            
            with open("create_start_menu.ps1", "w", encoding="utf-8") as f:
                f.write(start_menu_script)
            
            subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "create_start_menu.ps1"], 
                          capture_output=True)
            
            os.remove("create_start_menu.ps1")
            self.log_message("Entrada no menu iniciar criada")
            
        except Exception as e:
            self.log_message(f"Erro ao criar entrada no menu: {e}")
    
    def setup_auto_start(self, install_dir):
        """Configura inicialização automática"""
        try:
            reg_script = f'''
reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "AntiRansomwareShield" /t REG_SZ /d "{install_dir}\\run.bat" /f
'''
            
            with open("configure_autostart.bat", "w", encoding="utf-8") as f:
                f.write(reg_script)
            
            subprocess.run(["configure_autostart.bat"], capture_output=True)
            os.remove("configure_autostart.bat")
            self.log_message("Inicialização automática configurada")
            
        except Exception as e:
            self.log_message(f"Erro ao configurar auto-start: {e}")
    
    def setup_firewall_rule(self, install_dir):
        """Configura regra do firewall"""
        try:
            subprocess.run([
                "netsh", "advfirewall", "firewall", "add", "rule",
                "name=Anti-Ransomware Shield", "dir=in", "action=allow", 
                f"program={install_dir}\\run.bat", "enable=yes"
            ], capture_output=True)
            self.log_message("Regra do firewall configurada")
            
        except Exception as e:
            self.log_message(f"Erro ao configurar firewall: {e}")
    
    def log_message(self, message):
        """Adiciona mensagem ao log"""
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)
        self.status_label.config(text=message)
    
    def update_progress(self, value):
        """Atualiza progresso da instalação"""
        self.install_progress_var.set(value)
        self.root.update_idletasks()
    
    def finish_installation(self):
        """Finaliza instalação"""
        if self.installation_success:
            messagebox.showinfo("Sucesso", "Instalação concluída com sucesso!")
        else:
            messagebox.showerror("Erro", "A instalação falhou. Verifique os logs para mais detalhes.")
        
        self.root.quit()
    
    def cancel_installation(self):
        """Cancela instalação"""
        if messagebox.askyesno("Confirmar", "Deseja realmente cancelar a instalação?"):
            self.root.quit()
    
    def run(self):
        """Executa o instalador"""
        self.root.mainloop()

def main():
    """Função principal"""
    try:
        # Verifica se está executando como administrador
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        
        if not is_admin:
            result = messagebox.askyesno("Privilégios de Administrador", 
                                       "Para uma instalação completa, é recomendado executar como administrador.\n\n"
                                       "Deseja continuar mesmo assim?")
            if not result:
                return
        
        # Cria e executa instalador
        installer = InstallerWizard()
        installer.run()
        
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao iniciar instalador: {e}")

if __name__ == "__main__":
    main()
