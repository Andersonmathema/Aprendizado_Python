'''Exercício Python 074: Crie um programa que vai gerar cinco
números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique
o menor e o maior valor que estão na tupla.'''
from random import randint
lista = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(lista)
nmaior = nmenor = lista[0]
for c in range(0,5):
    if nmaior < lista[c]:
        nmaior = lista[c]
    if nmenor > lista[c]:
        nmenor = lista[c]
print(f'O maior número é {nmaior} e o menor número é {nmenor}') #Poderia usar as funções max(lista) e min(lista) para maiores e menores

