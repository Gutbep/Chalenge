"""
Correção do Processo de Teste
Remove simulação e implementa monitoramento real
"""

import os
import shutil

def fix_test_process():
    """Remove processo de teste e implementa monitoramento real"""
    print("🔧 Corrigindo processo de teste...")
    
    # Lê o arquivo original
    with open("src/gui/main_window.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Substitui a função update_process_list
    old_function = '''    def update_process_list(self):
        """Atualiza lista de processos"""
        try:
            # Limpa lista atual
            for item in self.process_tree.get_children():
                self.process_tree.delete(item)
            
            # Adiciona processos suspeitos (simulação)
            suspicious_processes = [
                ("1234", "suspicious.exe", "85%", "150 MB", "⚠️ Suspeito"),
                ("5678", "crypto.exe", "90%", "200 MB", "🚨 Malicioso"),
            ]
            
            for proc in suspicious_processes:
                self.process_tree.insert('', 'end', values=proc)
                
        except Exception as e:
            logging.error(f"Erro ao atualizar lista de processos: {e}")'''
    
    new_function = '''    def update_process_list(self):
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
            logging.error(f"Erro ao atualizar lista de processos: {e}")'''
    
    # Substitui no conteúdo
    if old_function in content:
        content = content.replace(old_function, new_function)
        
        # Salva arquivo corrigido
        with open("src/gui/main_window.py", "w", encoding="utf-8") as f:
            f.write(content)
        
        print("✅ Processo de teste removido")
        print("✅ Monitoramento real implementado")
        
        # Atualiza executáveis
        update_executables()
        
        return True
    else:
        print("❌ Função não encontrada")
        return False

def update_executables():
    """Atualiza executáveis com correção"""
    print("🔄 Atualizando executáveis...")
    
    try:
        # Atualiza executável simples
        if os.path.exists("dist/executavel_simples"):
            shutil.copytree("src", "dist/executavel_simples/src", dirs_exist_ok=True)
            print("✅ Executável simples atualizado")
        
        # Atualiza versão portável
        if os.path.exists("dist/portable"):
            shutil.copytree("src", "dist/portable/src", dirs_exist_ok=True)
            print("✅ Versão portável atualizada")
        
        print("✅ Todos os executáveis atualizados")
        
    except Exception as e:
        print(f"❌ Erro ao atualizar executáveis: {e}")

def main():
    """Função principal"""
    print("=" * 60)
    print("🔧 Anti-Ransomware Shield - Correção de Processo de Teste")
    print("=" * 60)
    print()
    
    print("⚠️  PROCESSO DE TESTE IDENTIFICADO!")
    print("   Localização: src/gui/main_window.py linha 400-404")
    print("   Problema: Simulação de processos suspeitos")
    print()
    
    if fix_test_process():
        print()
        print("🎉 CORREÇÃO APLICADA COM SUCESSO!")
        print("=" * 60)
        print()
        print("✅ Mudanças aplicadas:")
        print("   • Processo de teste removido")
        print("   • Monitoramento real implementado")
        print("   • Executáveis atualizados")
        print()
        print("🛡️ Agora o programa mostra apenas processos reais do sistema!")
        print("   • Processos com nomes suspeitos são marcados")
        print("   • Processos com alto CPU são identificados")
        print("   • Processos com alta memória são sinalizados")
        print("   • Limite de 20 processos para performance")
        
    else:
        print("❌ Falha ao aplicar correção")
    
    input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
