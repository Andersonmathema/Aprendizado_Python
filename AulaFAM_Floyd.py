def Floyd(G):
    n = len(G)
    D = G
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Floyd(lista)
