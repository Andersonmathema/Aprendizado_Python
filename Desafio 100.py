'''Exercício Python 100: Faça um programa que tenha uma lista chamada números
 e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear
5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
entre todos os valores pares sorteados pela função anterior.'''
from random import randint
numeros = list()


def sorteia():
    c = 0
    while c < 5:
        n = randint(0, 10)
        numeros.append(n)
        c += 1
    return numeros


def somaPar(lista):
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    return s


print(f'Os números sorteados foram {sorteia()}')
print(f'A soma dos pares foi {somaPar(numeros)}')
