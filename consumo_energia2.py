import os

# --- Constantes ---
PRECO_KWH = 0.80  # Preço do kWh em R$/kWh. Definido como constante em maiúsculas.

# --- Funções de Validação e Entrada ---
def get_int_input(prompt, min_val, max_val):
    """
    Solicita um número inteiro ao usuário, valida se está dentro de um intervalo
    específico e repete a solicitação até que uma entrada válida seja fornecida.

    Args:
        prompt (str): A mensagem a ser exibida para o usuário.
        min_val (int): O valor mínimo permitido para a entrada.
        max_val (int): O valor máximo permitido para a entrada.

    Returns:
        int: O valor inteiro válido inserido pelo usuário.
    """
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Ops! O valor precisa estar entre {min_val} e {max_val}. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")

def valida_nome_computador(nome):
    """
    Valida o comprimento do nome do computador.

    Args:
        nome (str): O nome do computador a ser validado.

    Returns:
        bool: True se o nome for válido, False caso contrário.
    """
    if 3 <= len(nome) <= 20:
        return True
    else:
        print("Poxa! O nome do computador deve ter entre 3 e 20 caracteres.")
        return False

# --- Funções de Cálculo ---
def calcular_consumo_mensal(potencia, horas_por_dia, dias_por_mes, preco_kwh):
    """
    Calcula o consumo mensal de energia em kWh e o custo mensal em Reais.

    Args:
        potencia (int): A potência do computador em Watts.
        horas_por_dia (int): O número de horas por dia que o computador fica ligado.
        dias_por_mes (int): O número de dias por mês que o computador fica ligado.
        preco_kwh (float): O preço do quilowatt-hora (kWh).

    Returns:
        tuple: Uma tupla contendo (consumo_mensal_kwh, custo_mensal).
    """
    consumo_mensal_kwh = (potencia * horas_por_dia * dias_por_mes) / 1000
    custo_mensal = consumo_mensal_kwh * preco_kwh
    return consumo_mensal_kwh, custo_mensal

# --- Funções Utilitárias ---
def limpa_tela():
    """Limpa a tela do console."""
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)

# --- Execução Principal ---
if __name__ == "__main__":
    limpa_tela()
    print("| CALCULADORA DE CONSUMO DE ENERGIA DO COMPUTADOR |\n")

    # Coleta e valida o nome do computador
    while True:
        nome_computador = input("Qual nome você gostaria de dar para este computador? \n")
        if valida_nome_computador(nome_computador):
            break

    # Coleta e valida os dados de consumo usando a função get_int_input
    potencia = get_int_input(
        "Qual é a potência do computador em WATTS (ex: 300, 500, 750)?\n", 1, 1000
    )
    horas_por_dia = get_int_input(
        "Quantas horas por dia o computador fica ligado (1 a 24 horas)?\n", 1, 24
    )
    dias_por_mes = get_int_input(
        "Quantos dias por mês o computador fica ligado (1 a 30 dias)?\n", 1, 30
    )

    # Realiza o cálculo do consumo e custo
    try:
        consumo_kwh, custo = calcular_consumo_mensal(
            potencia, horas_por_dia, dias_por_mes, PRECO_KWH
        )
        limpa_tela()
        print(f"--- Detalhes do Consumo para: {nome_computador} ---\n")
        print(f"Potência configurada: {potencia} W")
        print(f"Consumo mensal estimado: {consumo_kwh:.2f} kWh")
        print(f"Custo mensal estimado: R${custo:.2f}\n")
        print("Obrigado por usar a calculadora de consumo de energia!")

    except Exception as e:
        # Catch-all para qualquer erro inesperado no cálculo, embora a validação prévia minimize isso.
        print(f"\nOcorreu um erro inesperado ao calcular: {e}")