""" Aula 08 - Herança entre classes super() """
class Pessoa(): # SUPER CLASSE
""" Define uma classe pessoa com oa atributos, cpf, nome , sobrenome """
def
init
__
__(self, nome, sobrenome, cpf):
""" Construtor da classe com nome, sobrenome e cpf """
self.nome = nome
self.sobrenome = sobrenome
self.cpf = cpf
def obtem
nome
_
_
completo(self):
""" retorna o nome completo da pessoa """
return f'{self.nome} {self.sobrenome}'
class Cliente(Pessoa): # SUB CLASSE
""" Classe cliente feita usando herança """
def
init
__
__(self, nome, sobrenome, cpf):
""" método construtor da sub classe cliente """
super().
init
__
__(nome, sobrenome, cpf)
self.compras = []
class Funcionario(Pessoa):
""" Classe Funcionario que herda informações da classe pessoa """
def
init
__
__(self, nome, sobrenome, cpf, salario):
""" método construtor do objeto funcionario com o salário """
super().
init
__
__(nome, sobrenome, cpf)
self.salario = salario
def calcula
_pagamento(self):
""" método de cálculo de pagamento do funcionário """
return self.salario - self.salario * 0.1
class Programador(Funcionario):
""" Classe progamador """
def
init
__
__(self, nome, sobrenome, cpf, salario, bonus):
""" construtor da classe programador"""
super().
init
__
__(nome, sobrenome, cpf, salario)
self.bonus = bonus
def calcula
_pagamento(self):
""" método para o cálculo de salário do programador com o bonus usando
super() """
return super().calcula
_pagamento() + self.bonus
cliente = Cliente("João"
"da Silva"
,
,
"111.111.111-11")
print(cliente.obtem
nome
_
_
completo(), type(cliente))
funcionario = Funcionario("Maria"
,
"da Silva"
,
"222.222.222-22"
, 2000.45)
print(funcionario.obtem
nome
_
_
completo(), funcionario.calcula
_pagamento(),
funcionario.salario, type(funcionario))
prog = Programador("José"
,
"Lopes da Silva"
,
"333.333.333-33"
, 5000.00, 300.00)
print(prog.obtem
nome
_
_
completo())
print(prog.calcula
_pagamento())
print(type(prog))