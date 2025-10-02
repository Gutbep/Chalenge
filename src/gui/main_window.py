"""
Interface gráfica principal da ferramenta anti-ransomware
Interface moderna e profissional usando tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import time
from datetime import datetime
import logging
import os

class AntiRansomwareGUI:
    """Interface gráfica principal"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_styles()
        self.setup_variables()
        self.create_widgets()
        self.setup_logging()
        
        # Status da aplicação
        self.monitoring_active = False
        self.protection_active = False
        self.emergency_mode = False
        
    def setup_window(self):
        """Configura janela principal"""
        self.root.title("Anti-Ransomware Shield v1.0")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)
        
        # Ícone da aplicação
        try:
            self.root.iconbitmap("assets/icon.ico")
        except:
            pass
        
        # Centraliza janela
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (1000 // 2)
        y = (self.root.winfo_screenheight() // 2) - (700 // 2)
        self.root.geometry(f"1000x700+{x}+{y}")
        
        # Configura fechamento
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
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
            'info': '#3498db',
            'light': '#ecf0f1',
            'dark': '#2c3e50'
        }
        
        # Configura estilos
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), foreground=self.colors['primary'])
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'), foreground=self.colors['secondary'])
        style.configure('Status.TLabel', font=('Arial', 10), foreground=self.colors['info'])
        style.configure('Success.TLabel', foreground=self.colors['success'])
        style.configure('Warning.TLabel', foreground=self.colors['warning'])
        style.configure('Danger.TLabel', foreground=self.colors['danger'])
        
        # Botões personalizados
        style.configure('Primary.TButton', font=('Arial', 10, 'bold'))
        style.configure('Success.TButton', font=('Arial', 10, 'bold'))
        style.configure('Danger.TButton', font=('Arial', 10, 'bold'))
    
    def setup_variables(self):
        """Configura variáveis da interface"""
        self.status_var = tk.StringVar(value="Desconectado")
        self.threat_level_var = tk.StringVar(value="SAFE")
        self.blocked_processes_var = tk.StringVar(value="0")
        self.scanned_files_var = tk.StringVar(value="0")
        self.detected_threats_var = tk.StringVar(value="0")
        
    def create_widgets(self):
        """Cria widgets da interface"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configura grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Título
        title_label = ttk.Label(main_frame, text="🛡️ Anti-Ransomware Shield", style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Painel de status
        self.create_status_panel(main_frame, 1)
        
        # Painel de controles
        self.create_control_panel(main_frame, 2)
        
        # Painel de monitoramento
        self.create_monitoring_panel(main_frame, 3)
        
        # Painel de logs
        self.create_logs_panel(main_frame, 4)
        
        # Barra de status
        self.create_status_bar(main_frame, 5)
    
    def create_status_panel(self, parent, row):
        """Cria painel de status"""
        status_frame = ttk.LabelFrame(parent, text="Status do Sistema", padding="10")
        status_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        status_frame.columnconfigure(1, weight=1)
        
        # Status de monitoramento
        ttk.Label(status_frame, text="Monitoramento:", style='Header.TLabel').grid(row=0, column=0, sticky=tk.W)
        self.monitoring_status_label = ttk.Label(status_frame, text="❌ Inativo", style='Danger.TLabel')
        self.monitoring_status_label.grid(row=0, column=1, sticky=tk.W, padx=(10, 0))
        
        # Status de proteção
        ttk.Label(status_frame, text="Proteção:", style='Header.TLabel').grid(row=1, column=0, sticky=tk.W)
        self.protection_status_label = ttk.Label(status_frame, text="❌ Inativa", style='Danger.TLabel')
        self.protection_status_label.grid(row=1, column=1, sticky=tk.W, padx=(10, 0))
        
        # Nível de ameaça
        ttk.Label(status_frame, text="Nível de Ameaça:", style='Header.TLabel').grid(row=2, column=0, sticky=tk.W)
        self.threat_level_label = ttk.Label(status_frame, text="🟢 SEGURO", style='Success.TLabel')
        self.threat_level_label.grid(row=2, column=1, sticky=tk.W, padx=(10, 0))
        
        # Estatísticas
        stats_frame = ttk.Frame(status_frame)
        stats_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        
        ttk.Label(stats_frame, text="Processos Bloqueados:").grid(row=0, column=0, sticky=tk.W)
        ttk.Label(stats_frame, textvariable=self.blocked_processes_var).grid(row=0, column=1, sticky=tk.W, padx=(10, 0))
        
        ttk.Label(stats_frame, text="Arquivos Escaneados:").grid(row=0, column=2, sticky=tk.W, padx=(20, 0))
        ttk.Label(stats_frame, textvariable=self.scanned_files_var).grid(row=0, column=3, sticky=tk.W, padx=(10, 0))
        
        ttk.Label(stats_frame, text="Ameaças Detectadas:").grid(row=1, column=0, sticky=tk.W)
        ttk.Label(stats_frame, textvariable=self.detected_threats_var).grid(row=1, column=1, sticky=tk.W, padx=(10, 0))
    
    def create_control_panel(self, parent, row):
        """Cria painel de controles"""
        control_frame = ttk.LabelFrame(parent, text="Controles", padding="10")
        control_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Botões principais
        button_frame = ttk.Frame(control_frame)
        button_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        self.start_button = ttk.Button(button_frame, text="▶️ Iniciar Proteção", 
                                     command=self.start_protection, style='Success.TButton')
        self.start_button.grid(row=0, column=0, padx=(0, 10))
        
        self.stop_button = ttk.Button(button_frame, text="⏹️ Parar Proteção", 
                                    command=self.stop_protection, style='Danger.TButton', state='disabled')
        self.stop_button.grid(row=0, column=1, padx=(0, 10))
        
        self.emergency_button = ttk.Button(button_frame, text="🚨 Modo Emergência", 
                                         command=self.activate_emergency_mode, style='Danger.TButton')
        self.emergency_button.grid(row=0, column=2, padx=(0, 10))
        
        self.settings_button = ttk.Button(button_frame, text="⚙️ Configurações", 
                                        command=self.open_settings, style='Primary.TButton')
        self.settings_button.grid(row=0, column=3)
        
        # Barra de progresso
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(control_frame, variable=self.progress_var, 
                                          mode='indeterminate')
        self.progress_bar.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
    
    def create_monitoring_panel(self, parent, row):
        """Cria painel de monitoramento"""
        monitor_frame = ttk.LabelFrame(parent, text="Monitoramento em Tempo Real", padding="10")
        monitor_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        monitor_frame.columnconfigure(0, weight=1)
        monitor_frame.rowconfigure(1, weight=1)
        
        # Indicadores de atividade
        activity_frame = ttk.Frame(monitor_frame)
        activity_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Indicador de CPU
        ttk.Label(activity_frame, text="CPU:").grid(row=0, column=0, sticky=tk.W)
        self.cpu_label = ttk.Label(activity_frame, text="0%")
        self.cpu_label.grid(row=0, column=1, sticky=tk.W, padx=(5, 20))
        
        # Indicador de Memória
        ttk.Label(activity_frame, text="Memória:").grid(row=0, column=2, sticky=tk.W)
        self.memory_label = ttk.Label(activity_frame, text="0 MB")
        self.memory_label.grid(row=0, column=3, sticky=tk.W, padx=(5, 20))
        
        # Indicador de Rede
        ttk.Label(activity_frame, text="Rede:").grid(row=0, column=4, sticky=tk.W)
        self.network_label = ttk.Label(activity_frame, text="🟢 Ativa")
        self.network_label.grid(row=0, column=5, sticky=tk.W, padx=(5, 0))
        
        # Lista de processos monitorados
        process_frame = ttk.Frame(monitor_frame)
        process_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        process_frame.columnconfigure(0, weight=1)
        process_frame.rowconfigure(0, weight=1)
        
        ttk.Label(process_frame, text="Processos Monitorados:", style='Header.TLabel').grid(row=0, column=0, sticky=tk.W)
        
        # Treeview para processos
        columns = ('PID', 'Nome', 'CPU%', 'Memória', 'Status')
        self.process_tree = ttk.Treeview(process_frame, columns=columns, show='headings', height=8)
        
        for col in columns:
            self.process_tree.heading(col, text=col)
            self.process_tree.column(col, width=100)
        
        # Scrollbar para treeview
        process_scrollbar = ttk.Scrollbar(process_frame, orient=tk.VERTICAL, command=self.process_tree.yview)
        self.process_tree.configure(yscrollcommand=process_scrollbar.set)
        
        self.process_tree.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        process_scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))
    
    def create_logs_panel(self, parent, row):
        """Cria painel de logs"""
        logs_frame = ttk.LabelFrame(parent, text="Logs de Atividade", padding="10")
        logs_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        logs_frame.columnconfigure(0, weight=1)
        logs_frame.rowconfigure(1, weight=1)
        
        # Controles de log
        log_controls = ttk.Frame(logs_frame)
        log_controls.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(log_controls, text="Filtro:").grid(row=0, column=0, sticky=tk.W)
        self.log_filter_var = tk.StringVar()
        log_filter_combo = ttk.Combobox(log_controls, textvariable=self.log_filter_var, 
                                      values=['Todos', 'Ameaças', 'Proteção', 'Sistema'], width=15)
        log_filter_combo.grid(row=0, column=1, sticky=tk.W, padx=(5, 10))
        log_filter_combo.set('Todos')
        
        ttk.Button(log_controls, text="Limpar", command=self.clear_logs).grid(row=0, column=2, sticky=tk.W)
        ttk.Button(log_controls, text="Exportar", command=self.export_logs).grid(row=0, column=3, sticky=tk.W, padx=(5, 0))
        
        # Área de logs
        self.logs_text = scrolledtext.ScrolledText(logs_frame, height=10, wrap=tk.WORD)
        self.logs_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configura tags para colorir logs
        self.logs_text.tag_configure('INFO', foreground='blue')
        self.logs_text.tag_configure('WARNING', foreground='orange')
        self.logs_text.tag_configure('ERROR', foreground='red')
        self.logs_text.tag_configure('CRITICAL', foreground='red', font=('Arial', 9, 'bold'))
        self.logs_text.tag_configure('THREAT', foreground='red', font=('Arial', 9, 'bold'))
    
    def create_status_bar(self, parent, row):
        """Cria barra de status"""
        status_bar = ttk.Frame(parent)
        status_bar.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        status_bar.columnconfigure(0, weight=1)
        
        ttk.Label(status_bar, textvariable=self.status_var, style='Status.TLabel').grid(row=0, column=0, sticky=tk.W)
        ttk.Label(status_bar, text=f"Versão 1.0.0 | {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}").grid(row=0, column=1, sticky=tk.E)
    
    def setup_logging(self):
        """Configura sistema de logging"""
        # Cria diretório de logs
        os.makedirs("logs", exist_ok=True)
        
        # Configura logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('logs/antiransomware.log'),
                logging.StreamHandler()
            ]
        )
        
        # Handler personalizado para interface
        self.log_handler = GUILogHandler(self.logs_text)
        logging.getLogger().addHandler(self.log_handler)
    
    def start_protection(self):
        """Inicia proteção"""
        try:
            self.monitoring_active = True
            self.protection_active = True
            
            # Atualiza interface
            self.monitoring_status_label.config(text="✅ Ativo", style='Success.TLabel')
            self.protection_status_label.config(text="✅ Ativa", style='Success.TLabel')
            self.start_button.config(state='disabled')
            self.stop_button.config(state='normal')
            self.progress_bar.start()
            
            # Inicia monitoramento em thread separada
            threading.Thread(target=self._start_monitoring_thread, daemon=True).start()
            
            self.log_message("Sistema de proteção iniciado", "INFO")
            self.status_var.set("Proteção Ativa")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao iniciar proteção: {str(e)}")
            logging.error(f"Erro ao iniciar proteção: {e}")
    
    def stop_protection(self):
        """Para proteção"""
        try:
            self.monitoring_active = False
            self.protection_active = False
            
            # Atualiza interface
            self.monitoring_status_label.config(text="❌ Inativo", style='Danger.TLabel')
            self.protection_status_label.config(text="❌ Inativa", style='Danger.TLabel')
            self.start_button.config(state='normal')
            self.stop_button.config(state='disabled')
            self.progress_bar.stop()
            
            self.log_message("Sistema de proteção parado", "INFO")
            self.status_var.set("Proteção Parada")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao parar proteção: {str(e)}")
            logging.error(f"Erro ao parar proteção: {e}")
    
    def activate_emergency_mode(self):
        """Ativa modo de emergência"""
        if messagebox.askyesno("Modo de Emergência", 
                              "Deseja ativar o modo de emergência?\n\n"
                              "Isso irá:\n"
                              "- Bloquear todos os processos suspeitos\n"
                              "- Isolar o sistema da rede\n"
                              "- Ativar proteção máxima"):
            try:
                self.emergency_mode = True
                self.threat_level_label.config(text="🚨 CRÍTICO", style='Danger.TLabel')
                self.log_message("MODO DE EMERGÊNCIA ATIVADO", "CRITICAL")
                self.status_var.set("Modo de Emergência Ativo")
                
                # Aqui você chamaria o sistema de proteção real
                # self.protector.activate_emergency_mode()
                
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao ativar modo de emergência: {str(e)}")
                logging.error(f"Erro ao ativar modo de emergência: {e}")
    
    def open_settings(self):
        """Abre janela de configurações"""
        settings_window = SettingsWindow(self.root)
        self.root.wait_window(settings_window.window)
    
    def _start_monitoring_thread(self):
        """Thread de monitoramento"""
        while self.monitoring_active:
            try:
                # Simula monitoramento
                self.update_system_stats()
                time.sleep(1)
            except Exception as e:
                logging.error(f"Erro no monitoramento: {e}")
                time.sleep(5)
    
    def update_system_stats(self):
        """Atualiza estatísticas do sistema"""
        try:
            import psutil
            
            # CPU
            cpu_percent = psutil.cpu_percent()
            self.cpu_label.config(text=f"{cpu_percent}%")
            
            # Memória
            memory = psutil.virtual_memory()
            memory_mb = memory.used / (1024 * 1024)
            self.memory_label.config(text=f"{memory_mb:.0f} MB")
            
            # Atualiza treeview de processos
            self.update_process_list()
            
        except Exception as e:
            logging.error(f"Erro ao atualizar estatísticas: {e}")
    
    def update_process_list(self):
        """Atualiza lista de processos"""
        try:
            # Limpa lista atual
            for item in self.process_tree.get_children():
                self.process_tree.delete(item)
            
            # Lista processos reais do sistema
            try:
                import psutil
                processes = []
                
                for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
                    try:
                        info = proc.info
                        pid = str(info['pid'])
                        name = info['name']
                        cpu = f"{info['cpu_percent']:.1f}%"
                        memory = f"{info['memory_info'].rss / (1024 * 1024):.0f} MB"
                        
                        # Verifica se é suspeito
                        status = "🟢 Normal"
                        if any(susp in name.lower() for susp in ['crypto', 'encrypt', 'lock', 'ransom']):
                            status = "🚨 Suspeito"
                        elif info['cpu_percent'] > 80:
                            status = "⚠️ Alto CPU"
                        elif info['memory_info'].rss > 500 * 1024 * 1024:  # 500MB
                            status = "⚠️ Alta Memória"
                        
                        processes.append((pid, name, cpu, memory, status))
                        
                        # Limita a 20 processos para performance
                        if len(processes) >= 20:
                            break
                            
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        continue
                
                # Adiciona processos à lista
                for proc in processes:
                    self.process_tree.insert('', 'end', values=proc)
                    
            except Exception as e:
                logging.error(f"Erro ao obter processos: {e}")
                
        except Exception as e:
            logging.error(f"Erro ao atualizar lista de processos: {e}")
    
    def log_message(self, message: str, level: str = "INFO"):
        """Adiciona mensagem ao log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}\n"
        
        self.logs_text.insert(tk.END, log_entry)
        self.logs_text.see(tk.END)
        
        # Aplica tag de cor
        start_index = self.logs_text.index(tk.END + "-2l")
        end_index = self.logs_text.index(tk.END + "-1l")
        self.logs_text.tag_add(level, start_index, end_index)
    
    def clear_logs(self):
        """Limpa logs"""
        self.logs_text.delete(1.0, tk.END)
    
    def export_logs(self):
        """Exporta logs"""
        try:
            from tkinter import filedialog
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
            )
            
            if filename:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(self.logs_text.get(1.0, tk.END))
                messagebox.showinfo("Sucesso", "Logs exportados com sucesso!")
                
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao exportar logs: {str(e)}")
    
    def on_closing(self):
        """Evento de fechamento da janela"""
        if self.monitoring_active:
            if messagebox.askyesno("Confirmar", "O sistema de proteção está ativo. Deseja realmente fechar?"):
                self.stop_protection()
                self.root.destroy()
        else:
            self.root.destroy()
    
    def run(self):
        """Executa interface"""
        self.root.mainloop()

class GUILogHandler(logging.Handler):
    """Handler de logging para interface gráfica"""
    
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget
    
    def emit(self, record):
        """Emite log para widget de texto"""
        try:
            msg = self.format(record)
            self.text_widget.insert(tk.END, msg + '\n')
            self.text_widget.see(tk.END)
        except:
            pass

class SettingsWindow:
    """Janela de configurações"""
    
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Configurações")
        self.window.geometry("500x400")
        self.window.resizable(False, False)
        
        # Centraliza janela
        self.window.transient(parent)
        self.window.grab_set()
        
        self.create_widgets()
    
    def create_widgets(self):
        """Cria widgets da janela de configurações"""
        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(main_frame, text="Configurações do Anti-Ransomware", 
                 font=('Arial', 14, 'bold')).pack(pady=(0, 20))
        
        # Abas
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Aba Geral
        general_frame = ttk.Frame(notebook, padding="10")
        notebook.add(general_frame, text="Geral")
        
        # Aba Proteção
        protection_frame = ttk.Frame(notebook, padding="10")
        notebook.add(protection_frame, text="Proteção")
        
        # Aba Monitoramento
        monitoring_frame = ttk.Frame(notebook, padding="10")
        notebook.add(monitoring_frame, text="Monitoramento")
        
        # Botões
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(20, 0))
        
        ttk.Button(button_frame, text="Salvar", command=self.save_settings).pack(side=tk.RIGHT, padx=(5, 0))
        ttk.Button(button_frame, text="Cancelar", command=self.window.destroy).pack(side=tk.RIGHT)
    
    def save_settings(self):
        """Salva configurações"""
        messagebox.showinfo("Sucesso", "Configurações salvas com sucesso!")
        self.window.destroy()

if __name__ == "__main__":
    app = AntiRansomwareGUI()
    app.run()
