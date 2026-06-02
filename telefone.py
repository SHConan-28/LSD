# num1 é o dicionário da agenda
num1 = {}

def adicionar_contato():
    num2 = input("Qual o nome do contato?: ").strip()
    num3 = input("Diga o número de telefone: ").strip()
    num1[num2] = num3
    print(f"Contato {num2} adicionado")

def remover_contato():
    num4 = input("Qual contato deseja remover?: ").strip()
    if num4 in num1:
        num1.pop(num4)
        print(f"Contato {num4} removido")
    else:
        print("Contato não existente")

def buscar_contato():
    num5 = input("Digite o contato que procura: ").strip()
    if num5 in num1:
        print(f"{num5} {num1[num5]}")
    else:
        print("Contato não existente")
def listar_contato():
    if not num1:
        print("Agenda está vazia")
        return
    for num6, num7 in num1.items():
        print(f"Nome do contato: {num6} Telefone: {num7}")
while True:
    print("1- Adicionar contato: ")
    print("2- Remover contato: ")
    print("3- Buscar contato: ")
    print("4- Listar contatos: ")
    num8 = input("Escolha uma opção: ").strip()
    
    if num8 == "1":
        adicionar_contato()
    elif num8 == "2":
        remover_contato()
    elif num8 == "3":
        buscar_contato()
    elif num8 == "4":
        listar_contato()
    else:
        print("Opção inválida!")