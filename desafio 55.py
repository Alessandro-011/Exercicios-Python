maior_peso = 0
menor_peso = 0
for pessoas in range (1, 4):
    pesos = float(input(f'Digite o peso da {pessoas}° pessoa:'))
    if pessoas == 1:
        maior_peso = pesos
        menor_peso = pesos
    else:
        if pesos > maior_peso:
            maior_peso = pesos
        if pesos < menor_peso:
            menor_peso = pesos
print(f'O maior peso foi Kg{maior_peso} e o menor peso foi Kg{menor_peso}')




