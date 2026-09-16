#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:
preco01 = float(input("Digite o preço do primeiro produto: \n"))
preco02 = float(input("Digite o preço do segundo produto: \n"))
preco03 = float(input("Digite o preço do terceiro produto: \n"))

#eu pensei em resolver por conteudo de "listas", mas vou responder com estruturas condicionais.

if (preco03 > preco01) and (preco02 > preco01):
    print("O produto 1 é o mais barato, custando {} reais".format(preco01))
elif (preco03 > preco02) and (preco01 > preco02):
    print("O produto 2 é o mais barato, custando {} reais".format(preco02))
elif (preco03 < preco02) and (preco01 > preco03):
    print("O produto 3 é o mais barato, custando {} reais".format(preco03))