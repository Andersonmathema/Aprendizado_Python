#INTERATIVE HELP(manual de funções)
'''Abra python console e digite help(), deepois digite a função que tem dúvida'''
#help(print) #executando explica o print
#print(input.__doc__) #mesma coisa

#DOCSTRINGS(String de documentação)
'''def contador(i, f, p): # três aspas duplas e enter
    """
    -> Faz uma contagem  e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Anderson Andrade Silva
    """
    c = i
    while c < f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


help(contador)'''

#PARÂMETROS OPCIONAIS
'''def somar(a=0, b=0, c=0): #Inicializar as variáveis ajuda para menos valores indicados ou zero valores
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)#Caso queira parametros a mais, utilize *list
somar(8, 4)
somar()'''

#ESCOPO DE VARIÁVEIS
'''def teste():
    x = 8
    print(f'Na função teste, n vale {n} ')
    print(f'Na função teste, x vale {x} ')

n = 2
print(f'No programa principal, n vale {n}')
teste()
print(f'Na função teste, x vale {x} ') #Fora de escopo'''
'''def funcao(): #Demonstra o N1 em escopo global e local
    global n1 #garante n1 assumindo atribuições locais em vez de criar nova variável
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')'''

#RETORNANDO VALORES(return)
'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3} ')'''

'''def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f'''


'''n = int(input(f'Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')'''
'''f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')'''
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')
