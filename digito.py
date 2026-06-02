def contar_digitos(num1):
    if num1 < 0:
        num1 = num1 * -1
    return len(str(num1))
num2 = input("Digite um número: ").strip()
if num2.isdigit():
    num2 = int(num2)
    print(f"Esse número possui {contar_digitos(num2)} digito")
else:
    print("Digite somente números!")