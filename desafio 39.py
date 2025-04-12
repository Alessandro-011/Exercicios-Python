idade = int(input('Digite sua idade: '))
if idade < 18:
    restam = 18 - idade
    print(f' Você ainda não pode se alistar ainda faltam {restam} anos!')
elif idade == 18:
    print(f'Muito bom, está no momento certo do seu alistamento!')
elif idade > 18:
    atrasado = idade - 18
    print(f'Você está com o alistamento atrasado {atrasado} anos!')