def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print("Valor sacado com sucesso!")
        print("Retire seu dinheiro na boca do caixa.")
        
    print("Obrigado por usar nosso caixa eletrônico.")
    
def depositar(valor):
    saldo = 500
    saldo += valor
    
sacar(1000)