'''lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita']
print(lanche)
lanche.append('Café') #adiciona item ao final
lanche.insert(1, 'Sorvete') #adiciona item na posição indicada e desloca o resto à direita
print(lanche)
del lanche[6]
print(lanche)
lanche.pop(3) #normalmente utilizado para remover o último item com .pop()
print(lanche)
lanche.remove('Hamburguer') #remove a primeira ocorrência do item
print(lanche)
valores = list(range(4,11))
print(valores)
valores2 = [8,2,5,4,9,3,0]
valores2.sort() #ordena crescentemente
print(valores2)
valores2.sort(reverse=True) #parâmetro reverse inverte a ordem para decrescente
print(valores2)
tamanho = len(valores)
print(tamanho)
num= [7,5,2,3,2,1]
print(num)
num.remove(2) #remove o primeiro 2
print(num)
if 4 in num:
    num.remove(4)
    print(num)
else:
    print('Não achei o número 4')
    print(num)
valores2 = list()
valores2.append(5)
valores2.append(9)
valores2.append(4)'''
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: '))) #adicionar no teclado item numa lista
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista', valores)
'''a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''

