
from glob import escape


with open("web_and_computer_programming\weekEleven\list.txt") as f:
  for i in f:
    espace = i.strip()
    separador2 = espace.split(" ")
    cursos = separador2[0]
    print(f"O curso é {cursos}")
    print(separador2)

  print("Goodbye")
print("The file is closed")