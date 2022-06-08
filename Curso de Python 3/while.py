while True:
    num1 = input("Digite um numero: ")
    num2 = input("Digite outro numero: ")

    if not num1.isnumeric() or not num2.isnumeric():
        print("Digite um numero valido! ")
        continue
    else:
        soma = int(num1) + int(num2)
        print(f"A soma de {num1} + {num2} = {soma}")
        break
print("Boa noite")
