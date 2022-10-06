'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''
'''lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0:
        lista.append(n)
        print(f'Número adicionado na posição {c}')
    if c == 1:
        if n < lista[0]:
            lista.insert(0, n)
            print('Número adicionado na posição 0')
        else:
            lista.append(n)
            print(f'Número adicionado na posição {c}')
    if c == 2:
        if n < lista[0]:
            lista.insert(0, n)
            print('Número adicionado na posição 0')
        elif n > lista[0] and n < lista[1]:
            lista.insert(1, n)
            print('Número adicionado na posição 1')
        else:
            lista.append(n)
            print('Número adicionado ao final da lista')
    if c == 3:
        if n < lista[0]:
            lista.insert(0, n)
            print('Número adicionado na posição 0')
        elif n > lista[0] and n < lista[1]:
            lista.insert(1, n)
            print('Número adicionado na posição 1')
        elif n > lista[1] and n < lista[2]:
            lista.insert(2, n)
            print('Número adicionado na posição 2')
        else:
            lista.append(n)
            print('Número adicionado ao final da lista')
    if c == 4:
        if n < lista[0]:
            lista.insert(0, n)
            print('Número adicionado na posição 0')
        elif n > lista[0] and n < lista[1]:
            lista.insert(1, n)
            print('Número adicionado na posição 1')
        elif n > lista[1] and n < lista[2]:
            lista.insert(2, n)
            print('Número adicionado na posição 2')
        elif n > lista[2] and n < lista[3]:
            lista.insert(3, n)
            print('Número adicionado na posição 3')
        else:
            lista.append(n)
            print('Número adicionado ao final da lista')
print(lista)'''
#GUANABARA SOLUÇÂO
lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]: #Garante o maior no final da lista
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):  #Varre a lista inteira com while, de 0 até o tamanho da lista
            if n <= lista[pos]: #quando acha um menor que os da lista ele guarda a posição
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos +=1 #Necessário para a o pos aumentar a té o tamanho da lista, tipico de laços while
print(f'Os valores digitados em ordem foram {lista}')