#Um número de Harshad (ou Niven) é um número inteiro divisível pela soma
#dos seus próprios dígitos. Implemente um programa que faça esta verificação.

#Exemplo: 18 é Harshad pois 1 + 8 = 9, e 18 é divisível por 9.

num = int(input("Digite um número inteiro positivo: \n"))

num_backup = num

digito = 0
soma = 0


print("\n")

while num != 0:
    digito = num%10
    soma = soma + digito
    num = num//10

if num_backup%soma == 0:
    print("{} é um número de Hashard".format(num_backup))
else:
    print("{} NÃO é um número de Hashard".format(num_backup))
