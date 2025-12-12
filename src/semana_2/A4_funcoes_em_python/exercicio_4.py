def calcular_imc(individuo: dict) -> float:
    """Retorna o IMC calculado com base no dicionário do indivíduo."""
    peso = individuo.get('peso', 0.0)
    altura = individuo.get('altura', 1.0)

    # Evita divisão por zero
    if altura <= 0:
        return 0.0

    imc = peso / (altura ** 2)
    return round(imc, 2)


def obter_classificacao(imc: float) -> str:
    """Retorna a classificação da OMS com base no IMC."""
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25.0 <= imc <= 29.9:
        return "Excesso de peso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade de Classe 1"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"


def situacao_individuo(imc: float) -> str:
    """Define a ação recomendada baseada no IMC."""
    if imc < 18.5:
        return "ganhar peso"
    elif 18.5 <= imc <= 24.9:
        return "normal"
    else:
        return "perder peso"


if __name__ == "__main__":
    print("--- Calculadora de IMC ---")
    try:
        peso_input = float(input("Digite seu peso (kg): "))
        altura_input = float(input("Digite sua altura (m): "))

        individuo = {
            'peso': peso_input,
            'altura': altura_input
        }

        valor_imc = calcular_imc(individuo)
        classificacao = obter_classificacao(valor_imc)
        situacao = situacao_individuo(valor_imc)

        print("-" * 30)
        print(f"IMC: {valor_imc}")
        print(f"Classificação: {classificacao}")
        print(f"Situação: {situacao}")

    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")