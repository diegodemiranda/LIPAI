def calcular_volume(aquario: dict) -> float:
    """
    Calcula o volume em litros.
    Fórmula: (comp * alt * larg) / 1000
    """
    volume = (aquario['comprimento'] * aquario['altura'] * aquario['largura']) / 1000
    return volume


def calcular_potencia_termostato(volume: float, aquario: dict) -> float:
    """
    Calcula a potência necessária (Watts).
    Fórmula: vol * 0.05 * (temp_desejada - temp_ambiente)
    """
    delta_temp = aquario['temp_desejada'] - aquario['temp_ambiente']

    # Se a temperatura ambiente for maior que a desejada, potência é 0 (aquecedor não liga)
    if delta_temp < 0:
        return 0.0

    potencia = volume * 0.05 * delta_temp
    return round(potencia, 2)


def calcular_filtragem(volume: float) -> tuple[float, float]:
    """
    Retorna uma tupla com (filtragem_minima, filtragem_maxima).
    Regra: 2 a 3 vezes o volume.
    """
    minima = volume * 2
    maxima = volume * 3
    return (minima, maxima)


if __name__ == "__main__":
    print("--- Configuração do Aquário ---")

    try:
        # Coleta de dados
        print("Insira as medidas em cm:")
        comp = float(input("Comprimento: "))
        alt = float(input("Altura: "))
        larg = float(input("Largura: "))

        print("\nInsira as temperaturas em °C:")
        temp_amb = float(input("Temperatura ambiente média: "))
        temp_des = float(input("Temperatura desejada para os peixes: "))

        # Estrutura de dados
        dados_aquario = {
            'comprimento': comp,
            'altura': alt,
            'largura': larg,
            'temp_ambiente': temp_amb,
            'temp_desejada': temp_des
        }

        # Processamento
        vol_litros = calcular_volume(dados_aquario)
        potencia = calcular_potencia_termostato(vol_litros, dados_aquario)
        filt_min, filt_max = calcular_filtragem(vol_litros)

        # Saída formatada
        print("\n" + "=" * 30)
        print("RELATÓRIO DO AQUÁRIO")
        print("=" * 30)
        print(f"Volume de água:       {vol_litros:.2f} Litros")
        print(f"Potência Termostato:  {potencia:.2f} Watts")
        print(f"Filtragem necessária: Entre {filt_min:.0f} e {filt_max:.0f} Litros/hora")
        print("=" * 30)

    except ValueError:
        print("Erro: Certifique-se de digitar apenas números.")