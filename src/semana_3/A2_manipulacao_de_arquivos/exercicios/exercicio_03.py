"""Ex 03 - Convertendo uma linha em dicionário genérico

Função que converte uma linha (valores separados por vírgula)
em um dicionário usando uma lista de chaves fornecida.
"""


def linha_para_dict(frase, lista_chaves):
    """Recebe uma linha e uma lista de chaves e retorna um dicionário.

    A função aceita valores separados por vírgula. Aspas simples (') serão
    removidas dos valores. Se o número de itens na linha for diferente do
    número de chaves, a função retorna uma mensagem informativa.
    """
    if frase is None:
        return None

    # separa por vírgula, remove espaços e aspas simples
    lista_linha = [item.strip().replace("'", "") for item in frase.strip().split(",")]

    if len(lista_linha) != len(lista_chaves):
        return f"{frase} e {lista_chaves} devem ter a mesma quantidade de itens"

    dicionario = {k: v for k, v in zip(lista_chaves, lista_linha)}
    return dicionario


# casos de teste
if __name__ == "__main__":
    # caso teste 1
    LINHA = "SP000001,Maria da Silva,maria@email.com"
    chaves = ['prontuario', 'nome', 'email']
    print(linha_para_dict(LINHA, chaves))

    # caso teste 2
    LINHA2 = "banana,3"
    chaves2 = ['item', 'quantidade']
    print(linha_para_dict(LINHA2, chaves2))

    # caso teste 3
    TEXTO = 'pentium IV, 8gb, 120gb, False'
    itens = ['cpu', 'memoria', 'hd', 'cd-room']
    print(linha_para_dict(TEXTO, itens))

    # caso teste 4
    DATA = 'FM 104.5, canal 8, faixa cidadão'
    dados = ['radio', 'tv', 'faixa']
    print(linha_para_dict(DATA, dados))

