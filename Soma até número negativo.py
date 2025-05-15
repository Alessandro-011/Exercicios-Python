soma = 0
while True:
    número = int(input('Digite um número: '))
    if número >= 0:
        soma += número
    else:
        break
print(f'A soma de todos os números = {soma}')
