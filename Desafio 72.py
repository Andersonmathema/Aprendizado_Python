'''Exercício Python 072: Crie um programa que tenha uma Tupla
totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número
pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
            'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
            'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')
esc = int(input('Digite um número entre 0 e 20: '))
while esc > 20 or esc < 0:
    esc = int(input('Número fora da faixa. Digite um número entre 0 e 20: '))
print(f'Seu número: {contagem[esc]}')




