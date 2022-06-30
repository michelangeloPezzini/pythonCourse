print("Enter a list of numbers, type 0 when finished.")
var = -1
sum_numbers = 0
cont = 0
largest = 0
smallest = 10000000000000
lista = []
while var != 0:
  var = int(input("Enter a number: "))
  sum_numbers = sum_numbers + var
  cont = cont + 1
  average = sum_numbers / cont
  if var > largest:
    largest = var
  if var > 0 and var < smallest:
    smallest = var
  lista.append(var)
  lista.sort()
  
  
print(f"The sum is: {sum_numbers}")
print(f"The average is: {average}")
print(f"The largest number is: {largest}")
print(f"The smallest positive number is: {smallest}")
print(f"The sorted list is: {lista}")