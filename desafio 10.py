carteira = float(input('Quanto você tem ai na carteira? R$'))
print(f'Com \033[34mR${carteira}\033[0m você pode comprar \033[32mUS${(carteira/5.79):.2f}\033[0m')
