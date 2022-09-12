import math
temperature = float(input("What is the temperature? "))
new = float(temperature * 1.8 + 32)
f_or_c = input("Fahrenheit or Celsius (F/C)? ").upper()
if f_or_c == "F":
    def calculate_wind_chill_fahrenheit():
        wind_chill_f = 35.74 + 0.6215 * \
            (temperature) - 35.75 * (speed ** 0.16) + \
            (0.4275 * (temperature) * (speed ** 0.16))
        return wind_chill_f
if f_or_c == "C":
    def calculate_wind_chill_celsius():
        new = float(temperature * 1.8 + 32)
        wind_chill_c = 35.74 + 0.6215 * \
            (new) - 35.75 * (speed ** 0.16) + \
            (0.4275 * (new) * (speed ** 0.16))
        return wind_chill_c
if f_or_c == "F":
    for cal in range(5, 61, 5):
        speed = cal
        wind = calculate_wind_chill_fahrenheit()
        print(
            f"At temperature {temperature}F, and wind speed{speed} mph, the windchill is {wind:.2f}f")
if f_or_c == "C":
    for cal in range(5, 61, 5):
        speed = cal
        wind = calculate_wind_chill_celsius()
        print(
            f"At temperature {new}F, and wind speed{speed} mph, the windchill is {wind:.2f}f")
