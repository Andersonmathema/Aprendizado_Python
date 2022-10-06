'''Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
num = c = nmaior = nmenor = s = 0
opc= 'S'
while opc == 'S':
    c += 1
    num = int(input('Digite um número ou N para parar: '))
    opc = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    s += num
    if c == 1:
        nmaior = nmenor = num
    else:
        if num > nmaior:
            nmaior = num
        if num < nmenor:
            nmenor = num
m = s/c
print('A média dos valores digitados é {}, o maior número é {} e o menor número é {}'.format(m, nmaior, nmenor))
