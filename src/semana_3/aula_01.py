"""Aula 01 - Debug

Arquivo de exemplo: define funções para somar três notas e calcular a média.
"""


def somar(n1, n2, n3):
    """Retorna a soma das notas."""
    soma = n1 + n2 + n3
    return soma


def calcular_media(n1, n2, n3):
    """Calcula a média das notas."""
    soma = somar(n1, n2, n3)
    mean = soma / 3
    return mean


if __name__ == "__main__":
    # breakpoint()  # cria um ponto de parada (descomente se desejar debugar)
    NOTA1 = 10.0
    NOTA2 = 3.0
    NOTA3 = 5.5

    media = calcular_media(NOTA1, NOTA2, NOTA3)
    print(media)
