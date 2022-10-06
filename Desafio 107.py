'''Exercício Python 107: Crie um módulo chamado moeda.py que tenha
as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
(https://www.youtube.com/watch?v=y8pI8YBphQI)'''
import moeda
val = float(input('Digite um valor: '))
print(f'O valor acrescido de 10% é {moeda.aumentar(val)}')
print(f'O valor diminuído de 10% é {moeda.diminuir(val)}')
print(f'A metade de {val} é {moeda.metade(val)}')
print(f'O dobro de {val} é {moeda.dobro(val)}')
