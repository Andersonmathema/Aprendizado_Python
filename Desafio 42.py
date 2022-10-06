'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos,
 acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''
l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))
if ((l1+l2) < l3) or ((l1+l3) < l2) or ((l2+l3) < l1):
    print('Não é possível formar um triângulo!')
elif l1 == l2 == l3:
    print('Este triângulo é equilátero')
elif l1 != l2 != l3 != l1:
    print('Este triângulo é escaleno')
else:
    print('Este triângulo é isósceles')
