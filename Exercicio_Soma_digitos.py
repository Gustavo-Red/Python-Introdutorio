#Soma dos Dígitos) Escreva um programa que receba um número inteiro positivo e calcule a soma
#de todos os seus dígitos individuais. Este exercício é fundamental para praticar a decomposição de
#números usando operadores de divisão inteira e resto.


#Exemplo: Entrada 1234.

#Processamento: 1 + 2 + 3 + 4 = 10.

num = int(input("Digite um numero inteiro positivo: \n"))

soma = 0

contador = num

while contador > 0:
    digito = contador%10

    soma = soma + digito

    contador = contador//10

print ("A soma dos dígitos de {} é {}".format(num, soma))