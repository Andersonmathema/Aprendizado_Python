'''Exercício Python 037: Escreva um programa em Python que
leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.'''
num = int(input('Digite um número inteiro que quer converter: '))
'''conv = int(input('Digite 1 pra binário, 2 pra octal e 3 pra hexadecimal: '))
b = bin(num)
h = hex(num)
o = oct(num)
if conv == 1:
    print('O número {} em binário é{}'.format(num,b))
elif conv == 2:
    print('O numero {} em octal é {}'.format(num,o))
elif conv == 3:
    print('O número {} em hexadecimal será {}'.format(num,h))
else:
    print('Você não digitou uma opção válida!') minha tentativa'''
print('''Escolha um das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opc = int(input('Sua opção: '))
if opc == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente!')
