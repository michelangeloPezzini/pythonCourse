larger = 0
smaller = 99999999999999


with open("web_and_computer_programming\weekEleven\life-expectancy.csv") as life_expectancy:
  for i in life_expectancy:
    separator = i.strip()
    divider = separator.split(",")
    number_life_expectancy = float(divider[3])
    number_life_expectancy_country = divider[0] 


    if number_life_expectancy > larger:
      larger = number_life_expectancy
      
    
    if number_life_expectancy < smaller:
      smaller = number_life_expectancy
     

print(larger)
print(smaller)

