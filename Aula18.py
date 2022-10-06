#Listas dentro de listas (estruturas compostas)
'''teste = list()
teste.append('Anderson')
teste.append(31)
galera = list()
galera.append(teste[:]) #sem colchetes com dois pontos as listas ficam ligadas e mudam as variáveis de uma com a outra
teste[0]= 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''
'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1]) #Apresenta a lista da posição 2, e o item dessa lista na posição 1, no caso mostra 13
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade') # Formatação para apresentar a lista'''
galera = list()
dado = list()
totmai = totmen = 0 #Variáveis simples podem ser aninhados assim, lista NÂO
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
