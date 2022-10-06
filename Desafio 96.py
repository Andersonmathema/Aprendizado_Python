'''Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e
mostre a área do terreno.'''
def area(larg, alt):
    a = larg * alt
    print(f'A área equivale a {a:.2f}u²')

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area(largura, altura)
