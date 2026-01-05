carros = (
    "gol",
    "celta",
    "palio",
)

for carro in carros: # iterando sem índice
    print(carro)


for indice, carro in enumerate(carros): # iterando com índice
    print(f"{indice}: {carro}")
