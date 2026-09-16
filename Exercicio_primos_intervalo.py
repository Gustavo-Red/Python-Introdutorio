# Faça uma função que imprima os números primos de um intervalo com "inicio" e "fim".

inicio = int(input("Digite um número inteiro positivo: \n"))
fim = int(input("Digite outro número inteiro positivo (um maior): \n"))

print("\n")

while inicio != fim:
    divisiveis = 0
    for i in range(2, inicio):
        if inicio % i == 0:
            divisiveis = divisiveis + 1
            
    if divisiveis == 0:
        print(f"O número {inicio} é primo")
        
    inicio = inicio + 1