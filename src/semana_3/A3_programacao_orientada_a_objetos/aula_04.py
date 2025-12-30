""" Aula 04 - Propriedades
Forma de controle de acesso aos atributos de uma instância.
Usamos @property para expor getters/setters com validação.
"""

from __future__ import annotations

class Retangulo:
    """Classe Retangulo com propriedades para base e altura.

    Valida que base e altura sejam > 0 ao atribuir.
    """

    def __init__(self, base: float, altura: float):
        """Construtor da classe Retangulo."""
        # usa atributos privados para a propriedade
        self._base = None
        self._altura = None
        self.base = base
        self.altura = altura

    @classmethod
    def from_list(cls, lista):
        """Cria uma instância a partir de uma lista/tupla [base, altura]."""
        return cls(float(lista[0]), float(lista[1]))

    @classmethod
    def from_string(cls, rep_retangulo: str):
        """Cria uma instância a partir de uma string 'base,altura'."""
        base, altura = rep_retangulo.split(',')
        return cls(float(base.strip()), float(altura.strip()))

    @property
    def base(self) -> float:
        """Getter para a base."""
        return self._base

    @base.setter
    def base(self, value: float):
        """Setter para a base com validação (maior que zero)."""
        if value is None:
            raise ValueError('A base não pode ser None')
        value = float(value)
        if value <= 0:
            raise ValueError('A base deve ser maior que zero')
        self._base = value

    @property
    def altura(self) -> float:
        """Getter para a altura."""
        return self._altura

    @altura.setter
    def altura(self, value: float):
        """Setter para a altura com validação (maior que zero)."""
        if value is None:
            raise ValueError('A altura não pode ser None')
        value = float(value)
        if value <= 0:
            raise ValueError('A altura deve ser maior que zero')
        self._altura = value

    def calcular_area(self) -> float:
        """Retorna a área do retângulo."""
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        """Retorna o perímetro do retângulo."""
        return 2 * (self.base + self.altura)

    def __repr__(self) -> str:
        return f"Retangulo(base={self.base}, altura={self.altura})"


if __name__ == "__main__":
    # instâncias de exemplo
    retangulo1 = Retangulo(10.0, 5.0)
    retangulo2 = Retangulo(6.0, 3.0)

    # cria uma instância de um objeto Retangulo usando classmethod from_list
    print('--- Retangulo 3 ---')
    retangulo3 = Retangulo.from_list((3, 4))
    print('Retângulo criado pelo método de classe (from_list)')
    print(f'base -> {retangulo3.base} altura -> {retangulo3.altura}')
    print(f'Área -> {retangulo3.calcular_area():.2f}  Perímetro -> {retangulo3.calcular_perimetro():.2f}')

    # cria uma instância de um objeto Retangulo por meio de uma string
    print('\n--- Retangulo 4 ---')
    retangulo4 = Retangulo.from_string("5.5,3.6")
    print('Retângulo criado pelo método de classe (from_string)')
    print(f'base -> {retangulo4.base} altura -> {retangulo4.altura}')
    print(f'Área -> {retangulo4.calcular_area():.2f}  Perímetro -> {retangulo4.calcular_perimetro():.2f}')

    # imprimir na tela área e perimetro retangulo1
    print('\n---- Retangulo 1 ----')
    print(f'Área: {retangulo1.calcular_area():.2f}')
    print(f'Perímetro: {retangulo1.calcular_perimetro():.2f}')

    # exemplo rápido
    ret = Retangulo.from_list((10, 8))
    print('\nExemplo rápido: ', ret.base, ret.altura)
