#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
# A atribuição de conceitos obedece à tabela abaixo:

#Média de Aproveitamento  Conceito
#Entre 9.0 e 10.0         A
#Entre 7.5 e 9.0          B
#Entre 6.0 e 7.5          C
#Entre 4.0 e 6.0          D
#Entre 4.0 e zero         E


nota1 = float(input("Digite a sua primeira nota: \n"))

nota2 = float(input("Digite a sua segunda nota: \n"))

media = (nota1 + nota2)/2

if media >= 9 and media <= 10:
    nota_final= "A"
elif media >= 7.5 and media < 9:
    nota_final= "B"
elif media >= 6 and media < 7.5:
    nota_final= "C"
elif media >= 4 and media < 6:
    nota_final = "D"
else:
    nota_final = "E"


print("Sua nota final é {}".format(nota_final))

if nota_final == "D" or nota_final== "E":
    print ("VOCÊ FOI REPROVADO")
else:
    print ("PARABÉNS, VOCÊ FOI APROVADO!!!")
    