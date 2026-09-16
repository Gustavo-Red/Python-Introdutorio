#Defina uma função que retome o maior entre 3 valores
def maior(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(maior(1, 2, 3))
