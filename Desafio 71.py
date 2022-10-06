'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
print('='*20)
print('Banco do Anderson')
print('='*20)
valor = int(input('Digite quanto quer sacar: R$'))
c = valor // 50
s = valor % 50
v = s // 20
s = s % 20
d = s // 10
s = s % 10
print('='*20)
if c > 0:
    print(f'Serão {c} cédulas de R$ 50,00')
if v > 0:
    print(f'Serão {v} cédulas de R$ 20,00')
if d > 0:
    print(f'Serão {d} cédulas de R$ 10,00')
if s > 0:
    print(f'Serão {s} cédulas de R$ 1,00')
print('='*20)
print('Volte sempre ao Banco Anderson. Tenha um bom dia!')
