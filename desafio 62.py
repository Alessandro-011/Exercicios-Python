print('Gerador de PA')
print('=-'*7)
P_termo = int(input('\033[32mPrimeiro Termo:\033[0m '))
Razão= int(input('\033[32mRazão da PA:\033[0m'))

#inicializando as variáveis
total = 0
contador = 1
termo = P_termo
T_mais = 10
print('Os 10 primeiros termos da PA são:')
while T_mais !=0:
    total += T_mais
    while contador <= total:
        print(termo, end= " → ")    # essa linha mostra cada termo
        termo += Razão              #Próximo Termo na PA
        contador += 1               #Incrementa o contador
    print('Pausa')
    T_mais = int(input('Quantos termos vocês querem mostrar a mais?'))
print(f'Progressão finalizada com {total} termos.')