'''Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''
print('-'*20)
print('LEITOR DE PREÇOS')
print('-'*20)
total = contp = cont = pmenor = 0
esc = 'S'
nmenor = ''
while True:
    nomep = str(input('Qual o nome do produto? ')).upper().strip()
    preco = input('Qual o preço desse produto? R$')
    while not preco.isnumeric():
        preco = input('Qual o preço desse produto? R$')
    if cont == 0:
        pmenor = int(preco)
        nmenor = nomep
        cont += 1
    if int(preco) > 1000:
        contp += 1
    if int(preco) < pmenor:
        nmenor = nomep
    esc = str(input('Quer continuar cadastrando? [S/N] ')).strip().upper()[0]
    while esc not in 'SN':
        esc = str(input('Quer continuar cadastrando? [S/N] ')).strip().upper()[0]
    total += int(preco)
    if esc == 'N':
        break
print('='*20)
print(f'Sua compra deu um total de R${total:.2f}')
print(f'Na sua compra {contp} produtos custaram mais de R$ 1.000,00')
print(f'E {nmenor} foi o produto mais barato.')
