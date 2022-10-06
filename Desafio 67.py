'''Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
um de cada vez,
para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo. '''
'''print('='*20)
print('Tabuada')
print('-'*20)
c = n = 0
while True:
    n = int(input('Digite a tabuada ou um número negativo se quiser sair: '))
    if n >= 0:
        while c < 10:
            c += 1
            m = c*n
            print(f'{c}x{n} = {m}')
        print('-'*20)
        c = 0 #Zerar o contador pois aqui ele tava valendo 10 e nao entrava no laço c<10
    else:
        break
print('-'*20)
print('Fim da tabuada!!! Volte sempre!!!')
print('='*20)'''
#guanabara
print('='*20)
print('Tabuada')
print('-'*20)
c = n = 0
while True:
    n = int(input('Digite a tabuada ou um número negativo se quiser sair: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {n} = {n*c}')
print('-'*20)
print('Fim da tabuada!!! Volte sempre!!!')
print('='*20)
