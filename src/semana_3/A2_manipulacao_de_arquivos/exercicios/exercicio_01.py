""" Ex 02 - Carregar dados de projeto """
def carregar
dados
_
_projetos(nome
_
arquivo):
"""Retorna uma tupla de dicionários com dados de projetos.
"""
with open(nome
_
arquivo,
'r'
, encoding='utf-8') as arq:
projeto = []
for linha in arq:
codigo, titulo, responsavel = linha.strip().replace('\''
'').split('
,
')
projeto.append(
{
'codigo': codigo,
'titulo': titulo,
'responsavel': responsavel
,
}
)
return tuple(projeto)
ARQUIVO = 'arquivo
_
ex02.txt'
lista
_
dados = carregar
dados
_
_projetos(ARQUIVO)
print(type(lista
_
dados))
print(lista
_
dados)