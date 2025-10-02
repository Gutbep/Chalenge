"""
Sistema de detecção de ransomware
Analisa padrões e comportamentos suspeitos
"""

import os
import time
import re
from typing import Dict, List, Tuple, Optional
from collections import defaultdict, deque

class RansomwareDetector:
    """Detector principal de ransomware"""
    
    def __init__(self):
        self.suspicion_score = defaultdict(int)
        self.file_patterns = deque(maxlen=1000)
        self.process_patterns = deque(maxlen=1000)
        self.detection_threshold = 50  # Pontuação mínima para considerar ransomware
        self.known_ransomware_hashes = set()
        self.suspicious_extensions = {
            '.encrypted', '.locked', '.crypto', '.crypt', '.vault',
            '.enc', '.cryp1', '.cryp2', '.crypz',
            '.dharma', '.locky', '.cerber', '.petya',
            # Ransomwares específicos
            '.wncryt', '.wcry',  # WannaCry
            '.petya', '.locked',  # Petya/NotPetya
            '.locky',  # Locky
            '.ryuk', '.crypted',  # Ryuk
            '.sodinokibi', '.revil',  # Sodinokibi/REvil
            '.maze', '.maze_encrypted',  # Maze
            '.conti', '.conti_encrypted',  # Conti
            '.darkside', '.darkside_encrypted'  # DarkSide
        }
        self.callbacks = []
    
    def add_callback(self, callback):
        """Adiciona callback para eventos"""
        self.callbacks.append(callback)
    
    def analyze_event(self, event: Dict) -> Optional[Dict]:
        """Analisa evento e retorna detecção se houver"""
        event_type = event.get('type', '')
        
        if event_type == 'suspicious_file_activity':
            return self.analyze_file_activity(event)
        elif event_type == 'suspicious_process':
            return self.analyze_process_activity(event)
        elif event_type == 'honeypot_modified' or event_type == 'honeypot_deleted':
            return self.analyze_honeypot_activity(event)
        
        return None
        
    def analyze_file_activity(self, event: Dict) -> Optional[Dict]:
        """Analisa atividade de arquivo para detectar ransomware"""
        file_path = event.get('file_path', '')
        action = event.get('action', '')
        
        # Verifica extensões suspeitas
        if self._check_suspicious_extension(file_path):
            self.suspicion_score['suspicious_extensions'] += 20
            return {
                'type': 'suspicious_extension',
                'file_path': file_path,
                'confidence': 80,
                'reason': 'Suspicious file extension detected'
            }
        
        # Verifica padrões de criptografia
        if self._check_encryption_patterns(file_path, action):
            self.suspicion_score['encryption_patterns'] += 15
            return {
                'type': 'encryption_pattern',
                'file_path': file_path,
                'confidence': 70,
                'reason': 'Encryption pattern detected'
            }
        
        # Verifica atividade em massa
        if self._check_mass_file_activity():
            self.suspicion_score['mass_activity'] += 25
            return {
                'type': 'mass_file_activity',
                'confidence': 85,
                'reason': 'Mass file modification detected'
            }
        
        return None
    
    def analyze_process_activity(self, event: Dict) -> Optional[Dict]:
        """Analisa atividade de processo para detectar ransomware"""
        process_id = event.get('process_id')
        process_name = event.get('process_name', '')
        command = event.get('command', '')
        
        # Verifica nomes de processos suspeitos
        if self._check_suspicious_process_name(process_name):
            self.suspicion_score['suspicious_process'] += 30
            return {
                'type': 'suspicious_process',
                'process_id': process_id,
                'process_name': process_name,
                'confidence': 90,
                'reason': 'Known ransomware process name'
            }
        
        # Verifica comandos suspeitos
        if command and self._check_suspicious_command(command):
            self.suspicion_score['suspicious_command'] += 25
            return {
                'type': 'suspicious_command',
                'process_id': process_id,
                'command': command,
                'confidence': 80,
                'reason': 'Suspicious command detected'
            }
        
        # Verifica uso excessivo de recursos
        if event.get('type') == 'high_resource_usage':
            cpu_percent = event.get('cpu_percent', 0)
            memory_mb = event.get('memory_mb', 0)
            
            if cpu_percent > 90 and memory_mb > 200:
                self.suspicion_score['high_resource_usage'] += 15
                return {
                    'type': 'high_resource_usage',
                    'process_id': process_id,
                    'confidence': 60,
                    'reason': 'Excessive resource usage'
                }
        
        return None
    
    def analyze_honeypot_activity(self, event: Dict) -> Optional[Dict]:
        """Analisa atividade em honeypots"""
        if event.get('type') in ['honeypot_modified', 'honeypot_deleted']:
            self.suspicion_score['honeypot_activity'] += 40
            return {
                'type': 'honeypot_compromise',
                'file_path': event.get('file_path'),
                'confidence': 95,
                'reason': 'Honeypot file compromised'
            }
        
        return None
    
    def get_overall_threat_level(self) -> Tuple[int, str]:
        """Retorna nível geral de ameaça"""
        total_score = sum(self.suspicion_score.values())
        
        if total_score >= 100:
            return total_score, "CRITICAL"
        elif total_score >= 75:
            return total_score, "HIGH"
        elif total_score >= 50:
            return total_score, "MEDIUM"
        elif total_score >= 25:
            return total_score, "LOW"
        else:
            return total_score, "SAFE"
    
    def _check_suspicious_extension(self, file_path: str) -> bool:
        """Verifica se arquivo tem extensão suspeita"""
        _, ext = os.path.splitext(file_path.lower())
        return ext in self.suspicious_extensions
    
    def _check_encryption_patterns(self, file_path: str, action: str) -> bool:
        """Verifica padrões de criptografia"""
        # Verifica se arquivo foi renomeado com extensão suspeita
        if action == "modified" and self._check_suspicious_extension(file_path):
            return True
        
        # Verifica padrões de nomes de arquivos criptografados
        filename = os.path.basename(file_path).lower()
        encryption_patterns = [
            r'.*\.encrypted$',
            r'.*\.locked$',
            r'.*\.crypto$',
            r'.*\.crypt\d*$',
            r'.*\.vault$'
        ]
        
        return any(re.match(pattern, filename) for pattern in encryption_patterns)
    
    def _check_mass_file_activity(self) -> bool:
        """Verifica atividade em massa de arquivos"""
        current_time = time.time()
        recent_activities = [
            activity for activity in self.file_patterns
            if current_time - activity.get('timestamp', 0) < 10  # Últimos 10 segundos
        ]
        
        return len(recent_activities) > 20  # Mais de 20 arquivos em 10 segundos
    
    def _check_suspicious_process_name(self, process_name: str) -> bool:
        """Verifica se nome do processo é suspeito"""
        suspicious_names = {
            'cryptowall', 'locky', 'cerber', 'wannacry', 'petya',
            'notpetya', 'badrabbit', 'gandcrab', 'maze', 'ryuk',
            'sodinokibi', 'conti', 'revil', 'babuk', 'clop',
            # Ransomwares específicos analisados
            'wannacry', 'wcry',  # WannaCry
            'petya', 'notpetya',  # Petya/NotPetya
            'locky',  # Locky
            'ryuk',  # Ryuk
            'sodinokibi', 'revil',  # Sodinokibi/REvil
            'maze',  # Maze
            'conti',  # Conti
            'darkside'  # DarkSide
        }
        
        process_lower = process_name.lower()
        return any(susp_name in process_lower for susp_name in suspicious_names)
    
    def _check_suspicious_command(self, command: str) -> bool:
        """Verifica se comando é suspeito"""
        suspicious_patterns = [
            r'cipher\s+/e',  # Criptografia com cipher
            r'vssadmin\s+delete',  # Deletar shadow copies
            r'wmic\s+shadowcopy\s+delete',  # Deletar shadow copies via wmic
            r'bcdedit\s+/set\s+recoveryenabled\s+no',  # Desabilitar recovery
            r'fsutil\s+behavior\s+set\s+disablelastaccess\s+1',  # Desabilitar last access
            r'vssadmin\s+resize\s+shadowstorage',  # Redimensionar shadow storage
            r'wmic\s+process\s+where\s+name="vssadmin"',  # Processos vssadmin
            r'powershell.*encrypt',  # PowerShell com encrypt
            r'certutil.*decode',  # Certutil para decodificar
            r'bitsadmin.*transfer'  # Bitsadmin para transferir
        ]
        
        command_lower = command.lower()
        return any(re.search(pattern, command_lower) for pattern in suspicious_patterns)
    
    def reset_suspicion_score(self):
        """Reseta pontuação de suspeita"""
        self.suspicion_score.clear()
    
    def add_file_pattern(self, pattern: Dict):
        """Adiciona padrão de arquivo para análise"""
        self.file_patterns.append(pattern)
    
    def add_process_pattern(self, pattern: Dict):
        """Adiciona padrão de processo para análise"""
        self.process_patterns.append(pattern)

class BehavioralAnalyzer:
    """Analisador comportamental avançado"""
    
    def __init__(self):
        self.file_access_patterns = defaultdict(list)
        self.process_behavior = defaultdict(dict)
        self.timeline = deque(maxlen=10000)
        self.callbacks = []
    
    def add_callback(self, callback):
        """Adiciona callback para eventos"""
        self.callbacks.append(callback)
    
    def add_event(self, event: Dict):
        """Adiciona evento para análise"""
        self.timeline.append({
            'timestamp': time.time(),
            'event': event
        })
    
    def analyze_patterns(self) -> Optional[Dict]:
        """Analisa padrões comportamentais"""
        return self._detect_ransomware_pattern()
        
    def analyze_behavioral_patterns(self, events: List[Dict]) -> Optional[Dict]:
        """Analisa padrões comportamentais"""
        for event in events:
            self.timeline.append({
                'timestamp': time.time(),
                'event': event
            })
        
        # Verifica padrão de ransomware típico
        if self._detect_ransomware_pattern():
            return {
                'type': 'behavioral_ransomware_detection',
                'confidence': 95,
                'reason': 'Ransomware behavioral pattern detected'
            }
        
        return None
    
    def _detect_ransomware_pattern(self) -> bool:
        """Detecta padrão típico de ransomware"""
        current_time = time.time()
        recent_events = [
            event for event in self.timeline
            if current_time - event['timestamp'] < 60  # Último minuto
        ]
        
        # Verifica se há:
        # 1. Muitas modificações de arquivos
        # 2. Criação de arquivos com extensões suspeitas
        # 3. Comandos suspeitos
        # 4. Uso excessivo de recursos
        
        file_modifications = sum(1 for event in recent_events 
                                if event['event'].get('type') == 'suspicious_file_activity')
        
        suspicious_commands = sum(1 for event in recent_events 
                                 if event['event'].get('type') == 'suspicious_command')
        
        high_resource_usage = sum(1 for event in recent_events 
                                 if event['event'].get('type') == 'high_resource_usage')
        
        # Critérios para detecção de ransomware
        return (file_modifications > 10 and 
                suspicious_commands > 2 and 
                high_resource_usage > 3)
