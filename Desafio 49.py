'''Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada
de um número que o usuário escolher, só que agora utilizando um laço for.'''
t = int(input('Digite a tabuada escolhida: '))
print('-='*6)
print('Tabuada do {}'.format(t))
print('-='*6)
for c in range(0, 11):
    a = t*c
    print('{}x{}= {}'.format(t, c, a))
print('-='*6)

