'''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura
 de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
  de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
IMC = peso (em quilos) ÷ altura² (em metros)'''
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 24:
    print('Peso ideal')
elif imc >= 25 and imc <= 29:
    print('Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')
