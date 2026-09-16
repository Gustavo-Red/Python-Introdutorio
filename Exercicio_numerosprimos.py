#Crie um algoritimos que identifique se o número é primo

num = int(input("Digite um número: \n"))
quant_divisiveis=0

for i in range(2, num):
    if num%i == 0:
        print("O número {} é divisível por {}".format(num, i))
        quant_divisiveis = quant_divisiveis + 1
if (quant_divisiveis == 0):
    print(f"O número {num} é primo")
else:
    print(f"O número {num} não é primo")