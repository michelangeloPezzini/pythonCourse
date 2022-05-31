while True:
    num = int(input("Digite um numero: "))
    if num < 0:
        break
    print("-"*30)
    for x in range(1, 11):
        valores = num * x
        print(f"{num} x {x} = {valores}")
    print("-"*30)
print("Volte sempre")
