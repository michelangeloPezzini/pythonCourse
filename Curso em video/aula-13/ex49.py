#Desafio da tabuada

num = int(input("Digite um numero: "))

for i in range(11):
  resultado = num * i
  print(f"{i} x {num} = {resultado}")