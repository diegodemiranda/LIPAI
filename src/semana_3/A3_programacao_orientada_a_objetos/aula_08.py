""" Aula 08 - Herança entre classes e uso de super() """


class Pessoa:  # SUPER CLASSE
    """Define uma classe Pessoa com os atributos nome, sobrenome e cpf."""

    def __init__(self, nome: str, sobrenome: str, cpf: str):
        """Construtor da classe com nome, sobrenome e cpf."""
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def obtem_nome_completo(self) -> str:
        """Retorna o nome completo da pessoa."""
        return f"{self.nome} {self.sobrenome}"


class Cliente(Pessoa):  # SUBCLASSE
    """Classe Cliente feita usando herança de Pessoa."""

    def __init__(self, nome: str, sobrenome: str, cpf: str):
        """Construtor da subclasse Cliente."""
        super().__init__(nome, sobrenome, cpf)
        self.compras = []


class Funcionario(Pessoa):
    """Classe Funcionario que herda de Pessoa e adiciona salário."""

    def __init__(self, nome: str, sobrenome: str, cpf: str, salario: float):
        """Construtor do objeto Funcionario com o salário."""
        super().__init__(nome, sobrenome, cpf)
        self.salario = float(salario)

    def calcula_pagamento(self) -> float:
        """Calcula o pagamento líquido do funcionário (desconto de 10%)."""
        return self.salario - self.salario * 0.1


class Programador(Funcionario):
    """Classe Programador (subclasse de Funcionario) com bônus."""

    def __init__(self, nome: str, sobrenome: str, cpf: str, salario: float, bonus: float):
        """Construtor da classe Programador."""
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = float(bonus)

    def calcula_pagamento(self) -> float:
        """Calcula o pagamento do programador somando o bônus ao pagamento do funcionário."""
        return super().calcula_pagamento() + self.bonus


if __name__ == '__main__':
    # Cliente simples
    cliente = Cliente("João", "da Silva", "111.111.111-11")
    print(cliente.obtem_nome_completo(), type(cliente))

    # Funcionário
    funcionario = Funcionario("Maria", "da Silva", "222.222.222-22", 2000.45)
    print(funcionario.obtem_nome_completo(),
          funcionario.calcula_pagamento(),
          funcionario.salario,
          type(funcionario))

    # Programador com bônus
    prog = Programador("José", "Lopes da Silva", "333.333.333-33", 5000.00, 300.00)
    print(prog.obtem_nome_completo())
    print(prog.calcula_pagamento())
    print(type(prog))
