'''Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111,
temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz
de funcionar como a função input(), mas com uma validação de dados para aceitar
apenas valores que seja monetários.(https://www.youtube.com/watch?v=6vADeY5_pMs)'''
from utilidadesCeV import moeda
from utilidadesCeV import dado
val = dado.leiaDinheiro('Digite um valor: ')
aum = dado.leiaDinheiro('Digite a taxa de aumento: ')
red = dado.leiaDinheiro('Digite a taxa de redução: ')
moeda.resumo(val, aum, red)
