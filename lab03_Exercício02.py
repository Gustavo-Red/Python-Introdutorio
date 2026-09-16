#Contexto: Sistemas de triagem governamentais ou acadêmicos processam planilhas brutas ex-portadas em formatos de texto para separar registros de interesse.

#Enunciado: Considere um arquivo chamado usuarios.csv onde cada linha contém o nome e a
#idade de uma pessoa separados por vírgula (ex: Carlos,17). Escreva um programa que leia este
#arquivo e gere um novo arquivo chamado maiores idade.txt, gravando nele apenas os nomes das
#pessoas que possuem 18 anos ou mais.


#### Criando a "base de dados" (o arquivo usuarios.csv) ####

with open ("usuarios.csv", 'w') as arquivo:
    conteudo = arquivo.write("Carlos , 17 \n")
    conteudo = arquivo.write("Jorge, 20 \n")
    conteudo = arquivo.write("Pedro, 15 \n")
    conteudo = arquivo.write("Lucas, 18 \n")
    conteudo = arquivo.write("Mariana, 19 \n")
    conteudo = arquivo.write("Ester, 21 \n")
    conteudo = arquivo.write("Marcos, 18 \n")
    conteudo = arquivo.write("Eduardo, 20 \n")
    conteudo = arquivo.write("Mateus, 21 \n")
    conteudo = arquivo.write("João, 14 \n")
    conteudo = arquivo.write("Thiago, 22 \n")

with open ("usuarios.csv", 'r') as arquivo:
    with open('maiores_idade.txt', 'w') as arquivo2: # <-- esse open ("usuarios.csv", r) de dentro é para excluir o arquivo se ja existir e para criar o arquivo "maiores_idade.txt" já existindo ele ou não.
        for linha in arquivo:
            partes = linha.split(',') # <-- A função split pega a linha do arquivo e divide em partes usando a virgula ( , ) como critério de divisão.
            if int(partes[1].strip()) >= 18: # <-- A função .strip remove espaços em branco e caracteres invisíveis das pontas de uma string como espaços e tabulações
                nome = arquivo2.write(f"{partes[0]} \n")

        