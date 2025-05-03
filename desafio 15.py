KM = int(input('Quantos KM você percorreu com o Manco? '))
Dias = int(input('Quantos dias você ficou com o Manco? '))
Diária = Dias * 60
Rodagem = KM * 0.15
print(f'O valor total desse Manco ai vai ficar de R${Diária+Rodagem:.2f}')