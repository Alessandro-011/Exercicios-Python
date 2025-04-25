while True:
    número = int(input('Quer ver a tabuada de qual valor? '))
    if número <0:
        break
    print('<>' * 8)
    for c in range(1, 11):
        print(f' {número} X {c} = {número*c}')
    print('<>' * 8)
print('Programa encerrado!')

