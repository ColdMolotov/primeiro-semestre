numeros = ()
for _ in range(10):
    valor = int(input("Informe um número inteiro: "))
    numeros += (valor,)

print(numeros[::-1])
