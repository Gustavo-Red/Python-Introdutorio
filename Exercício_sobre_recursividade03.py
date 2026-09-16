#Exercício 3 — Soma de 1 até N
#Escreva uma função recursiva soma_ate(n) que retorne a soma de todos os números inteiros de 1
#até n (ex: soma_ate(5) deve retornar 15, porque 1+2+3+4+5=15).

def soma(n):
    if n == 1:
        return 1
    elif n == 0: # <- Coloquei essa condicional para caso o usuário peça n = 0
        return 0
    else:
        return n + soma(n-1)
print (soma(5))