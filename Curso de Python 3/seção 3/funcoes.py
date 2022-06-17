#Soma
""" 
def soma(v1, v2):
  return v1 + v2

resultado = soma(5, 9) """

#Percentual
""" def porcentagem(v1,v2):
  return v1 + (v1 * v2 / 100)

calculo = porcentagem(10,30)
print(f"R${calculo}") """


#Fizzbuzz

""" def fizzBuzz(var):
  if var % 3 == 0 and var % 5 == 0:
    return "fizzBuzz"
  if var % 5 == 0:
    return "buzz"
  if var % 3 == 0:
    return "Fizz" 
  return var
number = fizzBuzz(15)
print(number) """


""" def arg(*args, **kwargs):
  print(args)
  nome = kwargs.get("nome")
  print(nome, end=" ")
  sobrenome = kwargs.get("sobrenome")
  print(sobrenome)

lista1 = [1,2,3,4,5]
lista2 = [10,20,30,40,50]

arg(*lista1, *lista2, nome="mike", sobrenome="pezzini") """

def mestre(algo, *argumento, **keyArgumento):
  return algo(*argumento, *keyArgumento)

def ola_nome(nome):
  return f"olá {nome}"

def soma(v1, v2):
  return v1 + v2

executando = mestre(ola_nome, "mike")
executando2 = mestre(soma, 1, 2)
print(executando2)  