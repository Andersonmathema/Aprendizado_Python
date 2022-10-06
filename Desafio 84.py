'''Exercício Python 084: Faça um programa que leia nome
e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas. (>100 para exemplo)
C) Uma listagem com as pessoas mais leves. (<70 para exemplo)'''
individuo = list()
pessoas = list()
cont = 0
while True:
    nome = individuo.append(str(input('Digite o nome: ')))
    peso = individuo.append(float(input('Digite seu peso: ')))
    pessoas.append(individuo[:])
    if cont == 0:
        pmenor = pmaior = individuo[1]
    else:
        if individuo[1] > pmaior:
            pmaior = individuo[1]
        if individuo[1] < pmenor:
            pmenor = individuo[1]
    individuo.clear()
    esc = input('Quer continuar cadastrando? [S/N]: ').strip().upper()[0]
    if esc == 'N':
        break
    else:
        cont += 1
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {pmaior} das seguintes pessoas: ', end='')
for i in pessoas:
    if i[1] == pmaior:
        print(i[0], end='...')
print(f'\nO menor peso foi {pmenor} das seguintes pessoas: ', end='')
for i in pessoas:
    if i[1] == pmenor:
        print(i[0], end='...')
