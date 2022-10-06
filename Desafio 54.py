'''Exercício Python 054: Crie um programa que leia o ano de nascimento
de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.'''
from datetime import date
smaior = 0
smenor = 0
for c in range(1, 8):
    an = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = date.today().year - an
    if idade < 18:
        smenor += 1
    else:
        smaior += 1
print('{} pessoas são maiores de idade e {} são menores de idade.'.format(smaior, smenor))
