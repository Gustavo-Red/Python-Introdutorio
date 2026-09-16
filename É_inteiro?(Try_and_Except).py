"""
Crie um programa que identifica
se o usuário digitou um numero ou não
"""
x = input("Digite algo: \n")

def conta_numeros(a):
    quant = 0
    for i in a:
        if i.isdigit == True:
            quant += 1
    if quant != 0:
        return quant
    
            

if x.isdigit() == True:
    print("Você digitou apenas numeros.")
else:
    print("Você digitou letras.")