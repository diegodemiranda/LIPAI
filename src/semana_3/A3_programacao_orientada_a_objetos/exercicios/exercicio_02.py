"""
Exercício 02 - Implementar uma classe Projeto com código, título, responsável.

Requisitos resumidos:
- atributos: codigo (inteiro), titulo (str), responsavel (str)
- nenhum dos atributos pode ser nulo ou vazio
- fornecer @property/@setter para validação
- criar um projeto também a partir de uma string no formato
- "1,Laboratório de Desenvolvimento de Software,Pedro Gomes"
- dois projetos são iguais se tiverem o mesmo código (__eq__)
"""

from __future__ import annotations
from typing import Any


class Projeto:
    """Classe Projeto."""

    def __init__(self, codigo: int, titulo: str, responsavel: str):
        # Ao atribuir aqui, já acionamos os setters para validar
        self._codigo = None
        self._titulo = None
        self._responsavel = None

        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

    @classmethod
    def criar_projeto(cls, string_dados: str) -> "Projeto":
        """Cria um objeto Projeto a partir de uma string 'cod, titulo, responsavel'."""
        if not string_dados or not isinstance(string_dados, str):
            raise ValueError("Erro -> deve ser passada uma string válida")
        try:
            partes = [p.strip() for p in string_dados.split(',')]
            if len(partes) != 3:
                raise ValueError("A string deve ter 3 partes separadas por vírgula")
            codigo_str, titulo, responsavel = partes
            return cls(int(codigo_str), titulo, responsavel)
        except Exception as e:
            raise ValueError(f"Erro ao criar projeto: {e}")

    @property
    def codigo(self) -> int:
        """Retorna o código do projeto."""
        return self._codigo

    @codigo.setter
    def codigo(self, valor: Any) -> None:
        """Valida se é inteiro e positivo."""
        try:
            valor_int = int(valor)
        except (ValueError, TypeError):
            raise ValueError("O código deve ser um número inteiro.")
        if valor_int <= 0:
            raise ValueError("O código deve ser um inteiro positivo.")
        self._codigo = valor_int

    @property
    def titulo(self) -> str:
        """Retorna o título do projeto."""
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str) -> None:
        if not valor or not str(valor).strip():
            raise ValueError("O título não pode ser nulo ou vazio")
        self._titulo = str(valor).strip()

    @property
    def responsavel(self) -> str:
        """Retorna o responsável pelo projeto."""
        return self._responsavel

    @responsavel.setter
    def responsavel(self, valor: str) -> None:
        if not valor or not str(valor).strip():
            raise ValueError("O responsável não pode ser nulo ou vazio")
        self._responsavel = str(valor).strip()

    def __eq__(self, other: Any) -> bool:
        """Dois projetos são iguais se tiverem o mesmo código."""
        if isinstance(other, Projeto):
            return self.codigo == other.codigo
        return False

    def __repr__(self) -> str:
        return f"Projeto(codigo={self.codigo}, titulo='{self.titulo}', responsavel='{self.responsavel}')"

    def __str__(self) -> str:
        return f"Projeto [Código: {self.codigo}, Título: \"{self.titulo}\", Responsável: {self.responsavel}]"


if __name__ == '__main__':
    print('\n-----\nTestes do Projeto\n-----')

    # 1. Teste normal (Construtor)
    try:
        p1 = Projeto(1, 'Lab Software', 'Pedro Gomes')
        print(f"P1 criado: {p1}")
    except ValueError as e:
        print(f"Erro P1: {e}")

    # 2. Teste via String
    try:
        entrada = "2, Laboratório de IA, Maria Silva"
        p2 = Projeto.criar_projeto(entrada)
        print(f"P2 criado via string: {p2}")
    except ValueError as e:
        print(f"Erro P2: {e}")

    # 3. Teste de Igualdade
    try:
        p3 = Projeto(1, 'Outro Nome', 'Outra Pessoa')  # Mesmo código que P1
        print(f"P1 é igual a P3 (mesmo código) ? {p1 == p3}")  # Deve ser True
    except Exception as e:
        print(f"Erro P3: {e}")

    # 4. Teste de Erro (Título Vazio)
    try:
        p_erro = Projeto(3, '', 'Joao')
        print('ERRO: p_erro deveria ter lançado exceção')
    except ValueError as e:
        print(f"Erro esperado capturado: {e}")

    print('\n---\n')
