'''Exercício Python 051: Desenvolva um programa que leia o primeiro termo
e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''
a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
for c in range(0, 10):
    an = a1 + c*r
    print('a{} = {}'.format(c+1, an))
