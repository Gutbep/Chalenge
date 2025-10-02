"""
Aplicação principal do Anti-Ransomware Shield
Integra todos os componentes do sistema
"""

import sys
import os
import logging
import time
from typing import Dict
import signal

# Adiciona diretório src ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.monitor import AntiRansomwareMonitor
from core.detector import RansomwareDetector, BehavioralAnalyzer
from core.protector import AntiRansomwareProtector
from gui.main_window import AntiRansomwareGUI

class AntiRansomwareShield:
    """Aplicação principal anti-ransomware"""
    
    def __init__(self):
        self.monitor = AntiRansomwareMonitor()
        self.detector = RansomwareDetector()
        self.behavioral_analyzer = BehavioralAnalyzer()
        self.protector = AntiRansomwareProtector()
        self.gui = None
        
        self.running = False
        self.emergency_mode = False
        
        # Configura logging
        self.setup_logging()
        
        # Conecta componentes
        self.setup_connections()
    
    def setup_logging(self):
        """Configura sistema de logging"""
        # Cria diretório de logs
        os.makedirs("logs", exist_ok=True)
        
        # Configura logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('logs/antiransomware.log'),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.info("Anti-Ransomware Shield inicializado")
    
    def setup_connections(self):
        """Conecta componentes do sistema"""
        # Monitor -> Detector
        self.monitor.add_callback(self.handle_monitor_event)
        
        # Detector -> Protector
        self.detector.add_callback(self.handle_detection_event)
        
        # Behavioral Analyzer -> Protector
        self.behavioral_analyzer.add_callback(self.handle_behavioral_event)
    
    def handle_monitor_event(self, event: Dict):
        """Processa eventos do monitor"""
        self.logger.info(f"Evento do monitor: {event}")
        
        # Envia para detector
        detection_result = self.detector.analyze_event(event)
        if detection_result:
            self.handle_detection_event(detection_result)
        
        # Envia para analisador comportamental
        self.behavioral_analyzer.add_event(event)
        behavioral_result = self.behavioral_analyzer.analyze_patterns()
        if behavioral_result:
            self.handle_behavioral_event(behavioral_result)
    
    def handle_detection_event(self, detection: Dict):
        """Processa detecções de ransomware"""
        self.logger.warning(f"Ransomware detectado: {detection}")
        
        # Ativa proteção
        if self.protector.handle_threat(detection):
            self.logger.info("Ameaça neutralizada com sucesso")
        else:
            self.logger.error("Falha ao neutralizar ameaça")
    
    def handle_behavioral_event(self, behavioral: Dict):
        """Processa análise comportamental"""
        self.logger.warning(f"Padrão comportamental suspeito: {behavioral}")
        
        # Ativa proteção
        if self.protector.handle_threat(behavioral):
            self.logger.info("Ameaça comportamental neutralizada")
        else:
            self.logger.error("Falha ao neutralizar ameaça comportamental")
    
    def start_protection(self):
        """Inicia sistema de proteção"""
        try:
            self.logger.info("Iniciando sistema de proteção...")
            
            # Inicia monitor
            self.monitor.start_monitoring()
            
            # Inicia proteção
            self.protector.start_protection()
            
            self.running = True
            self.logger.info("Sistema de proteção iniciado com sucesso")
            
        except Exception as e:
            self.logger.error(f"Erro ao iniciar proteção: {e}")
            raise
    
    def stop_protection(self):
        """Para sistema de proteção"""
        try:
            self.logger.info("Parando sistema de proteção...")
            
            # Para monitor
            self.monitor.stop_monitoring()
            
            # Para proteção
            self.protector.stop_protection()
            
            self.running = False
            self.logger.info("Sistema de proteção parado")
            
        except Exception as e:
            self.logger.error(f"Erro ao parar proteção: {e}")
    
    def activate_emergency_mode(self):
        """Ativa modo de emergência"""
        try:
            self.logger.critical("ATIVANDO MODO DE EMERGÊNCIA")
            
            # Para monitoramento normal
            self.monitor.stop_monitoring()
            
            # Ativa proteção de emergência
            self.protector.activate_emergency_mode()
            
            self.emergency_mode = True
            self.logger.critical("MODO DE EMERGÊNCIA ATIVADO")
            
        except Exception as e:
            self.logger.error(f"Erro ao ativar modo de emergência: {e}")
    
    def get_status(self) -> Dict:
        """Retorna status do sistema"""
        return {
            'running': self.running,
            'emergency_mode': self.emergency_mode,
            'monitor_status': 'active' if self.monitor.running else 'inactive',
            'protection_status': self.protector.get_protection_status(),
            'threat_level': self.detector.get_overall_threat_level()
        }
    
    def run_gui(self):
        """Executa interface gráfica"""
        try:
            self.gui = AntiRansomwareGUI()
            
            # Conecta GUI ao sistema
            self.gui.start_protection_callback = self.start_protection
            self.gui.stop_protection_callback = self.stop_protection
            self.gui.emergency_mode_callback = self.activate_emergency_mode
            self.gui.status_callback = self.get_status
            
            self.gui.run()
            
        except Exception as e:
            self.logger.error(f"Erro na interface gráfica: {e}")
            raise
    
    def run_console(self):
        """Executa em modo console"""
        try:
            self.logger.info("Executando em modo console...")
            
            # Inicia proteção
            self.start_protection()
            
            # Loop principal
            while True:
                try:
                    time.sleep(1)
                    
                    # Verifica status
                    status = self.get_status()
                    if status['emergency_mode']:
                        self.logger.critical("Sistema em modo de emergência!")
                        break
                        
                except KeyboardInterrupt:
                    self.logger.info("Interrupção pelo usuário")
                    break
                except Exception as e:
                    self.logger.error(f"Erro no loop principal: {e}")
                    time.sleep(5)
            
            # Para proteção
            self.stop_protection()
            
        except Exception as e:
            self.logger.error(f"Erro no modo console: {e}")
            raise

def signal_handler(signum, frame):
    """Handler para sinais do sistema"""
    print("\nRecebido sinal de interrupção. Parando sistema...")
    sys.exit(0)

def main():
    """Função principal"""
    try:
        # Configura handlers de sinal
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        
        # Cria aplicação
        app = AntiRansomwareShield()
        
        # Verifica argumentos da linha de comando
        if len(sys.argv) > 1 and sys.argv[1] == '--console':
            # Modo console
            app.run_console()
        else:
            # Modo GUI
            app.run_gui()
            
    except Exception as e:
        print(f"Erro fatal: {e}")
        logging.error(f"Erro fatal: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
