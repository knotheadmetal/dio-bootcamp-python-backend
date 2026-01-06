def exibir_mensagem(): # Função sem parâmetros
    print("Olá mundo!")


def exibir_mensagem_2(nome): # Função com um parâmetro
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"): # Função com um parâmetro padrão
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")
