#Faça um programa que leia três números e mostre o maior deles:
numero01 = float(input("Digite o primeiro número: \n"))
numero02 = float(input("Digite o segundo número: \n"))
numero03 = float(input("Digite o terceiro número: \n"))

lista = []
lista.append(numero01)
lista.append(numero02)
lista.append(numero03)

lista.sort()
print("O número {} é maior que o número {}, que é maior que o número {}.".format(lista[-1], lista[-2], lista[-3]))
