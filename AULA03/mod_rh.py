# mod_rh.py

def cadastrar_colaborador(nome: str, cargo: str, salario: float) -> dict:
    """
    Cadastra um colaborador e retorna um dicionário padronizado.
    """
    return {
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }


def exibir_colaboradores(lista_colaboradores: list) -> None:
    """
    Exibe todos os colaboradores cadastrados de forma formatada.
    """
    print("\n=== Lista de Colaboradores ===")
    if not lista_colaboradores:
        print("Nenhum colaborador cadastrado.")
    else:
        for idx, colaborador in enumerate(lista_colaboradores, start=1):
            print(f"{idx}. Nome: {colaborador['nome']} | Cargo: {colaborador['cargo']} | Salário: R$ {colaborador['salario']:.2f}")
    print("==============================\n")
