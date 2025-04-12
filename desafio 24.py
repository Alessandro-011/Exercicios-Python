""""crie um programa que leia o nome de uma cidade
 e diga se ela começa ou não com o nome SANTOS"""

city = str (input('Digite o nome da cidade: ')).strip()
print(city[:5].upper() == 'SANTO')
"""":5 começa do começo da string.  
Os dois sinais de =  refere-se a igualdade. 
o comando .strip tira os espaços desnecessários.
o comando .upper vai verificar se há letras em maiúsculas
de qualquer maneira que a pessoa digitar essee comando 
vai transformar a palavra santo em letras maiúsculas 
"""