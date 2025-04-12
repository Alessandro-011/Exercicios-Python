numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções para converter:
[1] Binário 
[2] Octal
[3] hexadecimal''')
opção = int(input('Sua opção: '))

if opção ==1:
    print(f'{numero} Convertido para bináro é igual a {bin(numero)[2:]}')
elif opção ==2:
    print(f'{numero} Convertido para Octal é igual a {oct(numero)[2:]}')
elif opção==3:
    print(f'{numero} Convertido pra Hexadecimal é igual a {hex(numero)[2:]}')
else:
    print('Digito errado reinicie o programa.')