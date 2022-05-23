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


""" import random
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
print("Você tentou {} vezes! ".format(contador))  """

"""numero = True
while numero == True:
    numero1 = int(input("Digite o 1° numero: "))
    numero2 = int(input("Digite o 2° numero: "))

    print("
    O que você deseja?
    [1] Somar
    [2] Subtrair
    [3] Multiplicar
    [4] Dividir
    ")

   numero = int(input("Digite a opção desejada: "))

    if numero == 1:
        soma = numero1 + numero2
        print("A soma é {}".format(soma))

    elif numero == 2:
        subtracao = numero1 - numero2
        print("A subtração é {}".format(subtracao))

    elif numero == 3:
        multiplicar = numero1 * numero2
        print("A multiplicaçlão é {}".format(multiplicar))
    elif numero == 4:
        divisao = numero1 / numero2
        print("A divisão é {}".format(divisao))
    else:
        numero = False
        print("Digite novamente: ")
 """

""" from math import factorial
num = int(input("Digite um numero apra calcular seu factorial: "))
fac = factorial(num)
print(fac) """


""" 
n = int(input("Digite um numero: "))
c = n
f = 1
while c > 0:
    print("{} ".format(c) ,end="")
    print("x " if c > 1 else "= ", end="")
    f = f * c
    c = c - 1    
print(f)
print("Fim") """
