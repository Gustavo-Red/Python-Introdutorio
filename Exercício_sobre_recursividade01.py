#Exercício 1 — Fatorial (o clássico)
#Escreva uma função recursiva fatorial(n) que calcule o fatorial de n. Teste com n = 0, 1, 5, 7.

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fatorial(n-1)
num = int(input("Digite um número inteiro: \n"))
print(f"O fatorial de {num} é {fatorial(num)}")