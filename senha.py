import random
def senha(num1):
    num2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num3 = "0123456789"
    num4 = "!@#$%¨&*()_+{}~^:></?"
    num5 = num2 + num3 + num4
    senha = ""
    for i in range(num1):
        indice = random.randint(0, len(num5)-1)
        senha = senha + num5[indice]
    return senha
num7 = int(input("Qual o tamanho da senha? "))
num8 = senha(num7)
print(f"Sua senha é {num8}")