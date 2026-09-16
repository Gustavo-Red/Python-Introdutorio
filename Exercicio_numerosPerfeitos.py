#  Um número perfeito é aquele cuja soma dos seus divisores próprios
#  é igual a ele mesmo.
#  Escreva um programa que encontre e imprima na tela os 4 primeiros
#  números perfeitos.

num = 1
contador = 0
Quantidade_Perfeitos = 0

while Quantidade_Perfeitos < 4:

    soma = 0
    for i in range (1, num):   
        if num%i == 0:
            soma = soma + i
    if soma == num:
        print (f"O número {num} é perfeito")
        Quantidade_Perfeitos = Quantidade_Perfeitos + 1
    #else:
        #print(f"O número {num} NÃO é perfeito")
    num = num + 1




