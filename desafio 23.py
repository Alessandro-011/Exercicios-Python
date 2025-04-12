#faça um programa que leia um número de   0 a 9999 e mostre
# na tela cada um dos digitos separados.

"""ex:
digite um número:1834
unidade:4
dezena:3
centena8
milhar:1 """

numero = int(input('Digite um número: '))

unidades = numero % 10
desenas = (numero // 10) % 10
centenas = (numero // 100) % 10
milhares = (numero // 1000) % 10

print(f'unidades:{unidades}')
print(f'desenas:{desenas}')
print(f'centenas:{centenas}')
print(f'milhar:{milhares}')

