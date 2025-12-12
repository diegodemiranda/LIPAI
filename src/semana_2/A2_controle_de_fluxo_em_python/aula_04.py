""" Aula 04 - Loop while """

"""
O while repete instruções enquanto uma condição for verdadeira.
Muito usado quando não sabemos previamente quantas iterações serão necessárias.
"""

# Exemplo básico: contador de 0 até 10
contador = 0
while contador <= 10:
    print(contador)
    contador += 1  # incremento da condição
print('fim')

# Exemplo de loop infinito controlado com break
i = 0
while True:
    if i >= 5:
        break
    print('while True ->', i)
    i += 1
print('saímos do while True')

# Exemplo de leituras em arquivo (arquivo já deve estar aberto):
# arquivo = open('meu_arquivo.txt', 'r')
# linha = arquivo.readline()
# while linha:
#     # processa a linha
#     print(linha.rstrip('\n'))
#     linha = arquivo.readline()  # lê a próxima linha
# arquivo.close()

"""Observação: o while precisa de uma condição que, em algum momento, se torne False para evitar 
loops infinitos (a menos que isso seja intencional e controlado com break/return).
"""
