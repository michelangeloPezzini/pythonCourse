cart_itens = []
cart_itens_price = []

def add_itens():
    item_name = str(input("What item would you like to add? ")).capitalize()
    item_price = input(f"What is the price of {item_name}? ")
    cart_itens.append(item_name)
    cart_itens_price.append(item_price)
    #print(*cart_itens, sep = "\n")
    print(f"\033[31;45m{item_name} has been added to the cart. \033[m")
    print()

def cart_view():
    cont = 0
    for name, price in zip(cart_itens, cart_itens_price):
        cont = cont + 1
        print(f"{cont}| Product: {name} | ${price}")
    #print(f"{cont}: ", *cart_itens, sep="")

def remove_itens():
    delete_itens = int(input("What item would you like to remove? "))
    del(cart_itens[delete_itens - 1])
    print("Item removed successfully! ")
    print()

def compute_total():
    result = sum(map(float, cart_itens_price))
    print(
        f"The total price of the items in the shopping cart is \033[31;45m${result}\033[m")

choose = True
while choose:
    print('''
    Please select one of the following:
    \033[31;46m1. Add item \033[m
    \033[32;45m2. View cart \033[m
    \033[33;44m3. Remove item \033[m
    \033[34;43m4. Compute total \033[m
    \033[35;42m5. Quit \033[m
    ''')
    choose = int(input("Please enter an action: "))
    print()
    if choose == 1:
        add_itens()
    elif choose == 2:
        cart_view()
    elif choose == 3:
        remove_itens()
    elif choose == 4:
        compute_total()
    elif choose == 5:
        print("Thank you for shopping with us. Goodbye! ")
        break
    else:
        print('\n Choice not valid.\n Try again.')
