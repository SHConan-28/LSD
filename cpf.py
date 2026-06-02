def cpf(cpf):
    cpf = input("Digite o seu CPF: ")
    num1 = ""
    for num2 in cpf:
        if num2.isdigit():
            num1 += num2
    if len(num1) == 11:
        print("CPF válido")
    else:
        print("CPF inválido!")
cpf(cpf)