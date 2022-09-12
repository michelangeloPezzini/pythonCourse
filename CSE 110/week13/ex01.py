wind = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]


def celsius(fahrenheit):
    convert = (fahrenheit * 9 / 5) + 32
    return convert


def compute(temp):
    for ws in wind:
        wc = 35.75+0.6215*temp-35.75*ws**0.16+0.4275*temp*ws**0.16
        print(
            f"At temperature {temp}F, and wind speed {ws} mph, the wind chill is:{wc:.2f}F")
