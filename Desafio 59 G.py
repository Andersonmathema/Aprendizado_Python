from time import sleep
n1 = float(input('Digite o 1ª número: '))
n2 = float(input('Digite o 2ª número: '))
esc = 0
while esc != 5:
    print('''Qual a operação que você quer fazer:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair ''')
    esc = int(input('Qual é a sua opção? '))
    if esc == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif esc == 2:
        produto = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, produto))
    elif esc == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif esc == 4:
        print('Informe os números novamente: ')
        n1 = float(input('Digite o 1ª número: '))
        n2 = float(input('Digite o 2ª número: '))
    elif esc == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*10)
    sleep(2)
print('Fim do programa, volte sempre!!!')
