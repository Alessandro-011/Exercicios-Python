quantia = int(input('Qual o valor que  deseja sacar? '))
total = quantia
quantidades_de_notas_totais = 0
nota = 50

while True:
    if total >=  nota:
        total -= nota
        quantidades_de_notas_totais += 1
    else:
        if quantidades_de_notas_totais > 0:
            print(f'Total de {quantidades_de_notas_totais} cédulas de R${nota}')

        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1

        quantidades_de_notas_totais = 0

        if total == 0:
            break


