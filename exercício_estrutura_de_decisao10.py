#Faça um programa que pergunte em que turno você estuda. Peça para digitar:

    #M - Matutino
    #V - Vespertino
    #N - Noturno.

#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Digite aqui em qual turno estamos: (M para Matutino, V para vespertino, N para noturno) \n")

if turno.upper() == "M":
    print("Bom dia!")
elif turno.upper() == "V":
    print("Boa tarde!")
elif turno.upper() == "N":
    print("Boa noite!")
else:
    print("Comando inválido")
    