'''Exercício Python 104: Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante 'a função input() do Python, só que
fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')'''


'''def leiaInt(frase):
    valor = input(frase)
    while not valor.isnumeric():
        print('\033[0;31mErro! Digite um número válido: \033[0m')
        valor = input(frase)
    else:
        return valor


n = leiaInt('Digite um número: ')
print(f'O número digitado foi {n}')'''
#SOLUÇÂO GUANABARA


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = float(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número válido: \033[0m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
