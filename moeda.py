def aumentar(n, t=1.1, sit=False):
    val = n * (1+t/100)
    valf = moeda(val)
    if sit:
        return valf
    else:
        return val


def diminuir(n, t=0.9, sit=False):
    val = n * (1-t/100)
    valf = moeda(val)
    if sit:
        return valf
    else:
        return val


def dobro(n, sit=False):
    val = n*2
    valf = moeda(val)
    if sit:
        return valf
    else:
        return val


def metade(n, sit=False):
    val = n/2
    valf = moeda(val)
    if sit:
        return valf
    else:
        return val


def moeda(n=0):
    return f'R${n:.2f}'.replace('.', ',')


def resumo(n, a, r):
    tit = 'RESUMO DO VALOR'
    print('-'*30)
    print(f'{tit:^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n):<}') #\t serve para tabular e deixar reto a apresentação
    print(f'O dobro do preço: \t{dobro(n, True):<}')
    print(f'A metade do preço: \t{metade(n, True):<}')
    print(f'{a}% de aumento: \t{aumentar(n, a, True):<}')
    print(f'{r}% de redução: \t{diminuir(n, r, True):<}')
    print('-' * 30)


