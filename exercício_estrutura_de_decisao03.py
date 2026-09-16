#Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:

#    F - Feminino
#    M - Masculino
#    Sexo Inválido.

genero = input("Digite qual o seu gênero: ('F' para Feminino e 'M' para Masculino) \n")
while (genero.upper() != "F") and (genero.upper() != "M"):
    print("Sexo inválido")
    genero = input("Digite qual o seu gênero: ('F' para Feminino e 'M' para Masculino) \n")
if genero.upper() == "F":
    print("Você é do gênero Feminino")
elif genero.upper() == "M":
    print("Você é do gênero Masculino")

