secretWorld = "NEFI"
guess = ""
counter = 0
while guess != secretWorld:
  print("-"*30)
  print("Welcome to the word guessing game ")
  print("-"*30)
  guess = str(input("\nWhat is your guess? ")).upper()
  counter += 1
  print("-"*30)
  print("\033[36;41mTry again\033[m")
  print("-"*30)

print(f"you took {counter}x to get it right")
print("Congratulation\n")

""" nome = str(input("Digite seu nome? ")).upper()
print("A letra 'A' aparece {} vezes.".format(nome.count("A")))
print("A primeira letra 'A' apareceu na posição {}".format(nome.find('A')+1))
print("A ultima letra 'A' apareceu na posição {}".format(nome.rfind('A')+1))  """