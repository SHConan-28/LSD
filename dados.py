import random

def dados(num1):
    num2 = num1.lower().split("d")

    if len(num2) != 2:
        return "Escreve certo, tipo 1d20, 2d6, 3d10"

    if not num2[0].isdigit() or not num2[1].isdigit():
        return "Use apenas números inteiros"

    num3 = int(num2[0])
    num4 = int(num2[1])

    if num3 <= 0 or num4 <= 0:
        return "Já viu rolar d0 cara? Faz direito"

    num5 = []
    num6 = 0

    for _ in range(num3):
        num7 = random.randint(1, num4)
        num5.append(num7)
        num6 += num7

    print(f"Os dados foram {num5}")
    return f"Total: {num6}"

num8 = input("Muito boa noite! Senhoras e senhores! Digite os dados que quer rolar: ")
num9 = dados(num8)

print(num9)