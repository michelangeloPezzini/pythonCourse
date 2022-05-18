''' Ask the user for their grade percentage, then write a series of if-elif-else statements to print out the appropriate letter grade. (At this point, you'll have a separate print statement for each grade letter in the appropriate block.)'''
total = 0
for grade in range(1, 4):
    semesterGrade = float(input("Type your {}° grade: ".format(grade)))
    total = total + semesterGrade
    print(total)
finalGrade = total / 3

''' Assume that you must have at least a 70 to pass the class. After determining the letter grade and printing it out. Add a separate if statement to determine if the user passed the course, and if so display a message to congratulate them. If not, display a different message to encourage them for next time. '''

if finalGrade >= 90:
    letter = "\033[42m A \033[m"
elif finalGrade >= 80:
    letter = "\033[44m B \033[m"
elif finalGrade >= 70:
    letter = "\033[43m C \033[m"
elif finalGrade >= 60:
    letter = "\033[45m D \033[m"
else:
    letter = "\033[41m F \033[m"

''' Change your code from the first part, so that instead of printing the letter grade in the body of each if, elif, or else block, instead create a new variable called letter and then in each block, set this variable to the appropriate value. Finally, after the whole series of if-elif-else statements, have a single print statement that prints the letter grade once. '''

#print(f"\nYour letter grade is: {letter}")

""" Add to your code the ability to include a "+" or "-" next to the letter grade, such as B+ or A-. For each grade, you'll know it is a "+" if the last digit is >= 7. You'll know it is a minus if the last digit is < 3 and otherwise it has no sign.

 After your logic to determine the grade letter, add another section to determine the sign. Save this sign into a variable. Then, display both the grade letter and the sign in one print statement. 

Hint: To get the last digit, you could divide the number by 10, and get the remainder. You might refer back to the preparation material for Lesson 03 to see the operators and find the one that does division and gives you the remainder.

At this point, don't worry about the exceptional cases of A+, F+, or F-."""

sign = ""

lastDigit = finalGrade % 10

if lastDigit >= 7:
    sign = "+"
elif lastDigit < 3:
    sign = "-"
else:
    sign = ""


"""Recognize that there is no A+ grade, only A and A-. Add some additional logic to your program to detect this case and handle it correctly."""
if finalGrade >= 93:
    sign = ""

"""Similarly, recognize that there is no F+ or F- grades, only F. Add additional logic to your program to detect these cases and handle them correctly."""

if finalGrade <= 59:
    sign = ""

# Resolution
print("*"*35)
print("Your final grade is: {:.1f}".format(finalGrade))
print("Your letter grade is: {}{}".format(letter, sign))

if finalGrade >= 70:
    print("Congratulations!")
else:
    print("Good Job, study more to get a better grade")

print("*"*35)
