"""
Sistema de monitoramento de processos e arquivos
Detecta comportamentos suspeitos de ransomware
"""

import os
import time
import hashlib
import threading
from typing import Dict, Callable
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import psutil
import logging

class FileMonitor(FileSystemEventHandler):
    """Monitor de eventos do sistema de arquivos"""
    
    def __init__(self, callback: Callable):
        self.callback = callback
        self.suspicious_activities = []
        self.file_access_count = {}
        self.last_access_time = {}
        
    def on_modified(self, event):
        if not event.is_directory:
            self._analyze_file_activity(event.src_path, "modified")
    
    def on_created(self, event):
        if not event.is_directory:
            self._analyze_file_activity(event.src_path, "created")
    
    def on_deleted(self, event):
        if not event.is_directory:
            self._analyze_file_activity(event.src_path, "deleted")
    
    def _analyze_file_activity(self, file_path: str, action: str):
        """Analisa atividade de arquivo para detectar padrões suspeitos"""
        current_time = time.time()
        
        # Conta acessos por processo
        process_id = os.getpid()
        if process_id not in self.file_access_count:
            self.file_access_count[process_id] = 0
        self.file_access_count[process_id] += 1
        
        # Detecta atividade suspeita
        if self._is_suspicious_activity(file_path, action, current_time):
            self.callback({
                'type': 'suspicious_file_activity',
                'file_path': file_path,
                'action': action,
                'process_id': process_id,
                'timestamp': current_time
            })
    
    def _is_suspicious_activity(self, file_path: str, action: str, timestamp: float) -> bool:
        """Verifica se a atividade é suspeita"""
        # Verifica extensões suspeitas
        suspicious_extensions = {'.encrypted', '.locked', '.crypto', '.crypt', '.vault'}
        if any(file_path.lower().endswith(ext) for ext in suspicious_extensions):
            return True
        
        # Verifica atividade em massa (muitos arquivos modificados rapidamente)
        if action == "modified":
            recent_modifications = sum(1 for t in self.last_access_time.values() 
                                     if timestamp - t < 5.0)
            if recent_modifications > 50:  # Mais de 50 arquivos em 5 segundos
                return True
        
        self.last_access_time[file_path] = timestamp
        return False

class ProcessMonitor:
    """Monitor de processos do sistema"""
    
    def __init__(self, callback: Callable):
        self.callback = callback
        self.process_history = {}
        self.suspicious_processes = set()
        
    def start_monitoring(self):
        """Inicia monitoramento de processos"""
        threading.Thread(target=self._monitor_processes, daemon=True).start()
    
    def _monitor_processes(self):
        """Monitora processos em tempo real"""
        while True:
            try:
                for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline', 'cpu_percent', 'memory_info']):
                    try:
                        self._analyze_process(proc)
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        continue
                        
                time.sleep(1)  # Verifica a cada segundo
            except Exception as e:
                logging.error(f"Erro no monitoramento de processos: {e}")
                time.sleep(5)
    
    def _analyze_process(self, proc):
        """Analisa processo individual"""
        pid = proc.info['pid']
        name = proc.info['name']
        
        # Verifica processos suspeitos conhecidos
        suspicious_names = {
            'cryptowall', 'locky', 'cerber', 'wannacry', 'petya',
            'notpetya', 'badrabbit', 'gandcrab', 'maze', 'ryuk'
        }
        
        if any(susp_name in name.lower() for susp_name in suspicious_names):
            self.callback({
                'type': 'suspicious_process',
                'process_id': pid,
                'process_name': name,
                'reason': 'known_ransomware_name'
            })
            return
        
        # Verifica uso excessivo de CPU e memória
        cpu_percent = proc.info['cpu_percent']
        memory_info = proc.info['memory_info']
        
        if cpu_percent > 80 and memory_info.rss > 100 * 1024 * 1024:  # 100MB
            self.callback({
                'type': 'high_resource_usage',
                'process_id': pid,
                'process_name': name,
                'cpu_percent': cpu_percent,
                'memory_mb': memory_info.rss / (1024 * 1024)
            })
        
        # Verifica linha de comando suspeita
        cmdline = proc.info['cmdline']
        if cmdline:
            cmdline_str = ' '.join(cmdline).lower()
            suspicious_patterns = [
                'cipher', 'encrypt', 'decrypt', 'crypt',
                'del /f /s /q', 'attrib +h', 'vssadmin delete'
            ]
            
            if any(pattern in cmdline_str for pattern in suspicious_patterns):
                self.callback({
                    'type': 'suspicious_command',
                    'process_id': pid,
                    'process_name': name,
                    'command': cmdline_str
                })

class HoneypotManager:
    """Gerenciador de arquivos honeypot"""
    
    def __init__(self, callback: Callable):
        self.callback = callback
        self.honeypots = {}
        self.honeypot_dirs = [
            os.path.expanduser("~/Documents"),
            os.path.expanduser("~/Desktop"),
            os.path.expanduser("~/Pictures"),
            "C:/Users/Public/Documents"
        ]
    
    def create_honeypots(self):
        """Cria arquivos honeypot em diretórios estratégicos"""
        honeypot_names = [
            "important_document.txt",
            "family_photos.jpg",
            "financial_data.xlsx",
            "personal_notes.txt"
        ]
        
        for directory in self.honeypot_dirs:
            if os.path.exists(directory):
                for name in honeypot_names:
                    honeypot_path = os.path.join(directory, name)
                    try:
                        with open(honeypot_path, 'w') as f:
                            f.write("Este é um arquivo honeypot para detecção de ransomware.")
                        self.honeypots[honeypot_path] = {
                            'created': time.time(),
                            'hash': self._calculate_hash(honeypot_path)
                        }
                    except PermissionError:
                        continue
    
    def _calculate_hash(self, file_path: str) -> str:
        """Calcula hash do arquivo"""
        try:
            with open(file_path, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except:
            return ""
    
    def check_honeypots(self):
        """Verifica integridade dos honeypots"""
        for honeypot_path, info in self.honeypots.items():
            if os.path.exists(honeypot_path):
                current_hash = self._calculate_hash(honeypot_path)
                if current_hash != info['hash']:
                    self.callback({
                        'type': 'honeypot_modified',
                        'file_path': honeypot_path,
                        'original_hash': info['hash'],
                        'current_hash': current_hash
                    })
            else:
                self.callback({
                    'type': 'honeypot_deleted',
                    'file_path': honeypot_path
                })

class AntiRansomwareMonitor:
    """Monitor principal anti-ransomware"""
    
    def __init__(self):
        self.file_monitor = None
        self.process_monitor = None
        self.honeypot_manager = None
        self.observer = None
        self.running = False
        self.callbacks = []
        
    def add_callback(self, callback: Callable):
        """Adiciona callback para eventos"""
        self.callbacks.append(callback)
    
    def start_monitoring(self):
        """Inicia todo o sistema de monitoramento"""
        if self.running:
            return
        
        self.running = True
        
        # Inicia monitor de arquivos
        self.file_monitor = FileMonitor(self._handle_event)
        self.observer = Observer()
        
        # Monitora diretórios importantes
        watch_dirs = [
            os.path.expanduser("~/Documents"),
            os.path.expanduser("~/Desktop"),
            os.path.expanduser("~/Pictures"),
            "C:/Users/Public"
        ]
        
        for directory in watch_dirs:
            if os.path.exists(directory):
                self.observer.schedule(self.file_monitor, directory, recursive=True)
        
        self.observer.start()
        
        # Inicia monitor de processos
        self.process_monitor = ProcessMonitor(self._handle_event)
        self.process_monitor.start_monitoring()
        
        # Inicia honeypots
        self.honeypot_manager = HoneypotManager(self._handle_event)
        self.honeypot_manager.create_honeypots()
        
        # Thread para verificar honeypots periodicamente
        threading.Thread(target=self._honeypot_checker, daemon=True).start()
        
        logging.info("Sistema de monitoramento anti-ransomware iniciado")
    
    def stop_monitoring(self):
        """Para o sistema de monitoramento"""
        self.running = False
        
        if self.observer:
            self.observer.stop()
            self.observer.join()
        
        logging.info("Sistema de monitoramento anti-ransomware parado")
    
    def _handle_event(self, event: Dict):
        """Processa eventos detectados"""
        for callback in self.callbacks:
            try:
                callback(event)
            except Exception as e:
                logging.error(f"Erro no callback: {e}")
    
    def _honeypot_checker(self):
        """Verifica honeypots periodicamente"""
        while self.running:
            try:
                self.honeypot_manager.check_honeypots()
                time.sleep(10)  # Verifica a cada 10 segundos
            except Exception as e:
                logging.error(f"Erro na verificação de honeypots: {e}")
                time.sleep(30)
