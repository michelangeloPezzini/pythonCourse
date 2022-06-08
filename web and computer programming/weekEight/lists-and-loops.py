from ntpath import join


itens = ["Abacaxi", "Melancia", "Laranja", "Pera", "Morango"]

print(itens[2])

#Para cada item da lista, ele ira lopar e retornar para o incio.
contador = 0
for item in itens:
  #print(f"The fruit is {item}")
  contador = contador + 1

#print(f"O total de fruta é {contador}")

numbers= [192, 23, 43, 123, 65]

#print(numbers[2])

lists = range(11)

for i in lists:
  #print(i)
  pass

for m in range(6):
  print(m)
  for j in range(1,6):
    print(f"----{j}")


first_name = "Mike"
for a, letter in enumerate(first_name):
  #print(a, letter)
  pass
first_name = "Brigham"
total_letters = len(first_name)

for i in range(total_letters):
    letter = first_name[i]
    print(f"The letter is: {letter}")