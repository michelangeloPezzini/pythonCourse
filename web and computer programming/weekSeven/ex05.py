import random
number = random.randint(1,10)
play = True
def guessNumber():
  guess = str(input("Guess the number: "))
  print(guess)

while play:
  if again == "NO":
      play = False
  else: 
    guessNumber()
  guessNumber()
