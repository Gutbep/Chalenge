#!/usr/bin/env python3
"""
Exemplo básico de uso do Anti-Ransomware Shield
Demonstra como usar a API do sistema
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.monitor import AntiRansomwareMonitor
from src.core.detector import RansomwareDetector
from src.core.protector import AntiRansomwareProtector

def main():
    """Exemplo básico de uso"""
    print("🛡️ Anti-Ransomware Shield - Exemplo Básico")
    print("=" * 50)
    
    # Cria instâncias dos componentes
    monitor = AntiRansomwareMonitor()
    detector = RansomwareDetector()
    protector = AntiRansomwareProtector()
    
    # Configura callbacks
    def on_threat_detected(event):
        print(f"🚨 Ameaça detectada: {event}")
        protector.handle_threat(event)
    
    monitor.add_callback(on_threat_detected)
    detector.add_callback(on_threat_detected)
    
    # Inicia monitoramento
    print("🔍 Iniciando monitoramento...")
    monitor.start_monitoring()
    
    # Simula detecção
    print("🧪 Simulando detecção...")
    detector.analyze_event({
        'type': 'suspicious_process',
        'process_name': 'crypto.exe',
        'pid': 1234
    })
    
    print("✅ Exemplo concluído!")
    print("💡 Para uso completo, execute: python src/main.py")

if __name__ == "__main__":
    main()
