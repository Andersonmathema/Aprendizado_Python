nome = str(input('Digite o nome: ')).upper()
lista = nome.split()
teste = 'SILVA' in lista
print(' O seu nome contém Silva? {}'.format(teste))