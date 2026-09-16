#Escreva um programa que dado um número, imprima na tela a sua versão
#invertida.

#Exemplo: Entrada: 1234 -- Saída: 4321


# Para pegar o último dígito de um número:
# → use numero % 10

# Para remover o último dígito:
# → use numero // 10

# Estratégia geral:
# 1. Pegue o último dígito
# 2. Use esse dígito (ex: adicionar ao número invertido)
# 3. Remova o último dígito do número original
# 4. Repita até o número virar 0



numero = int(input("Digite um número inteiro positivo: \n"))

invertido = 0

while numero > 0:
    digito = numero%10 # <- separando o ultimo dígito

    invertido = invertido*10 + digito # <- adicionando o ultimo dígito a uma sequência

    numero = numero//10 # <- removendo o ultimo digito do numero do usuário

print("O número invertido é {}".format(invertido))