'''Exercício Python 053: Crie um programa que leia uma frase
qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''
#APOS A SOPA
frase = str(input('Digite uma frase: ')).strip().upper()
pal = frase.split()
junto = ''.join(pal)
inverso = ''
for letra in range(len(junto) - 1, -1, -1): #letra é contador, len-1 começa da ultima e vai até a primeira, -1 voltando de uma em uma
    inverso += junto[letra]  #Começa da ultima posição (A) da contagem, e vai juntando com a posição anteriores (fatiamento:A, AP, APOS...)
print(junto, inverso)
if inverso == junto:
    print('O inverso de {} é {} \nTemos um palíndromo!'.format(junto, inverso))
else:
    print('A frase digitada não é um palíndromo')

#Sem o FOR
'''frase = str(input('Digite uma frase: ')).strip().upper()
pal = frase.split()
junto = ''.join(pal)
inverso= junto[::-1]
if inverso == junto:
    print('O inverso de {} é {} \nTemos um palíndromo!'.format(junto, inverso))
else:
    print('A frase digitada não é um palíndromo')'''
