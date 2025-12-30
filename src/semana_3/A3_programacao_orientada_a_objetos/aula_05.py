""" Aula 05 - Métodos especiais

Exemplos de __str__ e __repr__ e uso de propriedades.
"""

from __future__ import annotations

class Retangulo:
    """Classe Retangulo com propriedades e métodos especiais."""

    def __init__(self, base: float, altura: float):
        """Construtor da classe Retangulo."""
        self._base = None
        self._altura = None
        self.base = base
        self.altura = altura

    @property
    def base(self) -> float:
        """Getter para a base."""
        return self._base

    @base.setter
    def base(self, value: float):
        """Setter para base com validação (maior que zero)."""
        if value is None:
            raise ValueError('A base não pode ser None')
        value = float(value)
        if value <= 0.0:
            raise ValueError('A base deve ser maior que zero')
        self._base = value

    @property
    def altura(self) -> float:
        """Getter para a altura."""
        return self._altura

    @altura.setter
    def altura(self, value: float):
        """Setter para altura com validação (maior que zero)."""
        if value is None:
            raise ValueError('A altura não pode ser None')
        value = float(value)
        if value <= 0.0:
            raise ValueError('Altura deve ser maior do que zero')
        self._altura = value

    @classmethod
    def from_list(cls, lista):
        """Cria uma instância usando @classmethod a partir de uma lista/tupla [base, altura]."""
        return cls(lista[0], lista[1])

    @classmethod
    def from_string(cls, rep_retangulo: str):
        """Cria uma instância a partir de uma string 'base,altura'."""
        base, altura = rep_retangulo.split(',')
        return cls(float(base.strip()), float(altura.strip()))

    def calcular_area(self) -> float:
        """Retorna a área do retângulo."""
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        """Retorna o perímetro do retângulo."""
        return 2 * (self.base + self.altura)

    def __str__(self) -> str:
        """Representação legível para humanos."""
        return f'Retangulo[base={self.base}, altura={self.altura}]'

    def __repr__(self) -> str:
        """Representação canônica capaz de recriar o objeto via eval(repr(obj))."""
        return f'Retangulo({self.base}, {self.altura})'


if __name__ == '__main__':
    # instancia de exemplo
    retangulo1 = Retangulo(10.0, 5.35)

    # __str__ e __repr__ (métodos especiais)
    print(retangulo1.__str__())       # equivalente a print(str(retangulo1))
    print(retangulo1.__repr__())      # equivalente a print(repr(retangulo1))

    # demonstrar uso de eval com a string retornada por __repr__
    repr_str = retangulo1.__repr__()
    print('repr_str =', repr_str)
    print('type(repr_str) =', type(repr_str))

    # avalia a string para recriar o objeto (só faça isso com strings confiáveis)
    retangulo2 = eval(repr_str)
    print(retangulo2)
    print(type(retangulo2))

    # verificar que eval(repr(obj)) funciona idempotentemente
    retangulo3 = eval(repr(retangulo2))
    print(retangulo3)
    print(type(retangulo3))

    # exemplos adicionais
    ret = Retangulo.from_list((10, 8))
    print('\nExemplo from_list ->', ret)
    ret_s = Retangulo.from_string('7.5, 2.0')
    print('Exemplo from_string ->', ret_s)
    print(f'Área de {ret_s} = {ret_s.calcular_area():.2f}, Perímetro = {ret_s.calcular_perimetro():.2f}')
