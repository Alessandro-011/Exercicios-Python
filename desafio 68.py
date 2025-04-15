
from random import randint
v = 0
while True:
    player = int(input('Diga um valor: '))
    pc = randint (0,10)
    total = player + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {player} e o PC {pc}. Total de {total}', end= ' ')
    print(f'Deu par!' if total % 2 == 0 else 'Deu impar!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu! ')
            v += 1
        else:
            print('Você PERDEU! ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu! ')
            v += 1
        else:
            print('Você PERDEU! ')
            break
    print('Vamos jogar novamente...')
print(f'FIM DE JOGO, você venceu {v} vezes.')

