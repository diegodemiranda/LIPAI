""" Aula 03 - loop for """

linguagens = ['C', 'Java', 'Python']

# acessar por índice
print(linguagens[0])
print(linguagens[1])
print(linguagens[2])

# loop for ajuda na iteração
# Sintaxe:
# for valor in colecao:
#     instrucao
#     instrucao
# nessa construção o operador in verifica se o elemento está dentro da coleção,
# retira e coloca o elemento na variável à esquerda

# imprime cada linguagem em uma linha (em maiúsculas)
for linguagem in linguagens:
    print(linguagem.upper())

# contar elementos e calcular a média (exemplo com 3 notas)
nota1 = 10.0
nota2 = 5.5
nota3 = 8.3
media = (nota1 + nota2 + nota3) / 3
print(f'Média (3 notas): {media}')

# em casos que temos uma lista o for ajuda a somar elementos
soma = 0
notas = [10, 9, 6, 7, 8, 10]
for nota in notas:
    soma = soma + nota
media_notas = soma / len(notas)
print(f'Média (lista de notas): {media_notas}')

# range em python
valores = range(0, 10)  # vai de 0 até 9 (10 não entra)
for valor in valores:
    print(valor)

# steps in range
valores = range(0, 11, 2)  # 0, 2, 4, 6, 8, 10
print('Range com step 2 ->', list(valores))

# steps com decremento in range
valores = range(10, 0, -1)  # 10, 9, ... ,1
print('Range decrescente -1 ->', list(valores))

valores = range(10, 0, -2)  # 10, 8, 6, 4, 2
print('Range decrescente -2 ->', list(valores))

# iterando usando índice
for i in range(len(linguagens)):
    print(linguagens[i])

# o range é mais utilizado em casos em que não iremos percorrer de maneira linear
# a nossa coleção
