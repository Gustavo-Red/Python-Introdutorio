#Exercício 4 — Potência
#Escreva uma função recursiva potencia(base, expoente) que calcule base elevado a expoente,
#sem usar o operador ** nem a função pow().
#Dica: 2^4 = 2 * 2^3, e o caso base é quando o expoente chega em 0, onde qualquer número elevado a 0 é 1.

def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base*(potencia(base, expoente - 1))
print(potencia(2, 3))