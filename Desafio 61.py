'''Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
 mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
c = 0
while c < 10:
    an = a1 + c*r
    c += 1  #range de while precisa estar dentro do laço
    print('a{} = {}'.format(c, an))
