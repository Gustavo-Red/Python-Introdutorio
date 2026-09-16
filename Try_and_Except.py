"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

#Exercício - Dobrar numeros

num = input("Digite um numero, vou dobrar ele: \n")

try:
    float_num = float(num) # se eu digitar uma string, aqui dará erro
    print(f"O dobro de {num} é {float_num*2}")
except:
    print("Isso não é um número.")