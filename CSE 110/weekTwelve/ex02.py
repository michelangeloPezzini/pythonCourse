people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 12",
    "Jacob 10"
]

youngest = 10000
names = ""
for lista in people:
  partes = lista.split()
  age = int(partes[1])
  name = partes[0]

  if age < youngest:
    youngest = age
    names = name
  

print(f"A pessoa mais jovem é {names} e tem {youngest} anos")
