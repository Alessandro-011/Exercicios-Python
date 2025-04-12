distancia = float(input('Qual a distancia da viagem?'))
if distancia <= 200:
    calculo = distancia * 0.50
    print(f'O valor da sua viagem ficará de R${calculo:.2f} cada km custou 50 centavos!')
else:
    calculo_2 = distancia * 0.45
    print(f'sua viagem custou 45 centavos por KM totalizando em R${calculo_2}')