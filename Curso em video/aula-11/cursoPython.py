# Praticando
print("Olá, \033[1;31;42mMichelangelo!\033[m")
x = "\033[1;34;45m"
y = "\033[m"
print(f"Olá, {x} tudo bem contigo?{y}")

cores = {'vermelho': '\033[33m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'branco': '\033[30m',
         'roxo': '\033[35m',
         'verde': '\033[32m',
         'ciano': '\033[36;43m',
         'limpa': '\033[m',
         'preto e branco': '\033[7;30;m',
         }
print(f"Olá, {cores['ciano']}Michelangelo, como foi o seu dia? {cores['limpa']}")


