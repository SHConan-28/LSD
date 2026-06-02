def eh_primo(num1):
    for num2 in range(2, num1):
        if num1 % num2 == 0:
            return False
    return num1 > 1
num1 = int(input("Digite um número: "))
if eh_primo(num1):
    print("Primo")
else:
    print("Não é primo")