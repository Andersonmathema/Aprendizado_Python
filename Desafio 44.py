'''Exercício Python 044: Elabore um programa que calcule o valor
a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''
preco = float(input('Digite o valor do produto: '))
'''cond = int(input('Digite 1 para à vista com desconto, 2 para à vista no cartão, 3 para 2x no cartão e 4 para 3x no cartão: '))
vistad = preco*0.90
vistac = preco*0.95
duas = preco
tres = preco*1.20
if cond == 1:
    print('Á vista com desconto de 10% ficará R${:.2f}'.format(vistad))
elif cond == 2:
    print('À vista no cartão com 5% de desconto ficará R${:.2f}'.format(vistac))
elif cond == 3:
    print('Em duas vezes o preço final será R${:.2f}'.format(duas))
elif cond == 4:
    print('Em 3 vezes o preço final será de R${:.2f}'.format(tres))
else:
    print('Digite uma condição válida!')'''
print('''FORMAS DE PAGAMENTO
[1] À vista em dinheiro com 10% desconto
[2] À vista no cartão com 5% de desconto
[3] 2x no cartão
[4] 3x no cartão''')
opc = int(input('Digite sua opção: '))
if opc ==1:
    total = preco * 0.90
elif opc == 2:
    total = preco * 0.95
elif opc == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opc ==4:
    total = preco * 1.20
    parcela = total / 3
    print('Sua compra será parcelada em 3x de R${:.2f} COM JUROS'.format(parcela))
else:
    total = 0
    print('\033[0;31mOPÇÃO INVÁLIDA DE PAGAMENTO\033[m. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))

