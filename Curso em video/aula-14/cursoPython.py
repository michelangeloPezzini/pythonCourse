number1 = int(input("Digite um numero: "))
number2 = int(input("Digite outro numero: "))

def soma():
    result = number1 + number2
    print(result)
def sub():
    result = number1 - number2
    print(result)

escolha = True

while escolha != 4:
    escolha = int(input("""
Digite sua escolha: 
Escolha sua opção:
[1] soma
[2] subtração
[3] escolher outros numeros
[4] sair
    """))
    if escolha == 1:
        soma()
    elif escolha == 2:
        sub()
    elif escolha == 3:
        number1 = int(input("Digite um numero: "))
        number2 = int(input("Digite outro numero: "))
    elif escolha == 4:
        print("GoodBye")
    else:
        print("Type Again")
print("See you next time")


