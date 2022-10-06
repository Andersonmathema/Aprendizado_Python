'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros
colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
times = ('Flamengo', 'Internacional', 'Atlético MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
         'Athletico PR', 'RB Bragantino', 'Ceará', 'Corinthians', 'Atlético GO', 'Bahia', 'Sport', 'Fortaleza',
         'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
print(f'Os cinco primeiros colocados foram: {times[0:5]}')
print(f'Os quatro últimos colocados foram: {times[16:]}') #ou times[-4:]
print(f'Os times em ordem alfabética foram: {sorted(times)}')
print(f'A posição do Ceará é {times.index("Ceará")}º')
