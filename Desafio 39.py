'''Exercício Python 039: Faça um programa que leia o ano de nascimento
de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
alistar ao serviço militar, se é a hora exata de se alistar
 ou se já passou do tempo do alistamento. Seu programa também deverá
 mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
an = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - an
if idade == 18:
    print('Agora é a hora de se alistar, você tem 18 anos!')
elif idade < 18:
    print('Você ainda vai se alistar daqui há {} anos'.format(18-idade))
else:
    print('já passou seu tempo de alistamento há {} anos'.format(idade-18))

