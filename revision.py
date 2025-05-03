quantia = int(input('Qual valor você deseja sacar? '))
total = quantia
cédula = 50
cédulas_totais = 0
while True:
    if total >= cédula:
        total -= cédula
        cédulas_totais += 1
    else:
        if cédulas_totais > 0:
            print(f'Total de {cédulas_totais} cédulas de R${cédula},00.')
        if cédulas_totais == 1:
            print(f'Total de {cédulas_totais} cédula de R${cédula},00.')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        cédulas_totais = 0
        if total == 0:
            break



