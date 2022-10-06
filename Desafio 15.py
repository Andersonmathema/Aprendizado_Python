km = float(input('Indique a quantidade de quilômetros rodados pelo carro: '))
d = int(input('Indique por quantos dias usou o carro: '))
p = km*0.15+d*60
print('O aluguel do carro custará R${:.2f}'.format(p))
