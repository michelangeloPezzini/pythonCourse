import random
number = random.randint(1,10)
play = True
def guessNumber():
  guess = str(input("Guess the number: "))
  print(guess)
  again = str(input("Do you wanna play again? [yes/no]")).strip().upper()
  if again == "NO":
      play = False
  else: 
    guessNumber()
  
while play:
  guessNumber()
