import os

#componentes
def calcular_consumo_mensal(potencia, horas_por_dia, dias_por_mes, preco_kwh):
    # Soma total de watts dos componentes
    #consumo_total_watts = sum(componentes.values())
    
    if verifica_dados(potencia, horas_por_dia, dias_por_mes):
        # Converte para kWh (Watts × horas × dias / 1000)
        consumo_mensal_kwh = (potencia * horas_por_dia * dias_por_mes) / 1000

        # Custo mensal
        custo_mensal = consumo_mensal_kwh * preco_kwh

        return potencia, consumo_mensal_kwh, custo_mensal
    else:
        return None
    
def verifica_dados(potencia, horas_por_dia, dias_por_mes):
    
    resultado_wallts =  (0 < potencia <= 1000 and 1 <= horas_por_dia <= 24 and <= dias_por_mes <= 30)
    return (
       
    )


def limpa_tela():
    
    """Limpa a tela do console."""
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)


# --- Execução principal ---
if __name__ == "__main__":
    limpa_tela()
    print("| CALCULADORA DE CONSUMO DE ENERGIA DO COMPUTADOR |")
    print("")

    try:
        computador    = str(input("Insira a marca e modelo do computador: \n"))
        potencia      = int(input("Insira a potência do computador em (WATTS):\n"))
        horas_por_dia = int(input("Insira quantas horas por dia o computador fica ligado (1 a 24):\n"))
        dias_por_mes  = int(input("Insira quantos dias por mês o computador fica ligado (1 a 30):\n"))
        preco_kwh     = 0.80  # R$/kWh

        resultado = calcular_consumo_mensal(potencia, horas_por_dia, dias_por_mes, preco_kwh)

        if resultado:
            consumo_total, consumo_kwh, custo = resultado
            limpa_tela()
            print(f"Consumo total estimado: {consumo_total} W")
            print(f"Consumo mensal: {consumo_kwh:.2f} kWh")
            print(f"Custo mensal estimado: R${custo:.2f}")
        else:
            print("\n[ERRO] Um ou mais valores inseridos estão fora dos limites permitidos.")
            print("Potência deve estar entre 1 e 1000 W")
            print("Horas por dia: entre 1 e 24")
            print("Dias por mês: entre 1 e 30")
    except ValueError:
        print("\n[ERRO] Entrada inválida. Por favor, insira apenas números inteiros.")