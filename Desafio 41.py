'''Exercício Python 041: A Confederação Nacional de Natação
 precisa de um programa que leia o ano de nascimento de um
 atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''
from datetime import date
an = int(input('Digite seua ano de nascimento: '))
idade = date.today().year - an
if idade <= 9:
    print('Pela sua idade {}, sua categoria é MIRIM'.format(idade))
elif idade <=14:
    print('Pela sua idade {}, sua categoria é INFANTIL'.format(idade))
elif idade <=25:
    print('Pela sua idade {}, sua categoria é SÊNIOR'.format(idade))
else:
    print('Pela sua idade {}, sua categoria é MASTER'.format(idade))
