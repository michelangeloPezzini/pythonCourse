import random
parOuImpar = str(input("Par ou impar? ")).upper()
numero = int(input("Digite seu numero: "))
var = random.randint(1,11)
resultado = var + numero
print(f"{var} e {numero} = {numero + var}")
if parOuImpar == "PAR" and  resultado % 2 == 0:
  print("Você Ganhou PAR")
else:
  print("Você perdeu!")
