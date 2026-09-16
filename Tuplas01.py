#### OBS: AS TUPLAS SÃO IMUTÁVEIS ####
# Não dá para atribuir valores à tupla depois da declaração
# Tupla é uma "variável" que dá para guardar vários valores




Tupla = ("Hamburguer", "Suco", "Pizza", "Pudim")

print("\n")

print(Tupla)

print("\n")

print (f"O {Tupla[0]} é o elemento de índice 0")

print('\n')

print(Tupla[:2])

print("\n")

print (Tupla[:-3])

print("\n")

print(Tupla[1:3]) # -> o elemento 3 é ignorado no fatiamento

print("\n")


for comida in Tupla:
    print(f"Eu vou comer {comida}")
print("Comi demais!")

print("\n")

# O comando len(lista/tupla) diz quantos elementos tem a lista/tupla

print(f"O lanche tem {len(Tupla)} alimentos...")


