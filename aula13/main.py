import random
from mostrar_menu import mostrar_menu
from verificar_data import verificar_idade
from verificar_cpf import verificar_cpf

def cadastrar():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    while True:
        cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
        if verificar_cpf(cpf):
            break
        else:
            print("CPF inválido!")
    while True:
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        if verificar_idade(data_nascimento):
            break
        else:
            print("Data inválida!")
    renda_bruta = float(input("Digite a renda bruta: "))
    print("Cadastro concluído com sucesso!")
    print("Nome:", nome)
    print("Sobrenome:", sobrenome)
    print("CPF:", cpf)
    print("Data de Nascimento:", data_nascimento)
    print("Renda Bruta:", renda_bruta)

def mostrar_mensagem():
    frases = [
        "A persistência realiza o impossível",
        "Seus sonhos não precisam de plateia, eles só precisam de você",
        "A persistência é o caminho do êxito",
        "No meio da dificuldade encontra-se a oportunidade"
    ]
    frase = random.choice(frases)
    print(frase)

if __name__ == "__main__":
    while True:
        opcao = mostrar_menu()
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            mostrar_mensagem()
        elif opcao == 3:
            print("Até logo!")
            break
