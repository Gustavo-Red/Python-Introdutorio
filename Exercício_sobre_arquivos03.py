#Contexto:
#Sistemas de cadastro de e-mail costumam padronizar tudo em minúsculo para evitar duplicidade de
#registros.

#Enunciado:
##Crie um arquivo emails.txt com pelo menos 5 e-mails, misturando maiúsculas e minúsculas (ex:
#Carlos@Email.COM). Leia o arquivo e grave uma cópia em emails_padronizados.txt, com todos os
#e-mails em letras minúsculas.

emails = ["JoaozinhoJunior@gmail.com", "AleatorioR@gmail.com", "Random02@gmail.com", "MalucoLouco@gmail.com", "PeterParker@gmail.com"]

print("SEM CORRIGIR OS EMAILS DEIXANDO COM LETRA MINÚSCULA \n")

with open('emails.txt', 'w') as arquivo:
    for email in emails:
        arquivo.write(f"{email}" + "\n")

with open('emails.txt', 'r') as arquivo:
    for email in arquivo:
        print(email)

print("DEPOIS DE CORRIGIR OS EMAILS DEIXANDO COM LETRA MINÚSCULA \n")

with open('emails_padronizados.txt', 'w') as arquivo:
    for email in emails:
        arquivo.write(f"{email.lower()}" + "\n")

with open("emails_padronizados.txt", 'r') as arquivo02:
    for email in arquivo02:
        print(email)
