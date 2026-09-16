qtd = int(input("Quantos numeros? "))
lista = []

for i in range(qtd):
    inp = int(input(f"Digite o {i+1}° número: "))
    lista.append(inp)

lista.sort()
lista = lista[::-1]

for i in range(qtd):
    print(f"{lista[i]} >")
    s
