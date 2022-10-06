nome = str(input('Digite o nome da cidade: '))
lista = nome.split()
teste = 'SANTO' in lista[0].upper()
print('O nome {} começa por Santo?: {}'.format(nome, teste))
