#Crie um perfil de usuário com Nome,
#Idade e Status (Ativo). Depois, simule
#um aniversário aumentando a idade em
#1 ano.

nome = input("Digite um nome: \n")
idade = int(input("Digite a idade do indivíduo: \n"))
idade_list = []

idade_list.append(idade)

print(f" {nome} tem {idade_list[0]} anos, antes do aniversário. \n")

idade_list[0] = idade_list[0] + 1

print(f" {nome} tem {idade_list[0]} anos, depois do aniversário. \n")