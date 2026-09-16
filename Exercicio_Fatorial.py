#6. Fatorial de um Número) Crie um algoritmo que receba um número inteiro positivo N e calcule
#o seu fatorial (N !). O fatorial de um número é o produto de todos os inteiros positivos menores ou
#iguais a ele.


#Lembrete Matemático:

#5! = 5 × 4 × 3 × 2 × 1 = 120


num = int(input("Digite um numero inteiro positivo: \n"))
backup_num = num
fatorial = 1

while num > 0:
    fatorial= fatorial*num
    num = num - 1
print("O fatorial de {} é {}".format(backup_num, fatorial))

