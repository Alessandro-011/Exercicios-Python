soma = 0
multiplicação = 0
número = int(input('Digite um número para sua tabuada: '))
while True:
    print('    =' * 5)
    escolha = int(input("""    Opções:
    [1] Soma 
    [2] Multiplicação
    [0] Para sair"""))
    print('    ='*5)
    if escolha == 1:
        for c in range (1,11):
            print(f'    {número} + {c} = {número + c}' )
    if escolha == 2:
        for c in range (1,11):
            print(f'    {número} x {c} = {número * c}')
    if escolha == 0:
        break
