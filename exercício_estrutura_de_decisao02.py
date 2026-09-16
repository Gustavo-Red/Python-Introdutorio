#Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input("Digite um número:"))
if numero > 0:
    print("Esse número é positivo")
elif numero == 0:
    print("Esse é o número 0")
else:
    print("Esse número é negativo")
