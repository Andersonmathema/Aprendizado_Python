'''Exercício Python 077: Crie um programa que tenha uma tupla
com várias palavras (não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são as suas vogais.'''
#NAO CONSEGUI ;-;
pal = ('Marcelo', 'Saulo', 'Maria', 'Joanna', 'Anderson')
for p in pal:
	print(f'\nNa palavra {p} temos ', end='')
	for letra in p:
		if letra.lower() in 'aeiou':
			print(letra, end=' ')
