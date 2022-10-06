'''Exercício Python 090: Faça um programa que leia nome
e média de um aluno, guardando também a situação (media >= 7 aprovado) em um
dicionário. No final, mostre o conteúdo da estrutura na tela.
Nome: fulano
Media das notas: 00
Situação: aprov/reprov'''
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
print(f'O nome é {aluno["nome"]}')
print(f'A média é {aluno["media"]}')
print(f'A situação é {aluno["Situação"]}')