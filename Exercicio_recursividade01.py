#Exercício 1: Soma dos Elementos de um Vetor

#Descrição: Escreva uma função recursiva que receba um vetor de números inteiros e retorne a
#soma de todos os seus elementos. A assinatura da função não deve receber o tamanho do vetor
#de forma explícita, devendo aproveitar os recursos idiomáticos do Python (fatiamento de listas).

numeros = [1, 2, 3, 4, 5]

def soma(vetor):
    if len(vetor) == 0:              # caso base: lista vazia
        return 0
    else:
        return vetor[0] + soma(vetor[1:])   # caso recursivo

print(soma(numeros))