# calcule a área e perímetro do retângulo

def calcular_area(retangulo):
    """retorna a área do retângulo"""
    return retangulo['base'] * retangulo['altura']

def calcular_perimetro(retangulo):
    """retorna o perímetro de um retângulo"""
    return 2 * (retangulo['base'] + retangulo['altura'])

# declaração dos retângulos
retangulo1 = {
    'base': 10.0,
    'altura': 5.0
}
retangulo2 = {
    'base': 6.0,
    'altura': 3.0
}

print(f'Área retângulo 1: {calcular_area(retangulo1)}')
print(f'Perímetro retângulo 1: {calcular_perimetro(retangulo1)}')
print()
print(f'Área retângulo 2: {calcular_area(retangulo2)}')
print(f'Perímetro retângulo 2: {calcular_perimetro(retangulo2)}')

# Classe representa um retângulo
class Retangulo:
    """Classe Retangulo"""
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """retorna a área do retângulo"""
        return self.base * self.altura

    def calcular_perimetro(self):
        """retorna o perímetro do retângulo"""
        return 2 * (self.base + self.altura)

# instanciando objetos do tipo Retangulo
r1 = Retangulo(10.0, 5.0)
r2 = Retangulo(6.0, 3.0)

print(type(r1))
print(r1.base, r1.altura)
print(type(r1.base), type(r1.altura))
print(r2.base, r2.altura)
print(f"Área retângulo 1 -> {r1.calcular_area()}")
print(f"Área retângulo 2 -> {r2.calcular_area()}")
print(f"Perímetro retângulo 1 -> {r1.calcular_perimetro()}")
print(f"Perímetro retângulo 2 -> {r2.calcular_perimetro()}")
