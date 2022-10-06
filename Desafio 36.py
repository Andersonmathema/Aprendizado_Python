'''Exercício Python 036: Escreva um programa para aprovar o
empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
o empréstimo será negado.'''
valor = float(input('Qual o valor da casa?: R$ '))
sal = float(input('Qual o seu salário?: R$ '))
tempo = int(input('Em qauntos anos pretende pagar?: '))
prest = valor/(tempo*12)
if prest > sal*0.3:
    print('Empréstimo negado, mensalidade de R${:.2f} está acima de 30% de seu salário'.format(prest))
else:
    print('Empréstimo aprovado, no valor mensal de R${:.2f}'.format(prest))
