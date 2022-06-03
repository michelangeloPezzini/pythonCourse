import random
# Implementar melhor o jogo do par ou impar
vitoriaPlayer = 0
vitoriaComputer = 0
while True:
    jogador = int(input("Digite um numero: "))
    computador = random.randint(0, 11)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou Impar? [P/I] ")).strip().upper()[0]
    if tipo == "P":
        if total % 2 == 0:
            print("-"*30)
            print("\033[32mVocê ganhou!\033[m")
            print(f"{jogador} + {computador} = {total}: PAR")
            print("-"*30)
            vitoriaPlayer = vitoriaPlayer + 1
        else:
            print("-"*30)
            print("\033[31mVocê perdeu!\033[m")
            print(f"{jogador} + {computador} = {total}: Impar")
            print("-"*30)
            vitoriaComputer = vitoriaComputer + 1
        print(f"Player {vitoriaPlayer} x {vitoriaComputer} Computer")
        print("-"*30)
    elif tipo == "I":
        if total % 2 == 1:
            print("-"*30)
            print("\033[32mVocê ganhou!\033[m")
            print(f"{jogador} + {computador} = {total}: Impar")
            print("-"*30)
            vitoriaPlayer = vitoriaPlayer + 1
        else:
            print("-"*30)
            print("\033[31mVocê perdeu!\033[m")
            print(f"{jogador} + {computador} = {total}: PAR")
            print("-"*30)
            vitoriaComputer = vitoriaComputer + 1
        print(f"Player {vitoriaPlayer} x {vitoriaComputer} Computer")
        print("-"*30)
    if vitoriaPlayer == 5:
        print(f"\nVocê ganhou por {vitoriaPlayer} x {vitoriaComputer}")
        break
    elif vitoriaComputer == 5:
        print(f"\nVocê perdeu por {vitoriaComputer} x {vitoriaPlayer}")
        break
print("\nFim do jogo! ")
