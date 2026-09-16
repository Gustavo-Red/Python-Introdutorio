with open ("notas.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

print("\n")

with open ("notas.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
    linha = conteudo[0].split(',')
    print(linha)

print("\n")

with open ("notas.txt", 'r') as arquivo:
    for linha in arquivo:
        dado = linha.split(",")
        print(dado)
print("\n")

with open ("notas.txt", 'r') as arquivo:
    for linha in arquivo:
        dado = linha.split(",")
        print(float(dado[1]))
