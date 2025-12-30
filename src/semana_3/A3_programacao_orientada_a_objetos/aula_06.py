""" Aula 06 - equal e hash code """

# Tanto em python quanto em outras linguagens temos formas de comparação
NOME1 = 'João'
NOME2 = 'João'

# avalia se duas strings são verdadeiras
print(NOME1 == NOME2)

class Pessoa():
""" Cria um objeto da classe pessoa """

    def __init__(self, nome):
    """ construtor da classe pessoa com nome como parametro"""
    self.nome = nome


pessoa1 = Pessoa('João')
pessoa2 = Pessoa('João')

# comparação entre pessoa1 e pessoa2
print(pessoa1 == pessoa2)
print(pessoa1)
print(pessoa2)
