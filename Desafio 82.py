'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
lista = []
listaP = []
listaI = []
n = int(input('Digite um número: '))
while True:
    lista.append(n)
    if n % 2 == 0:
        listaP.append(n)
    else:
        listaI.append(n)
    esc = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if esc not in 'SN':
        esc = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if esc == 'S':
        n = int(input('Digite um número: '))
    else:
        break
print(f'Os números digitados foram: {lista}')
print(f'Os números pares foram: {listaP}')
print(f'Os números ímpares foram: {listaI}')
