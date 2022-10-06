# else if == elif em Python, pode-se criar quantos quiser elif, else só um ou nenhum, if obrigatório.
nome = str(input('Qual é o seu nome?: ')).strip().upper()
if nome == 'ANDERSON':
    print('Que nome bonito!')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'ANA CLÁUDIA JÉSSICA JULIANA':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}'.format(nome))
