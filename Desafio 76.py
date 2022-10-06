'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência. No final, mostre uma listagem de preços,
organizando os dados em forma tabular.'''
produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
print("-=" * 30)
print("{:^60}".format('LISTAGEM DE PREÇOS'))
print("-=" * 30)
for c in range(0,17,2):
    print(produtos[c], end='.'*(40-len(produtos[c])))
    print(f'R${produtos[c+1]:>7.2f}')
print("-=" * 30)
