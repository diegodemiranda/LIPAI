""" Aula 02 - Tipos de Dados - Tuplas """

# criação da tupla
nomes = ('Maria', 'Pedro', 'João')
print('nomes ->', nomes, type(nomes))

# acessar os elementos da tupla da mesma forma que acessa em uma lista
print('nomes[0] ->', nomes[0])
print('nomes[0:3] ->', nomes[0:3])
print('nomes[-1] ->', nomes[-1])

# a leitura de dados na tupla e lista são iguais
# a tupla não aceita modificação de valores (imutável)
# iteração em tuplas é igual a de listas
for nome in nomes:
    print('for nome in nomes ->', nome)

# outra forma de criar tuplas
nomes2 = ('ana', 'amelia', 'marcos')
print('nomes2 ->', nomes2, type(nomes2))

# unpack - atribuir para variáveis os valores que estão na tupla
nome1 = nomes[0]
nome2 = nomes[1]
nome3 = nomes[2]
# usando o unpack temos:
nome1, nome2, nome3 = nomes
print('unpack ->', nome1, nome2, nome3)

# o unpack deve ser igual à quantidade de elementos da tupla ou do seu fatiamento
nome1, nome2 = nomes[0:2]  # unpack fatiado
print('unpack fatiado ->', nome1, nome2)

# juntar duas tuplas
todos_nomes = nomes + nomes2
print('todos_nomes ->', todos_nomes)

# exemplo de tupla unitária (um elemento) é preciso a vírgula
tupla_unica = ('apenas_um',)
print('tupla_unica ->', tupla_unica, type(tupla_unica))

# para escolher entre listas e tuplas, avaliar se os dados precisam ser mutáveis;
# se imutáveis, prefira tupla
print('\nObservação: use tuplas quando quiser proteger os dados contra atribuições acidentais.')
