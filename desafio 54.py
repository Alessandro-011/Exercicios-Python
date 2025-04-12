'''menor_idade = 0
maior_idade = 0
for c in range (1, 8):
    idade =int(input(f'Em que ano a pessoa {c}° nasceu:'))
    if idade < 2007:
        maior_idade += 1
    else:
        menor_idade += 1
print(f'Ao todo tivemos {maior_idade} pessoas de maior e {menor_idade} de menor.')'''''

from datetime import date
ano_atual = date.today().year
maior_idade = 0
menor_idade = 0
for pessoa in range (1, 4):
    nascimento =int(input(f'Em que ano a {pessoa}°pessoa nasceu?'))
    idade = ano_atual - nascimento
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print(f'Tivemos {menor_idade} menores e {maior_idade} maior.')



