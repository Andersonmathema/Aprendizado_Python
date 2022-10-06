'''Exercício Python 063: Escreva um programa que leia um número N
 inteiro qualquer e mostre na tela os N primeiros elementos de uma
Sequência de Fibonacci. '''
n = int(input('Digite quantos números da sequência você quer ver: '))
l= 2
n1 = 0
n2 = 1
print(n1, n2, end= ' ')
while l < n:
    l += 1
    c = n1 + n2
    n1 = n2
    n2 = c
    print('{}'.format(c), end=' ')
