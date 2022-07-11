#Course work on Programming Building Blocks.
#week 11-12
i = 0
lowest = 9999999
Lowest_year = ''
Lowest_Country = ''
highest = -1
highest_year = ''
highest_Country = ''
max_life = -1
min_life = 999999
max_country = ''
min_country = ''
lifeExp_array = []
yearChoice = int(input(f'Please enter the year of choice: '))
print()
with open('web_and_computer_programming\weekEleven\life-expectancy.csv') as life_exp:
 for line in life_exp:
    i = i + 1
    clean_line = line.strip()
    lifetime = clean_line.split(',')
    if i > 1:
      country = lifetime[0]
      code = lifetime[1]
      year = int(lifetime[2])
      expected_years = float(lifetime[3])

      if highest < expected_years:
        highest = expected_years
        highest_year = year
        highest_Country = country
      if lowest > expected_years:
        lowest = expected_years
        Lowest_year = year
        Lowest_Country = country

      if yearChoice == year:
        lifeExp_array.append(expected_years)
        if max_life < highest:
          max_life = highest
        highest_Country = country
        if min_life > highest:
          min_life = highest
        highest_Country = country


sum = sum(lifeExp_array)
quantity = len(lifeExp_array)

average = sum/quantity

print()

print(f'The overall highest life expectancy in {yearChoice} was {highest:.2f} from {highest_Country}.')
print(f'The overall lowest life expectancy in {yearChoice} was {lowest:.2f} from {Lowest_Country}.')
print()
print(f'For the year, {yearChoice} the average life expectancy in all countries was {average:.2f}.')
print()
print(f"In {yearChoice}, the highest life expectancy in {highest_Country} was {max_life:.2f}.")
print(f"In {yearChoice}, the lowest life expectancy in {Lowest_Country} was {min_life:.2f}.")

