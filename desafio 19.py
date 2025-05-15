from random import choice
lista = [] # cria a lista vazia antes do laço
for c in range (1, 5):
    aluno = str(input(f'{c}° aluno: '))
    lista.append(aluno) # Adiciona o nome do aluno na lista

escolhido = choice(lista) # Aqui ele sorteia um nome da lista
print(f'O aluno escolhido foi {escolhido}.')


