#crie um program que laia o nome completo de uma  pessoa  e mostre:

nome = (input('digite seu nome completo:'))

#O nome com todas as letras maiúsculas:
print('O nome com todas as letras maiúsculas:')
print(nome.upper())

#O nome com todas as letras minúsculas
print('O nome com todas as letras minusculas:')
print(nome.lower())

#Quantas letras ao todo sem considerar espaços:
print('Qantidade de letras desconsiderando os espaços: ')

print(len(nome.replace(' ','')))
'''Neste ponto, o comando len vai contar todos os caracteres
junto com os espaços e depois o replace vai substituir espaços por 
um espaço vazio'''

#quantas letras tem o primeiro nome:
print('Quntidade de letras contidas no primeiro nome: ')
primeiro_nome = nome.split()[0]
print(len(primeiro_nome))
''''O comando split é usado pra dividir uma string de uma lista de
substrings com base em um delimitador especifico que no caso são os
espaços entre as palavras'''