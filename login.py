usuários = {}

def cadastrar_usuario():
    num1 = input("Olá, crie um nome de usuário: ")
    if num1 in usuários:
        print("Usuário já existente!")
    else:
        num2 = input("Digite uma senha: ")
        usuários[num1] = num2
        print(f"Usuário {num1} cadastrado com sucesso!")

def login():
    num1 = input("Digite seu nome de usuário: ")
    if num1 not in usuários:
        print("Usuário não existente!")
    else:
        num2 = input("Digite sua senha: ")
        if num2 == usuários[num1]:
            print(f"Seja bem vindo {num1}!")
        else:
            print("Senha incorreta!")

def alterar_senha():
    num1 = input("Digite seu nome de usuário: ")
    if num1 not in usuários:
        print("Usuário não existente!")
    else:
        num2 = input("Digite sua senha atual: ")
        if num2 == usuários[num1]:
            num3 = input("Digite sua nova senha: ")
            usuários[num2]=num3
            print("Senha alterada com sucesso")
        else:
            print("Senha incorreta!")

while True:
    print("1-cadastrar usuário: ")
    print("2-login: ")
    print("3-alterar senha: ")
    num1 = input("Selecione uma opção: ")
    if num1 == "1":
        cadastrar_usuario()
    elif num1 == "2":
        login()
    elif num1 == "3":
        alterar_senha()