'''Exercício Python 029: Escreva um programa que leia a
velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado.
 A multa vai custar R$7,00 por cada Km acima do limite. '''
vel = float(input('Indique a velocidade do carro: '))
if vel > 80.0:
    print('Você passou o limite de velocidade e terá que pagar R${:.2f}'.format((vel-80)*7))
else:
    print('Você está na velocidade permitida!')

