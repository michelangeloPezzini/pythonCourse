""" frase = "Hoje o dia foi muito bom"
novaFrase = frase.count("o", 0 , 12)
novaFrase1 = len(frase)
novaFrase2 = frase[3::2]
novaFrase3 = frase.find("dia")
novaFrase4 = "foi" in frase
novaFrase5 = frase.replace("muito","super")
novaFrase6 = "-".join(frase)
novaFrase7 = frase.split()
print(novaFrase)
print(novaFrase1)
print(novaFrase2)
print(novaFrase3)
print(novaFrase4)
print(novaFrase5) #upper / lower / capitalize / title / r l strip / split 
print(novaFrase6)
print(novaFrase7) """

# Exercicio 22
""" nome = ("michelangelo pezzini").strip()
print(nome.capitalize())
print(nome.title())
print(len(nome) - nome.count(" "))
print(nome.find(" ")) #Quantas letras tem o primeiro nome
separa = nome.split()
print(separa[1]) """


# Exercicio 23
numero = "1954"
unidade = numero[0]
print("unidade ", unidade)
dezena = numero[1]
print("dezena ", dezena)
centena = numero[2]
print("centena ", centena)
milhar = numero[3]
print("milhar ", milhar)


# Exercicio 24
""" nome = str(input("Digite seu nome? ")).strip()
if nome[:4].capitalize() == "Mike":
  print("Verdadeiro")
else:
  print("Falso") """

# Exercicio 25
""" nome = str(input("Digite seu nome? ")).strip()
print("{}".format("pezzini" in nome.lower())) """

# Exercicio 26
""" nome = str(input("Digite seu nome? ")).upper()
print("A letra 'A' aparece {} vezes.".format(nome.count("A")))
print("A primeira letra 'A' apareceu na posição {}".format(nome.find('A')+1))
print("A ultima letra 'A' apareceu na posição {}".format(nome.rfind('A')+1)) """

# Exercicio 27
""" nomeCompleto = str(input("Digite seu nome? ")).strip()
nomeSeparado = nomeCompleto.split()
print("Primeiro nome {}".format(nomeSeparado[0]))
print("Ultimo nome {}".format(nomeSeparado[len(nomeSeparado)-1])) """
