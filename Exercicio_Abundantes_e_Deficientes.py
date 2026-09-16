#Classifique um número de entrada em:

#Deficiente: Soma dos divisores próprios < número.

#Abundante: Soma dos divisores próprios > número.

#Perfeito: Soma dos divisores próprios = número.




num = int(input("Digite um número inteiro positivo: \n"))

print("\n")

### Descobrindo a soma dos divisores ###
soma = 0

for i in range(1, num):
    if num%i == 0:
        soma = soma + i

print ("A soma de todos os divisores de {} é {}".format(num, soma))

print("\n")

if soma < num:
    print("O número {} é deficiente.".format(num))
elif soma > num:
    print("O número {} é Abundante.".format(num))
else: 
    print("O número {} é um número Perfeito...".format(num))