def obter_mes_por_tupla() -> None:
    """Converte número em nome do mês usando Tupla."""
    # Tupla: Estrutura imutável e ordenada
    meses: tuple[str, ...] = (
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    )

    try:
        mes_input = int(input("Digite o número do mês (1-12): "))

        if 1 <= mes_input <= 12:
            # O índice da tupla começa em 0, por isso usamos (mes_input - 1)
            nome_mes = meses[mes_input - 1]
            print(f"O mês {mes_input} corresponde a: {nome_mes}")
        else:
            print("Erro: O número deve ser entre 1 e 12.")

    except ValueError:
        print("Erro: Digite um número inteiro válido.")


if __name__ == "__main__":
    obter_mes_por_tupla()