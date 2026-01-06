carros = {"gol", "celta", "palio"} # Conjunto de carros

for carro in carros: # Iterando sobre o conjunto
    print(carro)

for indice, carro in enumerate(carros): # Iterando com índice
    print(f"{indice}: {carro}")
