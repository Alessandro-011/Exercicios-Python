from random import randint
computer = randint (0,10)
print('Sou computer... Acabei de pensar em número entre 0 e 10.')
print('Será que você consegue adivinha qual foi? ')
acertou = False
palpites = 0
while not acertou:
    player = int(input('Adivinhe qual é: '))
    palpites += 1
    if player  == computer:
        acertou = True
    else:
        if player < computer:
            print('Mais... vai mais uma vez: ')
        elif player > computer:
            print('Menos... vai mais uma vez: ')
if palpites <3:
    print(f'Acerotu com \033[32m{palpites}\033[0m tentativas, essa foi boa!')
else:
    print(f'Acerotu com \033[31m{palpites}\033[0m tentativas, foi baixo nengue.')




