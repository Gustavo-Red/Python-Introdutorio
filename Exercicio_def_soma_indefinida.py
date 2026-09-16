def soma(*num):
    s = 0
    for i in num: # <- como num se trata de uma tupla, você não precisa digitar o range
        s = s + i
    print (f"A soma é {s}")

soma(2, 3, 3)
