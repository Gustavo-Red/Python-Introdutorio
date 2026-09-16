#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)

#e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).

#  O Salário Líquido corresponde ao Salário Bruto menos os descontos.

#  O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.



#Desconto do IR: - Salário Bruto até 900 (inclusive) - isento - Salário Bruto até 1500 (inclusive) - desconto de 5% - Salário Bruto até 2500 (inclusive)

#  - desconto de 10% - Salário Bruto acima de 2500 - desconto de 20%



#Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.



#Salário Bruto: (5 * 220)        : R$ 1100,00

#(-) IR (5%)                     : R$   55,00

#(-) INSS ( 10%)                 : R$  110,00

#FGTS (11%)                      : R$  121,00

#Total de descontos              : R$  165,00

#Salário Liquido                 : R$  935,00


hora_valor = float(input("Digite aqui o valor da sua hora: \n"))

horas_trabalhadas = float(input("Digite aqui quantas horas voce trabalhou: \n"))


salario = hora_valor * horas_trabalhadas


if salario < 900:
    IR= 00
elif salario <= 1500:
    IR = (5*salario)/100
elif salario <=2500:
    IR = (10*salario)/100
elif salario > 2500:
    IR = (20*salario)/100

descontos = IR + (salario*10)/100

print("Salario bruto: {}".format(salario))
print("IR: R${}".format(IR))
print("INSS: R${}".format((salario*10)/100))
print("FGTS: R${}".format((salario*11)/100))
print("Total de descontos: R${}".format(descontos))
print("Salario Líquido: R${}".format(salario - ((salario*15)/100)))

