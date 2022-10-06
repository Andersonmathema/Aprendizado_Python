'''Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador
 vai "pensar" em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar
 até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
'''from random import choice
num = int(input('Pensei em um número entre 0 e 10, pensei em: '))
vez = 0
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ran = choice(lista)
while num != ran:
    print('Você errou, tente novamente!')
    num = int(input('Pensei em: '))
    vez += 1
if num == ran:
    print('Você acertou, você precisou de {} tentativas para acertar!!!'.format(vez+1))'''
#Resposta do Guanabara com condição se o número é mais alto ou mais baixo
from random import randint
computador = randint(0, 10)
print('Pensei em um número entre 0 e 10')
acertou = False
vez = 0
while not acertou:
    num = int(input('Pensei em: '))
    vez += 1
    if num == computador:
        acertou = True
    else:
        if num < computador:
            print('Mais...Tente mais uma vez.')
        elif num > computador:
            print('Menos...Tente mais uma vez')
print('Você acertou, você precisou de {} tentativas para acertar!!!'.format(vez))




