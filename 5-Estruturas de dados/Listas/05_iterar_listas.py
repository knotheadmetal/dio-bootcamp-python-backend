carros = ["gol", "celta", "palio"] # Lista de carros

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros): # Enumerando a lista de carros
    print(f"{indice}: {carro}")
