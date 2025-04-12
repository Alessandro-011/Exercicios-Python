'''print('Gerador de PA')
print('=-'*7)
P_termo = int(input('\033[32mPrimeiro Termo:\033[0m '))
Razão= int(input('\033[32mRazão da PA:\033[0m'))

#inicializando as variáveis

contador = 1
termo = P_termo
print('Os 10 primeiros termos da PA são:')
while contador <= 10:
    print(termo, end= " → ")    # essa linha mostra cada termo
    termo += Razão              #Próximo Termo na PA
    contador += 1               #Incrementa o contador

print('FIM')'''


print('Gerador de P.A.')
print('=-'*6)
Primeiro_termo = int(input('Primeiro Termo: '))
Razão = int(input('Razão da P.A: '))

contador = 1

termo = Primeiro_termo
print(f'Os 10 primeiros termos da PA são:')
while contador <= 10:
    print(f'{termo} → ', end= ' → ')
    termo += Razão
    contador += 1
    print('Fim.')
