senha = "ryan gay"
while True:
    digite = str(input('Digite sua senha para prosseguir: '))
    if digite.lower() != senha.lower():
        print(f'Senha incorreta tente novamente: ')
    else:
        print(f'{digite} É a senha correta!')
        break
