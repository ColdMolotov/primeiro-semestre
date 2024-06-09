dados_idade = {}
for _ in range(10):
    sobrenome = input("Informe o sobrenome da pessoa: ")
    idade = int(input("Informe a idade da pessoa: "))
    dados_idade[sobrenome] = idade

sobrenome_mais_velho = max(dados_idade, key=lambda x: dados_idade[x])

print(f"\nO sobrenome da pessoa mais velha é: {sobrenome_mais_velho}")
