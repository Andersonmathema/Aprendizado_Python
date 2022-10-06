nome = str(input('Digite seu nome: ')).strip()
lista = nome.split()
pn = lista[0]
un = lista[len(lista)-1]
print(' Nome: {} \n Primeiro nome: {} \n Último nome: {}'.format(nome, pn, un))
