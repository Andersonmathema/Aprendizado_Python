'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
'''mat = list()
maior2l = list()
c = somap = soma3c =  0
while c < 9:
    n = int(input(f'Digite o a{c+1}: '))
    if n % 2 == 0:
        somap += n
    if c == 2 or c == 5 or c == 8:
        soma3c += n
    mat.append(f'{n:^3}')
    c += 1
for a in range(0, 9):
    maior2l.append(mat[3:6])
    m = list()
    m.append(mat[a])
    if a == 2 or a == 5:
        print(f'{m}')
    else:
        print(f'{m}', end='')
nmaior = max(maior2l[0])
print(f'\nA soma dos pares dá: {somap}')
print(f'A soma dos valores da terceira coluna dá: {soma3c}')
print(f'O maior valor da segunda linha é: {nmaior}')'''
#Solução GUANABARA
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c]= int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-='*30)
print(f'\nA soma dos pares dá: {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna dá: {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é: {mai}')