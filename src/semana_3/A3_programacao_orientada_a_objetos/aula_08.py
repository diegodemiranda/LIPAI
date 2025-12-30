""" Exercício 01 - Implementar uma classe Aluno com atributos (prontuário, nome,
email)
email'
O objeto aluno pode ser criado com uma string do tipo 'prontuário, nome,
Nenhum atributo pode ser vazio ou nulo, usar @property e @setters
dois alunos são iguais se tiverem o mesmo prontuário, implementar o método
__
eq__
implementar
hash
__
__ para usar alunos em sets ou chaves de dicionário """
class Aluno():
""" Classe aluno com os atributos prontuario, nome, email """
def
init
__
__(self, prontuario, nome, email):
""" método construtor com prontuário, nome, email """
self.prontuario = prontuario
self.nome = nome
self.email = email
@classmethod
def criar
de
_
_
string(cls, dados
_
str):
"""
Cria um objeto Aluno a partir de uma string no formato 'prontuario, nome,
email'
.
Exemplo: Aluno.criar
de
_
_
string("SP001, Maria, maria@email.com")
"""
if not dados
_
str or not isinstance(dados
_
str, str):
raise ValueError("Dados incorretos.
")
try:
prontuario, nome, email = [item.strip()
for item in dados
_
str.split('
,
')]
# Retorna uma nova instância da classe (cls)
return cls(prontuario, nome, email)
except ValueError:
raise ValueError(
"A string deve estar no formato: 'prontuario, nome, email'")
@property
def prontuario(self):
""" retorna o prontuário """
return self.
_prontuario
@prontuario.setter
def prontuario(self, valor):
""" atribui valor e testa para o prontuário """
if not valor or not str(valor).strip():
raise ValueError("O prontuário não pode ser vazio ou nulo.
self.
_prontuario = valor
")
@property
def nome(self):
""" retorna o nome do aluno """
return self.
nome_
@nome.setter
def nome(self, valor):
""" atribui e testa valor para o nome do aluno """
if not valor or not str(valor).strip():
raise ValueError("O nome não pode ser vazio ou nulo.
self.
nome = valor
_
@property
def email(self):
""" retorna o email """
return self.
email
_
")
@email.setter
def email(self, valor):
""" testa e seta o valor do email """
if not valor or not str(valor).strip():
raise ValueError("O email não pode ser vazio ou nulo.
self.
email = valor
")
_
def
__
eq__(self, outro):
""" Dois alunos são iguais se tiverem o mesmo prontuário """
if isinstance(outro, Aluno):
return self.prontuario == outro.prontuario
return False
def
hash
__
__(self):
""" Necessário para usar objetos Aluno em sets ou chaves de dicionário
"""
return hash(self.prontuario)
def
__
repr
__(self):
""" Representação do objeto """
return f"Aluno(prontuario='{self.prontuario}'
email='{self.email}')"
, nome='{self.nome}'
,
def
str
__
__(self):
""" Retorna a string aluno """
return f"Aluno [ prontuario = {self.prontuario}, nome = {self.nome},
email = {self.email}]"
aluno1 = Aluno('sp001'
print(aluno1)
print('
----
')
,
'José da Silva'
,
'jose@email.com')
aluno2 = Aluno.criar
de
_
_
string("SP30394, Maria Silva, maria@ufu.br")
print(aluno2)