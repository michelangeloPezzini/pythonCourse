with open('life-expectancy.csv') as life_file:
  lowest_age_in_history = 9999999
  highest_age_in_data = 0.00000000001
  lowest_country = ""
  highest_country = ""
  lowest_year = 0.0000001
  highest_year = 99999999999
  next(life_file)

  for line in life_file:
    first_line = line.strip()
    parts = first_line.split(",")
    countries = parts[0]
    abbreviations = parts[1]
    years = int(parts[2])
    ages_data = float(parts[3])

    if ages_data < lowest_age_in_history:
      lowest_age_in_history = ages_data
      lowest_country = countries
      lowest_year = years
      
    if ages_data > highest_age_in_data:
      highest_age_in_data = ages_data
      highest_country = countries
      highest_year = years
