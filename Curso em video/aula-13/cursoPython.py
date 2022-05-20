# Como pegar um determinado numero
""" num = int(input("Digite um numero: "))
var = str(num).strip().upper()[1]
print(var) """

""" genero = True

while genero:
    print("
1-MASCULINO:
2-FEMINICO:
3-OUTRO:
4-PREFIRO NÃO DIZER:
")
    genero = str(input("Digite seu genero: ")).strip().upper()[0]
    if genero == "1":
        print("*"*20)
        print("Masculino")
        print("*"*20)
    elif genero == "2":
        print("*"*20)
        print("Feminino")
        print("*"*20)
    elif genero == "3":
        print("*"*20)
        print("Outro")
        print("*"*20)
    elif genero == "4":
        print("*"*20)
        print("Prefiro não dizer")
        print("*"*20)

    else:
        print("Tente denovo")

    genero = None """


import random
randomValue = random.randint(1, 10)

print("*"*20)
print("Tente acertar o mesmo numero que eu! ")
print("*"*20)
certo = False
contador = 0
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
        
print("Você venceu! {} x {}".format(randomValue, userAnswer))
print("Você tentou {} vezes! ".format(contador)) 

