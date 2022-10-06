def fatora(n):
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    lista = list()
    lista.append(n)
    x = 0
    for p in primos:        
        if n % p == 0:
            x = n//p
            lista.append(x)
            break
        else:
            continue
    fatora(x)
    
    

x = fatora(20)
print(x)
