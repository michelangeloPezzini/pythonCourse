""" lista = ["a", "b", "c", "d", 123]
print(lista[::2])
print(lista[-1])

listaDois = [1,2,3,4,5]
listaDois.append(6)
listaDois.insert(2, "Teste")
listaDois.pop()

print(listaDois)

for item in listaDois:
  print(item) """

import random
palavras = ["CORRER", "GATO", "IGREJA", "NADADOR", "ESCRITURAS"] 
palavra = random.choice(palavras)
digitadas = []
vida = 5
while True:
  user = str(input("Digite somente uma letra: ")).upper()
  if len(user) > 1:
    print("Digite apenas uma letra, tente novamente.")
    continue
  
  digitadas.append(user)
  if user in palavra:
    print(f"A letra {user} existe na palavra secreta.")
  else: 
    print(f"A letra {user} não existe na palavra secreta.")
    digitadas.pop()
    vida = vida - 1
    print(f"Você ainda tem {vida} chances!!!")
  
  letraSecreta = ""
  for letra in palavra:
    if letra in digitadas: 
      letraSecreta = letraSecreta + letra
    else: 
      letraSecreta = letraSecreta + "_"

  if letraSecreta == palavra:
    print(letraSecreta)
    print("Você acertou, parabens!!!")
    break
  elif vida == 0:
    print("Acabou suas tentativas")
    break
  else:
    print(letraSecreta)

    