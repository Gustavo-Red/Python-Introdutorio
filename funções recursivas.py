### Função mult ###


def mult(a,b):
    if ( b>0 ):
        return a + mult(a, b-1)
    else:
        return 0

print(mult(4, 2))

print("\n")


