#Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

#Dicas:

#    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#    Triângulo Equilátero: três lados iguais;
#    Triângulo Isósceles: quaisquer dois lados iguais;
#    Triângulo Escaleno: três lados diferentes;

lado1 = float(input("Digite o valor do lado 1 do triângulo em questão: \n"))
lado2 = float(input("Digite o valor do lado 2 do triângulo em questão: \n"))
lado3 = float(input("Digite o valor do lado 3 do triângulo em questão: \n"))
              
lista = [lado1, lado2, lado3]

lista.sort()

if lista[2] < (lista[0] + lista[1]):
    if lado1==lado2 and lado2==lado3:
        print("É um triângulo equilátero.")
    elif lado1!=lado2 and lado2!=lado3 and lado1!= lado3:
        print("É um triângulo escaleno.")
    else:
        print("É um triângulo Isóceles.")
else:
    print("Esses valores não satisfazem a condição de existência de um triângulo...")