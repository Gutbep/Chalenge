"""
Sistema de proteção e bloqueio
Interrompe processos maliciosos e protege arquivos
"""

import os
import time
import psutil
import subprocess
import logging
from typing import Dict, List
from datetime import datetime

class ProcessProtector:
    """Proteção contra processos maliciosos"""
    
    def __init__(self):
        self.blocked_processes = set()
        self.quarantine_dir = "C:/AntiRansomware/Quarantine"
        self.log_file = "C:/AntiRansomware/logs/protection.log"
        self._ensure_directories()
    
    def _ensure_directories(self):
        """Cria diretórios necessários"""
        os.makedirs(self.quarantine_dir, exist_ok=True)
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
    
    def terminate_malicious_process(self, process_id: int, reason: str) -> bool:
        """Termina processo malicioso"""
        try:
            process = psutil.Process(process_id)
            process_name = process.name()
            
            # Tenta terminar graciosamente primeiro
            process.terminate()
            time.sleep(2)
            
            # Se ainda estiver rodando, força a terminação
            if process.is_running():
                process.kill()
            
            self._log_action("PROCESS_TERMINATED", {
                'process_id': process_id,
                'process_name': process_name,
                'reason': reason,
                'timestamp': datetime.now().isoformat()
            })
            
            self.blocked_processes.add(process_id)
            return True
            
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            logging.error(f"Erro ao terminar processo {process_id}: {e}")
            return False
    
    def quarantine_file(self, file_path: str, reason: str) -> bool:
        """Move arquivo para quarentena"""
        try:
            if not os.path.exists(file_path):
                return False
            
            filename = os.path.basename(file_path)
            quarantine_path = os.path.join(self.quarantine_dir, f"{int(time.time())}_{filename}")
            
            # Move arquivo para quarentena
            os.rename(file_path, quarantine_path)
            
            self._log_action("FILE_QUARANTINED", {
                'original_path': file_path,
                'quarantine_path': quarantine_path,
                'reason': reason,
                'timestamp': datetime.now().isoformat()
            })
            
            return True
            
        except Exception as e:
            logging.error(f"Erro ao colocar arquivo em quarentena {file_path}: {e}")
            return False
    
    def _log_action(self, action: str, details: Dict):
        """Registra ação de proteção"""
        log_entry = f"[{datetime.now()}] {action}: {details}\n"
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(log_entry)
        except Exception as e:
            logging.error(f"Erro ao escrever log: {e}")

class SystemProtector:
    """Proteção do sistema"""
    
    def __init__(self):
        self.protection_enabled = True
        self.blocked_ips = set()
        self.blocked_ports = set()
        self.critical_files = self._get_critical_files()
    
    def _get_critical_files(self) -> List[str]:
        """Lista arquivos críticos do sistema"""
        return [
            "C:/Windows/System32/config/SAM",
            "C:/Windows/System32/config/SYSTEM",
            "C:/Windows/System32/config/SOFTWARE",
            "C:/Windows/System32/config/SECURITY",
            "C:/Windows/System32/config/DEFAULT"
        ]
    
    def enable_emergency_protection(self):
        """Ativa proteção de emergência"""
        self.protection_enabled = True
        
        # Desabilita serviços suspeitos
        self._disable_suspicious_services()
        
        # Bloqueia conexões suspeitas
        self._block_suspicious_connections()
        
        # Protege arquivos críticos
        self._protect_critical_files()
        
        logging.info("Proteção de emergência ativada")
    
    def _disable_suspicious_services(self):
        """Desabilita serviços suspeitos"""
        suspicious_services = [
            "VSS",  # Volume Shadow Copy Service
            "BITS",  # Background Intelligent Transfer Service
            "WSearch"  # Windows Search
        ]
        
        for service in suspicious_services:
            try:
                subprocess.run([
                    "sc", "config", service, "start=", "disabled"
                ], capture_output=True, check=False)
                logging.info(f"Serviço {service} desabilitado")
            except Exception as e:
                logging.error(f"Erro ao desabilitar serviço {service}: {e}")
    
    def _block_suspicious_connections(self):
        """Bloqueia conexões suspeitas"""
        # Bloqueia portas comuns de ransomware
        suspicious_ports = [445, 3389, 135, 139]  # SMB, RDP, RPC
        
        for port in suspicious_ports:
            try:
                # Bloqueia porta no firewall
                subprocess.run([
                    "netsh", "advfirewall", "firewall", "add", "rule",
                    f"name=BlockRansomwarePort{port}",
                    "dir=in", "action=block", "protocol=TCP", f"localport={port}"
                ], capture_output=True, check=False)
                
                self.blocked_ports.add(port)
                logging.info(f"Porta {port} bloqueada")
            except Exception as e:
                logging.error(f"Erro ao bloquear porta {port}: {e}")
    
    def _protect_critical_files(self):
        """Protege arquivos críticos do sistema"""
        for file_path in self.critical_files:
            if os.path.exists(file_path):
                try:
                    # Remove permissões de escrita
                    subprocess.run([
                        "icacls", file_path, "/deny", "Everyone:(F)"
                    ], capture_output=True, check=False)
                    logging.info(f"Arquivo crítico protegido: {file_path}")
                except Exception as e:
                    logging.error(f"Erro ao proteger arquivo {file_path}: {e}")

class NetworkProtector:
    """Proteção de rede"""
    
    def __init__(self):
        self.blocked_domains = set()
        self.blocked_ips = set()
    
    def block_suspicious_domain(self, domain: str):
        """Bloqueia domínio suspeito"""
        try:
            # Adiciona ao hosts file para bloquear
            hosts_file = "C:/Windows/System32/drivers/etc/hosts"
            with open(hosts_file, 'a') as f:
                f.write(f"\n127.0.0.1 {domain}")
            
            self.blocked_domains.add(domain)
            logging.info(f"Domínio bloqueado: {domain}")
            
        except Exception as e:
            logging.error(f"Erro ao bloquear domínio {domain}: {e}")
    
    def block_suspicious_ip(self, ip: str):
        """Bloqueia IP suspeito"""
        try:
            # Bloqueia IP no firewall
            subprocess.run([
                "netsh", "advfirewall", "firewall", "add", "rule",
                f"name=BlockRansomwareIP{ip}",
                "dir=in", "action=block", "remoteip={ip}"
            ], capture_output=True, check=False)
            
            self.blocked_ips.add(ip)
            logging.info(f"IP bloqueado: {ip}")
            
        except Exception as e:
            logging.error(f"Erro ao bloquear IP {ip}: {e}")

class AntiRansomwareProtector:
    """Proteção principal anti-ransomware"""
    
    def __init__(self):
        self.process_protector = ProcessProtector()
        self.system_protector = SystemProtector()
        self.network_protector = NetworkProtector()
        self.protection_active = False
        self.emergency_mode = False
        
    def start_protection(self):
        """Inicia sistema de proteção"""
        self.protection_active = True
        self.system_protector.enable_emergency_protection()
        logging.info("Sistema de proteção anti-ransomware iniciado")
    
    def stop_protection(self):
        """Para sistema de proteção"""
        self.protection_active = False
        logging.info("Sistema de proteção anti-ransomware parado")
    
    def handle_threat(self, threat_info: Dict) -> bool:
        """Processa ameaça detectada"""
        if not self.protection_active:
            return False
        
        threat_type = threat_info.get('type', '')
        confidence = threat_info.get('confidence', 0)
        
        # Só age se confiança for alta
        if confidence < 70:
            return False
        
        success = False
        
        if threat_type == 'suspicious_process':
            process_id = threat_info.get('process_id')
            if process_id:
                success = self.process_protector.terminate_malicious_process(
                    process_id, threat_info.get('reason', 'Suspicious process')
                )
        
        elif threat_type == 'suspicious_file_activity':
            file_path = threat_info.get('file_path')
            if file_path:
                success = self.process_protector.quarantine_file(
                    file_path, threat_info.get('reason', 'Suspicious file activity')
                )
        
        elif threat_type == 'honeypot_compromise':
            # Ativa modo de emergência
            self.activate_emergency_mode()
            success = True
        
        if success:
            self._log_threat_response(threat_info)
        
        return success
    
    def activate_emergency_mode(self):
        """Ativa modo de emergência"""
        if self.emergency_mode:
            return
        
        self.emergency_mode = True
        
        # Bloqueia todos os processos suspeitos
        self._block_all_suspicious_processes()
        
        # Isola sistema
        self._isolate_system()
        
        logging.critical("MODO DE EMERGÊNCIA ATIVADO - Sistema isolado")
    
    def _block_all_suspicious_processes(self):
        """Bloqueia todos os processos suspeitos"""
        suspicious_names = {
            'cryptowall', 'locky', 'cerber', 'wannacry', 'petya',
            'notpetya', 'badrabbit', 'gandcrab', 'maze', 'ryuk'
        }
        
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if any(susp_name in proc.info['name'].lower() 
                      for susp_name in suspicious_names):
                    self.process_protector.terminate_malicious_process(
                        proc.info['pid'], 'Emergency mode - known ransomware'
                    )
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    
    def _isolate_system(self):
        """Isola sistema de rede"""
        try:
            # Desabilita adaptadores de rede
            subprocess.run([
                "netsh", "interface", "set", "interface", "Ethernet", "disable"
            ], capture_output=True, check=False)
            
            subprocess.run([
                "netsh", "interface", "set", "interface", "Wi-Fi", "disable"
            ], capture_output=True, check=False)
            
            logging.info("Sistema isolado da rede")
            
        except Exception as e:
            logging.error(f"Erro ao isolar sistema: {e}")
    
    def _log_threat_response(self, threat_info: Dict):
        """Registra resposta à ameaça"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'threat_type': threat_info.get('type'),
            'confidence': threat_info.get('confidence'),
            'action_taken': 'Process terminated or file quarantined',
            'details': threat_info
        }
        
        logging.info(f"Threat response: {log_entry}")
    
    def get_protection_status(self) -> Dict:
        """Retorna status da proteção"""
        return {
            'protection_active': self.protection_active,
            'emergency_mode': self.emergency_mode,
            'blocked_processes': len(self.process_protector.blocked_processes),
            'blocked_domains': len(self.network_protector.blocked_domains),
            'blocked_ips': len(self.network_protector.blocked_ips)
        }
