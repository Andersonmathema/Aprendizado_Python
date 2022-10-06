'''Exercício Python 028: Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
from random import choice
num = int(input('Pensei em um número entre 0 e 5, pensei em : '))
if num > 5 or num < 0:
    print('Errado, escolha entre 0 e 5: ')
lista = [0, 1, 2, 3, 4, 5]
ran = choice(lista)
if num == ran:
    print('Você acertou!!!')
else:
    print('Você errou, o número pensado foi {}'.format(ran))
