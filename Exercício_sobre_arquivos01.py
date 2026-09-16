#Contexto:
#Sistemas de cadastro simples precisam saber quantos registros já foram salvos antes de continuar
#inserindo novos.

#Enunciado:
#Crie um arquivo nomes.txt com pelo menos 6 nomes (um por linha). Em seguida, leia o arquivo e
#exiba quantos nomes existem e qual é o nome mais curto (menor quantidade de caracteres).

with open('nome.txt', 'w') as arquivo:
    arquivo.write("João \n")
    arquivo.write("Tiago \n")
    arquivo.write("Gustavo \n")
    arquivo.write("Marcos \n")
    arquivo.write("Mateus \n")
    arquivo.write("Lucas \n")

contador = 0
with open('nome.txt', 'r') as arquivo:
    for nome in arquivo:
        print(nome)
        contador += 1
print(f"Há {contador} nomes")
