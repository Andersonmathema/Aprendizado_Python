'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os
parênteses abertos e fechados na ordem correta.'''
# solução errada pois nao percebe )( invertidos
'''lista = []
n = str(input('Digite sua expressão: '))
lista.append(n)
abre = fecha = 0
for c in lista:
    for item in c:
        if item in '(':
            abre += 1
        if item in ')':
            fecha += 1
print(lista)
print(abre, fecha)
if abre == fecha:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida')'''
#SOLUCÂO GUANABARA
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')