""" Ex 03 - Validação de identificador
Regras:
 - o identificador contém 7 caracteres;
 - começa com 'BR';
 - seguido de um número inteiro entre 0001 e 9999 (4 dígitos, leading zeros permitidos);
 - termina com o caractere 'X'.
Exemplos válidos: BR0001X, BR1236X, BR9999X
Exemplos inválidos: br0001X, BR126X, BR99999X, BR9999Y
"""


def validar_identificador(identificador: str) -> bool:
    identificador = identificador.strip()
    # deve ter exatamente 7 caracteres
    if len(identificador) != 7:
        return False
    # deve começar com 'BR' (case-sensitive)
    if not identificador.startswith('BR'):
        return False
    # os próximos 4 caracteres devem ser dígitos
    meio = identificador[2:6]
    if not meio.isdigit() or len(meio) != 4:
        return False
    # o número deve estar entre 1 e 9999 (0000 não é válido)
    numero = int(meio)
    if not (1 <= numero <= 9999):
        return False
    # deve terminar com 'X'
    if identificador[6] != 'X':
        return False
    return True


def main() -> None:
    identificador = input('Entre o identificador -> ')
    if validar_identificador(identificador):
        print(f'{identificador} é válido')
    else:
        print(f'{identificador} não é válido')


if __name__ == '__main__':
    main()

