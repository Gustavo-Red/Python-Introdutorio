#Faça um programa que leia três números e mostre o maior e o menor deles:
numero01 = float(input("Digite o primeiro número: \n"))
numero02 = float(input("Digite o segundo número: \n"))
numero03 = float(input("Digite o terceiro número: \n"))

lista = []
lista.append(numero01)
lista.append(numero02)
lista.append(numero03)
lista.sort()

print("O número {} é o maior e o número {} é o menor.".format(lista[2], lista[0]))
