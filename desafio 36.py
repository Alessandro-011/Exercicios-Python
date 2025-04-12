casa = float(input('Valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Digite em quantos anos você deseja pagar: '))

prestação = casa / (anos * 12)
minimo = salario * 30 / 100

print('\033[36m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[0m')

print(f'''Para pagar uma casa no valor de \033[34mR${casa:.2f} 
\033[0mem \033[34m{anos}\033[0m anos, a prestação será de \033[34mR${prestação:.2f}\033[0m''')

print('\033[36m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[0m')

if  prestação <= minimo:
    print('\033[32mEmpréstimo Concedido!\033[0m')
else:
    print('\033[31mEmpréstimo negado da melhor forma!\033[0m')