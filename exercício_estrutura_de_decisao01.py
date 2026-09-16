#Faça um programa que peça dois números e imprima o maior deles.

numero01 = float(input("Digite um número: \n"))
numero02 = float(input("Digite outro número: \n"))

if (numero01 > numero02):
    print("O {} é o maior número e o {} é o menor número".format(numero01, numero02))
elif (numero01==numero02):
    print("Os dois números são o número {}".format(numero01))
else:
    print("O {} é o maior número e o {} é o menor número".format(numero02, numero01))

