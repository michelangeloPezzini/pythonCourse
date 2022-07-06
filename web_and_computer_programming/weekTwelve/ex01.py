shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]

bigest = -1
produto = ""
for i in shopping_cart:
  preco = i[1]
  produto = i[0]
  if preco > bigest:
    bigest = preco
  
print(f"O produto mais caro é {produto} R${bigest}")