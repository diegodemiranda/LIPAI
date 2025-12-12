""" Aula 04 - Tipos de Dados - Dicionário (dic) """
# criar um dicionário
carro = {
    'marca': 'ford',
    'modelo': 'mustang',
    'ano': 1964
}
print('carro ->', carro, type(carro))

# acessar os valores de um dicionário
print("carro['marca'] ->", carro['marca'])
print("carro.get('marca') ->", carro.get('marca'))

# pegar todas as chaves
print('chaves ->', carro.keys(), type(carro.keys()))  # retorna um view de chaves
# pegar todos os valores
print('valores ->', carro.values(), type(carro.values()))
# pegar todos os pares (chave:valor)
print('itens ->', carro.items(), type(carro.items()))  # retorna view de tuplas

# verifica se a chave existe
print("'marca' in carro ->", 'marca' in carro)
print("'cor' in carro ->", 'cor' in carro)

# adicionar chave/valor de forma dinâmica
carro['cor'] = 'azul'
print('após adicionar cor ->', carro)
print("'cor' in carro ->", 'cor' in carro)

# remover um item do dicionario através de sua chave (capturando o valor removido)
marca_removida = carro.pop('marca')
print('marca removida ->', marca_removida)
print('carro após remover marca ->', carro)

# o pop no dicionário retorna o valor removido
cor_removida = carro.pop('cor')
print(f'A cor {cor_removida} foi removida do dicionário. Estado atual: {carro}')

# iterar com o dicionário
for key in carro:
    print('chave ->', key, 'valor ->', carro[key], 'tipo chave ->', type(key))

for key in carro.keys():
    print('key ->', key)

for value in carro.values():
    print('value ->', value)

for key, value in carro.items():
    print('item ->', key, ':', value)

# lista de dicionários
aluno1 = {
    'nome': 'João',
    'email': 'joao@mail.com',
    'notas': [10, 7, 8],
}

aluno2 = {
    'nome': 'Maria',
    'email': 'maria@mail.com',
    'notas': [10, 5, 6],
}

alunos = [aluno1, aluno2]
for aluno in alunos:
    print('\nAluno:', aluno['nome'], '| Email:', aluno['email'])
    for nota in aluno['notas']:
        print('  nota ->', nota)
