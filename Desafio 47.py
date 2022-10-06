'''Exercício Python 047: Crie um programa que mostre na tela todos
os números pares que estão no intervalo entre 1 e 50.'''
'''for c in range(1,51):
    if c % 2 == 0:
        print(c)''' # Este formato faz o laço acontecer 2 vezes, para otimizar melhor pular de 2 em 2
for c in range(2, 51, 2):
    print(c, end= ' ') # Nesta ele reduziu a quantidade de laços pela metade
print('Acabou')