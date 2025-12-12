""" Aula 01 - Tipos de Dados - Listas """
# exemplo lista vazia
nomes = []
print('nomes ->', nomes, type(nomes))

# criando uma lista com vários nomes
nomes = ['josé', 'maria', 'pedro', 'paulo', 'marcos']
print('nomes ->', nomes, type(nomes))

# permite adicionar tipos diferentes
coisas = ['panela', 2, 1.614, ['outra lista', 'coisas'], 100]
print('coisas ->', coisas, type(coisas))

# permite acessar elementos através de um índice
print('coisas[0] ->', coisas[0])
print('coisas[0:3] ->', coisas[0:3])
print('coisas[-1] ->', coisas[-1])
print('coisas[:2] ->', coisas[:2])
print('coisas[3:6] ->', coisas[3:6])

# modificação de elementos na lista
nomes = ['Maria', 'Marta', 'Ana', 'Priscila', 'Raquel', 'João']
print('nomes (antes) ->', nomes)
nomes[0] = 'Mariana'  # altera o primeiro elemento
print('nomes (depois de nomes[0] = "Mariana") ->', nomes)

# substituindo um slice
nomes[3:] = ['Pedro', 'Marta']
print('nomes (depois de nomes[3:] = ["Pedro","Marta"]) ->', nomes)

# tamanho de uma lista
print('tamanho de nomes ->', len(nomes))

# adicionar elementos na lista usando o append
nomes = []
nomes.append('Josefo')
nomes.append('Marta Gomes')
print('após append ->', nomes)

# insere um elemento em posição específica (insert desloca os demais)
nomes.insert(0, 'Guilherme Tavares')
print('após insert(0, ...) ->', nomes)

# método extend - acrescenta uma lista em outra lista no final da mesma
nomes2 = ['carlos gomes', 'caio silva']
nomes.extend(nomes2)
print('após extend ->', nomes)

# remover elementos da lista - passando o elemento a ser removido
# deve ser usado sempre com tratamento de erros
print('antes remove ->', nomes)
try:
    nomes.remove('carlos gomes')
except ValueError:
    print('Elemento não encontrado para remover: "carlos gomes"')
print('após tentativa de remove ->', nomes)

# del - deleta nomes passando o índice, remove da memória o item
print('antes del nomes[0] ->', nomes)
if nomes:
    del nomes[0]
print('após del ->', nomes)

# limpar o conteúdo da lista deixando ela vazia
print(f'Lista nomes -> {nomes}')
nomes.clear()  # limpa elementos da lista (todos)
print('após clear ->', nomes)

# iteração em listas
nomes = ['Alice', 'Bob', 'Carol']
for nome in nomes:
    print('for nome in nomes ->', nome)

for i in range(len(nomes)):
    print(f'for i in range(len(nomes)) -> nomes[{i}] =', nomes[i])
