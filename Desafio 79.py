'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''
lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Número cadastrado com sucesso!')
    else:
        print('Número já cadastrado, não será adicionado!')
    esc = str(input('Deseja cadastrar outro número? [S/N]: ')).strip().upper()[0]
    while esc not in 'SN':
        esc = str(input('Deseja cadastrar outro número? [S/N]:')).strip().upper()[0]
    if esc == 'N':
        break
lista.sort()
print(lista)


