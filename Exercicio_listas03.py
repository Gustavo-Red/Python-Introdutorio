notas = [7.5, 8.0, 5.5, 9.0, 6.5]

soma = 0
for i in notas:
    soma = soma + i

media = soma/len(notas)

print(f"A média das notas {notas} é {media}")