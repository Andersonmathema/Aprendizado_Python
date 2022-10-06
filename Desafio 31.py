''' Exercício Python 031: Desenvolva um programa que pergunte a distância
de uma viagem em Km.
1 Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
 200Km e R$0,45 parta viagens mais longas.'''
via = float(input('Digite a distância da viagem: '))
if via > 200:
    print('O valor da viagem será de R${:.2f}'.format(via * 0.45))
else:
    print('O valor da viagem será de R${:.2f}'.format(via * 0.5))