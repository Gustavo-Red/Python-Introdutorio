numeros = []
etapas = 0

for i in range(1, 101):
    numeros.append(i)

while True:  
    etapas += 1  
    try:
        inp = int(input(f"Seu número é {numeros[((len(numeros))//2)-1]}?\n1. Sim\n2. Maior\n3. Menor\n"))
    except ValueError:
        print("Digite apenas números")
        continue

    if inp == 1:
        print("acertei!")
        print(f"Etapas: {etapas}")
        break
    elif inp == 2:
        numeros = numeros[(len(numeros)//2):len(numeros)]
    elif inp == 3:
        numeros = numeros[:(len(numeros)//2)]
    else:
        print("inválido...")