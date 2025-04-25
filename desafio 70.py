palavra = 'LOJA DO NEGÃO'
total = mais_de_mil = 0
menor = 0
contadeiro = 0
cumpensa = ''
color = f'\033[34m{palavra}\033[0m'
final = 'Fim dessa Merda!'
print('-' * 30)
print(f'{color:-^39}')
print('-' * 30)
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    contadeiro += 1
    total += preço
    if preço > 1000:
        mais_de_mil += 1
    if contadeiro == 1:
        menor = preço
        cumpensa = produto
    else:
        if preço < menor:
            menor = preço
            cumpensa = produto

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
            break
print(f'{final:-^30}')
print(f'O total da compra foi de \033[33mR${total:.2f}\033[0m')
print(f'Temos \033[33m{mais_de_mil}\033[0m produtos que custam mais de \033[33mR$1.000\033[0m reais.')
print(f'O produto mais barato foi: \033[33m{cumpensa}\033[0m, que custou \033[33mR${menor:.2f}\033[0m')

