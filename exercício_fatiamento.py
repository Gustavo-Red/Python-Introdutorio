"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite seu nome: \n")

try:
    idade = int(input("Digite sua idade: \n")) # <- Isso tem que estar dentro do Try, pois ao digitar "" ja dará ValueError ali mesmo.
    if nome != "" and idade != "":
        print("\n")
        print(f"Seu nome é {nome}")
        print(f"Seu nome invertido é {nome[::-1]}")
        if " " in nome:
            print("Seu nome contém espaços")
        else:
            print("Seu nome NÃO contém espaços")
        print(f"Seu nome tem {len(nome)} caracteres")
        print(f"A primeira letra do seu nome é {nome[0]}")
        print(f"A última letra do seu nome é {nome[-1]}")
    else:
        print("Desculpe, você deixou campos vazios.")
except:
    print("Desculpe, você deixou campos vazios.")