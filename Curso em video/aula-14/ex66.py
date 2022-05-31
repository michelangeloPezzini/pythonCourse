contador = 0
soma = 0

while True:
    num = int(input("Digite um numero: "))
    if num == 999:
        break
    contador = contador + 1
    soma = soma + num

print(contador)
print(soma)
