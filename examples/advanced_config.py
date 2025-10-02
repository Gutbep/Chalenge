#!/usr/bin/env python3
"""
Exemplo de configuração avançada do Anti-Ransomware Shield
Demonstra como personalizar o sistema
"""

import json
import os

def create_advanced_config():
    """Cria configuração avançada"""
    config = {
        "monitoring": {
            "enabled": True,
            "scan_interval": 2,
            "directories": [
                "C:\\Users\\%USERNAME%\\Documents",
                "C:\\Users\\%USERNAME%\\Desktop",
                "C:\\Users\\%USERNAME%\\Pictures",
                "C:\\Users\\%USERNAME%\\Videos"
            ],
            "exclusions": [
                "C:\\Program Files\\",
                "C:\\Windows\\",
                "C:\\ProgramData\\",
                "C:\\Temp\\",
                "C:\\Users\\%USERNAME%\\AppData\\"
            ]
        },
        "detection": {
            "sensitivity": "high",
            "behavioral_analysis": True,
            "signature_detection": True,
            "honeypots": True,
            "thresholds": {
                "mass_file_activity": 15,
                "high_cpu_usage": 70,
                "high_memory_usage": 80
            }
        },
        "protection": {
            "auto_quarantine": True,
            "emergency_mode_threshold": 70,
            "block_suspicious_network": True,
            "protect_critical_files": True,
            "terminate_suspicious_processes": True
        },
        "logging": {
            "level": "DEBUG",
            "max_file_size": "5MB",
            "max_files": 3,
            "console_output": True
        },
        "gui": {
            "theme": "dark",
            "language": "pt_BR",
            "auto_start": True,
            "minimize_to_tray": True
        }
    }
    
    # Salva configuração
    with open("config_advanced.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    
    print("✅ Configuração avançada criada: config_advanced.json")
    print("📋 Características:")
    print("   • Sensibilidade alta")
    print("   • Monitoramento expandido")
    print("   • Proteção reforçada")
    print("   • Logs detalhados")
    print("   • Interface escura")

if __name__ == "__main__":
    create_advanced_config()
