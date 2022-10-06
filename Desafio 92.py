'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira
de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente
de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
(Aposenta com 35 anos de contribuição, se ctps = 0 nem pergunta ano de contrato)'''
from datetime import date
nome = str(input('Digite o nome: '))
anoNasc = int(input('Digite o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
ctps = int(input('Digite a carteira ou zero se não tiver: '))
emp = {'Nome': nome, 'CTPS': ctps, 'Idade': idade}
if ctps != 0:
    emp['Ano de Contratação'] = int(input('Digite o ano de contratação: '))
    emp['Salário'] = float(input('Digite o salário: '))
    emp['Aposentadoria'] = idade + 35
for k, v in emp.items():
    print(f'O {k} vale {v}')