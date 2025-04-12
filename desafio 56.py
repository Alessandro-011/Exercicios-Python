soma_de_idades = 0
media_de_idades = 0
homem_mais_velho = 0
mulheres_com_mais20 = 0
nome_do_mais_velho = ''
for pessoas in range(1,5):
    print(f'=-=-=-=- {pessoas}° Pessoa =-=-=-=- ')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]:')).strip()
    soma_de_idades += idade
    ''''^^^Isso é: a soma da idade, recebe ela mesma e a soma da idade.
    tipo se soma_de_idade estiver com 18 de idade e idade estiver 
    com 2 o soma_de_idade vai receber esses valores e acumular eles '''
    if pessoas == 1 and sexo in 'Mm':
        homem_mais_velho = idade
        nome_do_mais_velho = nome
        ''''^^^aqui iremos ter: se a  pessoa for a primeira pessoa, a idade do homem mais velho 
        vai recerber o valora da variável idade. e o nome do homem mais velho vai receber o
        dado digitado na variável nome.
         E o sexo ser masculino [in] em M ou m'''
    if sexo in 'Mm' and idade > homem_mais_velho:
        homem_mais_velho = idade
        nome_do_mais_velho = nome
        ''''^^^se o sexo ainda estiver dentro de masculino e se a idade do cara for maior
        do que a maior idade do homem '''
    if sexo in 'Ff' and idade < 20:
        mulheres_com_mais20 += 1
media_de_idades = soma_de_idades / 4
''''nessa parte aqui teremos uma variável que acumulou a soma de todas as idades 
e uma variável pra receber o valor da media que nesse caso vai ser o valor da idade de
todos as pessoas dididido por 4 porque o laço é feito pra essa quantia de pessoas'''

print(f'A média das idades foi de {media_de_idades:.0f} anos.')
print(f'O home mais velho tem {homem_mais_velho} e se chama {nome_do_mais_velho}')
print(f'Existe {mulheres_com_mais20} com menos de 20 anos.')
