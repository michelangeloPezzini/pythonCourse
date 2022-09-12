'''
Exercise Number One
An iconic line from the James Bond movies is that he would introduce himself as "Bond, James Bond."
For this assignment you will write a program that asks for your name and repeats it back in this way.

'''

userAnswer = input("Hello user, my name is mike, could you answer me some questions to get to know each other better? yes or no? ")

if userAnswer == "yes": 
    name = input("What`s your first name? ").capitalize()
    lastName = input("What`s is your last name? ").capitalize()
    print(f"It`s a plesure to know you {lastName}, {name} {lastName}! ")
elif userAnswer == "no": 
    print("I can not help you if you dont type 'yes'")
else: 
    print("Please enter yes or no.")