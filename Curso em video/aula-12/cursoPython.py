# Aprovar emprestimo bacario
# Valor da casa
# Salario da pessoa
# Quanto tempo vai pagar
# A prestação não pode ser superior a 30% do salario

""" nome = str(input("Digite seu nome: "))
valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salario: "))
prestacao = int(input("Qual a quantidade de parcelas: "))
parcelas = valor/prestacao
salario_30 = (salario * 30/100)
if parcelas > salario_30:
    print(
        f"Infelizmente sua compra não foi aprovada. Parcelas de R$:{parcelas:.1f} outrapassam 30% do seu salario que é de {salario_30}")
else:
    print(f"Parabens {nome} sua compra foi autorizada")
    print(f"Parcelas de R${parcelas} x {prestacao}") """

# Exercicio 46
""" import time
for count in range(10, -1, -1):
    print(count)
    time.sleep(0.5)
print("Parabens!!")
 """

# Exercicio 47
""" for num in range(1, 51):
    if num % 2 == 0:
        print(f"{num}", end=" ")
print("Acabou") """

# Exercico 48
""" soma = 0
cont = 0
for num in range(1,501,2):
  if num % 3 == 0:
    cont = cont + 1 
    soma = soma + num
print(cont)
print(soma)
 """

# Exercicio 49
""" tabuada = int(input("Digite o numero desejado: "))
for x in range(1, 11):
    print("{} x {} = {}".format(tabuada, x, tabuada * x))
 """

# Exercicio 50
""" soma = 0
for num in range(1, 7):
    var = int(input("Type the {} number: ".format(num)))
    if var % 2 == 0:
        soma = soma + var
print(soma)
 """

# Exercicio 52
""" total = 0
num = int(input("Digite um numero qualquer: "))
for i in range(1, num + 1):
    if num % i == 0:
        print("\033[33m", end=" ")
        total = total + 1
    else:
        print("\033[31m", end = " ")
    print("{}".format(i), end = " ")
print("\n\033[mO numero {} é divisivel {} vezes".format(num, total))
if total == 2:
    print("O numero é primo")
else:
    print("O numero nao é primo") """
