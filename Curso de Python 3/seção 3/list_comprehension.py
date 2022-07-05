

n1 = [1,2,3,4]
novos_numeros = n1 #errado
novos_numeros = n1.copy() #certo 
novos_numeros[0] = 20

#os valores de novos numeros alteram a lista n1, por isso utilizamos lists comprehension
#n retorna o valor do n1
n2 = [n for n in n1] # lists comprehension

n2_02 = [] #For normal
for numeros in n1:
  n2_02.append(numeros)

#n se torna iteravel 
n3 = [n * 2 for n in n1]

#Um for dentro de outro 
n4 = [(v , v2) for v in n1 for v2 in range(5)]

#iteração novamente

names = ["Mike", "Gabi", "Dudu"]
choose = [name.replace("i", "o") for name in names]
#print(choose)

tupla = (
  ("valor", "chave"),
  ("valor2", "chave2")
)
ex = [(x,y) for x, y in tupla]
ex = dict(ex)
#print(ex)

#Condicionais na lista
lista = list(range(51))
ex01 = [v if v % 3 == 0 and v % 8 == 0 else "n" for v in lista]
print(ex01)

