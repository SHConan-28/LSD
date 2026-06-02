num1 = {}
def num2():
    print(" ")
    num3 = input("Insira seu nome de jogador: ").strip()
    
    if num3 in num1:
        num4 = int(input("Insira seu novo ranking: "))
        num1[num3].append(num4)
    else:
        num5 = int(input("Insira seu ranking inicial: "))
        num1[num3] = [num5]
def num6():
    print(" ")
    if not num1:
        print("Nenhum jogador cadastrado.")
        return
    num7 = list(num1.keys())[0]
    num8 = num1[num7]
    
    print(f"Seus dados gameplays masters mr aura + ego (vulgo {num7}) ")
    print(" ")
    print(f"Seu valor máximo é: {max(num8)}.")
    print(" ")
    num9 = input("Pressione 'e' para voltar a jogadores (ou qualquer tecla para sair): ")
    if num9 == "e":
        num2()
        num6()
num2()
num6()
print(f"Estado final do banco:{num1}")