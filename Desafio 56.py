'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
 No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
e quantas mulheres têm menos de 20 anos.'''
from datetime import date
qf = 0
si = 0
ihvelho = 0
nhvelho = ''
for c in range(1,5):
    nome = str(input('Digite seu nome: ')).strip().upper()
    an = int(input('Seu ano de nascimento: '))
    idade = date.today().year - an
    si = si + idade
    sexo = int(input('''Digite
        [1] MASCULINO
        [2] FEMININO
        Sua escolha: '''))
    if sexo == 1 and idade > ihvelho:
        ihvelho = idade
        nhvelho = nome
    elif sexo == 2 and idade < 20:
        qf += 1
media = si / 4
print('''A média de idade do grupo é {}, o homem mais velho 
é {} e {} mulheres têm menos de 20 anos'''.format(media, nhvelho, qf))
