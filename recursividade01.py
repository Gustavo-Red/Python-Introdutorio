#Definição: Recursividade é quando uma função chama a si mesma pra resolver um problema,
#quebrando ele em pedaços menores e mais simples,
#até chegar num pedaço tão simples que não precisa mais quebrar.


# O exemplo clássico: fatorial

#Fatorial de um número n (escrito n!) é o produto de todos os números de 1 até n. Por exemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120.

def fatorial(n):
    if n == 0 or n == 1:      # caso base
        return 1
    else:
        return n * fatorial(n - 1)   # caso recursivo
    
#Vamos pensar no caso n = 5. Ele vai passar pelo seguinte caminho...
# o programa vai chamar a função fatorial(5), como 5 não é igual a 0 e nem a 1 o programa irá pular o "return 1"
# indo para o else... dentro do else, o programa ira chamar 5*fatorial(4).
# Em seguida, o programa irá buscar o fatorial de 4, iniciando a função fatorial(4).
# Como 4 não é igual a 0 e nem a 1... O programa pulará o "return 1", indo para o else...
# Dentro do else o programa irá chamar o 4*fatorial(3).
# Em seguida, o programa irá buscar o fatorial de 3, iniciando a função fatorial(3).
# Como 3 não é igual a 0 e nem a 1... O programa pulará o "return 1", indo para o else...
# Dentro do else o programa irá chamar o 3*fatorial(2).
# Em seguida, o programa irá buscar o fatorial de 2, iniciando a função fatorial(2).
# Como 2 não é igual a 0 e nem a 1... O programa pulará o "return 1", indo para o else...
# Dentro do else o programa irá chamar o 2*fatorial(1)
# Em seguida, o programa irá buscar o fatorial de 1, iniciando a função fatorial(1).
# Como n = 1, a condicional "if n == 0 or n == 1: " se torna verdadeira.
# O programa ira para o return 1 dentro do if...
# Em seguida, fará a multiplicação 2*fatorial(1), que é 2*1, obtendo fatorial(2) que é 2
# Depois obterá o fatorial (3), que é 3*fatorial(2), ou seja, 3*2, resultando em 6.
# Depois obterá o fatorial (4), que é 4*fatorial(3), ou seja, 4*6, resultando em 24.
# Depois obterá o fatorial (5), que é 5*fatorial(4), ou seja, 5*24, resultando em 120.


    
print (fatorial(5))