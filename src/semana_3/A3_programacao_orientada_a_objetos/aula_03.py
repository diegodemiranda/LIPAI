""" Aula 03 - Métodos de classe """
# calcule a área e perimetro do retangulo

class Retangulo:
    """Classe Retangulo"""

    def __init__(self, base, altura):
        """Construtor da classe Retangulo"""
        self.base = base
        self.altura = altura

    @classmethod
    def from_list(cls, lista):
        """Cria uma instância a partir de uma lista [base, altura]"""
        return cls(lista[0], lista[1])

    @classmethod
    def from_string(cls, rep_retangulo):
        """Cria uma instância a partir de uma string 'base,altura'"""
        base, altura = rep_retangulo.split(sep=',')
        return cls(float(base), float(altura))

    def calcular_area(self):
        """Retorna a área do retângulo"""
        return self.base * self.altura

    def calcular_perimetro(self):
        """Retorna o perímetro do retângulo"""
        return 2 * (self.base + self.altura)


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
print('--- Retangulo 4 ---')
retangulo4 = Retangulo.from_string("5.5,3.6")
print('Retângulo criado pelo método de classe (from_string)')
print(f'base -> {retangulo4.base} altura -> {retangulo4.altura}')
print(f'Área -> {retangulo4.calcular_area():.2f}  Perímetro -> {retangulo4.calcular_perimetro():.2f}')

# imprimir na tela área e perímetro retangulo1
print('---- Retangulo 1 ----')
print(f'Área: {retangulo1.calcular_area():.2f}')
print(f'Perímetro: {retangulo1.calcular_perimetro():.2f}')
