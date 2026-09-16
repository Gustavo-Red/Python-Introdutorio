#OBS: Funções podem receber parâmetros, exemplo: def função(a, b)


def soma(a, b):
    s = a + b
    print(f"A soma de {a} + {b} é igual a {s}")


a = int(input("Digite um número inteiro: \n"))
b = int(input("Digite outro número inteiro: \n"))

soma(a, b)