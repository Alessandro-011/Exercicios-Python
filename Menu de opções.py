resultado = 0
while True:
    Opção = int(input('''Qual a sua opção:
    [1] Somar dois números 
    [2] Subtrair dois números 
    [3] Multiplicar dois números
    [4] Sair do programa 
    Opção: '''))

    if Opção == 4:
        break
    número_1 = int(input('Digite o primeiro número: '))
    número_2 = int(input('Digite o segundo número: '))
    if Opção == 1:
        resultado = número_1 + número_2
    if Opção == 2:
        resultado = número_1 - número_2
    if Opção == 3:
        resultado = número_1 * número_2


    print(f'Resultado: {resultado}')
print('Programa encerrado!!!')




