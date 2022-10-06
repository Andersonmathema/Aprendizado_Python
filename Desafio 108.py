'''Exercício Python 108: Adapte o código do desafio #107, criando uma função
adicional chamada moeda() que consiga mostrar os números como um valor
monetário formatado.(https://www.youtube.com/watch?v=KtRkGEeUdqE)'''
import moeda
val = float(input('Digite um valor: '))
print(f'O valor acrescido de 10% é {moeda.moeda(moeda.aumentar(val))}')
print(f'O valor diminuído de 10% é {moeda.moeda(moeda.diminuir(val))}')
print(f'A metade de {moeda.moeda(val)} é {moeda.moeda(moeda.metade(val))}')
print(f'O dobro de {moeda.moeda(val)} é {moeda.moeda(moeda.dobro(val))}')
