'''Exercício Python 101: Crie um programa que tenha uma função chamada
voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO,
OPCIONAL e OBRIGATÓRIO nas eleições. (datetime, >= 16 vota, >= 65 opcional,
retorna frase: voto opcional, voto obrigatorio  )'''
from datetime import date #Poderia importar dentro da função num escopo local


def voto(an):
    idade = date.today().year - an
    if idade < 16:
        print('Voto NEGADO!')
    elif 16 <= idade < 18:
        print('Voto OPCIONAL!')
    elif idade >= 65:
        print('Voto OPCIONAL!')
    else:
        print('Voto OBRIGATÓRIO!')


anoNasc = int(input('Digite o ano de nascimento: '))
voto(anoNasc)
