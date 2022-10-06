from random import choice
from time import sleep
print('\033[1;35m-=\033[m' * 15)
print('Game : \033[1;33mPEDRA - PAPEL - TESOURA\033[m')
print('\033[1;35m-=\033[m' * 15)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
comp = lista.index(choice(lista))# escolha aleatória do computador
jog = int(input('''
[0]PEDRA
[1]PAPEL 
[2]TESOURA
Digite seu número: '''))# escolha aleatória do usuário
if jog != 0 and jog != 1 and jog != 2:
    print('Número inválido. Tente novamente.')
else:
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!')
    sleep(1)
    print('-=' * 15)
    print(f'Computador escolheu {lista[comp]}')
    print(f'Você escolheu {lista[jog]}')
    print('-=' * 15)
    if comp == 0:
        if jog == 0:
            print('EMPATE')
        elif jog == 1:
            print('Você GANHOU!')
        elif jog == 2:
            print('Você PERDEU')
    elif comp == 1:
        if jog == 0:
            print('Você PERDEU')
        elif jog == 1:
            print('EMPATE')
        elif jog == 2:
            print('Você GANHOU!')
    elif comp == 2:
        if jog == 0:
            print('Você GANHOU!')
        elif jog == 1:
            print('Você PERDEU')
        elif jog == 2:
            print('EMPATE')
