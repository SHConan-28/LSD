contas = {}

def conta():
    nome = input("Digite o nome da conta: ")
    if nome in contas:
        print("Conta já existente.")
        return
    contas[nome]= 0 
    print(f"Conta criada com sucesso {nome}!")

def deposito():
    nome = input("Digite o nome da conta: ")
    if nome not in contas:
        print("Conta não existente.")
        return
    deposito = float(input("Quanto deseja depositar?: "))
    if deposito <= 0:
        print("Valor inválido.")
        return
    contas[nome] += deposito
    print(f"Depósito de R${deposito} realizado.")

def saque():
    nome = input("Digite o nome da conta: ")
    if nome not in contas:
        print("Conta não existente.")
        return
    saque = float(input("Digite o valor do saque: "))
    if saque <= 0:
        print("Valor inválido.")
        return
    if contas[nome] >= saque:
        contas[nome] -= saque
        print(f"Saque de R${saque} realizado.")
    else:
        print("Saldo insuficiente,liso.")

def transferir():
    conta1 = input("Qual a conta de origem?: ")
    conta2 = input("Qual a conta de destino?: ")
    if conta1 not in contas:
        print("Conta não existente.")
        return
    if conta2 not in contas:
        print("Conta não existente.")
        return
    pix = float(input("Digite o valor da transferência: "))
    if pix <= 0:
        print("Valor inválido.")
        return
    if contas[conta1] >= pix:
        contas[conta1] -= pix
        contas[conta2] += pix
        print("Transferência realizada com sucesso.")
    
while True:
    print("Seja bem vindo ao banco MASTER, o que você deseja?")
    print("1- Criar conta: ")
    print("2- Depositar: ")
    print("3- Sacar: ")
    print("4- Transferir: ")
    print("0- Sair: ")
    num1 = input("Selecione uma opção: ")

    if num1 == "1":
        conta()
    elif num1 == "2":
        deposito()
    elif num1 == "3":
        saque()
    elif num1 == "4":
        transferir()
    elif num1 == "0":
        print("Obrigado por usar o Banco MASTER! Até a próxima!")
        break
    else:
        print("Opção inválida.")