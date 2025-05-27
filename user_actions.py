import os

from items.item import delete_item, get_user_items
from users.users import (
    delete_user,
    get_user,
    get_users,
    save_user,
    update_user,
    user_exists,
)
from utils.password import encrypt


def new_user():
    name = input("Nome: ")
    email = input("E-mail: ")
    psw = input("Senha Renner: ")

    if not user_exists(email):
        save_user(name, email, encrypt(psw))
        os.system("cls")
    else:
        os.system("cls")
        print(
            """
              Cadastro não realizado!
              
              Já existe um cadastro com os dados informados.
              """
        )
        input("Pressione ENTER para sair.")


def update():
    email = input("Digite o E-mail do usuário que deseja alterar: ")

    if select_user(email):
        print("Qual informação deseja alterar?\n\t1 - Nome\n\t2 - E-mail\n\t3 - Senha")
        option = int(input("Digite a opção desejada: "))

        match option:
            case 1:
                field = "name"
            case 2:
                field = "email"
            case 3:
                field = "psw"

        value = input("Digite o novo valor do campo: ")
        update_user(email, field, value)
        print("Usuário alterado com sucesso!")

    input("Pressione ENTER para sair.")


def delete():
    email = input("Digite o E-mail do usuário que deseja excluir: ")

    if select_user(email):
        option = input("Confirma a exclusão do cadastro? (S/N): ")

        if option.upper() == "S":
            try:
                user = get_user(email)
                items = get_user_items(user["id"])

                if items:
                    for item in items:
                        delete_item(item["sku"])

                delete_user(user["id"])
            except Exception as e:
                print(f"Houve um erro ao tentar excluir o cadastro: {e}")

    input("Pressione ENTER para sair.")


def select_user(email):
    user = get_user(email)

    if user:
        print(
            f"Usuário selecionado:\n"
            f"Nome: \t\t{user['name']}\n"
            f"E-mail: \t{user['email']}\n"
            "Senha: \t\t************"
        )
        return True
    else:
        print("Usuário não encontrado!")


def list_users():
    users = get_users()

    for user in users:
        print(
            f"ID:\t {user['id']}\n"
            f"Nome:\t {user['name']}\n"
            f"E-mail:\t {user['email']}\n"
            "---------------------------------------\n\n"
        )
    input("Pressione ENTER para sair.")


def main():
    exit = False

    while not exit:
        os.system("cls")
        print(
            "\t1 - Cadastrar usuário\n\t"
            "2 - Alterar cadastro\n\t"
            "3 - Excluir cadastro\n\t"
            "4 - Lista usuários\n\t"
            "5 - Sair"
        )

        option = int(input("Digite a opçao desejada: "))

        if option == 1:
            os.system("cls")
            new_user()
        elif option == 2:
            os.system("cls")
            update()
        elif option == 3:
            os.system("cls")
            delete()
        elif option == 4:
            os.system("cls")
            list_users()
        else:
            exit = True
            os.system("cls")


if __name__ == "__main__":
    main()
