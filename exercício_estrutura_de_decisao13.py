#Faça um programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

lista = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

escolha = int(input("Digite um número, de 1 a 7, para eu retornar um dia da semana, respectivamente: \n"))
escolha = escolha - 11

print(lista[escolha])