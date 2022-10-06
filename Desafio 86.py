'''Exercício Python 086: Crie um programa que declare uma
matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''
'''mat = list()
c = 0
while c < 9:
    n = int(input(f'Digite o a posição : '))
    mat.append(f'{n:^3}')
    c += 1
for a in range(0,9):
    m = list()
    m.append(mat[a])
    if a == 2 or a == 5:
        print(f'{m}')
    else:
        print(f'{m}', end='')'''
#Solução GUANABARA
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c]= int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()