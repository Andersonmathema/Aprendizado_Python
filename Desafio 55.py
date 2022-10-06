'''Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
 No final, mostre qual foi o maior e o menor peso lidos.'''
pmaior = 0
pmenor = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1: #No primeiro laço o maior e o menor são iguais, logo substituo só no primeiro laço o peso digitado
        pmaior = peso
        pmenor = peso
    elif peso > pmaior:
        pmaior = peso
    elif peso < pmenor:
        pmenor = peso #Embora no início o menor era zero, eu substitui no primeiro if pra conseguir comparar
print('O menor peso é {}Kg e o maior peso é {}Kg'.format(pmenor, pmaior))
