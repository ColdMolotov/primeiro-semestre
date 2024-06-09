numero = int(input("Informe um número inteiro: "))

if not numero % 15:
    print(f"O número {numero} é divisível por 3 e 5 simultaneamente.")
else:
    print(f"O número {numero} NÃO é divisível por 3 e 5 simultaneamente.")
