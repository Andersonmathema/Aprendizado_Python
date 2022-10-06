'''Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''
print('-'*20)
print('Cadastre uma pessoa')
print('-'*20)
contidade = conthomem = contmulher = 0
esc = 'S'
while True:
    idade = input('Digite sua idade: ')
    while idade.isnumeric() == False:
        idade = input('Digite sua idade: ')
    sexo = str(input('Digite o sexo [M/F]')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]')).strip().upper()[0]
    esc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while esc not in 'SN':
        esc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if int(idade) >= 18:
        contidade += 1
    if sexo == 'M':
        conthomem += 1
    elif sexo == 'F': #Poderia ter colocado 'and int(idade) < 20'
        if int(idade) < 20:
            contmulher += 1
    if esc == 'N':
        break
print(f'Você registrou {contidade} pessoas com mais de 18 anos.')
print(f'Dessas pessoas {conthomem} são homens.')
print(f'Entre as mulheres {contmulher} tem menos de 20 anos')
