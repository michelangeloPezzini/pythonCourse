# Exercicio 28
""" from functools import partial
import random
from time import sleep
numberRandon = random.randint(1, 10)
print("*" * 20)
print("Tente ganhar este jogo!")
print("*" * 20)
userChoose = int(input("Escolha um numero entre 1 e 10! "))
print("Verificando...")
sleep(3)
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
""" from datetime import date
ano = int(input("Digite o ano desejado | Digite 0 para o ano atual! "))
if ano == 0:
    year = date.today().year
    month = date.today().month
    day = date.today().day
    print("Hoje é dia {} do mês {} de {}".format(day, month, year))
if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print("O ano {} é bissexto".format(ano))
else: 
    print("O ano {} não é bissexto".format(ano)) """

