#Calcule em quantas voltas um carro a 4 segundos de distancia vai ultrapassar o outro, se consegue descontar 2 décimos a cada volta
distancia = 4.0
voltas = 0
while ( distancia > 1): 
    distancia = distancia - 0.2
    voltas = voltas + 1
    print("O carro está a {:.2f} segundos de distancia. Ja se passaram {} voltas".format(distancia, voltas))
    
print("O carro ultrapassou após {} voltas".format(voltas))
