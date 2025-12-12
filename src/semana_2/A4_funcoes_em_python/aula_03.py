# Aula_03

"""
F-Strings: Substituí a concatenação antiga ('Country: ', country) por f-strings (f'Country: {country}') para maior legibilidade e desempenho.
Type Hints: Adicionei → None e → float para deixar claro o que entra e o que sai da função.
Main Block: Encapsulei os testes no if __name__ == "__main__": para evitar que o código rode sozinho se você importar essas funções em outro arquivo.
"""


"""
exemplo_wargs
"""

def world_cup_titles(country: str, *args: str) -> None:
    """
    Imprime o país e os anos em que ganhou a copa.
    O parâmetro *args recebe uma tupla com todos os anos passados.
    """
    print(f'Country: {country}')

    # Iterando sobre os argumentos variáveis
    for title in args:
        print(f'Year: {title}')

if __name__ == "__main__":
    print("--- Teste 1: Brasil (Múltiplos args) ---")
    # Passando 5 argumentos posicionais extras
    world_cup_titles('Brasil', '1958', '1962', '1970', '1994', '2002')

    print("\n--- Teste 2: Espanha (Um arg) ---")
    # Passando apenas 1 argumento posicional extra
    world_cup_titles('Espanha', '2010')

"""
exemplo_kwargs
"""

def calculate_price(value: float, **kwargs: float) -> float:
        """
        Calcula o preço final aplicando impostos e descontos se fornecidos.
        O parâmetro **kwargs recebe um dicionário com os parâmetros nomeados.
        """
        # .get() é seguro: retorna None se a chave não existir
        tax_percentage = kwargs.get('tax_percentage')
        discount = kwargs.get('discount')

        if tax_percentage:
            value += value * (tax_percentage / 100)

        if discount:
            value -= discount

        return value


    if __name__ == "__main__":
        print("--- Testes de Cálculo de Preço ---")

        # Caso 1: Sem argumentos opcionais
        preco_base = calculate_price(100.0)
        print(f"Preço base: {preco_base}")  # Esp: 100.0

        # Caso 2: Apenas desconto (nomeado)
        com_desconto = calculate_price(100.0, discount=5.0)
        print(f"Com desconto: {com_desconto}")  # Esp: 95.0

        # Caso 3: Apenas imposto (nomeado)
        com_imposto = calculate_price(100.0, tax_percentage=7)
        print(f"Com imposto: {com_imposto}")  # Esp: 107.0

        # Caso 4: Imposto e Desconto (ordem não importa no kwargs)
        completo = calculate_price(100.0, tax_percentage=7, discount=5.0)
        print(f"Completo: {completo}")  # Esp: 102.0