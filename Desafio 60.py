'''Exercício Python 060: Faça um programa que leia um
 número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120. Dá pra fazer com for'''
# Com FOR
'''num = int(input('Digite o número escolhido: '))
r = 1
for c in range(num, 1, -1):
    r = r*c
print('O resultado de {}! é {}.'.format(num, r))'''
# Com biblioteca math.factorial
'''from math import factorial
num = int(input('Digite o número escolhido: '))
f = factorial(num)
print('O resultado de {}! é {}.'.format(num, f))'''
# Com WHILE
'''num = int(input('Digite o número escolhido: '))
r = 1
p = num
while num != 1:
    num = num - 1
    r = (num + 1) * r
print('O resultado de {}! é {}.'.format(p, r))'''
#Guanabara
num = int(input('Digite o número escolhido: '))
r = 1
p = num
print('Calculando {}! = '.format(num, end=' '))
while p > 0:
    print('{}'.format(p), end=' ')
    print('x' if p > 1 else ' = ', end=' ')
    r *= p
    p -= 1
print('{}.'.format(r))
