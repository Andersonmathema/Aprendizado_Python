'''Exercício Python 109: Modifique as funções que foram criadas no desafio
107 para que elas aceitem um parâmetro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108.(https://www.youtube.com/watch?v=Y0zNYTHoGhQ)'''
import moeda
val = float(input('Digite um valor: '))
print(f'O valor acrescido de 10% é {moeda.aumentar(val, 10, True)}')
print(f'O valor diminuído de 90% é {moeda.diminuir(val, 90, False)}')
print(f'A metade de {moeda.moeda(val)} é {moeda.metade(val, True)}')
print(f'O dobro de {moeda.moeda(val)} é {moeda.dobro(val, True)}')
