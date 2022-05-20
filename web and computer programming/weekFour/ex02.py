# Exercise number 3°
# I added a tip to plus with the total costs

childMeal = float(input("Whats is the price of a child`s meal? R$"))
adultMeal = float(input("Whats is the price of an adult`s meal? R$"))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
salesTax = int(input("Whats is the sales tax rate? "))

subtotal = float((childMeal * children) + (adultMeal * adults))
taxRate = float((subtotal * salesTax / 100))
tip = str(input("Você gostaria de doar gorjeta? yes or no? "))
if tip == "yes":
    value = float(input("Quanto você gostaria de doar? "))
    total = float(subtotal + taxRate + value)
else:
    total = float(subtotal + taxRate)

print(f"\nO total é de {total}")
choose = True
while choose:
    print("\n")
    print("Qual o metodo de pagamento? ")
    print("""
  1.Credit:
  2.Debit:
  3.Pix:
  4.Money:
  """)

    choose = input("Choose some option: ")
    if choose == "1":
        print("Credit Payment \n")
        print("Subtotal: R${:.2f}".format(subtotal))
        print("Sales Tax: R${:.2f}".format(taxRate))
        print("Total: R${:.2f}".format(total))
        break

    elif choose == "2":
        print("Debit Payment \n")
        print("Subtotal: R${:.2f}".format(subtotal))
        print("Sales Tax: R${:.2f}".format(taxRate))
        print("Total: R${:.2f}".format(total))
        break
    elif choose == "3":
        print("Pix Payment \n")
        print("Subtotal: R${:.2f}".format(subtotal))
        print("Sales Tax: R${:.2f}".format(taxRate))
        print("Total: R${:.2f}".format(total))
        break
    elif choose == "4":
        print("Money Payment \n")
        payment = float(input("Whats is the payment amount? "))
        if total < payment:
            change = float(payment - total)
            print("Subtotal: R${:.2f}".format(subtotal))
            print("Sales Tax: R${:.2f}".format(taxRate))
            print("Total: R${:.2f}".format(total))
            print("Payment: R${}".format(payment))
            print("Chance: R${:.2f}".format(change))
            break
        else:
            print("Not enought money")

        choose = None
    else:
        print("\n Choice not valid.\n Try again.")
