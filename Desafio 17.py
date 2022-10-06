from math import sqrt, pow, hypot
'''co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = sqrt(pow(co,2)+pow(ca,2))
print('Num triângulo retângulo de cateto oposto {} e cateto adjacente {} sua hipotenusa será de {:.2f}'.format(co, ca, h))'''

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = hypot(co, ca)
print('Num triângulo retângulo de cateto oposto {} e cateto adjacente {} sua hipotenusa será de {:.2f}'.format(co, ca, h))