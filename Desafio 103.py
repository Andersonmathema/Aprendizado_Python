'''Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele
marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
algum dado não tenha sido informado corretamente. (se nao for dito o nome ou
gols indique jogador <desconhecido> e 0 gols)'''


def ficha(jogador = '<desconhecido>', gols = 0):
    print(f'O jogador {jogador} fez {gols} gols')


jogador = str(input('Digite o nome do jogador: '))
gols = str(input('Digite a quantidade de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    ficha(gols=0)
else:
    ficha(jogador, gols)

