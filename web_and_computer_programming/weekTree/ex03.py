import math


def triangleAreaCalculator():
    triangleHeight = float(input('Type the height of triangle: '))
    triangleBase = float(input('Type the base of triangle: '))
    triangleArea = round(((triangleBase * triangleHeight) / 2), 2)
    print('The area of the triangle is: {} '.format(triangleArea))


def squareAreaCalculator():
    squareHeight = float(input('Type the height or side of square: '))
    squareArea = squareHeight**2
    print("The area of the square is: {}".format(squareArea))


def rectangleAreaCalculator():
    rectangleHeight = float(input('Type the height of rectangle: '))
    rectangleBase = float(input('Type the base of rectangle: '))
    rectangleArea = round((rectangleHeight*rectangleBase), 2)
    print('The area of the rectangle is: {}'.format(rectangleArea))


def circleAreaCalculator():
    # Area of circle is:  π . r2
    circleRadius = float(input('Type the radius of circle: '))
    circleArea = round((math.pi * circleRadius**2), 2)
    print('The area of circle is: {}'.format(circleArea))


choose = True
while choose:
    print("\n")
    print("Area Calculator")
    print("""
  1.Calculate area of the triangle
  2.Calculate the area of the square
  3.Calculate rectangle area
  4.Calculate circle area
  5.Exit/Quit/Exit
    """)

    choose = input("Choose some option:  ")
    if choose == "1":
        print('\n')
        triangleAreaCalculator()
        

    elif choose == "2":
        print('\n')
        squareAreaCalculator()

    elif choose == "3":
        print('\n')
        rectangleAreaCalculator()
    elif choose == "4":
        print('\n')
        circleAreaCalculator()
    elif choose == "5":
        print("\n Goodbye")

        choose = None
    else:
        print("\n Choice not valid.\n Try again.")
