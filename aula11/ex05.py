lista1 = [int(input(f"Informe o {i + 1}º valor da primeira lista: ")) for i in range(5)]
lista2 = [int(input(f"Informe o {i + 1}º valor da segunda lista: ")) for i in range(5)]
uniao_geral = set(lista1).union(lista2)

print("Primeira lista: ", lista1)
print("Segunda lista: ", lista2)
print("\nUnião entre a primeira e a segunda lista:", uniao_geral)
