número = soma = contador = 0

while True:
    número = int(input('Digite um número: '))
    if número == 00:
        break
    soma += número
    contador += 1
print(f'Foram digitados {contador} números e a soma deles é igual a: {soma}.')
