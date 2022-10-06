'''Exercício Python 102: Crie um programa que tenha uma função fatorial()
que receba dois parâmetros: o primeiro que indique o número a calcular e
outro chamado show, que será um valor lógico (opcional) indicando se será
mostrado ou não na tela o processo de cálculo do fatorial. (show = true or
false, inclua docstrings explicando a função)'''


def fatorial(num = 1, show = False):
    """
    fatorial(num, show)
    :param num: Indica o número que você quer calcular o fatorial
    :param show: Se quiser apresentar o cálculo completo
    :return: Retorna o resultado do fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show = True))
help(fatorial)
