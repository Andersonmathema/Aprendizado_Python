'''Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha
dois módulos internos chamados moeda e dado. Transfira todas as funções
utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha
tudo funcionando.(https://www.youtube.com/watch?v=uBQ0--sRFUI)'''
from utilidadesCeV import moeda
val = float(input('Digite um valor: '))
aum = float(input('Digite a taxa de aumento: '))
red = float(input('Digite a taxa de redução: '))
moeda.resumo(val, aum, red)
