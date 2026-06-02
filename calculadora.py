def calculadora():
    num1 = float(input("Selecione o primeiro número: "))
    num2 = float(input("Selecione o segundo número: "))
    opc = input("Digite a operação (+ - * /): ")
    if opc == "+":
        num3 = num1 + num2
    elif opc == "-":
        num3 = num1 - num2
    elif opc == "*":
        num3 = num1 * num2
    elif opc == "/":
        if num2 == 0:
            print("Não existe divisão por 0")
            return
        num3 = num1 / num2
    else:
        print("Operação inválida")
        return
    print (f"O resultado foi de: {num3}")
calculadora()