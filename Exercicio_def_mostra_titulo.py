# O comando "def" define funções personalizadas.

def mostra_titulo(nome):
    print("=" * 30)
    print(f"             {nome}               ")
    print("=" * 30)


Titulo = input("Digite um título: \n")

mostra_titulo(Titulo)