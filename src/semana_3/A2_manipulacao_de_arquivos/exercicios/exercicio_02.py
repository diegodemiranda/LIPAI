""" Ex 03 - Convertendo uma linha em dicionário genérico """
def linha
_para
_
dict(frase, lista
_
chaves):
"""Recebe uma linha e uma lista de chaves e retorna um dicionário.
"""
# cria uma lista com separador na vírgula para cada elemento da lista
lista
_
linha = frase.strip().replace("'"
,
"").split('
,
')
if len(lista
_
linha) != len(lista
_
chaves):
return f"{frase} e {lista
_
chaves} devem ter a mesma quantidade de itens"
else:
dicionario = {}
for i in range(len(lista
_
chaves)):
key = lista
_
chaves[i]
valor = lista
_
linha[i]
dicionario[key] = valor
return dicionario
# casos testes
# caso teste 1
LINHA = "SP000001,Maria da Silva,maria@email.com"
chaves = ['prontuario'
'nome'
,
,
'email']
print(linha
_para
_
dict(LINHA, chaves))
# caso teste 2
LINHA2 = "banana,3"
chaves2 = ['item'
,
'quantidade']
print(linha
_para
_
dict(LINHA2, chaves2))
# caso teste 3
TEXTO = 'pentium IV, 8gb, 120gb, False'
itens = ['cpu'
'memoria'
'hd'
,
,
,
print(linha
_para
_
dict(TEXTO, itens))
'cd-room']
# caso teste 4
DATA = 'FM 104.5, canal 8, faixa cidadão'
dados = ['radio'
,
'tv']
print(linha
_para
_
dict(DATA, dados))