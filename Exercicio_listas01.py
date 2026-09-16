#Exercício 1: Processador de Sensor de Temperatura

# Contexto: Um sensor IoT registra temperaturas a cada hora. Você precisa ajustar a lista de
# leituras.

# Enunciado: Crie uma lista leituras = [21.5, 22.0, 23.1]. Realize as seguintes operações
# em sequência:

# 1. O sensor registrou uma nova leitura de 24.8◦ C. Adicione-a ao final da lista.

# 2. A primeira leitura (21.5) foi invalidada por erro de calibração. Remova-a.

# 3. Insira uma leitura de correção de 22.5 na segunda posição (índice 1).

# 4. Exiba o total de leituras presentes e a lista final ordenada de forma crescente.

lista = [21.5, 22.0, 23.1]

lista.append(24.8)

print(lista)

del lista[0]

print(lista)

lista.insert(1, 22.5)

print(f"Total de leituras: {len(lista)}")
print(f"Leituras ordenadas: {sorted(lista)}")


# Calcule e exiba a “amplitude térmica” do período (a diferença entre a maior e a menor temperatura registrada).

maior = 0
menor = 10000000000000000000000
for i in lista:
    if maior < i:
        maior = i
    if menor > i:
        menor = i

amplitude = maior - menor

print(f"A amplitude é {amplitude:.2f}")