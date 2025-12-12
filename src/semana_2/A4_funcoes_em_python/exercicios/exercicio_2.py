def somar_tupla(numeros: tuple[float, ...]) -> float:
    """Recebe uma tupla de números e retorna a soma usando built-in."""
    return sum(numeros)

if __name__ == "__main__":
    minha_tupla = (10.5, 20.0, 30.5)
    print(f"Soma da tupla: {somar_tupla(minha_tupla)}")