"""
Exercício 03 - Implementar uma classe Participacao, com os atributos:
codigo - identificador da participação pode ser inteiro ou string
data
data
_
inicio - data inicial pode ser string
_
fim - data final pode ser string
aluno - Objeto da classe Aluno
projeto - Objeto da classe Projeto associado
"""
# reaproveitamento dos exercícios Aluno e Projeto
from ex01 import Aluno
from ex02 import Projeto
class Participacao:
""" Classe participação """
def
init
__
__(self, codigo, data
_
inicio, data
_
fim,
*dados):
""" Construtor da classe participação com dois objetos Aluno e Projeto
"""
self.codigo = codigo
self.data
inicio = data
inicio
_
_
self.data
fim = data
fim
_
_
self.aluno = Aluno.criar
de
_
_
string(dados[0])
self.projeto = Projeto.criar
_projeto(dados[1])
@classmethod
def criar
_participacao(cls, string_participacoes):
""" cria um objeto participacao a partir de uma string """
if not string_participacoes or not isinstance(string_participacoes, str):
raise ValueError("Erro -> a string deve ser válida")
try:
{len(partes)}")
partes = [p.strip().strip('"')
for p in string_participacoes.split(';')]
if len(partes) != 5:
raise ValueError(
f"String deve ter 5 partes separadas por ';'
. Encontrado:
codigo, data
_
inicio, data
_
fim,
return cls(int(codigo), data
_
*dados = partes
inicio, data
fim,
_
*dados)
except ValueError as e:
raise ValueError(f'Erro ao criar participacao: {e}')
def
str
__
__(self):
return f'Participacao [ codigo={self.codigo}, data
_
inicio=
{self.data
inicio}, data
{self.projeto}]'
_
_
fim={self.data
_
fim}, \n {self.aluno}, \n
# teste 01
print('\n----- Início do Teste Classe Participacao ----\n')
DATA = '1234 ; "01-10-2025" ; "29-12-2026" ; "SP001, José da Silva,
josé@email.com" ; "2, Laboratório de IA, Maria Silva"'
try:
participacao = Participacao.criar
_participacao(DATA)
print(participacao)
except Exception as e:
print(e)
# teste 02
# --- TESTE 02: SIMULAÇÃO DE ERRO ---
print("\n--- Iniciando Teste 02 (Deve retornar erro) ---
")
DATA
_
ERRO = '9999;"01-01-2024";"30-06-2024";"SP002, Aluno Sem Email";"3, Projeto
X, Prof. Girafales"'
try:
participacao
_
erro = Participacao.criar
_participacao(DATA
_
ERRO)
print(participacao
_
erro)
except ValueError as e:
print(f"Mensagem de erro capturada: {e}")