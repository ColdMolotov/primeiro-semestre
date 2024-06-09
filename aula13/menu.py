def mostrar_menu():
    while True:
        print("Opções do menu:")
        print("1. Adicionar")
        print("2. Mostrar Mensagem")
        print("3. Encerrar")

        selecao = input("Escolha uma das opções: ")

        if selecao.isdigit():
            if int(selecao) in range(1, 4):
                return int(selecao)

        print("Seleção inválida! Por favor, escolha uma opção entre 1 e 3.")


if __name__ == '__main__':
    mostrar_menu()
