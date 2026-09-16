def conta_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + conta_digitos(n//10)
print(conta_digitos(100))