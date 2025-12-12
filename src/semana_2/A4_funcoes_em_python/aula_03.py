def analisar_numeros() -> None:
    """Solicita 3 números, armazena em lista e exibe min/max."""
    numeros: list[float] = []

    print("--- Digite 3 números ---")

    # Loop para coletar exatamente 3 números
    while len(numeros) < 3:
        try:
            entrada = input(f"Digite o {len(numeros) + 1}º número: ")
            valor = float(entrada)
            numeros.append(valor)
        except ValueError:
            print("Erro: Entrada inválida. Digite apenas números.")

    # Processamento usando funções built-in (O(n))
    menor = min(numeros)
    maior = max(numeros)

    print("-" * 30)
    print(f"Lista armazenada: {numeros}")
    print(f"Menor elemento: {menor}")
    print(f"Maior elemento: {maior}")


if __name__ == "__main__":
    analisar_numeros()