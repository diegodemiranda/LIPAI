""" Aula 05 - break e continue """

# Usa-se o break e continue num loop.
for i in range(0, 10, 1):
    if i == 4:
        print('saída do loop')
        break
    print(i)

# Encontrar a posição de um número em uma lista de inteiros.
# Caso não encontre, posicao permanece -1.
busca = 5
numeros = [1, 33, 51, 6, 5, 7, 8, 9, 5, 1, 7]
posicao = -1
contador = 0
for numero in numeros:
    if numero == busca:
        posicao = contador
        print(f"Achei {busca} na posicao {posicao}")
    contador += 1

# usando o break para achar a primeira posicao
print("Usando o break para cancelar a execução do laço for")
busca = 5
numeros = [1, 33, 51, 6, 5, 7, 8, 9, 5, 1, 7]
posicao = -1
contador = 0
for numero in numeros:
    if numero == busca:
        posicao = contador
        print(f"Achei {busca} na posicao {posicao}")
        print('Saindo do for')
        break
    contador += 1

print(f'Posição encontrada (primeira ocorrência): {posicao}')

# exemplo com o range: procurar usando índices
print('Usando o range e o break no laço for')
busca = 5
numeros = [1, 33, 51, 6, 5, 7, 8, 9, 5, 1, 7]
posicao = -1
for i in range(len(numeros)):
    print(f'Procurando na posição {i}...')
    if numeros[i] == busca:
        posicao = i
        print(f'{busca} encontrada na posicao {posicao}')
        break

# Funcionamento do continue
# Apenas pula a iteração atual indo para a próxima iteração sem sair do loop
numeros = [1, 33, 513, 3, 3, 3, 3, 3, 3, 6, 5,
           7, 8, 9, 5, 1, 7, 3, 3, 3, 3, 3, 3, 3, 333]
print('Exemplo de continue: pulando o valor 3')
for numero in numeros:
    if numero == 3:
        continue  # pula a iteração atual do loop e vai para a próxima
    print(numero)
