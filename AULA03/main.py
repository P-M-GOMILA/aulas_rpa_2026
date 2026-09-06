# main.py
from mod_rh import cadastrar_colaborador, exibir_colaboradores

# Lista em memória para armazenar os colaboradores
colaboradores = []

while True:
    print("=== Menu RH ===")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do colaborador: ")
        cargo = input("Digite o cargo do colaborador: ")
        salario = float(input("Digite o salário do colaborador: "))
        colaborador = cadastrar_colaborador(nome, cargo, salario)
        colaboradores.append(colaborador)
        print("[SUCESSO] Colaborador cadastrado!\n")

    elif opcao == "2":
        exibir_colaboradores(colaboradores)

    elif opcao == "0":
        print("Encerrando sistema de RH...")
        break

    else:
        print("[ERRO] Opção inválida. Tente novamente.\n")
