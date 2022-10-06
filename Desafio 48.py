'''Exercício Python 048: Faça um programa que calcule a soma entre todos
os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
s = 0
for c in range(1, 501):
    if c % 3 == 0:
        s = s + c
print('A soma de todos os múltiplos de 3 entre 1 e 500 dá {}'.format(s))
