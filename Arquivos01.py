# COMO CRIAR E MODIFICAR ARQUIVOS:
valores_celulares = [850, 2230, 1500, 3500, 5000]
###

# 'r' -> Usado somente para ler algo
# 'w' -> Usado somente para escrever algo (ele apaga tudo e escreve novamente)
# 'r+' -> Usado para ler e escrever algo
# 'a' -> Usado para acrescentar algo

#ESTRUTURA BASICA DE UM CODIGO DE MANIPULAÇÃO DE ARQUIVOS:
# with open ('[Nome do arquivo].[extensão]', '[modo - (r/w/r+/a)]') as [variável no caso w/r+/a]:

# PARA ESCREVER NO MODO 'w' E NO MODO 'a':
# [variável criada na estrutura anterior].write([O que voce quer escrever])

# FORMAS DE LER NO MODO 'r':
# [variável].read()       -> lê tudo como uma string só
# [variável].readlines()  -> lê tudo como uma lista de linhas
# for linha in [variável] -> lê linha por linha (usado no código acima)


with open ('valores_celulares.txt', 'w') as arquivo:
    for valor in valores_celulares:
        arquivo.write(str(valor) + '\n')


#Lendo o arquivo:
with open('valores_celulares.txt', 'r') as arquivo:
    for valor in arquivo:
        print(valor)