#Michelangelo Pezzini
#Projeto de python
cart_itens = []
cart_itens_price = []


def add_itens():
    item_name = str(input("What item would you like to add? ")).capitalize()
    item_price = input(f"What is the price of {item_name}? ")
    cart_itens.append(item_name)
    cart_itens_price.append(item_price)
    #print(*cart_itens, sep = "\n")
    print(f"\033[35;42m '{item_name}' has been added to the cart. \033[m")
    print()


def cart_view():
    cont = 0
    for name, price in zip(cart_itens, cart_itens_price):
        cont = cont + 1
        print(f"{cont}| Product: {name} | ${price}")                                                                                                                                                                          
    #print(f"{cont}: ", *cart_itens, sep="")


def remove_itens():
    cart_view()
    print()
    delete_itens = int(
        input("What is the number of the item that you would like to remove? "))
    del(cart_itens[delete_itens - 1])
    del(cart_itens_price[delete_itens -1])
    print("\033[35;42mItem removed successfully!\033[m ")
    print()


def change_itens():
    cart_view()
    print()
    change_item_index = int(input("Which item would you like to change? "))
    change_item = change_item_index - 1
    new_item = str(input("What is the new item? ")).capitalize()
    new_item_price = input(f"What is the price of {new_item}? ")
    cart_itens[change_item] = new_item
    cart_itens_price[change_item] = new_item_price
    print("\033[35;42mitem successfully changed!\033[m")


def compute_total():
    result = sum(map(float, cart_itens_price))
    print(f"The total price of the items in the shopping cart is \033[31;45m${result}\033[m")
        

choose = True
while choose:
    print('''
    Please select one of the following:
    \033[31;46m1. Add item \033[m
    \033[32;45m2. View cart \033[m
    \033[33;44m3. Remove item \033[m
    \033[34;43m4. Change item \033[m
    \033[35;42m5. Compute total \033[m
    \033[36;41m6. Quit \033[m
    ''')
    list_numbers = ["1", "2", "3", "4", "5", "6"]
    number = input("Please type a number: ")
    if number in list_numbers:
        choose = int(number)
        print()
        if choose == 1:
            add_itens()
        elif choose == 2:
            cart_view()
        elif choose == 3:
            remove_itens()
        elif choose == 4:
            change_itens()
        elif choose == 5:
            compute_total()
        elif choose == 6:
            print()
            print("Thank you for shopping with us. Goodbye! ")
            break
    else:
        print()
        print("\033[36;41mType again! \033[m")
