lista = [
  ["p4", 13],
  ["p3", 4],
  ["p1", 78],
  ["p2", 43]
]

lista.sort(key=lambda item: item[0], reverse=True)
print(lista)