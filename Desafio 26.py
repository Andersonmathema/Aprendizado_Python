frase = str(input('Digite uma frase: ')).strip()
fm = frase.upper()
qa = fm.count('A')
pa = fm.find('A')
ua = fm.rfind('A')
print('A sua frase tem {} a, o primeiro a na posição {} e a último na posição {}'.format(qa, pa, ua))