def somar_args(*args: float) -> float:
    """Recebe n argumentos numéricos e retorna a soma."""
    return sum(args)

if __name__ == "__main__":
    # Podemos passar quantos argumentos quisermos
    print(f"Soma args: {somar_args(1, 2, 3, 4, 5)}")