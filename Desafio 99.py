'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu programa tem que analisar
todos os valores , mostrar quantos foram informados e dizer qual deles é o maior.'''
from time import sleep


def maior(*valores):
    if len(valores) == 0:
        tam = 0
        maior = 0
    else:
        maior = valores[0]
        print('Analisando os valores passados...')
        for n in valores:
            if n > maior:
                maior = n
            print(f' {n} ', end='')
            sleep(1)
        tam = len(valores)
    print(f'Foram informados {tam} valores ao todo')
    sleep(1)
    print(f'O maior valor foi {maior}')
    print('-'*30)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


