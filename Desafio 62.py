'''Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário
 se ele quer mostrar mais alguns termos. O programa encerrará quando ele
 disser que quer mostrar 0 termos.'''
a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
c = 0
q = 10
while c < q:
    an = a1 + c*r
    c += 1
    print('a{} = {}'.format(c, an))
opc = int(input('Digite quantos termos você quer ver mais ou 0 pra sair: '))
while opc != 0:
    q += opc
    while c < q:
        an = a1 + c * r
        c += 1
        print('a{} = {}'.format(c, an))
    opc = int(input('Digite quantos termos você quer ver mais ou 0 pra sair: '))
print('FIM')
