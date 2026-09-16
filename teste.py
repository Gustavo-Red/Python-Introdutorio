numero = int(input("Digite um número inteiro positivo: \n"))


invertido = 0

while numero > 0:
    # pega o último dígito
    digito = numero % 10
    
    # adiciona no número invertido
    invertido = invertido * 10 + digito
    
    # remove o último dígito
    numero = numero // 10

print(f"Número invertido: {invertido}")