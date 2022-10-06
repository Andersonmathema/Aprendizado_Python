'''Exercício Python 089: Crie um programa que leia nome e duas notas
 de vários alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário possa
mostrar as notas de cada aluno individualmente.'''
'''aluno = list()
boletim = list()
opc = 100
while True:
    nome = input('Nome: ')
    aluno.append(nome)
    n1 = float(input('Nota 1: '))
    aluno.append(n1)
    n2 = float(input('Nota 2: '))
    aluno.append(n2)
    media = (n1 + n2)/2
    aluno.append(media)
    boletim.append(aluno[:])
    aluno.clear()
    esc = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while esc not in 'SN':
        esc = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if esc == 'N':
        break
print('-='*30)
print('No. NOME           MEDIA')
for pos, alunos in enumerate(boletim):
    print(f'{pos}   {alunos[:][0]:<10}      {alunos[:][3]:>4.1f}')
while opc != 999:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    while opc > len(boletim)-1:
        opc = int(input('Aluno inexistente, digite uma posição válida: '))
        if opc == 999:
            break
    if opc == 999:
        break
    print(f'Notas de {boletim[opc][0]} são {boletim[opc][1:3]}')'''
#Solução GUANABARA
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<VOLTE SEMPRE>>>')
