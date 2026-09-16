#Faça um programa que leia três números e mostre-os em ordem decrescente:
numero01 = float(input("Digite o primeiro número: \n"))
numero02 = float(input("Digite o segundo número: \n"))
numero03 = float(input("Digite o terceiro número: \n"))

lista = []

lista.append(numero01)
lista.append(numero02)
lista.append(numero03)

lista.sort()

print("Os números em ordem decrescente são respectivamente: {}, {} e {}. ".format(lista[2], lista[1], lista[0]))

