sexo = str(input('Informe seu Sexo [M/F]:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos,informe seu Sexo [M/F]:')).strip().upper()[0]
print(f'Sexo {sexo} registrado.')





