#Dicionários
'''dados = {'Nome': 'Pedro', 'Idade': 25}
print(dados['Nome']) #Chama o nome da classe em vez da posição
print(dados['Idade'])
dados['Sexo'] = 'M'
print(dados)
del dados['Idade']
print(dados)'''
'''filme1 = {'titulo': 'Star Wars',
         'ano':1977,
         'diretor': 'George Lucas'
        }
for k, v in filme1.items():
    print(f'O {k} é {v}') # Mostra 'O {key} é {value}'
filme2 = {'titulo': 'Avengers',
         'ano':2012,
         'diretor': 'Joss Whedon'
        }
filme3 = {'titulo': 'Matrix',
         'ano':1999,
         'diretor': 'Wachowski'
        }
locadora = list()
locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)
print(locadora[0]['ano'])
print(locadora[2]['titulo'])'''
'''pessoas = {'nome': 'Anderson', 'sexo': 'M', 'idade': 31}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.items())
#del pessoas['sexo'] 
#pessoas['nome'] = 'Leandro'
pessoas['peso'] = 120
for k, v in pessoas.items():
    print(f'{k} = {v}')'''
'''brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf':'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['sigla'])'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #Dicionário não aceitam fatiamento [:], precisa do método copy()
for e in brasil:
    for k, v in e.items():
        #print(f'O campo {k} tem valor {v}.')
        print(v, end='-')
    print()
