

def calcular_consumo_mensal(componentes, horas_por_dia, dias_por_mes, preco_kwh):
    # Soma total de watts dos componentes
    consumo_total_watts = sum(componentes.values())

    # Converte para kWh (Watts × horas × dias / 1000)
    consumo_mensal_kwh = (consumo_total_watts * horas_por_dia * dias_por_mes) / 1000

    # Custo mensal
    custo_mensal = consumo_mensal_kwh * preco_kwh

    # Resultados
    return consumo_total_watts, consumo_mensal_kwh, custo_mensal


# --- Exemplo de uso ---
if __name__ == "__main__":

    print("Digite as informações a seguir para realizar o calculo.\n")
    cpu = float(input("CPU (em Watts): "))
    gpu = float(input("GPU (em Watts): "))
    ram = float(input("RAM (em Watts): "))
    ssd = float(input("SSD (em Watts): "))
    ventoinha = float(input("Ventoinha (em Watts): "))
    placa_mae = float(input("Placa Mãe (em Watts): "))

    componentes = {
        "CPU": cpu,
        "GPU": gpu,
        "RAM": ram,
        "SSD": ssd,
        "Ventoinhas": ventoinha,
        "Placa-mãe": placa_mae
    }

    horas_por_dia = 5
    dias_por_mes = 30
    preco_kwh = 0.80  # R$/kWh

    consumo_total, consumo_kwh, custo = calcular_consumo_mensal(componentes, horas_por_dia, dias_por_mes, preco_kwh)

    print(f"Consumo total estimado: {consumo_total} W")
    print(f"Consumo mensal: {consumo_kwh:.2f} kWh")
    print(f"Custo mensal estimado: R$ {custo:.2f}")