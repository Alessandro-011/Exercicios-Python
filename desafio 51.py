
Primeiro_Termo = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a razão: '))
enezimo_termo = Primeiro_Termo + (10 - 1) * razão
for i in range (Primeiro_Termo, enezimo_termo + razão, razão):
    print(f'\033[34m{i} \033[0m', end = '\033[34m  -> \033[0m')
print('acabou!')