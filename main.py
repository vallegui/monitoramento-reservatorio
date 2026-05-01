import colorama
from colorama import Fore, Style

# Inicializa o colorama para garantir compatibilidade com diferentes sistemas (como Windows)
colorama.init()

def exibir_status_reservatorio(niveis):
    """
    Função responsável por definir a cor e exibir a mensagem 
    conforme o nível informado na lista.
    """
    print("-" * 40)
    print("SISTEMA DE MONITORAMENTO DE RESERVATÓRIO")
    print("-" * 40)

    for nivel in niveis:
        # Lógica para associar nível à cor e mensagem
        if nivel == 1:
            status = "Muito baixo (crítico)"
            cor = Fore.RED
        elif nivel == 2:
            status = "Baixo"
            cor = Fore.YELLOW
        elif nivel == 3:
            status = "Médio"
            cor = Fore.GREEN
        elif nivel == 4:
            status = "Alto"
            cor = Fore.CYAN
        elif nivel == 5:
            status = "Muito alto (alerta)"
            cor = Fore.BLUE
        else:
            status = "Nível Desconhecido"
            cor = Fore.WHITE

        # Exibição da mensagem com a cor correspondente
        print(f"Monitoramento: Nível {nivel} -> {cor}{status}{Style.RESET_ALL}")

    # Garante que o terminal volte ao padrão após a execução
    print("-" * 40)
    print("Fim do monitoramento.")

if __name__ == "__main__":
    # Simulação de dados: Lista representando a variação dos níveis
    historico_niveis = [1, 2, 3, 4, 5]
    
    # Execução do sistema
    exibir_status_reservatorio(historico_niveis)
