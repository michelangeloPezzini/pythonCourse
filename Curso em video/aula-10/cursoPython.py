# Exercicio 28
""" import random
numberRandon = random.randint(1, 10)
print("********************")
print("Tente ganhar este jogo!")
userChoose = int(input("Escolha um numero entre 1 e 10! "))
print("********************")
if userChoose == numberRandon:
    print("Você ganhou!!!!")
    print("{} x {}".format(userChoose, numberRandon))
else:
    print("Você perdeu!!!!")
    print("{} x {}".format(userChoose, numberRandon)) """

# Exercicio 29
""" velocidade = int(input("Qual foi a velocidade do carro? "))
limite = 80
if velocidade > limite:
    multa = (velocidade - limite) * 7
    print("Você está acima da velocidade permitida.")
    print("Multa de R${}".format(multa))
else:
  print("Você está na velocidade permitida") """

from functools import partial
 # Ecercicio 30

""" number = int(input("Digite um numero: "))
if number % 2 == 0:
    print("{} É PAR!".format(number))
else:
    print("{} É IMPAR".format(number))
 """
# Ecercicio 31

""" distancia = float(input("Digite a distancia da viagem: "))
if distancia <= 200:
    passagem = distancia * 0.60
    print("O valor da passagem será R${}".format(passagem))
else: 
    passagem = distancia * 0.45
    print("O valor da passagem será R${}".format(passagem)) """

# Exercicio 32
anoBissexto = int(input("Digite o ano desejado: "))
var = anoBissexto % 4 
print(var)