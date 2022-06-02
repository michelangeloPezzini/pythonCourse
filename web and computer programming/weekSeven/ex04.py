import random
randomValue = random.randint(1, 10)

print("*"*20)
print("Tente acertar o mesmo numero que eu! ")
print("*"*20)
certo = False
contador = 0
player1= 0
computer = 0
while not certo:
    userAnswer = int(input("Digite um numero entre 1 e 10: "))
    contador = contador + 1
    if randomValue == userAnswer:
        certo = True
    else:
        if randomValue > userAnswer:
            print("Um pouco mais")
        elif randomValue < userAnswer:
            print("Um pouco menos")
        
print("\033[36mVocê venceu!\033[m {} x {}".format(randomValue, userAnswer))
print("Você tentou {} vezes! ".format(contador)) 


