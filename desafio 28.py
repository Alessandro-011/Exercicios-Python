from random import randint
nu = randint(0,5)
resp = int(input('Adivinhe o número que eu estou pensando: '))

if nu == resp:
    print(f'Acertou, pensei no número {nu} mesmo')
else:
    print(f'não é esse não! eu pensei no número {nu} e não em {resp}')
