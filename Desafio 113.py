'''Exercício Python 113: Reescreva a função leiaInt() que fizemos
no desafio 104, incluindo agora a possibilidade da digitação de
um número de tipo inválido. Aproveite e crie também uma função
leiaFloat() com a mesma funcionalidade.
(https://www.youtube.com/watch?v=KowQ_UIMuI8)'''
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg).strip())
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite um número inteiro válido\033[0m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mEntrada de dados intempida pelo usuário.\033[0m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
       try:
           v = float(input(msg).strip())
       except (ValueError, TypeError):
           print('\033[0;31mERRO! Por favor digite um número real válido\033[0m')
           continue
       except (KeyboardInterrupt):
           print('\033[0;31mEntrada de dados intempida pelo usuário.\033[0m')
           return 0
       else:
           return v


n = leiaInt('Digite um número inteiro: ')
v = leiaFloat('Digite um número Real: ')
print(f'Você acabou de digitar o número inteiro {n} e o número Real {v}')
