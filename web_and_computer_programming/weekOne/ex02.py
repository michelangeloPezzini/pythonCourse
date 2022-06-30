userAnswer = input("Hello user, my name is Mike, could you answer some question? yes or no? ")

if userAnswer == "yes": 
    name = input("What`s yout name?")
    lastName = input("What`s is your last name?")
    color = input("What`s is your favorite color?")
    print("It`s a plesure to know you "+ name +" "+ lastName + ", we have the same favorite color " + color + ", that`s awesome !!")

elif userAnswer == "no": 
    print("I can not help you if you dont type 'yes'")
else: 
    print("Please enter yes or no.") 



