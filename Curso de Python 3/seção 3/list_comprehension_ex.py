lista = "012345678901234567890123456789"
n = 10
nova_lista = [lista[i:i + n] for i in range(0,len(lista),n)]
nova_lista_retorno = ".".join(nova_lista)
print(nova_lista_retorno)