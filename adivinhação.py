import random
def jogo_adivinhação():
    num1 = int(input("selecione um número de 1 á 100: "))
    num2 = random.randint (1, 100)
    while num1 != num2:
        print ("Você errou, tente novamente")
        if num1 > num2:
            print ("mais baixo")
        elif num1 < num2:
            print ("mais alto")
        num1 = int(input("selecione um número de 1 á 100: "))
    else:
        print (f"parabéns, você acertou o número {num2}")
