'''Exercício Python 034: Escreva um programa que pergunte o
salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento
de 10%. Para os inferiores ou iguais, o aumento é de 15%. '''
sal = float(input('Digite o salário do funcionário: '))
if sal > 1250.00:
    print('O salário de R${:.2f} receberá um aumento de 10% passando a valer R${:.2f}'.format(sal, sal*1.1))
else:
    print('O salário de R${:.2f} receberá um aumento de 15% passando a valer R${:.2f}'.format(sal,sal*1.15))
