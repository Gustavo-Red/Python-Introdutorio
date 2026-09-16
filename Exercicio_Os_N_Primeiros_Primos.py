#Escreva um programa que peça ao utilizador um valor N e imprima os N primeiros números primos da sequência natural

N = int(input("Digite os quantos números primos voce quer imprimir: \n"))

contador = 0
quant_primos = 0
num = 2

print("\n")

while quant_primos < N:

    quant_divisores = 0

    for i in range(1, num +1):
        if num%i == 0:
            quant_divisores = quant_divisores + 1
        
    if (quant_divisores == 2):
        print(f"{num} é um número primo")
        quant_primos = quant_primos + 1
    num = num + 1