#Exercício04) Crie um algorítimo que conta quantos dígitos tem um número.

numero = int(input("Digite um número inteiro: "))
cont = 0
while (numero!=0):
    numero = numero // 10
    cont= cont + 1

print("O numero tem {} caracteres".format(cont))
