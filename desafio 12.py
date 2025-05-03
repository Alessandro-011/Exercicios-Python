produto = float(input('Digite o valor do produto: '))
desconto = produto * 0.05
print(f'O produto que custava R${produto}, na promoção com desconto de 5% vai custar R${produto - desconto:.2f}')