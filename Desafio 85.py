'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e
ímpares. No final, mostre os valores pares e ímpares em ordem crescente. (Precisa ter
duas listas(lista par e lista impar) dentro de uma maiore coloque o numero na lista
correta dentro do listão)'''
'''numPar = []
numImpar = []
numeros = [numPar, numImpar]
for n in range(1,8):
    num = int(input(f'Digite o {n}º valor: '))
    if num % 2 == 0:
        numPar.append(num)
        numPar.sort()
    else:
        numImpar.append(num)
        numImpar.sort()
print(f'O números pares foram {numeros[0]}')
print(f'Os números ímpares foram {numeros[1]}')'''
#Solução GUANABARA
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'O números pares foram {num[0]}')
print(f'Os números ímpares foram {num[1]}')
