def fibonacci(num1):
    if num1 == 0:
        return 0
    elif num1 == 1:
        return 1
    else:
        return fibonacci(num1 - 1) + fibonacci(num1 - 2)
num2 = int(input("Digite a posição da sequência de Fibonacci: "))
print(f"O valor na posição {num2} é {fibonacci(num2)}")