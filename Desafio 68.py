'''Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''
from random import randint
c = 0
print('-='*20)
print('      Vamos jogar PAR ou ÍMPAR!')
print('-='*20)
while True:
    pc = randint(0, 11)
    num = int(input('Escolha um número: '))
    esc = str(input('Escolha PAR ou ÍMPAR [P/I]: ')).strip().upper()[0]
    s = num + pc
    if s % 2 == 0:
        r = 'P'
        print('-' * 50)
        print(f'Você jogou {num} e o pc jogou {pc}. A soma {s} é PAR')
        print('-' * 50)
        if r == esc:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
        else:
            print('Você PERDEU!')
            break
    else:
        r = 'I'
        print('-' * 50)
        print(f'Você jogou {num} e o pc jogou {pc}. A soma {s} é ÍMPAR')
        print('-' * 50)
        if r == esc:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
        else:
            print('Você PERDEU!')
            break
    c += 1
print('-='*25)
print(f'GAME OVER! Você conseguiu {c} vitórias consecutivas!')
print('-='*25)
