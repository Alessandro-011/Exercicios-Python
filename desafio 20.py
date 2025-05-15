from random import shuffle
squad_1 = []
squad_2 = []
for c in range (1,5):
    Aluno = str(input(f'Nome dos players: '))
    squad_1.append(Aluno)
shuffle(squad_1)
shuffle(squad_2)
print('Primeiro squad:')
print(squad_1)
print('Segundo squad:')
print(squad_2)
