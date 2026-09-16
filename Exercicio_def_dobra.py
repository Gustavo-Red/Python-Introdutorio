def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos]*=2
        pos += 1

lista = [7, 2, 5, 0, 4]
print(lista)
dobra(lista)
print(lista)