'''Exercício Python 094: Crie um programa que leia nome, sexo e idade
de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
pessoas = list()
individuo = dict()
listF = list()
cont = 0
sidade = 0
while True:
    individuo['Nome'] = str(input('Digite o nome: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Opção inválida! Digite o sexo [M/F]: ')).strip().upper()[0]
    individuo['Sexo'] = sexo
    if sexo in 'F':
        listF.append(individuo['Nome'])
    individuo['Idade'] = int(input('Digite a idade: '))
    pessoas.append(individuo.copy())
    sidade += individuo['Idade']
    cont += 1
    esc = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while esc not in 'SN':
        esc = str(input('Opção inválida! Quer continuar? [S/N]: ')).strip().upper()[0]
    if esc == 'N':
        break
media = sidade/cont
print(f'Foram cadastradas {cont} pessoas.') #o len(pessoas) tambem dava a quantidade
print(f'A média das idades foi de {media:5.2f} anos.')
print(f'A mulheres cadastratas foram {listF}')
print('Pessoas com idade acima da média: ', end='')
for pos, i in enumerate(pessoas):
    if pessoas[pos]['Idade'] > media:
        print(pessoas[pos]['Nome'], end='')
'''Tambem poderia em vez de listar as mulheres fazer:
for p in pessoas:
    if p['Sexo'] in 'F':
        print(f'{p['Nome']} ', end='')'''