valor_inicial = float(input("Valor inicial: "))
juros = float(input("Taxa de juros anual em %: "))
aumento = (juros / 100) * valor_inicial
print(f"com taxa de {int(juros)}% ao ano num valor inicial de {int(valor_inicial)}, ")
print(f"o aumento é igual a {int(aumento)} e o valor total depois de um ano será {int(valor_inicial + aumento)}. ")