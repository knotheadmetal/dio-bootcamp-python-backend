MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade, pode tirar a CNH")
    
if idade < MAIOR_IDADE:
    print("Você é menor de idade, não pode tirar a CNH")

if idade >= MAIOR_IDADE:
    print("Você é maior de idade, pode tirar a CNH")
    
else:
    print("Você é menor de idade, não pode tirar a CNH")

if idade >= MAIOR_IDADE:
    print("Você é maior de idade, pode tirar a CNH")

elif idade == IDADE_ESPECIAL:
    print("Você tem 17 anos, pode fazer aulas teóricas da CNH")

else:
    print("Você é menor de idade, não pode tirar a CNH")