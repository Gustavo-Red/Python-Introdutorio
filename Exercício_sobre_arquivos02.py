#Contexto:
#Um caixa eletrônico precisa registrar cada saque feito, sem apagar o histórico de saques anteriores.

#Enunciado:
#Escreva um programa que simule 3 saques diferentes (valores fixos no código, sem precisar de
#input()), adicionando cada um em uma nova linha do arquivo extrato.txt, sem apagar os saques
#anteriores. No final, leia e exiba todo o extrato.

saques = [500, 300, 1200]

with open('extrato.txt', 'w') as arquivo:
    for i in saques:
        arquivo.write(f'{i}' + '\n')

saques02 = [700, 80, 10000]

with open('extrato.txt', 'a') as arquivo02:
    for i in saques02:
        arquivo02.write(f'{i}' + '\n')

contador = 0
with open('extrato.txt', 'r') as arquivo_read:
    for i in arquivo_read:
        print(i)
        contador += 1

print(f"Houve {contador} saques até o momento.")