#Apuração de Dados
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
#Verificando o menor número:
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print(f'O menor valor digitado foi {menor}.')

#Verificando o maior número:
maior = a
if b>a and b>c:
    menor = b
if c>a and c>b:
    maior = c
print(f'O maior número é {maior}.')


