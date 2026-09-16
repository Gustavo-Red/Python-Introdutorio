def soma(N):
    S = 0
    for i in range(1, N+1):
        S += i
    return S

A = int(input("informe um numero: "))
print(f"A soma é {soma(A)}")

