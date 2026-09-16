#Números Amigos: Escreva um programa que receba dois números inteiros positivos e determine se eles são "Amigos". Dois números são amigos se a soma dos divisores próprios de um (excluindo o próprio número) for igual ao outro e vice-versa.

#Exemplo : 220 e 284 são amigos

#Divisores de 220: 1, 2, 4, 5, 10, 11, 20, 22, 44,, 55, 55, 110 (Soma =284)

#Divisores de 284: 1, 2, 4, 71, 142 (Soma = 220)

numero01 = 0

numero02 = 0

numero01 = int(input("Digite um número inteiro positivo: \n"))
divisores01 = 0


numero02 = int(input("Digite outro número inteiro positivo: \n"))
divisores02 = 0


# como é uma divisão:  Quociente x divisor = dividendo + resto

for i in range (1, numero01):
    if numero01%i == 0:
        divisores01 = i + divisores01


for i in range (1, numero02):
    if numero02%i == 0:
        divisores02 = i + divisores02


if (divisores01 == numero02) and (divisores02 == numero01):
    print("A soma do primeiro numero é  {}".format(divisores01))
    print("A soma do segundo numero é {} ".format(divisores02))
    print("São números Amigos")
else: 
    print("Não são números amigos")
    print("A soma do primeiro numero é  {}".format(divisores01))
    print("A soma do segundo numero é {} ".format(divisores02))

