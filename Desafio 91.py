'''Exercício Python 091: Crie um programa onde 4 jogadores joguem
um dado e tenham resultados aleatórios. Guarde esses resultados
em um dicionário em Python. No final, coloque esse dicionário em
ordem, sabendo que o vencedor tirou o maior número no dado.
jogador 1 tirou 5...
Ranking
1º lugar: jogador 3 com 6'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('---Ranking dos jogadores---')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #para ordenar dicionarios library operator
print('-='*30)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
