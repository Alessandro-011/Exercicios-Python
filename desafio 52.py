numero = int(input('Digite um número: '))
total = 0
for c in range (1, numero+1):
    if numero % c == 0:
        print('\033[32m', end= '')
        total += 1
    else:
        print('\033[31m', end= '')
    print(f'{c} ', end= '')
print(f'\n\033[0mO número {numero} foi dividido {total} vezes.')
if total == 2:
    print('Por isso ele é primo.')
else:
    print('por isso ele não é primo.')