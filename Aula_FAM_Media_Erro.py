from random import randint

def sorteio(a,b):
    return randint(a,b)


def media_erro(n,m):
    soma = 0
    lista = list()
    x = sorteio(n,m)
    for i in range(n,m+1):
        soma = i-x
        lista.append(soma)         
    media = sum(lista) / (len(lista))
    media_por_erro = media+x
    return media_por_erro


h = media_erro(1,100)
print(h)
