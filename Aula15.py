n = s = 0
nome = 'José'
idade = 33
salário = 987.3
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break #Antes da soma freia em 999
    s +=n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}') #A partir do Puthon 3.6 esse é o novo print, f strings
print(f'O {nome:20} tem {idade} anos e ganha R${salário:.2f}') # 20 espaços
print(f'O {nome:-^20} tem {idade} anos e ganha R${salário:.2f}') #---jose--- em 20 espaços
print(f'O {nome:-<20} tem {idade} anos e ganha R${salário:.2f}')# jose----- em 20 espaços