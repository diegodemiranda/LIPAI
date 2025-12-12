"""
Ex 04 - Baseado no ex03.py, apresente todas as inconsistências
do identificador informado usando uma lista de erros.

Regras do identificador:
 - contém exatamente 7 caracteres;
 - começa com 'BR' (case-sensitive);
 - os caracteres 3 a 6 são dígitos representando um inteiro entre 0001 e 9999;
 - termina com o caractere 'X'.
"""

from typing import List


def validar_identificador_detalhado(identificador: str) -> List[str]:
    """Retorna uma lista de mensagens de erro (vazia se válido)."""
    erros: List[str] = []
    s = identificador.strip()

    # comprimento
    if len(s) != 7:
        erros.append('O identificador não possui exatamente 7 caracteres.')

    # prefixo BR
    if len(s) >= 2:
        if not (s[0] == 'B' and s[1] == 'R'):
            erros.append("O identificador não inicia com a sequência BR.")
    else:
        erros.append("O identificador não inicia com a sequência BR.")

    # parte numérica (posições 2..5 -> índices 2,3,4,5)
    if len(s) >= 6:
        meio = s[2:6]
        if not meio.isdigit() or len(meio) != 4:
            erros.append('O identificador não apresenta número inteiro entre 0001 e 9999.')
        else:
            numero = int(meio)
            if not (1 <= numero <= 9999):
                erros.append('O identificador não apresenta número inteiro entre 0001 e 9999.')
    else:
        erros.append('O identificador não apresenta número inteiro entre 0001 e 9999.')

    # sufixo X
    if len(s) >= 1:
        if s[-1] != 'X':
            erros.append("O identificador não finaliza com o caractere X.")
    else:
        erros.append("O identificador não finaliza com o caractere X.")

    return erros


def main() -> None:
    identificador = input('Entre o identificador -> ')
    erros = validar_identificador_detalhado(identificador)

    print()
    if not erros:
        print(f'{identificador} é válido')
    else:
        print(f'{identificador} não é válido')
        print('\nErros:')
        for erro in erros:
            print(f'# {erro}')


if __name__ == '__main__':
    main()
