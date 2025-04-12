soma = 0
acumulador = 0
for contador in range (1, 7):
    numeros=int(input('Digite um número inteiro:'))
    if numeros % 2 == 0:
        soma += numeros
        acumulador += 1
print(f'Foi informado {acumulador} números pares e a soma foi {soma}')


