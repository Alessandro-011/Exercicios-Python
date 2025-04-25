'''total_18 = 0
total_homis = 0
total_muié_20 = 0
while True:
    idade  = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade > 18:
        total_18 += 1
    if sexo == 'M':
        total_homis += 1
    if sexo == 'F' and idade < 20:
        total_muié_20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
            break
print(f'Total de pessoas com mais de 18 anos: {total_18}.')
print(f'Total de homens {total_homis}.')
print(f'E temos {total_muié_20} mulheres com menos de 20 anos.')
print('\033[32mSe acabou kikiki\033[0m')'''
total_18 = total_machos = total_femia = 0
while True:
    idade = int(input('Qual tua idade?'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('teu secsu? [M/F]')).strip().upper()[0]
    if idade > 18:
        total_18 += 1
    if sexo == 'M':
        total_machos += 1
    if sexo == 'F' and idade < 20:
        total_femia += 1
        resposta = ' '
        while resposta not in 'SN':
            resposta = str(input('Quer mais rubu? [S/N]' )).strip().upper()[0]
        if resposta == 'N':
                break
print(f'Pessoas com mais de 18: {total_18}')
print(f'Machos: {total_machos}')


