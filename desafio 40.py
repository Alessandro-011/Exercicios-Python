nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite o valor da segunda nota: '))

media = (nota_2 + nota_1) / 2
if media < 5.0:
    print(f' {media}  Reprovado ')
elif 5.0 < media < 6.9:
    print(f'{media} Recuperação ')
elif media > 7.0:
    print(f'{media} Aprovado ')

