#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

#    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math



print("Dada uma função do segundo grau f(X)= ax² + bx + c")
a = float(input("Digite o valor de 'a': \n "))

if a!=0:
    b = float(input("Digite o valor de 'b': \n "))
    c = float(input("Digite o valor de 'c': \n "))

    delta=(b**2)-(4*a*c)


    if delta < 0:
        print("Essa equação não possui raízes reais.")
    elif delta == 0:
        raiz = (b*(-1))/(2*a)
        print("A equação f(x) = ({})² + ({})x + ({}) só tem uma raiz real, sendo ela {} .".format(a, b, c, raiz))
    else:
        raiz_delta = math.sqrt(delta)
        raiz1 = ((b*(-1)) + raiz_delta)/(2*a)
        raiz2 = ((b*(-1)) - raiz_delta)/(2*a)
        print ("A equação f(x) = ({})² + ({})x + ({}) tem duas raízes reais, sendo elas {} e {}".format(a, b, c, raiz1, raiz2))
else:
    print("Essa equação não é do segundo grau.")