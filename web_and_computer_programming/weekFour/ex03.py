def restaurantMenu():
    print("*" * 20)
    print("""
      Menu of foods:
      1. Complete Hamburguer ($15,00)
      2. SuperBurguer "two meats" ($25,00 )
      3. Hamburguer with Bacon ($20,00)
      4. Heart chicken Burguer ($23,00)
    """)
    print("*"*20)

    foodChosed = input(
        "Qual o numero do prato desejado? ")
    foodQuantidade = int(input("Qual a quantidade? "))

    if foodChosed == "1":
        totalFood = foodQuantidade * 15
    elif foodChosed == "2":
        totalFood = foodQuantidade * 25
    elif foodChosed == "3":
        totalFood = foodQuantidade * 20
    elif foodChosed == "4":
        totalFood = foodQuantidade * 23
    else:
        print("\n Choice not valid.\n Try again.")

    print("""
      Menu of drinks:
      1. Coca cola ($6,00)
      2. Milk shake ($10,00 )
      3. Water ($4,00)
      4. Juice ($7,00)
      """)
    print("*"*20)

    drinkChosed = input(
        "Qual o numero da bebida desejada? ")
    drinkQuantidade = int(input("Qual a quantidade? "))

    if drinkChosed == "1":
        totalDrink = drinkQuantidade * 6
    elif drinkChosed == "2":
        totalDrink = drinkQuantidade * 10
    elif drinkChosed == "3":
        totalDrink = drinkQuantidade * 4
    elif drinkChosed == "4":
        totalDrink = drinkQuantidade * 7
    else:
        print("\n Choice not valid.\n Try again.")
    total = totalFood + totalDrink
    print("Total é = ${}".format(total))


restaurantMenu()
