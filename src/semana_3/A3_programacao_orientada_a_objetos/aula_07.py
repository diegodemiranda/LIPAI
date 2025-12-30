""" Aula 07 - Relacionamentos entre classes

Exemplos de composição/associação entre Pessoa, Endereco e Telefone.
"""

from __future__ import annotations
from typing import List, Optional


class Endereco:
    """Endereço de uma localidade."""

    def __init__(self, cep: str, numero: int):
        """Construtor do endereço que tem cep e número."""
        self.cep = str(cep)
        self.numero = int(numero)

    def __str__(self) -> str:
        """Retorna a representação do objeto Endereco."""
        return f'Endereco[cep={self.cep}, numero={self.numero}]'

    def __repr__(self) -> str:
        return f"Endereco('{self.cep}', {self.numero})"


class Telefone:
    """Classe que representa um telefone (ddd + número)."""

    def __init__(self, ddd: str, numero: str):
        """Construtor do telefone com ddd e número."""
        self.ddd = str(ddd)
        self.numero = str(numero)

    def __str__(self) -> str:
        """Retorna a string do objeto Telefone."""
        return f'Telefone[ddd={self.ddd}, numero={self.numero}]'

    def __repr__(self) -> str:
        return f"Telefone('{self.ddd}', '{self.numero}')"


class Pessoa:
    """Classe Pessoa com nome, cpf, telefone e lista de endereços."""

    def __init__(self, nome: str, cpf: str, telefone: Optional[Telefone] = None):
        """Construtor da classe Pessoa."""
        self.nome = str(nome)
        self.cpf = str(cpf)
        self.telefone = telefone
        # lista de endereços associados
        self.enderecos: List[Endereco] = []

    def add_endereco(self, endereco: Endereco) -> None:
        """Adiciona um endereço ao objeto Pessoa."""
        if not isinstance(endereco, Endereco):
            raise TypeError('endereco deve ser uma instância de Endereco')
        self.enderecos.append(endereco)

    def print_enderecos(self) -> None:
        """Imprime os endereços associados à pessoa."""
        print(f'Endereços de {self.nome}:')
        if not self.enderecos:
            print('  (nenhum endereço)')
            return
        for endereco in self.enderecos:
            print('  ', endereco)

    def __str__(self) -> str:
        telefone_str = str(self.telefone) if self.telefone is not None else 'None'
        return f'Pessoa[cpf={self.cpf}, nome={self.nome}, telefone={telefone_str}]'

    def __repr__(self) -> str:
        return f"Pessoa('{self.nome}', '{self.cpf}', {repr(self.telefone)})"


if __name__ == '__main__':
    # Pessoa criada com telefone como string (versão simples)
    pessoa = Pessoa('João da Silva', '12312312333', Telefone('11', '99999-0000'))
    print(pessoa)
    print(pessoa.nome, pessoa.cpf, pessoa.telefone)

    # Passando um telefone como instância da classe Telefone
    print('\nAcessando Classe Telefone')
    pessoa1 = Pessoa('Maria da Silva', '111111111-11', Telefone('21', '5467-1290'))
    print(pessoa1)
    print(pessoa1.nome, pessoa1.cpf, pessoa1.telefone.ddd, pessoa1.telefone.numero)

    # criando um objeto telefone e atribuindo a diferentes pessoas
    tel = Telefone('33', '98765-7520')
    pessoa3 = Pessoa('José da Silva', '222222222-22', tel)
    pessoa4 = Pessoa('Ana da Silva', '333333333-33', tel)
    print('\nPessoas com mesmo telefone')
    print(pessoa3)
    print(pessoa4)

    # adicionando endereços a pessoas criadas
    pessoa.add_endereco(Endereco('12345-890', 450))
    pessoa.add_endereco(Endereco('23456-789', 759))
    local = Endereco('78909-786', 515)
    pessoa1.add_endereco(local)
    pessoa3.add_endereco(local)
    pessoa4.add_endereco(local)

    # imprimindo pessoas e seus endereços
    print('\nImprimindo pessoas e endereços:')
    print(pessoa1)
    print(pessoa3)
    print(pessoa4)

    # imprimindo endereços com o método específico
    print('\nListagem de endereços por pessoa:')
    pessoa1.print_enderecos()
    pessoa3.print_enderecos()
    pessoa.print_enderecos()
