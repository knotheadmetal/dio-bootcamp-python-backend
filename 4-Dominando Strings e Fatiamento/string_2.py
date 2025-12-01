nome = "Faeow"
idade = 30
profissao = "Engenheiro de dados"
linguaguem = "Python"
saldo = 45.435

dados = {"nome": "Faeow", "idade": 30}

print("Nome: %s Idade: %d % (nome, idade)")  # Usando %s e %d para formatar strings e inteiros

print("Nome: {} Idade: {}".format(nome, idade))  # Usando o método format()

print("Nome: {1} Idade: {0}".format(nome, idade))  # Usando índices para ordenar os argumentos
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))  # Repetindo argumentos

print("Nome: {nome} Idade: {idade} ".format(nome=nome, idade=idade))  # Usando nomes de argumentos
print("Nome: {name} Idade: {age} {name} {name} {age}".format(name=nome, age=idade))  # Repetindo argumentos nomeados
print("Nome: {nome} Idade: {idade}".format(**dados))  # Usando dicionário para formatar strings

print(f"Nome: {nome} Idade: {idade}")  # Usando f-strings para formatar strings
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")  # Formatando número de ponto flutuante com f-strings
print(f"Nome : {nome} Idade: {idade} Saldo: {saldo:10.1f}")  # Definindo largura mínima para números com f-strings  
