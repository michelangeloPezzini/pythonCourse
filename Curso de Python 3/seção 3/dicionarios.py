clientes = {
  "cliente1": {
    "nome" : "Mike",
    "id" : "47"    
  },
  "cliente2": {
    "nome" : "gabi",
    "id" : "85"
  }
}

for k, v in clientes.items():
  print(k)
  for key, value in v.items():
    print(f"\t{key} = {value}")