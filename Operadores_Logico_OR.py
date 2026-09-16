entrada = input("[E]ntrar [S]air: \n")
print('\n')

senha_digitada = input("Senha: \n")
print("\n")

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print("ENTRANDO...")
else:
    print("Até a próxima...")



