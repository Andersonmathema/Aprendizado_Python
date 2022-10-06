'''Exercício Python 105: Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional, true or false)
Adicione também as docstrings dessa função para consulta pelo desenvolvedor. (com docstrings)'''


def notas(*valores, sit=False):
    """
    notas(*valores, sit=False)
    Função para analisar as notas e situações de alunos;
    :param valores: Define as notas
    :param sit: Opcional, define a situação do aluno só se for True
    :return: Retorna uma biblioteca com as notas e situação se for True
    """
    alunos = dict()
    maior = menor = valores[0]
    s = c = m = 0
    for n in valores:
        c += 1 #Poderia usar len(valores)
        s += n #Poderia usar sum(valores)
        if n < menor:
            menor = n #Poderia usar min(valores)
        if n > maior:
            maior = n #Poderia usar max(valores)
    m = s / (len(valores)) #Poderia usar m = sum(valores)/len(valores)
    alunos['Total'] = c
    alunos['menor'] = menor
    alunos['maior'] = maior
    alunos['média'] = m
    if sit:
        if m < 5:
            alunos['situação'] = 'Ruim'
        elif 5 <= m < 7:
            alunos['situação'] = 'Razoável'
        else:
            alunos['situação'] = 'Boa'
    return alunos


resp = notas(7.5, 7.5, 7.5, 1, sit=True)
print(resp)
help(notas)

