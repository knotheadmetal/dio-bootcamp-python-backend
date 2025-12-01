nome = "Faeow"

print(nome.upper())  # Converte todos os caracteres para maiúsculo
print(nome.lower())  # Converte todos os caracteres para minúsculo
print(nome.title())  # Converte a primeira letra de cada palavra para maiúsculo

texto = "   Aprendendo Python   "
print(texto.strip())  # Remove espaços em branco no início e no fim da string
print(texto.rstrip()) # Remove espaços em branco no fim da string
print(texto.lstrip()) # Remove espaços em branco no início da string

menu = "Python"
print("###" + menu + "###")   # Adiciona caracteres antes e depois da string
print(menu.center(14))       # Centraliza a string em um campo de largura 14
print(menu.center(14, "#"))  # Centraliza a string em um campo de largura 14, preenchendo com '#'
print("-".join(menu))      # Insere '-' entre cada caractere da string

