number = int(input("Digite um numero positivo: "))

while number < 0:
    print("Digite novamente...")
    number = int(input("Digite um numero positivo: "))
print(number)

cake = ""
while cake != "yes":
  cake = str(input("Can I have a piece of cake? "))
print("Thank you")