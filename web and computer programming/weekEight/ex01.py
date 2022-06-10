from itertools import count
import math
secretWorld = "Moroni"
display = "_" * len(secretWorld)
displayNone = " "
hintDiplay = (F"Your hint is: {displayNone}")
userGuess = str(input("Type your guess: "))
count = 1

while userGuess != 

'''


If the guess is not correct, the user will be given a hint to help them improve their guess for the next round.

The game continues prompting the user for new guesses and showing them hints until they guess the word correctly. When the game is over, the program displays the number of guesses that were made.

The hint is a rendering of the letters in the guess according to the following guidelines:

An underscore _ indicates that the letter was not present in the secret word.

A lowercase letter indicates that the letter was present somewhere in the secret word, but not at that position.

An uppercase letter indicates that the letter was present at that exact spot in the secret word. (In other words, if the second letter in the guess is also the second letter in the secret word, then that letter is shown as a capital.)'''