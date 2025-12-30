""" Exercício 01 - Implementar a classe Aluno

Requisitos (resumido):
- atributos: prontuario, nome, email
- pode ser criado a partir da string 'prontuario, nome, email'
- nenhum atributo pode ser vazio/nulo (usar @property e setters)
- dois alunos são iguais se tiverem o mesmo prontuário (__eq__)
- implementar __hash__ para permitir uso em sets/dicionários
"""

from __future__ import annotations
from typing import Any


class Aluno:
    """Classe Aluno com validação em propriedades."""

    def __init__(self, prontuario: str, nome: str, email: str):
        # atributos privados
        self._prontuario = None
        self._nome = None
        self._email = None

        # usa setters para validação
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @classmethod
    def criar_de_string(cls, dados_str: str) -> "Aluno":
        """Cria um Aluno a partir de uma string 'prontuario, nome, email'."""
        if not dados_str or not isinstance(dados_str, str):
            raise ValueError("Dados incorretos: deve ser uma string não vazia")
        try:
            partes = [p.strip() for p in dados_str.split(',')]
            if len(partes) != 3:
                raise ValueError
            prontuario, nome, email = partes
            return cls(prontuario, nome, email)
        except ValueError:
            raise ValueError("A string deve estar no formato: 'prontuario, nome, email'")

    @property
    def prontuario(self) -> str:
        """Getter do prontuário."""
        return self._prontuario

    @prontuario.setter
    def prontuario(self, valor: str) -> None:
        """Setter com validação: não pode ser vazio ou nulo."""
        if valor is None or not str(valor).strip():
            raise ValueError('O prontuário não pode ser vazio ou nulo')
        self._prontuario = str(valor).strip()

    @property
    def nome(self) -> str:
        """Getter do nome."""
        return self._nome

    @nome.setter
    def nome(self, valor: str) -> None:
        """Setter com validação: não pode ser vazio ou nulo."""
        if valor is None or not str(valor).strip():
            raise ValueError('O nome não pode ser vazio ou nulo')
        self._nome = str(valor).strip()

    @property
    def email(self) -> str:
        """Getter do email."""
        return self._email

    @email.setter
    def email(self, valor: str) -> None:
        """Setter com validação básica: não pode ser vazio ou nulo."""
        if valor is None or not str(valor).strip():
            raise ValueError('O email não pode ser vazio ou nulo')
        self._email = str(valor).strip()

    def __eq__(self, outro: Any) -> bool:
        """Dois alunos são iguais se tiverem o mesmo prontuário."""
        if isinstance(outro, Aluno):
            return self.prontuario == outro.prontuario
        return False

    def __hash__(self) -> int:
        """Permite usar Aluno em sets e como chave de dicionário."""
        return hash(self.prontuario)

    def __repr__(self) -> str:
        return f"Aluno(prontuario='{self.prontuario}', nome='{self.nome}', email='{self.email}')"

    def __str__(self) -> str:
        return f"Aluno [ prontuario = {self.prontuario}, nome = {self.nome}, email = {self.email} ]"


if __name__ == '__main__':
    # exemplos de uso
    aluno1 = Aluno('SP001', 'José da Silva', 'jose@email.com')
    print(aluno1)
    print('----')

    aluno2 = Aluno.criar_de_string('SP30394, Maria Silva, maria@ufu.br')
    print(aluno2)

    # igualdade e uso em set
    aluno3 = Aluno('SP001', 'Outro Nome', 'outro@email.com')
    print('\nAluno1 == Aluno3 ? ', aluno1 == aluno3)

    s = {aluno1, aluno2, aluno3}
    print('\nConteúdo do set (deve conter 2 elementos distintos por prontuário):')
    for a in s:
        print(' ', repr(a))

