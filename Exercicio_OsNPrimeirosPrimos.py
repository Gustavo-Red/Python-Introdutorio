N = int(input("Digite quantos números primos você quer imprimir:\n"))

quant_primos = 0
num = 2

while quant_primos < N:
    eh_primo = True

    for i in range(2, num):
        if num % i == 0:
            eh_primo = False

    if eh_primo:
        print(num)
        quant_primos = quant_primos + 1

    num = num + 1