'''Exercício Python 064: Crie um programa que leia vários
números inteiros pelo teclado.
O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e
qual foi a soma entre eles (desconsiderando o flag 999).'''
#Meu jeito
'''num = c = l = 0
while num != 999:
    num = int(input('Digite um número ou 999 para parar: '))
    l += num
    c += 1
print('Você digitou {} números e a soma deles é {}'.format(c-1, l - 999))'''
#Guanabara
num = c = l = 0
num = int(input('Digite um número ou 999 para parar: ')) # diminuiu a contagem em 1 == c - 1, se digitar 999 ele vai sair sem somar 999
while num != 999:
    l += num
    c += 1
    num = int(input('Digite um número ou 999 para parar: '))
print('Você digitou {} números e a soma deles é {}'.format(c, l))
