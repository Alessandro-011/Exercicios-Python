largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
litros = area / 2
print(f'Sua parede tema a dimensão de {altura}x{largura} e sua área é de {area:.2f}m².')
print(f'Para pintar essa parede, você precisará de {litros:.2f} de tinta.')