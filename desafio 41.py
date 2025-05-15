ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = 2025
idade = ano_atual - ano_nascimento
if idade <= 9 :
    print(f'O atleta tem {idade} anos.')
    print('Classificação: MIRIM.')
elif idade <= 14:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: INFANTIL.')
elif idade <= 19:
    print(f'O atetla tem {idade} anos.')
    print('Classificação: JÚNIOR.')
elif  idade <= 25:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: SÊNIOR.')
else:
    print(f'O atetla tem {idade} anos.')
    print('Classificação: MASTER.')



