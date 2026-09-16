#A Conjectura de Collatz afirma que, partindo de qualquer número inteiro
#positivo e aplicando repetidamente a seguinte regra, sempre se chega ao número 1:

#Se o número for par, divida-o por 2.

#Se o número for ímpar, multiplique-o por 3 e some 1.

#Escreva um programa que receba um número inteiro, imprima toda a sequência até chegar a 1 e
#informe quantos passos foram necessários.

#Exemplo: 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 (8 passos).

num = int(input("Digite um número inteiro positivo: \n"))

print("\n")

passos = 0

while num != 1:
    if num%2 == 0:
        num = num/2
        passos = passos + 1
        print(num)
    else: 
        num = (num*3) + 1 
        passos = passos + 1
        print(num)
print("A sequência terá {} passos".format(passos))
    
    