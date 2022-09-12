import random
def guessing():
    computer = random.randint(1, 9)
    number_of_guesses = 0
    while True:
        number_of_guesses += 1
        pick = input("Guess, if you dare: ")
        if pick.lower() == "exit":
            print("Better luck next time!")
            print("Attempts:", number_of_guesses - 1)
            break
        elif int(pick) > computer:
            print("Too high.")
        elif int(pick) < computer:
            print("Too low.")
        elif int(pick) == computer:
            print("Yes!")
            if number_of_guesses == 1:
                print("Are you God?!")
            elif number_of_guesses < 3:
                print(f"Impressive! Only {number_of_guesses} attemps.")
            else:
                print(f"Finally! After {number_of_guesses} attemps.")
            break
    again()
 
def again():
    if input("Continue?(y/n) ") == 'y':
        guessing()
    else:
        exit
 
guessing()