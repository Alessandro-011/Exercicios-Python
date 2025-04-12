""""Faça um programa que leia uma frase pelo teclado e mostre:

quantas vezes aparece a letra (a)

em que posição ela aparece a primeira vez.

em qeu posição ela aparece a última vez."""

fsr = str(input('Digite uma frase pelo teclado: ')).upper().strip()
print(f'A letra A aparece {(fsr.count('A'))} vezes na frase.')
"""o metodo count  é usado pra contar quantas vezes um determinado item
 aparece em uma string"""
#exemplo do uso do metodo count
"""lista = [1,2,3,4,1,2,1]
contagem = lista.count(1)

print(f'O número 1 aparece {contagem} vezes na lista.')"""

print(f'A primeira letra A apareceu na position {(fsr.find('A')+1)}.')
"""o .find é usado pra encontrar a primeira ocorrencia de uma substring
dentro de uma string no caso uma substring é uma palavra dentro de uma frase"""
print(f'E a última letra A apareceu na position {(fsr.rfind('A')+1)}.')
"""e o .rfind vai fazer a mesma coisa só que pelo lado contrário do codigo"""


