#Faça um programa que peça uma nota, entre zero e dez. 
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    try:
        numero = int(input("Digite um número inteiro de 0 a 10: \n"))
        if 0<= numero <=10:
            break
        else:
            print("Valor inválido, digite um valor entre 0 e 10...")
    except ValueError:
            print("Digite um valor inteiro...")


print("Ok... Você escolheu o numero {} ...".format(numero))


