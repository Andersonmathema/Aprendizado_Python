'''Exercício Python 093: Crie um programa que gerencie o aproveitamento
de um jogador de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada
partida. No final, tudo isso será guardado em um dicionário, incluindo
o total de gols feitos durante o campeonato.'''
nome = str(input('Digite o nome do jogador: '))
partidas = int(input('Digite quantas partidas ele jogou: '))
tot = 0
gol = list()
for n in range(0, partidas):
    gols = int(input(f'Quantos gols ele fez na partida {n}? '))
    gol.append(gols)
    tot += gols #sum(gol) == soma os valores dentro da lista
jogador = {'Nome': nome, 'Gols': gol, 'Total': tot}
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas')
for pos in range(0, partidas):
    print(f'=> Na partida {pos}, fez {jogador["Gols"][pos]} gols')
print(f'Foi um total de {tot} gols.')
