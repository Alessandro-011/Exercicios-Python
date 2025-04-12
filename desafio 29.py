vel = int (input('qual a velocidade atual do carro: '))
if vel > 80:
    print('\033[33mSua velocidade excedeu o limite de 80km/h\033[m')
    mu = (vel-80)*7
    print(f'\033[31mvocê foi multado no valor de R${mu}\033[m')
else:
    print('\033[36mOk, tenha um bom dia e dirija com cuidado!\033[m')