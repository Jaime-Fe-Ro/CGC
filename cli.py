import sys

from services import get_old_acc_hist_data, select_and_get_download, update_db
from constants import ACC_LIST


def main():
    intro()
    account_selected = select_account()
    select_option(account_selected)


def intro():
    pass


def select_account():
    accounts = ACC_LIST

    print("\nCuentas disponibles:\n")
    for i, account in enumerate(accounts, start=1):
        print(f"{i}) {account}")

    account_selection = input("\nPor favor, seleccione una cuenta -> ")
    selected_account = accounts[int(account_selection) - 1]
    print(f"\n\n\n - Cuenta seleccionada: {selected_account} -\n")

    return selected_account


def select_option(account_selected):
    options = [
        "Salir del programa",
        "Cambiar selección de cuenta (reiniciar programa)",
        "Añadir datos al registro histórico",
        "Generar declaraciones"
    ]

    for i, option in enumerate(options):
        print(f"{i}) {option}")

    option_selection = input("\nPor favor, seleccione una opción -> ")

    if option_selection == "0":
        sys.exit(0)
    elif option_selection == "1":
        main()
    elif option_selection == "2":
        add_downloaded_data(account_selected)
    elif option_selection == "3":
        generate_statements(account_selected)
    else:
        print("Opción no válida. Saliendo del programa.")
        sys.exit(1)


def add_downloaded_data(account):
    old_data = get_old_acc_hist_data(account)
    new_data = select_and_get_download(account)
    update_db(old_data, new_data)
    return None


def generate_statements(account):
    pass


if __name__ == "__main__":
    main()
