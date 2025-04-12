while True:
    número = int(input('Quer ver a tabuada de qual valor? '))
    print('<>'*10)
    if número <0:
        break
    print('<>' * 10)
    for c in range(1, 11):
        print(f' {número} X {c} = {número*c}')
    print('<>' * 10)
print('Programa encerrado!')
