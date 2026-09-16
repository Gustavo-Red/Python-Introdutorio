pressoes = [110, 125, 140, 115, 150, 135, 120]

# 1. Crie uma nova lista vazia chamada alertas.

alertas = []

# 2. Percorra a lista pressoes e adicione à lista alertas apenas os valores maiores ou iguais a 140.

for i in pressoes:
    if i >= 140:
        alertas.append(i)

print(f"Os valores coletados foram: {alertas}")
print(f"A quantidade de alertas gerados foi: {len(alertas)}")