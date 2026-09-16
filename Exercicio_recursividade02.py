#Exercício 2: Localizar o Maior Elemento

#Descrição: Desenvolva uma função recursiva que encontre e retorne o maior elemento contido
#em um vetor de inteiros, sem passar variáveis auxiliares de tamanho ou índices pelos parâmetros
#da função.

numeros = [1, 5, 2, 3, 4]

def maior(vetor):
    if len(vetor) == 1:
        return vetor[0]
    else:
        maior_numero = maior(vetor[1:])
        if vetor[0] > maior_numero:
            return vetor[0]
        else:
            return maior_numero 
print(maior(numeros))