'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo
teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
par = 0
lista = (n1, n2, n3, n4)
num3 = lista.count(3)
print(f'O número 9 apareceu {lista.count(9)} vezes')
if num3 == 0:
    print('O número 3 foi digitado em nenhuma posição')
else:
    print(f'O número 3 foi digitado na {lista.index(3)+1}ª posição ')
print('O números pares foram', end=' ')
for c in range (0,4):
    if lista[c] % 2 == 0:
        print(lista[c], end=' ')

