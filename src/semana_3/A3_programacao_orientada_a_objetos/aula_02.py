""" Aula 02 - Atributos de classe e instância """

class Pessoa:
    """Classe Pessoa"""
    # atributo de classe
    especie = 'Humano'

    def __init__(self, nome, email):
        """atributos de instância: nome, email"""
        self.nome = nome
        self.email = email

# criação das instâncias
pessoa1 = Pessoa('Maria da Silva', 'maria@email.com')
pessoa2 = Pessoa('João Santos', 'joao@email.com')

# imprimir dados da Pessoa
print(pessoa1.nome, pessoa1.email)
print(pessoa2.nome, pessoa2.email)
print('------')

# dados da pessoa com atributo de classe
print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)
print('------')

# dados de atributo de classe acessando a classe
print(Pessoa.especie)
print('------')

# alterar um atributo de classe na instância (somente altera essa instância)
print("Alterando pessoa1.especie para 'Alien'")
pessoa1.especie = 'Alien'
print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print('------')

# alterar um atributo de classe na classe altera para todos os objetos
# desde que a instância não tenha o atributo sobrescrito localmente
Pessoa.especie = 'Anunakis'
print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)