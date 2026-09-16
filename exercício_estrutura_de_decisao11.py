# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#
#    salários até R$ 280,00 (incluindo) : aumento de 20%
#    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#    o salário antes do reajuste;
#    o percentual de aumento aplicado;
#    o valor do aumento;
#    o novo salário, após o aumento.
#

salario = float(input("Digite aqui o salário em questão: \n"))
reajuste = None
if salario <= 280:
    reajuste = salario + ((salario*20)/100)
    print("O salário de R${} foi reajustado para R${}".format(salario, reajuste))
elif salario > 280 and salario <= 700:
    reajuste = salario + ((salario*15)/100)
    print("O salário de R${} foi reajustado para R${}".format(salario, reajuste))
elif salario > 700 and salario <= 1500:
    reajuste = salario + ((salario*10)/100)
    print("O salário de R${} foi reajustado para R${}".format(salario, reajuste))
elif salario > 1500:
    reajuste = salario + ((salario*5)/100)
    print("O salário de R${} foi reajustado para R${}".format(salario, reajuste))