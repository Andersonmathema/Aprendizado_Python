'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
#Minha tentativa toda bagunçada kkkkk
n1 = float(input('Digite o 1ª número: '))
n2 = float(input('Digite o 2ª número: '))
esc = int(input('''Qual a operação que você quer fazer:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair
Sua escolha: '''))
while esc == 4:
    n1 = float(input('Digite o 1ª número: '))
    n2 = float(input('Digite o 2ª número: '))
    esc = int(input('''Qual a operação que você quer fazer:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair
    Sua escolha: '''))
if esc == 1: #As condições estarem depois e fora do laço ajudam na opção 4
    s = n1 + n2
    print('A soma entre {} e {} é {}'.format(n1, n2, s))
elif esc == 2:
    m = n1 * n2
    print('A multiplicação entre {} e {} é {}'.format(n1, n2, m))
elif esc == 3:
    if n1 > n2:
        print('O número {} é maior que {}'.format(n1, n2))
    elif n1 < n2:
        print('O número {} é menor que {}'.format(n1, n2))
    else:
        print('Os números {} e {} são iguais'.format(n1, n2))
print('Fim')
