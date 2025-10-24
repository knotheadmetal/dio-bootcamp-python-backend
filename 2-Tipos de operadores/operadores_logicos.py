# AND = para ser TRUE, ambas as expressões devem ser TRUE
# OR  = para ser TRUE, uma das expressões deve ser TRUE

print(True and True and True)    # TRUE
print(True and False and True)   # FALSE
print(False and False and True)  # FALSE
print(False and False and False) # FALSE
print(True or False or True)     # TRUE
print(True or False or False)    # TRUE
print(False or False or False)   # FALSE

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)



