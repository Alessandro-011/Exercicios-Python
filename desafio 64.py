n = cont = soma = 0
n = int(input('Digite um número [999 para parar!]: '))
while n != 999:
    cont+= 1
    soma += n
    n = int(input('Digite um número [999 para parar!]: '))
#print(f'Você digitou {cont-1} números e a soma é {soma-999}')
print(f'Você digitou {cont} números e a soma é {soma}')


