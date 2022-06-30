'''
*Prompt for all of the necessary values and store them in variables. Then display each item to the screen, without worrying about any spacing, punctuation, or formatting yet.

*Arrange the display so that the spacing and punctuation exactly match the example shown.

*Use the built-in string functions to make the last name display in all caps, the job title display in "title case," and the email display in all lowercase.

'''


userAnswer = input(
    "Hello user, please fill out the form for the issuance of a driver's license? are you ok with that? yes or no? ")

if userAnswer == "yes":
    firstName = input("What`s your first name? ").capitalize()
    lastName = input("What`s is your last name? ").upper()
    emailAddress = input("Whats`s is your email Address?").lower()
    phoneNumber = input("What`s is your phone number?")
    jobPosition = input("What`s is your job position?").title()
    idNumber = int(input("Type your ID number! "))

    print("\nThe  ID Card is:")
    print("****************************************")
    print(f"{lastName}, {firstName}")
    print(jobPosition)
    print(f"ID: {idNumber}")
    print()
    print(emailAddress)
    print(phoneNumber)
    print(" ****************************************")

elif userAnswer == "no":
    print("You can not have your driver's license if you dont type 'yes'")
else:
    print("Please enter yes or no.")

