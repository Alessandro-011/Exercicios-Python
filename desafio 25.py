""""crie um programa que leia o nome de uma pessoa
e diga se tem SILVA no nome."""

nome = str(input('Digite seu nome: ')).strip()
print(f'Seu nome tem Silva? {'silva'in nome.lower().split()}')
