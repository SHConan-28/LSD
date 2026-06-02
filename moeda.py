def conversor_moeda():
    num1 = float(input("Digite o valor em Real R$: "))
    num2 = float(input("Digite a taxa de câmbio: "))
    num3 = num1 / num2
    print(f"R$ {num1:.2f} equivalem a US$ {num3:.2f}")
conversor_moeda()
