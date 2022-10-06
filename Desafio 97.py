'''Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
Olá, Mundo!
~~~~~~~~~'''
def escreva(n):
    tam = len(n)
    print('-'*tam)
    print(n)
    print('-' * tam)


while True:
    text = str(input('Digite algo: '))
    escreva(text)
    esc = str(input('Outra frase? S/N: ')).upper().strip()[0]
    while esc not in 'SN':
        esc = str(input('Outra frase? S/N: ')).upper().strip()[0]
    if esc == 'N':
        break
