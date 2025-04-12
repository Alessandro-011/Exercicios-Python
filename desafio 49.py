numero = int(input('Digite um número para ver sua tabuada: '))
for contador in range(1,11):
    print(f' {numero} X {contador:2} = {contador*numero}')