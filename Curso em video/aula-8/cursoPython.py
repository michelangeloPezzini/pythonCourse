""" 
import math
num = int(input("Digite um numero? "))
raiz = math.sqrt(num)
print("A riz de {} é {:.2f}".format(num, raiz))
 """
""" 
import random
aleatorio = random.randint(1,10)
print(aleatorio) """

# Exercicio 16
""" 
import math
num = float(input("Digite um numero? "))
arredondamento = math.trunc(num)
print(math.ceil(arredondamento)) """

# Exercicio 17
""" 
co = float(input("Digite o comprimento do cateto oposto? "))
ca = float(input("Digite o comprimento do cateto adjacente? "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print("{:.2f}".format(hi)) """

""" import math
co = float(input("Digite o comprimento do cateto oposto? "))
ca = float(input("Digite o comprimento do cateto adjacente? "))
hi = math.hypot(co, ca)
print("{:.2f}".format(hi))
 """

# Exercicio 18
""" import math
angulo = float(input("Digite um angulo? "))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print("O angulo de {} tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}".format(
    angulo, seno, cos, tan)) """

# Exercicio 19
""" import random
aluno1 = str(input("Digite o primeiro aluno? "))
aluno2 = str(input("Digite o segundo aluno? "))
aluno3 = str(input("Digite o terceiro aluno? "))
aluno4 = str(input("Digite o quarto aluno? "))
alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(alunos)
print(escolhido) """

# Exercicio 20
""" aluno1 = str(input("Digite o primeiro aluno? "))
aluno2 = str(input("Digite o segundo aluno? "))
aluno3 = str(input("Digite o terceiro aluno? "))
aluno4 = str(input("Digite o quarto aluno? "))
alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)
print(alunos) """

