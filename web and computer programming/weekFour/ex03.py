def food():
    print("*" * 20)
    print("""
    Menu of foods:
    1. Complete Hamburguer ($15,00)
    2. SuperBurguer "two meats" ($25,00 )
    3. Hamburguer with Bacon ($20,00)
    4. Heart chicken Burguer ($23,00)
  """)
    print("*"*20)

    foodChosed = input("Qual o numero do prato desejado? ")
    quantidade = int(input("Qual a quantidade? "))

    if foodChosed == "1":
        total = quantidade * 15
        print(f"Total = {total:.2f}")
    elif foodChosed == "2":
        total = quantidade * 25
        print(f"Total = {total:.2f}")
    elif foodChosed == "3":
        total = quantidade * 20
        print(f"Total = {total:.2f}")
    elif foodChosed == "4":
        total = quantidade * 23
        print(f"Total = {total:.2f}")
    else:
        print("\n Choice not valid.\n Try again.")
food()