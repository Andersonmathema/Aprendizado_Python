def bubblesort(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


lista = [1, 2, 4, 3, 5, 9, 7, 10, 6, 8]
bubblesort(lista)
print(lista)
           
