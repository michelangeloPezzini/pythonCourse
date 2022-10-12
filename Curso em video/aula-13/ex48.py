from re import I


#Somar numeros que são multiplos de tres
soma = 0
for i in range(1,501,2):
  if i % 3 == 0:
    soma = soma + i

print(soma)