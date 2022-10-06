''' Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas
 e diga ao usuário se elas podem ou não formar um triângulo. '''
l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))
if ((l1+l2) < l3) or ((l1+l3) < l2) or ((l2+l3) < l1):
    print('Não é possível formar um triângulo!')
else:
    print('É possível formar um triângulo!')
