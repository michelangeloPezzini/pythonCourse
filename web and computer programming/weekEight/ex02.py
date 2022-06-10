import random
wordList = ["profets", "alma", "testimony", "jerusalem", "Jews", "children", "family"]
chosenWord = random.choice(wordList)
guess = ""
display = []
count = 0
print("Lets play the guessing game!")

#Apartir daqui o programa adiciona (_) para cada letra do chosenWord
for i in range(0, len(chosenWord.lower())):
    display.append("_")
while chosenWord.lower() != guess:
    #Com o .join é possivel add (_) para o display
    print(f"Your hint is: {''.join(display)}")
    #contador para identificar o numero de tentativas
    count = count + 1
    guess = input("What is your guess: ").lower()

    #for utilizado para o looping rodar em cada letra da secretworld
    for i in range(0, len(chosenWord.lower())):
        #for utilizado para o looping rodar em cada letra do guess
        for x in range(0, len(guess)):
            if chosenWord[i] == guess[x]:
                if i == x:
                    display[x] = guess[x].upper()
                    print(chosenWord, guess)
                else:
                    display[x] = guess[x].lower()   
                    print(chosenWord, guess)
else:
    print(f"You guessed it!")    
    print(f"Your tried {count} guesses.")