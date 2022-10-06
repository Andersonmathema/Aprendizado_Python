'''Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores,
uma função chamada resumo(), que mostre na tela algumas informações geradas pelas
funções que já temos no módulo criado até aqui.(https://www.youtube.com/watch?v=1Ks218WINT8)'''
import moeda
val = float(input('Digite um valor: '))
aum = float(input('Digite a taxa de aumento: '))
red = float(input('Digite a taxa de redução: '))
moeda.resumo(val, aum, red)
