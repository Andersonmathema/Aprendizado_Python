#frase= 'Curso em video Python'

'''Fatiamento'''
'''print(frase[9]) aparece v '''
'''print(frase[9:21]) aparece video Python'''
'''print(frase[9:21:2]) aparece vdoPto (inicio, fim, pulos)'''
'''print(frase[:5]) aparece Curso'''
'''print(frase[15:]) aparece Python'''
'''print(frase[9::3]) aparece vePh'''
'''print(len(frase)) conta caracteres :21'''
'''print(frase.count('o')) conta quantos caracteres indicados aparecem, no caso 3, maiusculas e minusculas 
tem diferença'''
'''print(frase.count('o', 0, 13)) conta dentro da faixa entre 0 e 12 quantos 'o' aparecem, no caso 1'''
'''print(frase.find('deo')) mostra a partir de quando aparece o indicado, no caso 'deo' aparece a partir da 11'''
'''print(frase.find('Android')) aparece -1, indica que não há essa string'''
'''print('Curso' in frase) booleano, indica se existe a o objeto indicado, no caso dá True'''
'''print(frase.replace('Python','Android')) substitui a primeira palavra pela segunda indicada'''
'''print(frase.upper()) método que escreve tudo em maiúscula'''
'''print(frase.lower()) método que escreve tudo em minúscula'''
'''print(frase.capitalize()) método que escreve a primeira em maiúscula e resto em minúscula'''
'''print(frase.title()) Método que coloca todas as primeiras letras em maiúscula'''
frase = '   Aprenda Python  '
'''print(frase.strip()) remove espaços iniciais e finais'''
'''print(frase.rstrip()) r = direita, remove os espaços da direita e mantém esquerda'''
'''print(frase.lstrip()) l = esquerda, remove os espaços da esquerda e mantém os da direita'''
frase= 'Curso em video Python'
'''print(frase.split()) cria uma lista com as palavras separadas entre espaços, iniciando a ordem da contagem
das strings em cada palavra'''
frase = ['Curso', 'em', 'video', 'Python']
'''print('-'.join(frase)) volta a ser uma string unica e contando corretamente da primeira a ultima, separando pelo
indicado em aspas'''

