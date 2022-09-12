# Write a program to convert from Fahrenheit to Celsius. Display the result to one decimal place of precision.

# Celsius to Kelvin
def celsius_to_kelvin():
    C = float(input('Type a value in °C(celsius) to convert to K(Kelvin): '))
    K = (C + 273.15)
    print("\nCelsius to Kelvin = {:.1f}K".format(K))

# Celsius to Fahrenheit


def celsius_to_fahrenheit():
    C = float(input('Type a value in °C(Celsius) to convert to °F(Fahrenheit): '))
    F = (C * 1.8 + 32)
    print("\nCelsius to Fahrenheit = {:.1f}°F".format(F))

# Kelvin to Celsius


def kelvin_to_celsius():
    K = float(input('Type a value in K(Kelvin) to be converted to °C(Celsius): '))
    C = (K - 273.15)
    print("\nKelvin to Celsius = {:.1f}°C".format(C))

# Kelvin to Fahrenheit


def kelvin_to_fahrenheit():
    K = float(input('Type a value in K(Kelvin) to convert to °F(Fahrenheit): '))
    F = (K * 1.8 - 459.7)
    print("\nKelvin to Fahrenheit = {:.1f}°F".format(F))

# Fahrenheit to Celsius


def fahrenheit_to_celsius():
    F = float(input('Type a value in °F(Fahrenheit) to convert to °C(celsius): '))
    C = ((F - 32) / 1.8)
    print("\nFahrenheit to Celsius = {:.1f}°C".format(C))

# Fahrenheit to Kelvin


def fahrenheit_to_kelvin():
    F = float(input('Type a value in °F(Fahrenheit) to convert to K(Kelvin): '))
    K = ((F - 32) / 1.8 + 273)
    print("\nFahrenheit to Kelvin = {:.1f}K".format(K))


choose = True
while choose:
    choose = int(input('''
    Menu:
    1 - Celsius to Kelvin
    2 - Celsius to Fahrenheit
    3 - Kelvin to Celsius
    4 - Kelvin to Fahrenheit
    5 - Fahrenheit to Celsius
    6 - Fahrenheit to Kelvin
    7 - EXIT

Choose: '''))
    if choose == 1:
        celsius_to_kelvin()
    elif choose == 2:
        celsius_to_fahrenheit()
    elif choose == 3:
        kelvin_to_celsius()
    elif choose == 4:
        kelvin_to_fahrenheit()
    elif choose == 5:
        fahrenheit_to_celsius()
    elif choose == 6:
        fahrenheit_to_kelvin()
    elif choose == 7:
        print("Goodbye")
        choose = None
    else:
        print('\n Choice not valid.\n Try again.')
