'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = []
n = lista.append(int(input('Digite um número: ')))
while True:
    esc = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while esc not in 'SN':
        esc = str(input('Opção inválida. Quer continuar? [S/N]')).strip().upper()[0]
    if esc == 'S':
        n = lista.append(int(input('Digite um número: ')))
    else:
        break
lista.sort(reverse=True)
print(lista)
tam = len(lista)
print(f'Foram digitados {tam} números')
if 5 in lista:
    print(f'O número cinco está na lista.')
else:
    print(f'O número cinco não está na lista.')
