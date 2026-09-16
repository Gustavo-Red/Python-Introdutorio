#Contexto: Módulos de processamento de texto frequentemente precisam computar estatísticas
#básicas de arquivos para alocação de buffers de memória.

#Enunciado: Crie um programa que leia um arquivo de texto chamado poema.txt. O programa
#deve iterar pelo arquivo e exibir na tela duas estatíısticas: o número total de linhas e o número
#total de palavras presentes nele.



with open ("poema.txt", 'w') as arquivo:
    poema = arquivo.write("A vós correndo vou, braços sagrados,\n")
    poema =arquivo.write("Nessa cruz sacrossanta descobertos \n")
    poema =arquivo.write("Que, para receber-me, estais abertos, \n")
    poema =arquivo.write("E, por não castigar-me, estais cravados.\n")
    poema =arquivo.write("A vós, divinos olhos, eclipsados \n")
    poema =arquivo.write("De tanto sangue e lágrimas cobertos, \n")
    poema =arquivo.write(" Pois, para perdoar-me, estais despertos, \n")
    poema =arquivo.write("E, por não condenar-me, estais fechados. \n")
    poema =arquivo.write("A vós, pregados pés, por não deixar-me, \n")
    poema =arquivo.write("A vós, sangue vertido, para ungir-me, \n")
    poema =arquivo.write("A vós, cabeça baixa, p’ra chamar-me, \n")
    poema =arquivo.write("A vós, lado patente, quero unir-me, \n")
    poema =arquivo.write("A vós, cravos preciosos, quero atar-me, \n")
    poema =arquivo.write("Para ficar unido, atado e firme. \n")
    poema =arquivo.write(" ~ Gregório de Matos.")
 
 


soma = 0
with open ("poema.txt", 'r') as arquivo:
    conteudo = arquivo.readlines()
    print(f"Há {len(conteudo)} linhas no arquivo poema.txt")
    for linha in conteudo:
        palavra = linha.split()
        soma = len(palavra) + soma
    print(f"Há {soma} palavras no arquivo poema.txt")
