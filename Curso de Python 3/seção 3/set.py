lista = set()
lista.add(1)
lista.discard(1) 

#sets não possuem elementos duplucados
lista2 = set()
lista2.update([1,2,3], {4,5,6})

n1 = {1,2,3}
n2 = {1,2,3,4}
#Une todos os diferentes
n3 = n1 | n2

#Une todos os iguais
n4 = n1 & n2
#print(n3)

teste = set()
teste.add("Mike")
print(teste)
#update retorna elementos fora de ordem 
teste.update("Gabi")
print(teste)

x = {1,2,3,"x"}
y = {1,2,3,"y"}

xy = x ^ y
print(xy)