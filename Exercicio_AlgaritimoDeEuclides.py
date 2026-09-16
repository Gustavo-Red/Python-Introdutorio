#Escreva um programa que calcule o Máximo Divisor Comum
#(MDC) entre dois números inteiros positivos utilizando o Algoritmo de Euclides.

#Explicação do Método: O algoritmo baseia-se no princípio de que o MDC de dois números não
#muda se o maior número for substituído pelo resto da sua divisão pelo menor. O processo é repetido
#(divisões sucessivas) até que o resto seja zero. O último resto não nulo é o MDC.

#Passo a passo (Exemplo MDC de 48 e 18):

#48 ÷ 18: quociente 2, resto 12.

#18 ÷ 12: quociente 1, resto 6.

#12 ÷ 6: quociente 2, resto 0.


#Resultado: O MDC é 6.


num01 = int(input("Digite um número inteiro positivo: \n"))

num02 = int(input("Digite outro número inteiro positivo (um menor): \n"))

print("\n")

backup_num01 = num01

backup_num02 = num02


backup = 1

resto = num01%num02

#resto02 = 0

while num02 != 0 :
    resto = num01%num02
    num01 = num02
    if resto != 0:
        backup = resto
    num02 = resto

print("O MDC de {} e {} é {}".format(backup_num01, backup_num02, backup))


