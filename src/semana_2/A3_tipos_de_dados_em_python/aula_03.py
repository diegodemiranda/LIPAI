""" Aula 03 - Tipos de Dados - Set ( Conjuntos ) """
# criar um set
numeros = {1, 2, 3, 4, 5, 6, 6.25, 6.5, 7, 8}
print('numeros ->', numeros, type(numeros))

# acesso dos elementos no set (ordem não garantida)
for numero in numeros:
    print('numero ->', numero)

# adicionar itens no set
numeros.add(100)
print('após add(100) ->', numeros)
# se adicionar um item que já existe no set, nada muda
numeros.add(100)
print('após add(100) novamente ->', numeros)
print('\n------\n')

# adicionar elementos de um set em outro
print('numeros (antes update) ->', numeros)
numeros2 = {42, 3, 1, 11, 17}
print('numeros2 ->', numeros2)
numeros.update(numeros2)
print('após update ->', numeros, type(numeros))
print('\n------\n')

# remove elementos de um set (preferir checar se existe para evitar KeyError)
if 100 in numeros:
    numeros.remove(100)
    print('após remove(100) ->', numeros)
else:
    print('100 não encontrado para remover')

# copiando um set para outro
outro_set = numeros.copy()
print('outro_set ->', outro_set)
