def retornar_soma(n1: float, n2: float, n3: float) -> float:
    """Recebe três números e retorna a soma."""
    return n1 + n2 + n3

if __name__ == "__main__":
    res = retornar_soma(10, 20, 30)
    print(f"Resultado retornado: {res}")