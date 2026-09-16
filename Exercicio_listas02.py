vendas_ano = [120, 150, 110, 200, 250, 190, 300, 310, 280, 220, 190, 210]

# 1. Crie uma lista primeiro trimestre contendo as vendas dos 3 primeiros meses.

primeiro_trimestre = vendas_ano[:3]

print(primeiro_trimestre)

#2. Crie uma lista segundo semestre contendo as vendas dos últimos 6 meses utilizando fatiamento por índices negativos.

segundo_semestre = vendas_ano[-7:]

print(segundo_semestre)

# 3. Exiba a lista completa invertida (do último mês para o primeiro).

print(vendas_ano[::-1])

