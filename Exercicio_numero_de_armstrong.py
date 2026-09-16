# Um número de Armstrong é um número de n digitos que é igual à soma de seus dígitos elevados à mesma potência.
# Exemplo: 153 possui 3 digitos. Verifique se 1³ + 5³ + 3³ = 153

numero = int(input("Digite um número inteiro: \n"))

numero02 = numero

algarismo=0

potencia = 0

num = 0

### Descobrindo a potencia ###

while numero != 0:
    numero = numero //10
    potencia = potencia + 1
    num = num + 1

####################################

print(f"tem {num} digitos e potencia de valor {potencia}")

#até aqui temos a quantidade de algarismos e o valor da potencia
resultado = 0
numero = numero02

while numero02!=0: 
    resultado = resultado + (numero02%10)**num
    numero02 = numero02 // 10

if(resultado == numero):
    print("Armstrong")
else:
    print("Não Armstrong")