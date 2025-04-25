while True:
    número = int(input('Quer ver a tabuada de qual valor?'))
    if número <0:
        break
    print('='*12)
    for i in range (1,11):
        print(f'{i} x {número} = {i*número}')
    print('=' * 12)
print('Prontinho!')
