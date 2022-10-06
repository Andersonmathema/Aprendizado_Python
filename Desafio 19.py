import random
a1 = str(input("Digite o primeiro aluno: "))
a2 = str(input("Digite o segundo aluno: "))
a3 = str(input("Digite o terceiro aluno: "))
a4 = str(input("Digite o quarto aluno: "))
l = [a1, a2, a3, a4]
escolhido = random.choice(l)
print(" Entre os alunos {}, {}, {} e {} o escolhido foi {}".format(a1, a2, a3, a4, escolhido))
