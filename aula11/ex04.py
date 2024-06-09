informacoes_pessoais = {}
for i in range(5):
    nome = input("Informe o nome da pessoa: ")
    idade = int(input("Informe a idade da pessoa: "))
    informacoes_pessoais[nome] = idade

lista_idades = list(informacoes_pessoais.values())
media_idade = sum(lista_idades) / len(lista_idades)

for pessoa, idade in informacoes_pessoais.items():
    if idade > media_idade:
        print(f"{pessoa}: {idade} anos tem idade acima da média {media_idade} anos")
