def obter_mes_por_dict() -> None:
    """Converte número em nome do mês usando Dicionário (Hash Map)."""

    # Dicionário: Mapeamento direto Chave -> Valor
    meses: dict[int, str] = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

    try:
        mes_input = int(input("Digite o número do mês (1-12): "))

        # O método .get(chave, valor_padrao) elimina a necessidade de if/else para validação
        resultado = meses.get(mes_input, "Mês inválido (não encontrado)")

        print(f"Entrada {mes_input} -> Saída: {resultado}")

    except ValueError:
        print("Erro: Digite um número inteiro válido.")


if __name__ == "__main__":
    obter_mes_por_dict()