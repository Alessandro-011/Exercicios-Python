import time
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('Qual a tua opção? '))
    if opção == 1:
        print(f' {n1} + {n2} = {n1+n2}')
    elif opção == 2:
        print(f'{n1} x {n2} = {n1*n2}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f' {maior} é o maior.')
    elif opção == 4:
        print('Informe novamnete os valores:')
        n1 = int(input('Digite o primeiro número:'))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        time.sleep(2)
    else:
        print('Essa opção não existe!')
    print('⟫⟪'*14)
print('Fim.')

