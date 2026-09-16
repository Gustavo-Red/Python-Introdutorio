#Operadores in e not in
#String são iteráveis
# "Iterável" é algo que voce consegue navegar item por item

nome = "Otávio"

print(nome[2])


print("=" * 50)
print('vio' in nome)
print('zero' in nome)
print("=" *50)

encontrar = input("Digite o que deseja encontrar: \n")

if encontrar in nome:
    print(f"{encontrar} está na string")
if encontrar not in nome: # not in inverte o valor da função: de TRUE para FALSE e de FALSE para TRUE
    print(f"{encontrar} NÃO está na string {nome}")


