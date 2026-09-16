#Contexto:
#Sistemas de folha de pagamento leem planilhas simples de horas trabalhadas para calcular o
#salário.


#Enunciado:
#Crie um arquivo horas.csv onde cada linha tem nome,horas_trabalhadas (ex: Bruna,160).
#Considere o valor da hora fixo em R$ 25,00. Leia o arquivo e gere pagamentos.txt, com cada linha
#no formato "nome: R$ valor_total".



with open('horas.csv', 'w') as arquivo:
        arquivo.write("Júlia,160\n")
        arquivo.write("Lucas,80\n")
        arquivo.write("Mateus,120\n")
        arquivo.write("Marcos,165\n")
        arquivo.write("Gabriel,180\n")
        arquivo.write("Maria,200\n")
        arquivo.write("Luiza,145\n")

lista = []
with open("horas.csv", 'r') as arquivo:
    for i in arquivo:
        partes = i.strip().split(',')
        lista.append(partes)

print(lista)

with open('pagamentos.txt', 'w') as arquivo:
    for i in lista:
        arquivo.write(f"{i[0]}: R$ {(int(i[1]))*25} \n")

with open('pagamentos.txt', 'r') as arquivo:
  for i in arquivo:
      print(i)   

