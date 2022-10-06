'''Exercício Python 033: Faça um programa que leia três números e
mostre qual é o maior e qual é o menor.'''
'''n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
menor = 0
maior = 0
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
print('O maior número é {} e o menor é {}'.format(maior,menor)) o meu criado'''
#_________________________________________________________________________________________
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# Verificando menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número é {} e o menor é {}'.format(maior,menor))

