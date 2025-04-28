# cabeçalho do caixa eletrônico
placa = "Banco do Pega"
color = f'\033[34m{placa}\033[0m'
print('='* 32)
print(f'{color: ^39}')
print('='*32)

# entrada de dados do usuário
valor = int(input('Que valor você quer sacar? R$'))

#inicialização das variáveis de saque
total = valor
cédula = 50
total_cédulas = 0

#Estrutura principal o laço while
while True:
    if total >= cédula:     # Se o total ainda for maior ou igual ao valor da cédula atual:
        total -= cédula     # Subtrai o valor da cédula do total.
        total_cédulas += 1  # Incrementa 1 na quantidade de cédulas da nota.

    else:   # Se o total não for mais suficiente para tirar uma cédula do valor atual:

        if total_cédulas > 0:   # Só vai escrever se o total de cédulas for maior que zero.
            print(f'Total de {total_cédulas} cédulas de R${cédula}')    # Quantas cédulas daquele valor foram usadas.


        #Aqui irá mudar o valor da cédula
        if cédula == 50:  # Aqui ele estava usando 50, e passou para 20
            cédula = 20
        elif cédula == 20:  # De 20 para 10
            cédula = 10
        elif cédula == 10:  # De 10 para 1
            cédula = 1

        # Depois de mudar o valor da cédula, zera o contador de cédulas para contar a quantidade da nova nota.
        total_cédulas = 0

        # Quando o valor total for sacado o break vai parar o programa exibindo o resultado lá de cima
        if total == 0:
            break




