# Para segurar um comando você pode utilizar o pass ou ...
valor = True
if valor:
    ...
else:
    print("Error")

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
""" userType = int(input("Digite um numero inteiro: "))
if userType % 2 == 0:
  print("Par")
else: 
  print("Impar") """
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = int(input("Que horas são? "))
if horario <= 11:
    print("Bom dia")
elif horario >= 12 and horario <= 17:
    print("Boa tarde")
elif horario >= 18 and horario <= 24:
    print("Boa noite")
else:
    print("Digite um horario valido!")
