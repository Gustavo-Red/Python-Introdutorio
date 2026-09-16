#Defina uma função que retorne a somatória de 1 até N

def somat(N):
    soma = 0
    for i in range(N + 1):
        soma = soma + i
    return soma

print(somat(3))