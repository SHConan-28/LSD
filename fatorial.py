def fatorial():
    num1 = int(input("insira um número: "))
    fatorial = 1
    while num1 > 1:
        fatorial *= num1
        num1 -= 1
    print (f"fatorial: {fatorial}")
