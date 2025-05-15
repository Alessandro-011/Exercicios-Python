salário = float (input('Qual o seu salário atual? '))
if salário > 1250.00:
    aumento = salário * 0.10
    novo_salário = salário + aumento
else:
    aumento = salário * 0.15
    novo_salário = salário + aumento
print(f'Seu salário passa a ser {novo_salário}')








