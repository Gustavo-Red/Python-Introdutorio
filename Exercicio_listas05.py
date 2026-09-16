pontuacoes = [45, 89, 32, 102, 67, 95]
nota = 0
for i in pontuacoes:
    if nota < i:
        nota = i
print(f"A maior nota foi {nota}")