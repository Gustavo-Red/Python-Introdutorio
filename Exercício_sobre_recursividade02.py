#Exercício 2 — Contagem regressiva
#Escreva uma função recursiva contagem_regressiva(n) que imprima os números de n até 1, um
#por linha, e depois imprima "Fim!".

def contagem_regressiva(n):
    if n == 0 or n == 1:
        return 1
    else:
        print (n)
        return contagem_regressiva(n-1)
print(contagem_regressiva(20))
print("\n")
print("FIM!")


# Se voce rodar o codigo acima analisando a recursividade da função, ainda vai imprimir o 1 dentro do if...
# Isso porque o print(contagem_regressiva()) que está fora do def imprime o "return 1".
# Ilustrando essa logica no codigo abaixo:

def um():
    return 1
print(f"Testando... {um()}")